from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommodityNode(_message.Message):
    __slots__ = ("commodity_code", "name", "bea_sector_code", "icio_sector_code")
    COMMODITY_CODE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    BEA_SECTOR_CODE_FIELD_NUMBER: _ClassVar[int]
    ICIO_SECTOR_CODE_FIELD_NUMBER: _ClassVar[int]
    commodity_code: str
    name: str
    bea_sector_code: str
    icio_sector_code: str
    def __init__(self, commodity_code: _Optional[str] = ..., name: _Optional[str] = ..., bea_sector_code: _Optional[str] = ..., icio_sector_code: _Optional[str] = ...) -> None: ...

class CommodityNodesFile(_message.Message):
    __slots__ = ("version", "updated_at", "nodes")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    version: str
    updated_at: int
    nodes: _containers.RepeatedCompositeFieldContainer[CommodityNode]
    def __init__(self, version: _Optional[str] = ..., updated_at: _Optional[int] = ..., nodes: _Optional[_Iterable[_Union[CommodityNode, _Mapping]]] = ...) -> None: ...
