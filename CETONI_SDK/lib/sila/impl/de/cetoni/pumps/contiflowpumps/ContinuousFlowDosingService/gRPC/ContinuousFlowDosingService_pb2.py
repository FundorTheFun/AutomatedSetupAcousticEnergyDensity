# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ContinuousFlowDosingService.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import sila2lib.framework.SiLAFramework_pb2 as SiLAFramework__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ContinuousFlowDosingService.proto',
  package='sila2.de.cetoni.pumps.contiflowpumps.continuousflowdosingservice.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!ContinuousFlowDosingService.proto\x12\x43sila2.de.cetoni.pumps.contiflowpumps.continuousflowdosingservice.v1\x1a\x13SiLAFramework.proto\"I\n\x17GenerateFlow_Parameters\x12.\n\x08\x46lowRate\x18\x01 \x01(\x0b\x32\x1c.sila2.org.silastandard.Real\"\x18\n\x16GenerateFlow_Responses\"\x17\n\x15StopDosage_Parameters\"\x16\n\x14StopDosage_Responses\"\"\n Subscribe_MaxFlowRate_Parameters\"T\n\x1fSubscribe_MaxFlowRate_Responses\x12\x31\n\x0bMaxFlowRate\x18\x01 \x01(\x0b\x32\x1c.sila2.org.silastandard.Real\"\x1f\n\x1dSubscribe_FlowRate_Parameters\"N\n\x1cSubscribe_FlowRate_Responses\x12.\n\x08\x46lowRate\x18\x01 \x01(\x0b\x32\x1c.sila2.org.silastandard.Real2\xe3\x08\n\x1b\x43ontinuousFlowDosingService\x12\x9b\x01\n\x0cGenerateFlow\x12\\.sila2.de.cetoni.pumps.contiflowpumps.continuousflowdosingservice.v1.GenerateFlow_Parameters\x1a+.sila2.org.silastandard.CommandConfirmation\"\x00\x12l\n\x11GenerateFlow_Info\x12,.sila2.org.silastandard.CommandExecutionUUID\x1a%.sila2.org.silastandard.ExecutionInfo\"\x00\x30\x01\x12\xa2\x01\n\x13GenerateFlow_Result\x12,.sila2.org.silastandard.CommandExecutionUUID\x1a[.sila2.de.cetoni.pumps.contiflowpumps.continuousflowdosingservice.v1.GenerateFlow_Responses\"\x00\x12\xc5\x01\n\nStopDosage\x12Z.sila2.de.cetoni.pumps.contiflowpumps.continuousflowdosingservice.v1.StopDosage_Parameters\x1aY.sila2.de.cetoni.pumps.contiflowpumps.continuousflowdosingservice.v1.StopDosage_Responses\"\x00\x12\xe8\x01\n\x15Subscribe_MaxFlowRate\x12\x65.sila2.de.cetoni.pumps.contiflowpumps.continuousflowdosingservice.v1.Subscribe_MaxFlowRate_Parameters\x1a\x64.sila2.de.cetoni.pumps.contiflowpumps.continuousflowdosingservice.v1.Subscribe_MaxFlowRate_Responses\"\x00\x30\x01\x12\xdf\x01\n\x12Subscribe_FlowRate\x12\x62.sila2.de.cetoni.pumps.contiflowpumps.continuousflowdosingservice.v1.Subscribe_FlowRate_Parameters\x1a\x61.sila2.de.cetoni.pumps.contiflowpumps.continuousflowdosingservice.v1.Subscribe_FlowRate_Responses\"\x00\x30\x01\x62\x06proto3'
  ,
  dependencies=[SiLAFramework__pb2.DESCRIPTOR,])




_GENERATEFLOW_PARAMETERS = _descriptor.Descriptor(
  name='GenerateFlow_Parameters',
  full_name='sila2.de.cetoni.pumps.contiflowpumps.continuousflowdosingservice.v1.GenerateFlow_Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='FlowRate', full_name='sila2.de.cetoni.pumps.contiflowpumps.continuousflowdosingservice.v1.GenerateFlow_Parameters.FlowRate', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=127,
  serialized_end=200,
)


_GENERATEFLOW_RESPONSES = _descriptor.Descriptor(
  name='GenerateFlow_Responses',
  full_name='sila2.de.cetoni.pumps.contiflowpumps.continuousflowdosingservice.v1.GenerateFlow_Responses',
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
  serialized_start=202,
  serialized_end=226,
)


_STOPDOSAGE_PARAMETERS = _descriptor.Descriptor(
  name='StopDosage_Parameters',
  full_name='sila2.de.cetoni.pumps.contiflowpumps.continuousflowdosingservice.v1.StopDosage_Parameters',
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
  serialized_start=228,
  serialized_end=251,
)


_STOPDOSAGE_RESPONSES = _descriptor.Descriptor(
  name='StopDosage_Responses',
  full_name='sila2.de.cetoni.pumps.contiflowpumps.continuousflowdosingservice.v1.StopDosage_Responses',
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
  serialized_start=253,
  serialized_end=275,
)


