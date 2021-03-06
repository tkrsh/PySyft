# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/lib/sympc/session.proto
"""Generated protocol buffer code."""
# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


# syft absolute
from syft.proto.core.node.common import (
    client_pb2 as proto_dot_core_dot_node_dot_common_dot_client__pb2,
)
from syft.proto.lib.python import dict_pb2 as proto_dot_lib_dot_python_dot_dict__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/lib/sympc/session.proto",
    package="syft.lib.sympc",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x1dproto/lib/sympc/session.proto\x12\x0esyft.lib.sympc\x1a#proto/core/node/common/client.proto\x1a\x1bproto/lib/python/dict.proto"\xe4\x01\n\nMPCSession\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0c\n\x04rank\x18\x02 \x01(\x05\x12\x11\n\tring_size\x18\x03 \x01(\x0c\x12\x12\n\nnr_parties\x18\x04 \x01(\x0c\x12%\n\x06\x63onfig\x18\x05 \x01(\x0b\x32\x15.syft.lib.python.Dict\x12.\n\x07parties\x18\x06 \x03(\x0b\x32\x1d.syft.core.node.common.Client\x12*\n\x03ttp\x18\x07 \x01(\x0b\x32\x1d.syft.core.node.common.Client\x12\x10\n\x08protocol\x18\x08 \x01(\x0c\x62\x06proto3',
    dependencies=[
        proto_dot_core_dot_node_dot_common_dot_client__pb2.DESCRIPTOR,
        proto_dot_lib_dot_python_dot_dict__pb2.DESCRIPTOR,
    ],
)


_MPCSESSION = _descriptor.Descriptor(
    name="MPCSession",
    full_name="syft.lib.sympc.MPCSession",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="uuid",
            full_name="syft.lib.sympc.MPCSession.uuid",
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
            name="rank",
            full_name="syft.lib.sympc.MPCSession.rank",
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
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
            name="ring_size",
            full_name="syft.lib.sympc.MPCSession.ring_size",
            index=2,
            number=3,
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
        _descriptor.FieldDescriptor(
            name="nr_parties",
            full_name="syft.lib.sympc.MPCSession.nr_parties",
            index=3,
            number=4,
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
        _descriptor.FieldDescriptor(
            name="config",
            full_name="syft.lib.sympc.MPCSession.config",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
            name="parties",
            full_name="syft.lib.sympc.MPCSession.parties",
            index=5,
            number=6,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
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
            name="ttp",
            full_name="syft.lib.sympc.MPCSession.ttp",
            index=6,
            number=7,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
            name="protocol",
            full_name="syft.lib.sympc.MPCSession.protocol",
            index=7,
            number=8,
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
    serialized_start=116,
    serialized_end=344,
)

_MPCSESSION.fields_by_name[
    "config"
].message_type = proto_dot_lib_dot_python_dot_dict__pb2._DICT
_MPCSESSION.fields_by_name[
    "parties"
].message_type = proto_dot_core_dot_node_dot_common_dot_client__pb2._CLIENT
_MPCSESSION.fields_by_name[
    "ttp"
].message_type = proto_dot_core_dot_node_dot_common_dot_client__pb2._CLIENT
DESCRIPTOR.message_types_by_name["MPCSession"] = _MPCSESSION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MPCSession = _reflection.GeneratedProtocolMessageType(
    "MPCSession",
    (_message.Message,),
    {
        "DESCRIPTOR": _MPCSESSION,
        "__module__": "proto.lib.sympc.session_pb2"
        # @@protoc_insertion_point(class_scope:syft.lib.sympc.MPCSession)
    },
)
_sym_db.RegisterMessage(MPCSession)


# @@protoc_insertion_point(module_scope)
