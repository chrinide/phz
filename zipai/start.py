# -*- encoding=utf-8 -*-
import random
import time

from concurrent import futures

import zipai_pb2_grpc
from zipai_pb2 import *


class Daer(object):
    """
    :大贰
    """

    @staticmethod
    def possible(handlist, degree):
        """
        :可能的牌
        :param handlist:
        :param degree:
        :return:
        """
        possible_list = set()
        for s in handlist:
            possible_list.add(s)
            for i in range(0, degree):
                if (s + i + 1) % 100 < 11:
                    possible_list.add(s + i + 1)
                if (s - i - 1) % 100 > 0:
                    possible_list.add(s - i - 1)
        if 2 in possible_list or 7 in possible_list or 10 in possible_list:
            possible_list.add(2)
            possible_list.add(7)
            possible_list.add(10)
        if 102 in possible_list or 107 in possible_list or 110 in possible_list:
            possible_list.add(102)
            possible_list.add(107)
            possible_list.add(110)
        return possible_list

    @staticmethod
    def chi(handlist):
        """
        :能吃的牌
        :param handlist:
        :return:
        """
        chi = set()
        possible = Daer.possible(handlist, 1)
        for s in possible:
            if (s - 2 in handlist and s - 1 in handlist) or (s + 1 in handlist and s - 1 in handlist) or (
                                s + 2 in handlist and s + 1 in handlist):
                chi.add(s)
            if (s == 2 and 7 in handlist and 10 in handlist) or (s == 7 and 2 in handlist and 10 in handlist) or (
                                s == 10 and 7 in handlist and 2 in handlist):
                chi.add(s)
            if (s == 102 and 107 in handlist and 110 in handlist) or (
                                s == 107 and 102 in handlist and 110 in handlist) or (
                                s == 110 and 107 in handlist and 102 in handlist):
                chi.add(s)
        return chi

    @staticmethod
    def peng(handlist):
        """
        :能碰的牌
        :param handlist:
        :return:
        """
        peng = Daer.get_dui(handlist)
        zhao = Daer.get_san(handlist, [])
        for z in zhao:
            peng.remove(z)
        return peng

    @staticmethod
    def get_dui(handlist):
        """
        :获取对子
        :param handlist:
        :return:
        """
        dui = set()
        temp = list()
        temp.extend(handlist)
        temp = sorted(temp, cmp=Daer.reversed_cmp)
        for i in range(0, len(temp) - 1):
            if temp[i] == temp[i + 1]:
                dui.add(temp[i])
        return dui

    @staticmethod
    def get_san(handlist, penglist):
        """
        :获取三个
        :param handlist:
        :param penglist:
        :return:
        """
        zhao = set()
        temp = list()
        temp.extend(handlist)
        temp = sorted(temp, cmp=Daer.reversed_cmp)
        for i in range(0, len(temp) - 2):
            if temp[i] == temp[i + 2]:
                zhao.add(temp[i])
                i += 2
        for p in penglist:
            zhao.add(p)
        return zhao

    @staticmethod
    def hu(handlist, penglist):
        """
        :计算能胡哪些牌
        :param handlist:
        :param penglist:
        :return:
        """
        hu = set()
        possible = Daer.possible(handlist, 1)
        temp = []
        temp.extend(handlist)
        if Daer.check_lug(temp):
            hu.union(penglist)
        for p in possible:
            temp = []
            temp.extend(handlist)
            temp.append(p)
            temp = sorted(temp, cmp=Daer.reversed_cmp)
            dui = Daer.get_dui(temp)
            for d in dui:
                tempd = list()
                tempd.extend(temp)
                tempd.remove(d)
                tempd.remove(d)
                if Daer.check_lug(tempd):
                    hu.add(p)
            if Daer.check_lug(temp):
                hu.add(p)
        return hu

    @staticmethod
    def reversed_cmp(x, y):
        """
        :排序
        :param x:
        :param y:
        :return:
        """
        if x > y:
            return 1
        if x < y:
            return -1
        return 0

    @staticmethod
    def check_lug(handlist):
        """
        :胡牌规则
        :param handlist:
        :return:
        """
        if 0 == len(handlist):
            return True
        temp = list()
        temp.extend(handlist)
        md_val = temp[0]
        temp.remove(md_val)
        if 2 == Daer.containSize(temp, md_val):
            tempSame = list()
            tempSame.extend(temp)
            tempSame.remove(md_val)
            tempSame.remove(md_val)
            if Daer.check_lug(tempSame):
                return True
        if md_val + 1 in temp and md_val + 2 in temp:
            tempShun = list()
            tempShun.extend(temp)
            tempShun.remove(md_val + 1)
            tempShun.remove(md_val + 2)
            if Daer.check_lug(tempShun):
                return True
        if 2 == md_val and 7 in temp and 10 in temp:
            xiao2710 = list()
            xiao2710.extend(temp)
            xiao2710.remove(7)
            xiao2710.remove(10)
            if Daer.check_lug(xiao2710):
                return True
        if 102 == md_val and 107 in temp and 110 in temp:
            da2710 = list()
            da2710.extend(temp)
            da2710.remove(107)
            da2710.remove(110)
            if Daer.check_lug(da2710):
                return True
        if 1 < Daer.containSize(temp, md_val + 100):
            xiaoxie = list()
            xiaoxie.extend(temp)
            xiaoxie.remove(md_val + 100)
            xiaoxie.remove(md_val + 100)
            if Daer.check_lug(xiaoxie):
                return True
        if md_val + 100 in temp and md_val in temp:
            xiaoxie = list()
            xiaoxie.extend(temp)
            xiaoxie.remove(md_val)
            xiaoxie.remove(md_val + 100)
            if Daer.check_lug(xiaoxie):
                return True
        return False

    @staticmethod
    def check_hu(handlist, val, zimo):
        """
        :检查胡
        :param handlist:
        :param val:
        :param zimo:
        :return:
        """
        if 0 == len(handlist):
            return val
        temp = list()
        temp.extend(handlist)
        md_val = temp[0]
        temp.remove(md_val)
        valtemp = 0
        if 2 == Daer.containSize(temp, md_val):
            tempSame = list()
            tempSame.extend(temp)
            tempSame.remove(md_val)
            tempSame.remove(md_val)
            tempSame = Daer.check_hu(tempSame, val, zimo)
            if tempSame > -1:
                if zimo:
                    if 2 == md_val % 100 or 7 == md_val % 100 or 10 == md_val % 100:
                        if md_val > 100:
                            tempSame += 12
                        else:
                            tempSame += 9
                else:
                    if md_val > 100:
                        tempSame += 9
                    else:
                        tempSame += 6
                valtemp = tempSame
        if md_val + 1 in temp and md_val + 2 in temp:
            tempShun = list()
            tempShun.extend(temp)
            tempShun.remove(md_val + 1)
            tempShun.remove(md_val + 2)
            tempShunVal = Daer.check_hu(tempShun, val, zimo)
            if tempShunVal > -1:
                if md_val == 1:
                    tempShunVal += 3
                if md_val == 101:
                    tempShunVal += 6
                if tempShunVal > valtemp:
                    valtemp = tempShunVal
        if 2 == md_val and 7 in temp and 10 in temp:
            xiao2710 = list()
            xiao2710.extend(temp)
            xiao2710.remove(7)
            xiao2710.remove(10)
            xiao2710 = Daer.check_hu(xiao2710, val, zimo)
            if xiao2710 > -1:
                xiao2710 += 6
                if xiao2710 > valtemp:
                    valtemp = xiao2710
        if 102 == md_val and 107 in temp and 110 in temp:
            da2710 = list()
            da2710.extend(temp)
            da2710.remove(107)
            da2710.remove(110)
            da2710 = Daer.check_hu(da2710, val, zimo)
            if da2710 > -1:
                da2710 += 9
                if da2710 > valtemp:
                    valtemp = da2710
        if 1 < Daer.containSize(temp, md_val + 100):
            daxiaoxie = list()
            daxiaoxie.extend(temp)
            daxiaoxie.remove(md_val + 100)
            daxiaoxie.remove(md_val + 100)
            daxiaoxie = Daer.check_hu(daxiaoxie, val, zimo)
            if daxiaoxie > -1:
                if daxiaoxie > valtemp:
                    valtemp = daxiaoxie
        if md_val + 100 in temp and md_val in temp:
            daxiaoxie1 = list()
            daxiaoxie1.extend(temp)
            daxiaoxie1.remove(md_val)
            daxiaoxie1.remove(md_val + 100)
            daxiaoxie1 = Daer.check_hu(daxiaoxie1, val, zimo)
            if daxiaoxie1 > -1:
                if daxiaoxie1 > valtemp:
                    valtemp = daxiaoxie1
        if valtemp > -1:
            return val + valtemp
        return -1

    @staticmethod
    def containSize(cardlist, card):
        """
        :包含数量
        :param cardlist:
        :param card:
        :return:
        """
        size = 0
        for c in cardlist:
            if c == card:
                size += 1
        return size


