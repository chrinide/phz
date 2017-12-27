# coding=utf-8
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: zhipai.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='zhipai.proto',
    package='',
    syntax='proto3',
    serialized_pb=_b(
        '\n\x0czhipai.proto\"i\n\nSettleData\x12\x0f\n\x07\x61llocid\x18\x01 \x01(\x05\x12\x0e\n\x06\x62\x61nker\x18\x02 \x01(\x05\x12\'\n\x0euserSettleData\x18\x03 \x03(\x0b\x32\x0f.UserSettleData\x12\x11\n\textraData\x18\x04 \x01(\x0c\"K\n\x10NiuniuSettleData\x12\x10\n\x08playRule\x18\x01 \x01(\x05\x12\x12\n\ndoubleRule\x18\x02 \x01(\x05\x12\x11\n\tgameRules\x18\x03 \x01(\x05\"7\n\x12PiBanBanSettleData\x12\x10\n\x08playType\x18\x01 \x01(\x05\x12\x0f\n\x07jackpot\x18\x02 \x01(\x05\"O\n\x0eUserSettleData\x12\x0e\n\x06userId\x18\x01 \x01(\x05\x12\x10\n\x08\x63\x61rdlist\x18\x02 \x03(\x05\x12\r\n\x05score\x18\x03 \x01(\x05\x12\x0c\n\x04grab\x18\x04 \x01(\x05\";\n\x0cSettleResult\x12+\n\x10userSettleResule\x18\x01 \x03(\x0b\x32\x11.UserSettleResult\"B\n\x10UserSettleResult\x12\x0e\n\x06userId\x18\x01 \x01(\x05\x12\x11\n\tcardValue\x18\x02 \x01(\x05\x12\x0b\n\x03win\x18\x03 \x01(\x05\"1\n\x0bShuffleData\x12\x0f\n\x07\x61llocid\x18\x01 \x01(\x05\x12\x11\n\textraData\x18\x02 \x01(\x0c\"!\n\rShuffleResult\x12\x10\n\x08\x63\x61rdlist\x18\x01 \x03(\x05\"\x1e\n\nJinhuaData\x12\x10\n\x08gameType\x18\x01 \x01(\x08\x32[\n\x06Zhipai\x12&\n\x06settle\x12\x0b.SettleData\x1a\r.SettleResult\"\x00\x12)\n\x07shuffle\x12\x0c.ShuffleData\x1a\x0e.ShuffleResult\"\x00\x42\x15\n\x11zhipai.mode.protoP\x01\x62\x06proto3')
)

_SETTLEDATA = _descriptor.Descriptor(
    name='SettleData',
    full_name='SettleData',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='allocid', full_name='SettleData.allocid', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='banker', full_name='SettleData.banker', index=1,
            number=2, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='userSettleData', full_name='SettleData.userSettleData', index=2,
            number=3, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='extraData', full_name='SettleData.extraData', index=3,
            number=4, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=_b(""),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=16,
    serialized_end=121,
)

_NIUNIUSETTLEDATA = _descriptor.Descriptor(
    name='NiuniuSettleData',
    full_name='NiuniuSettleData',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='playRule', full_name='NiuniuSettleData.playRule', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='doubleRule', full_name='NiuniuSettleData.doubleRule', index=1,
            number=2, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='gameRules', full_name='NiuniuSettleData.gameRules', index=2,
            number=3, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=123,
    serialized_end=198,
)

_PIBANBANSETTLEDATA = _descriptor.Descriptor(
    name='PiBanBanSettleData',
    full_name='PiBanBanSettleData',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='playType', full_name='PiBanBanSettleData.playType', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='jackpot', full_name='PiBanBanSettleData.jackpot', index=1,
            number=2, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=200,
    serialized_end=255,
)

_USERSETTLEDATA = _descriptor.Descriptor(
    name='UserSettleData',
    full_name='UserSettleData',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='userId', full_name='UserSettleData.userId', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='cardlist', full_name='UserSettleData.cardlist', index=1,
            number=2, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='score', full_name='UserSettleData.score', index=2,
            number=3, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='grab', full_name='UserSettleData.grab', index=3,
            number=4, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=257,
    serialized_end=336,
)

_SETTLERESULT = _descriptor.Descriptor(
    name='SettleResult',
    full_name='SettleResult',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='userSettleResule', full_name='SettleResult.userSettleResule', index=0,
            number=1, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=338,
    serialized_end=397,
)

_USERSETTLERESULT = _descriptor.Descriptor(
    name='UserSettleResult',
    full_name='UserSettleResult',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='userId', full_name='UserSettleResult.userId', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='cardValue', full_name='UserSettleResult.cardValue', index=1,
            number=2, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='win', full_name='UserSettleResult.win', index=2,
            number=3, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=399,
    serialized_end=465,
)

_SHUFFLEDATA = _descriptor.Descriptor(
    name='ShuffleData',
    full_name='ShuffleData',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='allocid', full_name='ShuffleData.allocid', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='extraData', full_name='ShuffleData.extraData', index=1,
            number=2, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=_b(""),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=467,
    serialized_end=516,
)

_SHUFFLERESULT = _descriptor.Descriptor(
    name='ShuffleResult',
    full_name='ShuffleResult',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='cardlist', full_name='ShuffleResult.cardlist', index=0,
            number=1, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=518,
    serialized_end=551,
)

