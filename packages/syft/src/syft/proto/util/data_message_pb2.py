# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/util/data_message.proto
"""Generated protocol buffer code."""
# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/util/data_message.proto",
    package="syft.util",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x1dproto/util/data_message.proto\x12\tsyft.util"0\n\x0b\x44\x61taMessage\x12\x10\n\x08obj_type\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\x0c\x62\x06proto3',
)


_DATAMESSAGE = _descriptor.Descriptor(
    name="DataMessage",
    full_name="syft.util.DataMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="obj_type",
            full_name="syft.util.DataMessage.obj_type",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="content",
            full_name="syft.util.DataMessage.content",
            index=1,
            number=2,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=44,
    serialized_end=92,
)

DESCRIPTOR.message_types_by_name["DataMessage"] = _DATAMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DataMessage = _reflection.GeneratedProtocolMessageType(
    "DataMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _DATAMESSAGE,
        "__module__": "proto.util.data_message_pb2"
        # @@protoc_insertion_point(class_scope:syft.util.DataMessage)
    },
)
_sym_db.RegisterMessage(DataMessage)


# @@protoc_insertion_point(module_scope)
