# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ReqAckApplyFriend.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ReqAckApplyFriend.proto',
  package='blink',
  syntax='proto2',
  serialized_options=b'\n\036com.bilibili.bplus.im.protobuf',
  serialized_pb=b'\n\x17ReqAckApplyFriend.proto\x12\x05\x62link\"M\n\x11ReqAckApplyFriend\x12\x10\n\x08\x61pply_id\x18\x01 \x02(\x04\x12\x0f\n\x07op_code\x18\x02 \x02(\r\x12\x15\n\rreply_content\x18\x03 \x01(\tB \n\x1e\x63om.bilibili.bplus.im.protobuf'
)




_REQACKAPPLYFRIEND = _descriptor.Descriptor(
  name='ReqAckApplyFriend',
  full_name='blink.ReqAckApplyFriend',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='apply_id', full_name='blink.ReqAckApplyFriend.apply_id', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='op_code', full_name='blink.ReqAckApplyFriend.op_code', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reply_content', full_name='blink.ReqAckApplyFriend.reply_content', index=2,
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
  serialized_start=34,
  serialized_end=111,
)

DESCRIPTOR.message_types_by_name['ReqAckApplyFriend'] = _REQACKAPPLYFRIEND
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReqAckApplyFriend = _reflection.GeneratedProtocolMessageType('ReqAckApplyFriend', (_message.Message,), {
  'DESCRIPTOR' : _REQACKAPPLYFRIEND,
  '__module__' : 'ReqAckApplyFriend_pb2'
  # @@protoc_insertion_point(class_scope:blink.ReqAckApplyFriend)
  })
_sym_db.RegisterMessage(ReqAckApplyFriend)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