_SUBSCRIBE_MAXFLOWRATE_PARAMETERS = _descriptor.Descriptor(
  name='Subscribe_MaxFlowRate_Parameters',
  full_name='sila2.de.cetoni.pumps.contiflowpumps.continuousflowdosingservice.v1.Subscribe_MaxFlowRate_Parameters',
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
  serialized_start=277,
  serialized_end=311,
)


_SUBSCRIBE_MAXFLOWRATE_RESPONSES = _descriptor.Descriptor(
  name='Subscribe_MaxFlowRate_Responses',
  full_name='sila2.de.cetoni.pumps.contiflowpumps.continuousflowdosingservice.v1.Subscribe_MaxFlowRate_Responses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='MaxFlowRate', full_name='sila2.de.cetoni.pumps.contiflowpumps.continuousflowdosingservice.v1.Subscribe_MaxFlowRate_Responses.MaxFlowRate', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=313,
  serialized_end=397,
)


_SUBSCRIBE_FLOWRATE_PARAMETERS = _descriptor.Descriptor(
  name='Subscribe_FlowRate_Parameters',
  full_name='sila2.de.cetoni.pumps.contiflowpumps.continuousflowdosingservice.v1.Subscribe_FlowRate_Parameters',
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
  serialized_start=399,
  serialized_end=430,
)


_SUBSCRIBE_FLOWRATE_RESPONSES = _descriptor.Descriptor(
  name='Subscribe_FlowRate_Responses',
  full_name='sila2.de.cetoni.pumps.contiflowpumps.continuousflowdosingservice.v1.Subscribe_FlowRate_Responses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='FlowRate', full_name='sila2.de.cetoni.pumps.contiflowpumps.continuousflowdosingservice.v1.Subscribe_FlowRate_Responses.FlowRate', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=432,
  serialized_end=510,
)

_GENERATEFLOW_PARAMETERS.fields_by_name['FlowRate'].message_type = SiLAFramework__pb2._REAL
_SUBSCRIBE_MAXFLOWRATE_RESPONSES.fields_by_name['MaxFlowRate'].message_type = SiLAFramework__pb2._REAL
_SUBSCRIBE_FLOWRATE_RESPONSES.fields_by_name['FlowRate'].message_type = SiLAFramework__pb2._REAL
DESCRIPTOR.message_types_by_name['GenerateFlow_Parameters'] = _GENERATEFLOW_PARAMETERS
DESCRIPTOR.message_types_by_name['GenerateFlow_Responses'] = _GENERATEFLOW_RESPONSES
DESCRIPTOR.message_types_by_name['StopDosage_Parameters'] = _STOPDOSAGE_PARAMETERS
DESCRIPTOR.message_types_by_name['StopDosage_Responses'] = _STOPDOSAGE_RESPONSES
DESCRIPTOR.message_types_by_name['Subscribe_MaxFlowRate_Parameters'] = _SUBSCRIBE_MAXFLOWRATE_PARAMETERS
DESCRIPTOR.message_types_by_name['Subscribe_MaxFlowRate_Responses'] = _SUBSCRIBE_MAXFLOWRATE_RESPONSES
DESCRIPTOR.message_types_by_name['Subscribe_FlowRate_Parameters'] = _SUBSCRIBE_FLOWRATE_PARAMETERS
DESCRIPTOR.message_types_by_name['Subscribe_FlowRate_Responses'] = _SUBSCRIBE_FLOWRATE_RESPONSES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenerateFlow_Parameters = _reflection.GeneratedProtocolMessageType('GenerateFlow_Parameters', (_message.Message,), {
  'DESCRIPTOR' : _GENERATEFLOW_PARAMETERS,
  '__module__' : 'ContinuousFlowDosingService_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.contiflowpumps.continuousflowdosingservice.v1.GenerateFlow_Parameters)
  })
_sym_db.RegisterMessage(GenerateFlow_Parameters)

GenerateFlow_Responses = _reflection.GeneratedProtocolMessageType('GenerateFlow_Responses', (_message.Message,), {
  'DESCRIPTOR' : _GENERATEFLOW_RESPONSES,
  '__module__' : 'ContinuousFlowDosingService_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.contiflowpumps.continuousflowdosingservice.v1.GenerateFlow_Responses)
  })
_sym_db.RegisterMessage(GenerateFlow_Responses)

StopDosage_Parameters = _reflection.GeneratedProtocolMessageType('StopDosage_Parameters', (_message.Message,), {
  'DESCRIPTOR' : _STOPDOSAGE_PARAMETERS,
  '__module__' : 'ContinuousFlowDosingService_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.contiflowpumps.continuousflowdosingservice.v1.StopDosage_Parameters)
  })
_sym_db.RegisterMessage(StopDosage_Parameters)

