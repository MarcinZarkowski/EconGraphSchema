from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SectorTaxonomy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ICIO: _ClassVar[SectorTaxonomy]
    BEA: _ClassVar[SectorTaxonomy]
ICIO: SectorTaxonomy
BEA: SectorTaxonomy

class SectorNode(_message.Message):
    __slots__ = ("code", "name", "taxonomy", "agency", "description")
    CODE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TAXONOMY_FIELD_NUMBER: _ClassVar[int]
    AGENCY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    code: str
    name: str
    taxonomy: SectorTaxonomy
    agency: str
    description: str
    def __init__(self, code: _Optional[str] = ..., name: _Optional[str] = ..., taxonomy: _Optional[_Union[SectorTaxonomy, str]] = ..., agency: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class SectorNodesFile(_message.Message):
    __slots__ = ("version", "updated_at", "nodes")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    version: str
    updated_at: int
    nodes: _containers.RepeatedCompositeFieldContainer[SectorNode]
    def __init__(self, version: _Optional[str] = ..., updated_at: _Optional[int] = ..., nodes: _Optional[_Iterable[_Union[SectorNode, _Mapping]]] = ...) -> None: ...
