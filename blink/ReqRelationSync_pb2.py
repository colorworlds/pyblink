# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ReqRelationSync.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ReqRelationSync.proto',
  package='blink',
  syntax='proto2',
  serialized_options=b'\n\036com.bilibili.bplus.im.protobuf',
  serialized_pb=b'\n\x15ReqRelationSync.proto\x12\x05\x62link\"6\n\x0fReqRelationSync\x12#\n\x1b\x63lient_relation_oplog_seqno\x18\x01 \x02(\x04\x42 \n\x1e\x63om.bilibili.bplus.im.protobuf'
)




_REQRELATIONSYNC = _descriptor.Descriptor(
  name='ReqRelationSync',
  full_name='blink.ReqRelationSync',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_relation_oplog_seqno', full_name='blink.ReqRelationSync.client_relation_oplog_seqno', index=0,
      number=1, type=4, cpp_type=4, label=2,
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
  serialized_start=32,
  serialized_end=86,
)

DESCRIPTOR.message_types_by_name['ReqRelationSync'] = _REQRELATIONSYNC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReqRelationSync = _reflection.GeneratedProtocolMessageType('ReqRelationSync', (_message.Message,), {
  'DESCRIPTOR' : _REQRELATIONSYNC,
  '__module__' : 'ReqRelationSync_pb2'
  # @@protoc_insertion_point(class_scope:blink.ReqRelationSync)
  })
_sym_db.RegisterMessage(ReqRelationSync)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
