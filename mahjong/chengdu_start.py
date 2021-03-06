# coding=utf-8
import datetime
import logging
import random
import re
import time
from logging.handlers import TimedRotatingFileHandler

import grpc
from concurrent import futures

import chengdu_mahjong
import mahjong_pb2_grpc
from mahjong_pb2 import *
from mahjong_utils import MahjongUtils

logging.basicConfig(level=logging.INFO)
thislog = logging.getLogger()


class Performance(mahjong_pb2_grpc.MajongCalculateServicer):
    """
    :实现grpc
    """

    def settle(self, request, context):
        """
        :结算
        :param request:
        :param context:
        :return:
        """
        logging.info("封顶")
        logging.info(request.fengding)
        logging.info("赔叫")
        logging.info(request.peijiao)
        settle = SettleResult()
        user_settles = {}
        users = {}
        cannothu_user = []
        for user in request.player:
            user_settle = settle.userSettleResule.add()
            user_settle.userId = user.player_id
            user_settles.setdefault(user.player_id, user_settle)
            users.setdefault(user.player_id, user)
            cannothu_user.append(user.player_id)
        if not request.peijiao:
            # 杠分计算
            for user in request.player:
                for g in user.gang:
                    if g.type == BGANG:
                        user_settles[user.player_id].gangScore += len(g.fighter)
                        for f in g.fighter:
                            user_settles[f].gangScore -= 1
                    if g.type == MGANG:
                        user_settles[user.player_id].gangScore += 2 * len(g.fighter)
                        for f in g.fighter:
                            user_settles[f].gangScore -= 2
                    if g.type == AGANG:
                        user_settles[user.player_id].gangScore += 2 * len(g.fighter)
                        for f in g.fighter:
                            user_settles[f].gangScore -= 2

        # 胡牌计算
        for hudata in request.hudata:
            if hudata.huUser in cannothu_user:
                cannothu_user.remove(hudata.huUser)
            tempcard = list()
            tempcard.extend(users[hudata.huUser].handlist)
            tempcard.append(hudata.majong)
            # 获取牌型
            ct = chengdu_mahjong.getCardType(tempcard, users[hudata.huUser].peng, users[hudata.huUser].gang, 0)
            ct.extend(hudata.settle)
            user_settles[hudata.huUser].settlePatterns.extend(ct)
            score = chengdu_mahjong.getScore(ct)
            # 带跟翻倍
            allcard = []
            allcard.extend(tempcard)
            for p in users[hudata.huUser].peng:
                allcard.append(p)
                allcard.append(p)
                allcard.append(p)
            for g in users[hudata.huUser].gang:
                allcard.append(g.gangvalue)
                allcard.append(g.gangvalue)
                allcard.append(g.gangvalue)
                allcard.append(g.gangvalue)
            for i in range(0, len(MahjongUtils.get_si(allcard))):
                score *= 2
            if 0 in ct and request.zimojiafan:
                score *= 2
            if score > request.fengding:
                score = request.fengding
            if 0 in ct and not request.zimojiafan:
                score += 1
            for u in hudata.loseUsers:
                user_settles[u].cardScore -= score
                user_settles[hudata.huUser].cardScore += score
        if request.peijiao:
            peijiao_users = list()
            user_score = {}
            if 1 < len(cannothu_user):
                for c in cannothu_user:
                    huTemp = MahjongUtils.get_hu(users[c].handlist, request.rogue)
                    # 有叫
                    if 0 < len(huTemp):
                        score = 0
                        for h in huTemp:
                            tempcard = list()
                            tempcard.extend(users[c].handlist)
                            tempcard.append(h)
                            # 获取牌型
                            cardtype = chengdu_mahjong.getCardType(tempcard, users[c].peng, users[c].gang,
                                                                   request.rogue)
                            cardscore = chengdu_mahjong.getScore(cardtype)
                            # 带跟翻倍
                            allcard = []
                            allcard.extend(tempcard)
                            for p in users[c].peng:
                                allcard.append(p)
                                allcard.append(p)
                                allcard.append(p)
                            for g in users[c].gang:
                                allcard.append(g.gangvalue)
                                allcard.append(g.gangvalue)
                                allcard.append(g.gangvalue)
                                allcard.append(g.gangvalue)
                            for i in range(0, len(MahjongUtils.get_si(allcard))):
                                cardscore *= 2
                            if cardscore > score:
                                score = cardscore
                            if score > request.fengding:
                                score = request.fengding
                        if score > 0:
                            user_score.setdefault(c, score)
                    else:
                        peijiao_users.append(c)
                if 0 < len(user_score) and 0 < len(peijiao_users):
                    for key, value in user_score.items():
                        for p in peijiao_users:
                            user_settles[p].cardScore -= value
                            user_settles[key].cardScore += value
        for sett in settle.userSettleResule:
            logging.info("userid")
            logging.info(sett.userId)
            logging.info("cardScore")
            logging.info(sett.cardScore)
            logging.info("gangScore")
            logging.info(sett.gangScore)
            logging.info("settlePatterns")
            logging.info(sett.settlePatterns)
        return settle

    def calculate(self, request, context):
        """
        :计算
        :param request:
        :param context:
        :return:
        """
        calculate = CalculateResult()
        san = MahjongUtils.get_san(request.player.handlist)
        calculate.dui.extend(MahjongUtils.get_dui(request.player.handlist))
        calculate.san.extend(san)
        calculate.si.extend(MahjongUtils.get_si(request.player.handlist))
        zimo = MahjongUtils.get_hu(request.player.handlist, request.rogue)
        calculate.zimo.extend(zimo)
        calculate.hu.extend(zimo)
        return calculate

    def shuffle(self, request, context):
        """
        :洗牌
        :param request:
        :param context:
        :return:
        """
        shuffle = ShuffleResult()
        cardlist = list()
        if 2 == request.count:
            cardlist.extend([11, 11, 11, 11,
                             12, 12, 12, 12,
                             13, 13, 13, 13,
                             14, 14, 14, 14,
                             15, 15, 15, 15,
                             16, 16, 16, 16,
                             17, 17, 17, 17,
                             18, 18, 18, 18,
                             19, 19, 19, 19,
                             21, 21, 21, 21,
                             22, 22, 22, 22,
                             23, 23, 23, 23,
                             24, 24, 24, 24,
                             25, 25, 25, 25,
                             26, 26, 26, 26,
                             27, 27, 27, 27,
                             28, 28, 28, 28,
                             29, 29, 29, 29])
        else:
            cardlist.extend([1, 1, 1, 1,
                             2, 2, 2, 2,
                             3, 3, 3, 3,
                             4, 4, 4, 4,
                             5, 5, 5, 5,
                             6, 6, 6, 6,
                             7, 7, 7, 7,
                             8, 8, 8, 8,
                             9, 9, 9, 9,
                             11, 11, 11, 11,
                             12, 12, 12, 12,
                             13, 13, 13, 13,
                             14, 14, 14, 14,
                             15, 15, 15, 15,
                             16, 16, 16, 16,
                             17, 17, 17, 17,
                             18, 18, 18, 18,
                             19, 19, 19, 19,
                             21, 21, 21, 21,
                             22, 22, 22, 22,
                             23, 23, 23, 23,
                             24, 24, 24, 24,
                             25, 25, 25, 25,
                             26, 26, 26, 26,
                             27, 27, 27, 27,
                             28, 28, 28, 28,
                             29, 29, 29, 29])
        random.shuffle(cardlist)
        shuffle.cardlist.extend(cardlist)
        return shuffle


