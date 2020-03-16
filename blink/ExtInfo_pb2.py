# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ExtInfo.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ExtInfo.proto',
  package='blink',
  syntax='proto2',
  serialized_options=b'\n\036com.bilibili.bplus.im.protobuf',
  serialized_pb=b'\n\rExtInfo.proto\x12\x05\x62link\"]\n\x07\x45xtInfo\x12\r\n\x05\x62uvid\x18\x02 \x01(\t\x12\r\n\x05refer\x18\x04 \x01(\t\x12\x0e\n\x06seq_no\x18\x06 \x01(\x05\x12\x0b\n\x03sid\x18\x01 \x01(\t\x12\n\n\x02ua\x18\x05 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\tB \n\x1e\x63om.bilibili.bplus.im.protobuf'
)




_EXTINFO = _descriptor.Descriptor(
  name='ExtInfo',
  full_name='blink.ExtInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='buvid', full_name='blink.ExtInfo.buvid', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='refer', full_name='blink.ExtInfo.refer', index=1,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seq_no', full_name='blink.ExtInfo.seq_no', index=2,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sid', full_name='blink.ExtInfo.sid', index=3,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ua', full_name='blink.ExtInfo.ua', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='blink.ExtInfo.url', index=5,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=24,
  serialized_end=117,
)

DESCRIPTOR.message_types_by_name['ExtInfo'] = _EXTINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExtInfo = _reflection.GeneratedProtocolMessageType('ExtInfo', (_message.Message,), {
  'DESCRIPTOR' : _EXTINFO,
  '__module__' : 'ExtInfo_pb2'
  # @@protoc_insertion_point(class_scope:blink.ExtInfo)
  })
_sym_db.RegisterMessage(ExtInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)