StopDosage_Responses = _reflection.GeneratedProtocolMessageType('StopDosage_Responses', (_message.Message,), {
  'DESCRIPTOR' : _STOPDOSAGE_RESPONSES,
  '__module__' : 'ContinuousFlowDosingService_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.contiflowpumps.continuousflowdosingservice.v1.StopDosage_Responses)
  })
_sym_db.RegisterMessage(StopDosage_Responses)

Subscribe_MaxFlowRate_Parameters = _reflection.GeneratedProtocolMessageType('Subscribe_MaxFlowRate_Parameters', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBE_MAXFLOWRATE_PARAMETERS,
  '__module__' : 'ContinuousFlowDosingService_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.contiflowpumps.continuousflowdosingservice.v1.Subscribe_MaxFlowRate_Parameters)
  })
_sym_db.RegisterMessage(Subscribe_MaxFlowRate_Parameters)

Subscribe_MaxFlowRate_Responses = _reflection.GeneratedProtocolMessageType('Subscribe_MaxFlowRate_Responses', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBE_MAXFLOWRATE_RESPONSES,
  '__module__' : 'ContinuousFlowDosingService_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.contiflowpumps.continuousflowdosingservice.v1.Subscribe_MaxFlowRate_Responses)
  })
_sym_db.RegisterMessage(Subscribe_MaxFlowRate_Responses)

Subscribe_FlowRate_Parameters = _reflection.GeneratedProtocolMessageType('Subscribe_FlowRate_Parameters', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBE_FLOWRATE_PARAMETERS,
  '__module__' : 'ContinuousFlowDosingService_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.contiflowpumps.continuousflowdosingservice.v1.Subscribe_FlowRate_Parameters)
  })
_sym_db.RegisterMessage(Subscribe_FlowRate_Parameters)

Subscribe_FlowRate_Responses = _reflection.GeneratedProtocolMessageType('Subscribe_FlowRate_Responses', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBE_FLOWRATE_RESPONSES,
  '__module__' : 'ContinuousFlowDosingService_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.contiflowpumps.continuousflowdosingservice.v1.Subscribe_FlowRate_Responses)
  })
_sym_db.RegisterMessage(Subscribe_FlowRate_Responses)



_CONTINUOUSFLOWDOSINGSERVICE = _descriptor.ServiceDescriptor(
  name='ContinuousFlowDosingService',
  full_name='sila2.de.cetoni.pumps.contiflowpumps.continuousflowdosingservice.v1.ContinuousFlowDosingService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=513,
  serialized_end=1636,
  methods=[
  _descriptor.MethodDescriptor(
    name='GenerateFlow',
    full_name='sila2.de.cetoni.pumps.contiflowpumps.continuousflowdosingservice.v1.ContinuousFlowDosingService.GenerateFlow',
    index=0,
    containing_service=None,
    input_type=_GENERATEFLOW_PARAMETERS,
    output_type=SiLAFramework__pb2._COMMANDCONFIRMATION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GenerateFlow_Info',
    full_name='sila2.de.cetoni.pumps.contiflowpumps.continuousflowdosingservice.v1.ContinuousFlowDosingService.GenerateFlow_Info',
    index=1,
    containing_service=None,
    input_type=SiLAFramework__pb2._COMMANDEXECUTIONUUID,
    output_type=SiLAFramework__pb2._EXECUTIONINFO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GenerateFlow_Result',
    full_name='sila2.de.cetoni.pumps.contiflowpumps.continuousflowdosingservice.v1.ContinuousFlowDosingService.GenerateFlow_Result',
    index=2,
    containing_service=None,
    input_type=SiLAFramework__pb2._COMMANDEXECUTIONUUID,
    output_type=_GENERATEFLOW_RESPONSES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StopDosage',
    full_name='sila2.de.cetoni.pumps.contiflowpumps.continuousflowdosingservice.v1.ContinuousFlowDosingService.StopDosage',
    index=3,
    containing_service=None,
    input_type=_STOPDOSAGE_PARAMETERS,
    output_type=_STOPDOSAGE_RESPONSES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Subscribe_MaxFlowRate',
    full_name='sila2.de.cetoni.pumps.contiflowpumps.continuousflowdosingservice.v1.ContinuousFlowDosingService.Subscribe_MaxFlowRate',
    index=4,
    containing_service=None,
    input_type=_SUBSCRIBE_MAXFLOWRATE_PARAMETERS,
    output_type=_SUBSCRIBE_MAXFLOWRATE_RESPONSES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Subscribe_FlowRate',
    full_name='sila2.de.cetoni.pumps.contiflowpumps.continuousflowdosingservice.v1.ContinuousFlowDosingService.Subscribe_FlowRate',
    index=5,
    containing_service=None,
    input_type=_SUBSCRIBE_FLOWRATE_PARAMETERS,
    output_type=_SUBSCRIBE_FLOWRATE_RESPONSES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CONTINUOUSFLOWDOSINGSERVICE)

DESCRIPTOR.services_by_name['ContinuousFlowDosingService'] = _CONTINUOUSFLOWDOSINGSERVICE

# @@protoc_insertion_point(module_scope)