def rpc_server():
    """
    :启动grpc服务
    :return:
    """
    thislog.info("started!")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mahjong_pb2_grpc.add_MajongCalculateServicer_to_server(Performance(), server)
    server.add_insecure_port('[::]:50005')
    server.start()
    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    log_fmt = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
    formatter = logging.Formatter(log_fmt)
    log_file_handler = TimedRotatingFileHandler(
        filename='../logs/chengdu_mahjong.log', when="H", interval=1,
        backupCount=200)
    log_file_handler.suffix = "%Y-%m-%d_%H-%M.log"
    log_file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}.log$")
    log_file_handler.setFormatter(formatter)
    log_file_handler.setLevel(logging.DEBUG)
    thislog.addHandler(log_file_handler)

    rpc_server()
    thislog.removeHandler(log_file_handler)()
    # print wanzhou_mahjong.getCardType([5, 7, 22, 22, 9, 29, 9, 29, 14, 17, 14, 17, 5, 7], [], [], 21)


class Formatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        """
        Return the creation time of the specified LogRecord as formatted text.

        This method should be called from format() by a formatter which
        wants to make use of a formatted time. This method can be overridden
        in formatters to provide for any specific requirement, but the
        basic behaviour is as follows: if datefmt (a string) is specified,
        it is used with time.strftime() to format the creation time of the
        record. Otherwise, the ISO8601 format is used. The resulting
        string is returned. This function uses a user-configurable function
        to convert the creation time to a tuple. By default, time.localtime()
        is used; to change this for a particular formatter instance, set the
        'converter' attribute to a function with the same signature as
        time.localtime() or time.gmtime(). To change it for all formatters,
        for example if you want all logging times to be shown in GMT,
        set the 'converter' attribute in the Formatter class.
        """
        ct = self.converter(record.created)
        if datefmt:
            s = time.strftime(datefmt, ct)
        else:
            # t = time.strftime("%Y-%m-%d %H:%M:%S", ct)
            # s = "%s,%03d" % (t, record.msecs)
            s = str(datetime.datetime.now())
        return s
