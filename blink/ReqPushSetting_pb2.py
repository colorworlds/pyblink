# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ReqPushSetting.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ReqPushSetting.proto',
  package='blink',
  syntax='proto2',
  serialized_options=b'\n\036com.bilibili.bplus.im.protobuf',
  serialized_pb=b'\n\x14ReqPushSetting.proto\x12\x05\x62link\"c\n\x0eReqPushSetting\x12\x13\n\x0b\x62usiness_id\x18\x01 \x02(\x05\x12\x12\n\nmsg_src_id\x18\x03 \x02(\x04\x12\x14\n\x0cmsg_src_type\x18\x02 \x02(\x05\x12\x12\n\npush_state\x18\x04 \x02(\x05\x42 \n\x1e\x63om.bilibili.bplus.im.protobuf'
)




_REQPUSHSETTING = _descriptor.Descriptor(
  name='ReqPushSetting',
  full_name='blink.ReqPushSetting',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='business_id', full_name='blink.ReqPushSetting.business_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg_src_id', full_name='blink.ReqPushSetting.msg_src_id', index=1,
      number=3, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg_src_type', full_name='blink.ReqPushSetting.msg_src_type', index=2,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='push_state', full_name='blink.ReqPushSetting.push_state', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=130,
)

DESCRIPTOR.message_types_by_name['ReqPushSetting'] = _REQPUSHSETTING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReqPushSetting = _reflection.GeneratedProtocolMessageType('ReqPushSetting', (_message.Message,), {
  'DESCRIPTOR' : _REQPUSHSETTING,
  '__module__' : 'ReqPushSetting_pb2'
  # @@protoc_insertion_point(class_scope:blink.ReqPushSetting)
  })
_sym_db.RegisterMessage(ReqPushSetting)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