_JINHUADATA = _descriptor.Descriptor(
    name='JinhuaData',
    full_name='JinhuaData',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='gameType', full_name='JinhuaData.gameType', index=0,
            number=1, type=8, cpp_type=7, label=1,
            has_default_value=False, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=553,
    serialized_end=583,
)

_SETTLEDATA.fields_by_name['userSettleData'].message_type = _USERSETTLEDATA
_SETTLERESULT.fields_by_name['userSettleResule'].message_type = _USERSETTLERESULT
DESCRIPTOR.message_types_by_name['SettleData'] = _SETTLEDATA
DESCRIPTOR.message_types_by_name['NiuniuSettleData'] = _NIUNIUSETTLEDATA
DESCRIPTOR.message_types_by_name['PiBanBanSettleData'] = _PIBANBANSETTLEDATA
DESCRIPTOR.message_types_by_name['UserSettleData'] = _USERSETTLEDATA
DESCRIPTOR.message_types_by_name['SettleResult'] = _SETTLERESULT
DESCRIPTOR.message_types_by_name['UserSettleResult'] = _USERSETTLERESULT
DESCRIPTOR.message_types_by_name['ShuffleData'] = _SHUFFLEDATA
DESCRIPTOR.message_types_by_name['ShuffleResult'] = _SHUFFLERESULT
DESCRIPTOR.message_types_by_name['JinhuaData'] = _JINHUADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SettleData = _reflection.GeneratedProtocolMessageType('SettleData', (_message.Message,), dict(
    DESCRIPTOR=_SETTLEDATA,
    __module__='zhipai_pb2'
    # @@protoc_insertion_point(class_scope:SettleData)
))
_sym_db.RegisterMessage(SettleData)

NiuniuSettleData = _reflection.GeneratedProtocolMessageType('NiuniuSettleData', (_message.Message,), dict(
    DESCRIPTOR=_NIUNIUSETTLEDATA,
    __module__='zhipai_pb2'
    # @@protoc_insertion_point(class_scope:NiuniuSettleData)
))
_sym_db.RegisterMessage(NiuniuSettleData)

PiBanBanSettleData = _reflection.GeneratedProtocolMessageType('PiBanBanSettleData', (_message.Message,), dict(
    DESCRIPTOR=_PIBANBANSETTLEDATA,
    __module__='zhipai_pb2'
    # @@protoc_insertion_point(class_scope:PiBanBanSettleData)
))
_sym_db.RegisterMessage(PiBanBanSettleData)

UserSettleData = _reflection.GeneratedProtocolMessageType('UserSettleData', (_message.Message,), dict(
    DESCRIPTOR=_USERSETTLEDATA,
    __module__='zhipai_pb2'
    # @@protoc_insertion_point(class_scope:UserSettleData)
))
_sym_db.RegisterMessage(UserSettleData)

SettleResult = _reflection.GeneratedProtocolMessageType('SettleResult', (_message.Message,), dict(
    DESCRIPTOR=_SETTLERESULT,
    __module__='zhipai_pb2'
    # @@protoc_insertion_point(class_scope:SettleResult)
))
_sym_db.RegisterMessage(SettleResult)

UserSettleResult = _reflection.GeneratedProtocolMessageType('UserSettleResult', (_message.Message,), dict(
    DESCRIPTOR=_USERSETTLERESULT,
    __module__='zhipai_pb2'
    # @@protoc_insertion_point(class_scope:UserSettleResult)
))
_sym_db.RegisterMessage(UserSettleResult)

ShuffleData = _reflection.GeneratedProtocolMessageType('ShuffleData', (_message.Message,), dict(
    DESCRIPTOR=_SHUFFLEDATA,
    __module__='zhipai_pb2'
    # @@protoc_insertion_point(class_scope:ShuffleData)
))
_sym_db.RegisterMessage(ShuffleData)

ShuffleResult = _reflection.GeneratedProtocolMessageType('ShuffleResult', (_message.Message,), dict(
    DESCRIPTOR=_SHUFFLERESULT,
    __module__='zhipai_pb2'
    # @@protoc_insertion_point(class_scope:ShuffleResult)
))
_sym_db.RegisterMessage(ShuffleResult)

JinhuaData = _reflection.GeneratedProtocolMessageType('JinhuaData', (_message.Message,), dict(
    DESCRIPTOR=_JINHUADATA,
    __module__='zhipai_pb2'
    # @@protoc_insertion_point(class_scope:JinhuaData)
))
_sym_db.RegisterMessage(JinhuaData)

DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\021zhipai.mode.protoP\001'))

_ZHIPAI = _descriptor.ServiceDescriptor(
    name='Zhipai',
    full_name='Zhipai',
    file=DESCRIPTOR,
    index=0,
    options=None,
    serialized_start=585,
    serialized_end=676,
    methods=[
        _descriptor.MethodDescriptor(
            name='settle',
            full_name='Zhipai.settle',
            index=0,
            containing_service=None,
            input_type=_SETTLEDATA,
            output_type=_SETTLERESULT,
            options=None,
        ),
        _descriptor.MethodDescriptor(
            name='shuffle',
            full_name='Zhipai.shuffle',
            index=1,
            containing_service=None,
            input_type=_SHUFFLEDATA,
            output_type=_SHUFFLERESULT,
            options=None,
        ),
    ])
_sym_db.RegisterServiceDescriptor(_ZHIPAI)

DESCRIPTOR.services_by_name['Zhipai'] = _ZHIPAI

# @@protoc_insertion_point(module_scope)