class Performance(zipai_pb2_grpc.ZipaiServicer):
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
        settle = SettleResult()
        hu = 0
        bang = 0
        settle_type = set()
        for u in request.userSettleData:
            if u.userId == request.huUserId:
                for p in u.penglist:
                    if 2 == p % 100 or 7 == p % 100 or 10 == p % 100:
                        if p > 100:
                            hu += 9
                        else:
                            hu += 6
                    else:
                        if p > 100:
                            hu += 3
                        else:
                            hu += 1
                for p in u.kanlist:
                    if 2 == p % 100 or 7 == p % 100 or 10 == p % 100:
                        if p > 100:
                            hu += 12
                        else:
                            hu += 9
                    else:
                        if p > 100:
                            hu += 9
                        else:
                            hu += 6
                for p in u.zhaolist:
                    if 2 == p % 100 or 7 == p % 100 or 10 == p % 100:
                        if p > 100:
                            hu += 15
                        else:
                            hu += 12
                    else:
                        if p > 100:
                            hu += 12
                        else:
                            hu += 9
                for p in u.longlist:
                    if 2 == p % 100 or 7 == p % 100 or 10 == p % 100:
                        if p > 100:
                            hu += 18
                        else:
                            hu += 15
                    else:
                        if p > 100:
                            hu += 15
                        else:
                            hu += 12
                for i in range(0, u.chilist, 3):
                    if u.chilist[i] == 1 and u.chilist[i] == 2 and u.chilist[i] == 3:
                        hu += 3
                    elif u.chilist[i] == 101 and u.chilist[i] == 102 and u.chilist[i] == 103:
                        hu += 6
                    elif u.chilist[i] == 2 and u.chilist[i] == 7 and u.chilist[i] == 10:
                        hu += 6
                    elif u.chilist[i] == 102 and u.chilist[i] == 107 and u.chilist[i] == 110:
                        hu += 9
                hu += Daer.check_hu(u.handlist, 0, ZIMO in request.settlePatterns)
                if hu < 27:
                    bang = 2
                if hu < 21:
                    bang = 1
                if hu < 10:
                    bang = 0
                if hu > 26:
                    bang = (hu - 27) / 3 + 3
                if request.qia:
                    bang += 1
                temp_card = list()
                temp_card.extend(u.chilist)
                temp_card.extend(u.penglist)
                temp_card.extend(u.kanlist)
                temp_card.extend(u.zhaolist)
                temp_card.extend(u.longlist)
                temp_card.extend(u.handlist)
                if Daer.containSize(temp_card, 2) + Daer.containSize(temp_card, 7) \
                        + Daer.containSize(temp_card, 10) + Daer.containSize(temp_card, 102) \
                        + Daer.containSize(temp_card, 107) + Daer.containSize(temp_card, 110) > 9:
                    settle_type.add(HONGHU)
                    if request.dagun:
                        bang *= 2
                    else:
                        bang += 2
                if Daer.containSize(temp_card, 2) + Daer.containSize(temp_card, 7) \
                        + Daer.containSize(temp_card, 10) + Daer.containSize(temp_card, 102) \
                        + Daer.containSize(temp_card, 107) + Daer.containSize(temp_card, 110) == 0:
                    settle_type.add(HEIHU)
                    bang += 5
                    if request.dagun:
                        bang *= bang
                    else:
                        bang += 5
                if TIANHU in request.settlePatterns:
                    settle_type.add(TIANHU)
                    bang += 5
                if DIHU in request.settlePatterns:
                    settle_type.add(DIHU)
                    bang += 5
                if ZIMO in request.settlePatterns:
                    settle_type.add(ZIMO)
                    bang += 1
                if 0 == len(u.kanlist) + len(u.longlist):
                    settle_type.add(PIAOHU)
                    bang += 1
                if 5 > bang and 0 == hu:
                    bang = 5
                    settle_type.clear()
                    settle_type.add(LANHU)
        for u in request.userSettleData:
            if u.userId == request.huUserId:
                userSettleResult = UserSettleResult()
                userSettleResult.userId = u.userId
                userSettleResult.hu = hu
                userSettleResult.bang = bang
                userSettleResult.score = 2 * hu * bang
                userSettleResult.settlePatterns.extend(settle_type)
                settle.userSettleResule.append(userSettleResult)
            else:
                userSettleResult = UserSettleResult()
                userSettleResult.userId = u.userId
                userSettleResult.score = -hu * bang
                settle.userSettleResule.append(userSettleResult)
        return settle

    def calculate(self, request, context):
        """
        :逻辑计算
        :param request:
        :param context:
        :return:
        """
        print "calculate传入handlist", request.handlist
        print "calculate传入penglist", request.penglist
        calculate = CalculateResult()
        if 1 == request.allocid:
            calculate.chilist.extend(Daer.chi(request.handlist))
            calculate.penglist.extend(Daer.peng(request.handlist))
            calculate.zhaolist.extend(Daer.get_san(request.handlist, request.penglist))
            calculate.hulist.extend(Daer.hu(request.handlist, request.penglist))

        return calculate

    def shuffle(self, request, context):
        """
        :洗牌
        :param request:
        :param context:
        :return:
        """
        shuffle = ShuffleResult()
        cardlist = [1, 1, 1, 1,
                    2, 2, 2, 2,
                    3, 3, 3, 3,
                    4, 4, 4, 4,
                    5, 5, 5, 5,
                    6, 6, 6, 6,
                    7, 7, 7, 7,
                    8, 8, 8, 8,
                    9, 9, 9, 9,
                    10, 10, 10, 10,
                    101, 101, 101, 101,
                    102, 102, 102, 102,
                    103, 103, 103, 103,
                    104, 104, 104, 104,
                    105, 105, 105, 105,
                    106, 106, 106, 106,
                    107, 107, 107, 107,
                    108, 108, 108, 108,
                    109, 109, 109, 109,
                    110, 110, 110, 110]
        random.shuffle(cardlist)
        shuffle.cardlist.extend(cardlist)
        return shuffle


def rpc_server():
    """
    :启动grpc服务
    :return:
    """
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    zipai_pb2_grpc.add_ZipaiServicer_to_server(Performance(), server)
    server.add_insecure_port('[::]:50000')
    server.start()
    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    rpc_server()