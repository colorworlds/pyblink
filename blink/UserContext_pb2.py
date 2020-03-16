# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: UserContext.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import TracePoint_pb2 as TracePoint__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='UserContext.proto',
  package='blink',
  syntax='proto2',
  serialized_options=b'\n\036com.bilibili.bplus.im.protobuf',
  serialized_pb=b'\n\x11UserContext.proto\x12\x05\x62link\x1a\x10TracePoint.proto\"\xed\x01\n\x0bUserContext\x12\x0e\n\x06\x63li_ip\x18\x02 \x02(\t\x12\x0f\n\x07\x63onn_ip\x18\x03 \x02(\t\x12\x11\n\tconn_port\x18\x04 \x02(\x05\x12\x11\n\tdev_crc32\x18\x07 \x01(\x05\x12\x10\n\x08\x64\x65v_type\x18\x05 \x01(\x05\x12\x11\n\tflag_test\x18\n \x01(\x05\x12\x10\n\x08platform\x18\x0b \x01(\t\x12\x13\n\x0bss_trace_id\x18\x06 \x01(\x04\x12\x15\n\rss_trace_id_s\x18\t \x01(\t\x12\'\n\x0ctrace_points\x18\x08 \x03(\x0b\x32\x11.blink.TracePoint\x12\x0b\n\x03uid\x18\x01 \x02(\x04\x42 \n\x1e\x63om.bilibili.bplus.im.protobuf'
  ,
  dependencies=[TracePoint__pb2.DESCRIPTOR,])




_USERCONTEXT = _descriptor.Descriptor(
  name='UserContext',
  full_name='blink.UserContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cli_ip', full_name='blink.UserContext.cli_ip', index=0,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conn_ip', full_name='blink.UserContext.conn_ip', index=1,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conn_port', full_name='blink.UserContext.conn_port', index=2,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dev_crc32', full_name='blink.UserContext.dev_crc32', index=3,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dev_type', full_name='blink.UserContext.dev_type', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flag_test', full_name='blink.UserContext.flag_test', index=5,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='platform', full_name='blink.UserContext.platform', index=6,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ss_trace_id', full_name='blink.UserContext.ss_trace_id', index=7,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ss_trace_id_s', full_name='blink.UserContext.ss_trace_id_s', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trace_points', full_name='blink.UserContext.trace_points', index=9,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uid', full_name='blink.UserContext.uid', index=10,
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
  serialized_start=47,
  serialized_end=284,
)

_USERCONTEXT.fields_by_name['trace_points'].message_type = TracePoint__pb2._TRACEPOINT
DESCRIPTOR.message_types_by_name['UserContext'] = _USERCONTEXT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserContext = _reflection.GeneratedProtocolMessageType('UserContext', (_message.Message,), {
  'DESCRIPTOR' : _USERCONTEXT,
  '__module__' : 'UserContext_pb2'
  # @@protoc_insertion_point(class_scope:blink.UserContext)
  })
_sym_db.RegisterMessage(UserContext)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)