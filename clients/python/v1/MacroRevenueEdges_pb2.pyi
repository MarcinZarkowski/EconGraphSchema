import SectorNodes_pb2 as _SectorNodes_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MacroRevenueEdge(_message.Message):
    __slots__ = ("sector_market_share", "country_market_share", "company_revenue_weight", "allocated_revenue", "currency", "scale", "sector_code", "sector_taxonomy", "country_iso", "company_id")
    SECTOR_MARKET_SHARE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_MARKET_SHARE_FIELD_NUMBER: _ClassVar[int]
    COMPANY_REVENUE_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    ALLOCATED_REVENUE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    SCALE_FIELD_NUMBER: _ClassVar[int]
    SECTOR_CODE_FIELD_NUMBER: _ClassVar[int]
    SECTOR_TAXONOMY_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_ISO_FIELD_NUMBER: _ClassVar[int]
    COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
    sector_market_share: float
    country_market_share: float
    company_revenue_weight: float
    allocated_revenue: float
    currency: str
    scale: int
    sector_code: str
    sector_taxonomy: _SectorNodes_pb2.SectorTaxonomy
    country_iso: str
    company_id: int
    def __init__(self, sector_market_share: _Optional[float] = ..., country_market_share: _Optional[float] = ..., company_revenue_weight: _Optional[float] = ..., allocated_revenue: _Optional[float] = ..., currency: _Optional[str] = ..., scale: _Optional[int] = ..., sector_code: _Optional[str] = ..., sector_taxonomy: _Optional[_Union[_SectorNodes_pb2.SectorTaxonomy, str]] = ..., country_iso: _Optional[str] = ..., company_id: _Optional[int] = ...) -> None: ...

class MacroRevenueEdgesFile(_message.Message):
    __slots__ = ("version", "updated_at", "edges")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    EDGES_FIELD_NUMBER: _ClassVar[int]
    version: str
    updated_at: int
    edges: _containers.RepeatedCompositeFieldContainer[MacroRevenueEdge]
    def __init__(self, version: _Optional[str] = ..., updated_at: _Optional[int] = ..., edges: _Optional[_Iterable[_Union[MacroRevenueEdge, _Mapping]]] = ...) -> None: ...
