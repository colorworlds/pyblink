# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ReqRebuildCacheCb.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ReqRebuildCacheCb.proto',
  package='blink',
  syntax='proto2',
  serialized_options=b'\n\036com.bilibili.bplus.im.protobuf',
  serialized_pb=b'\n\x17ReqRebuildCacheCb.proto\x12\x05\x62link\"5\n\x11ReqRebuildCacheCb\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x13\n\x0bmsg_content\x18\x01 \x01(\tB \n\x1e\x63om.bilibili.bplus.im.protobuf'
)




_REQREBUILDCACHECB = _descriptor.Descriptor(
  name='ReqRebuildCacheCb',
  full_name='blink.ReqRebuildCacheCb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='blink.ReqRebuildCacheCb.msg', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg_content', full_name='blink.ReqRebuildCacheCb.msg_content', index=1,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=34,
  serialized_end=87,
)

DESCRIPTOR.message_types_by_name['ReqRebuildCacheCb'] = _REQREBUILDCACHECB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReqRebuildCacheCb = _reflection.GeneratedProtocolMessageType('ReqRebuildCacheCb', (_message.Message,), {
  'DESCRIPTOR' : _REQREBUILDCACHECB,
  '__module__' : 'ReqRebuildCacheCb_pb2'
  # @@protoc_insertion_point(class_scope:blink.ReqRebuildCacheCb)
  })
_sym_db.RegisterMessage(ReqRebuildCacheCb)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)