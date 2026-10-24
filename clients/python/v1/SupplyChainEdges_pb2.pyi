from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SupplyKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMMODITY: _ClassVar[SupplyKind]
    COMPANY: _ClassVar[SupplyKind]
    SECTOR: _ClassVar[SupplyKind]
COMMODITY: SupplyKind
COMPANY: SupplyKind
SECTOR: SupplyKind

class SupplyChainEdge(_message.Message):
    __slots__ = ("supplier_revenue_weight", "supplied_dependency_weight", "to_company_id", "from_country_iso", "supply_kind", "commodity_code", "from_company_id", "from_sector_code")
    SUPPLIER_REVENUE_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    SUPPLIED_DEPENDENCY_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    TO_COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
    FROM_COUNTRY_ISO_FIELD_NUMBER: _ClassVar[int]
    SUPPLY_KIND_FIELD_NUMBER: _ClassVar[int]
    COMMODITY_CODE_FIELD_NUMBER: _ClassVar[int]
    FROM_COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
    FROM_SECTOR_CODE_FIELD_NUMBER: _ClassVar[int]
    supplier_revenue_weight: float
    supplied_dependency_weight: float
    to_company_id: int
    from_country_iso: str
    supply_kind: SupplyKind
    commodity_code: str
    from_company_id: int
    from_sector_code: str
    def __init__(self, supplier_revenue_weight: _Optional[float] = ..., supplied_dependency_weight: _Optional[float] = ..., to_company_id: _Optional[int] = ..., from_country_iso: _Optional[str] = ..., supply_kind: _Optional[_Union[SupplyKind, str]] = ..., commodity_code: _Optional[str] = ..., from_company_id: _Optional[int] = ..., from_sector_code: _Optional[str] = ...) -> None: ...

class SupplyChainEdgesFile(_message.Message):
    __slots__ = ("version", "updated_at", "edges")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    EDGES_FIELD_NUMBER: _ClassVar[int]
    version: str
    updated_at: int
    edges: _containers.RepeatedCompositeFieldContainer[SupplyChainEdge]
    def __init__(self, version: _Optional[str] = ..., updated_at: _Optional[int] = ..., edges: _Optional[_Iterable[_Union[SupplyChainEdge, _Mapping]]] = ...) -> None: ...
