# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ReqApplyFriend.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ReqApplyFriend.proto',
  package='blink',
  syntax='proto2',
  serialized_options=b'\n\036com.bilibili.bplus.im.protobuf',
  serialized_pb=b'\n\x14ReqApplyFriend.proto\x12\x05\x62link\"F\n\x0eReqApplyFriend\x12\x12\n\nfriend_uid\x18\x02 \x02(\x04\x12\x0b\n\x03uid\x18\x01 \x02(\x04\x12\x13\n\x0bverify_text\x18\x03 \x01(\tB \n\x1e\x63om.bilibili.bplus.im.protobuf'
)




_REQAPPLYFRIEND = _descriptor.Descriptor(
  name='ReqApplyFriend',
  full_name='blink.ReqApplyFriend',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='friend_uid', full_name='blink.ReqApplyFriend.friend_uid', index=0,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uid', full_name='blink.ReqApplyFriend.uid', index=1,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='verify_text', full_name='blink.ReqApplyFriend.verify_text', index=2,
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
  serialized_start=31,
  serialized_end=101,
)

DESCRIPTOR.message_types_by_name['ReqApplyFriend'] = _REQAPPLYFRIEND
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReqApplyFriend = _reflection.GeneratedProtocolMessageType('ReqApplyFriend', (_message.Message,), {
  'DESCRIPTOR' : _REQAPPLYFRIEND,
  '__module__' : 'ReqApplyFriend_pb2'
  # @@protoc_insertion_point(class_scope:blink.ReqApplyFriend)
  })
_sym_db.RegisterMessage(ReqApplyFriend)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)