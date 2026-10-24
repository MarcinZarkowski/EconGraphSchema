from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CompanyNode(_message.Message):
    __slots__ = ("id", "cik", "ticker", "name", "country_iso")
    ID_FIELD_NUMBER: _ClassVar[int]
    CIK_FIELD_NUMBER: _ClassVar[int]
    TICKER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_ISO_FIELD_NUMBER: _ClassVar[int]
    id: int
    cik: str
    ticker: str
    name: str
    country_iso: str
    def __init__(self, id: _Optional[int] = ..., cik: _Optional[str] = ..., ticker: _Optional[str] = ..., name: _Optional[str] = ..., country_iso: _Optional[str] = ...) -> None: ...

class CompanyNodesFile(_message.Message):
    __slots__ = ("version", "updated_at", "nodes")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    version: str
    updated_at: int
    nodes: _containers.RepeatedCompositeFieldContainer[CompanyNode]
    def __init__(self, version: _Optional[str] = ..., updated_at: _Optional[int] = ..., nodes: _Optional[_Iterable[_Union[CompanyNode, _Mapping]]] = ...) -> None: ...
