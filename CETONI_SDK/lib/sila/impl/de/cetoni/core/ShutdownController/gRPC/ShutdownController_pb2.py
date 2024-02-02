# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ShutdownController.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import sila2lib.framework.SiLAFramework_pb2 as SiLAFramework__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ShutdownController.proto',
  package='sila2.de.cetoni.pumps.syringepumps.shutdowncontroller.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18ShutdownController.proto\x12\x38sila2.de.cetoni.pumps.syringepumps.shutdowncontroller.v1\x1a\x13SiLAFramework.proto\"\x15\n\x13Shutdown_Parameters\"\x14\n\x12Shutdown_Responses2\x9b\x03\n\x12ShutdownController\x12\x88\x01\n\x08Shutdown\x12M.sila2.de.cetoni.pumps.syringepumps.shutdowncontroller.v1.Shutdown_Parameters\x1a+.sila2.org.silastandard.CommandConfirmation\"\x00\x12h\n\rShutdown_Info\x12,.sila2.org.silastandard.CommandExecutionUUID\x1a%.sila2.org.silastandard.ExecutionInfo\"\x00\x30\x01\x12\x8f\x01\n\x0fShutdown_Result\x12,.sila2.org.silastandard.CommandExecutionUUID\x1aL.sila2.de.cetoni.pumps.syringepumps.shutdowncontroller.v1.Shutdown_Responses\"\x00\x62\x06proto3'
  ,
  dependencies=[SiLAFramework__pb2.DESCRIPTOR,])




_SHUTDOWN_PARAMETERS = _descriptor.Descriptor(
  name='Shutdown_Parameters',
  full_name='sila2.de.cetoni.pumps.syringepumps.shutdowncontroller.v1.Shutdown_Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=107,
  serialized_end=128,
)


_SHUTDOWN_RESPONSES = _descriptor.Descriptor(
  name='Shutdown_Responses',
  full_name='sila2.de.cetoni.pumps.syringepumps.shutdowncontroller.v1.Shutdown_Responses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=130,
  serialized_end=150,
)

DESCRIPTOR.message_types_by_name['Shutdown_Parameters'] = _SHUTDOWN_PARAMETERS
DESCRIPTOR.message_types_by_name['Shutdown_Responses'] = _SHUTDOWN_RESPONSES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Shutdown_Parameters = _reflection.GeneratedProtocolMessageType('Shutdown_Parameters', (_message.Message,), {
  'DESCRIPTOR' : _SHUTDOWN_PARAMETERS,
  '__module__' : 'ShutdownController_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.syringepumps.shutdowncontroller.v1.Shutdown_Parameters)
  })
_sym_db.RegisterMessage(Shutdown_Parameters)

Shutdown_Responses = _reflection.GeneratedProtocolMessageType('Shutdown_Responses', (_message.Message,), {
  'DESCRIPTOR' : _SHUTDOWN_RESPONSES,
  '__module__' : 'ShutdownController_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.syringepumps.shutdowncontroller.v1.Shutdown_Responses)
  })
_sym_db.RegisterMessage(Shutdown_Responses)



_SHUTDOWNCONTROLLER = _descriptor.ServiceDescriptor(
  name='ShutdownController',
  full_name='sila2.de.cetoni.pumps.syringepumps.shutdowncontroller.v1.ShutdownController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=153,
  serialized_end=564,
  methods=[
  _descriptor.MethodDescriptor(
    name='Shutdown',
    full_name='sila2.de.cetoni.pumps.syringepumps.shutdowncontroller.v1.ShutdownController.Shutdown',
    index=0,
    containing_service=None,
    input_type=_SHUTDOWN_PARAMETERS,
    output_type=SiLAFramework__pb2._COMMANDCONFIRMATION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Shutdown_Info',
    full_name='sila2.de.cetoni.pumps.syringepumps.shutdowncontroller.v1.ShutdownController.Shutdown_Info',
    index=1,
    containing_service=None,
    input_type=SiLAFramework__pb2._COMMANDEXECUTIONUUID,
    output_type=SiLAFramework__pb2._EXECUTIONINFO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Shutdown_Result',
    full_name='sila2.de.cetoni.pumps.syringepumps.shutdowncontroller.v1.ShutdownController.Shutdown_Result',
    index=2,
    containing_service=None,
    input_type=SiLAFramework__pb2._COMMANDEXECUTIONUUID,
    output_type=_SHUTDOWN_RESPONSES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SHUTDOWNCONTROLLER)

DESCRIPTOR.services_by_name['ShutdownController'] = _SHUTDOWNCONTROLLER

# @@protoc_insertion_point(module_scope)
