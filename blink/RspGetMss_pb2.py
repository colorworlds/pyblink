# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RspGetMss.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import MssItem_pb2 as MssItem__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='RspGetMss.proto',
  package='blink',
  syntax='proto2',
  serialized_options=b'\n\036com.bilibili.bplus.im.protobuf',
  serialized_pb=b'\n\x0fRspGetMss.proto\x12\x05\x62link\x1a\rMssItem.proto\")\n\tRspGetMss\x12\x1c\n\x04item\x18\x01 \x03(\x0b\x32\x0e.blink.MssItemB \n\x1e\x63om.bilibili.bplus.im.protobuf'
  ,
  dependencies=[MssItem__pb2.DESCRIPTOR,])




_RSPGETMSS = _descriptor.Descriptor(
  name='RspGetMss',
  full_name='blink.RspGetMss',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='blink.RspGetMss.item', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=41,
  serialized_end=82,
)

_RSPGETMSS.fields_by_name['item'].message_type = MssItem__pb2._MSSITEM
DESCRIPTOR.message_types_by_name['RspGetMss'] = _RSPGETMSS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RspGetMss = _reflection.GeneratedProtocolMessageType('RspGetMss', (_message.Message,), {
  'DESCRIPTOR' : _RSPGETMSS,
  '__module__' : 'RspGetMss_pb2'
  # @@protoc_insertion_point(class_scope:blink.RspGetMss)
  })
_sym_db.RegisterMessage(RspGetMss)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
