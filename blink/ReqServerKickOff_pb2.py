# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ReqServerKickOff.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ReqServerKickOff.proto',
  package='blink',
  syntax='proto2',
  serialized_options=b'\n\036com.bilibili.bplus.im.protobuf',
  serialized_pb=b'\n\x16ReqServerKickOff.proto\x12\x05\x62link\"Z\n\x10ReqServerKickOff\x12\x0e\n\x06\x64\x65v_id\x18\x03 \x01(\t\x12\x10\n\x08\x64\x65v_type\x18\x02 \x01(\x05\x12\x10\n\x08login_ip\x18\x01 \x01(\t\x12\x12\n\nlogin_time\x18\x04 \x01(\x04\x42 \n\x1e\x63om.bilibili.bplus.im.protobuf'
)




_REQSERVERKICKOFF = _descriptor.Descriptor(
  name='ReqServerKickOff',
  full_name='blink.ReqServerKickOff',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dev_id', full_name='blink.ReqServerKickOff.dev_id', index=0,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dev_type', full_name='blink.ReqServerKickOff.dev_type', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='login_ip', full_name='blink.ReqServerKickOff.login_ip', index=2,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='login_time', full_name='blink.ReqServerKickOff.login_time', index=3,
      number=4, type=4, cpp_type=4, label=1,
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
  serialized_start=33,
  serialized_end=123,
)

DESCRIPTOR.message_types_by_name['ReqServerKickOff'] = _REQSERVERKICKOFF
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReqServerKickOff = _reflection.GeneratedProtocolMessageType('ReqServerKickOff', (_message.Message,), {
  'DESCRIPTOR' : _REQSERVERKICKOFF,
  '__module__' : 'ReqServerKickOff_pb2'
  # @@protoc_insertion_point(class_scope:blink.ReqServerKickOff)
  })
_sym_db.RegisterMessage(ReqServerKickOff)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
