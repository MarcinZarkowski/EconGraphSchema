from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CountryNode(_message.Message):
    __slots__ = ("iso", "name")
    ISO_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    iso: str
    name: str
    def __init__(self, iso: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class CountryNodesFile(_message.Message):
    __slots__ = ("version", "updated_at", "nodes")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    version: str
    updated_at: int
    nodes: _containers.RepeatedCompositeFieldContainer[CountryNode]
    def __init__(self, version: _Optional[str] = ..., updated_at: _Optional[int] = ..., nodes: _Optional[_Iterable[_Union[CountryNode, _Mapping]]] = ...) -> None: ...
