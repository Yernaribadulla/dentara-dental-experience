from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Protocol


class DiscoveryProvider(Protocol):
    name: str
    def search(self, query: str, target_count: int = 10) -> list[dict[str, Any]]: ...
    def get_business_details(self, result: dict[str, Any]) -> dict[str, Any]: ...
    def extract_contacts(self, result: dict[str, Any]) -> list[dict[str, Any]]: ...


@dataclass
class PublicSourceProvider:
    """Provider contract for manually reviewed public-source results.

    The first real test uses reviewed source records collected from 2GIS/Yandex/
    official pages. This adapter keeps source provenance instead of hiding it in
    one search-engine-specific implementation.
    """
    name: str
    records: list[dict[str, Any]]
    def search(self, query: str, target_count: int = 10) -> list[dict[str, Any]]:
        _ = query; return self.records[:target_count]
    def get_business_details(self, result: dict[str, Any]) -> dict[str, Any]: return result
    def extract_contacts(self, result: dict[str, Any]) -> list[dict[str, Any]]: return result.get("contacts", [])


def merge_provider_results(providers: list[DiscoveryProvider], query: str, target_count: int) -> list[dict[str, Any]]:
    merged: dict[str, dict[str, Any]] = {}
    for provider in providers:
        for raw in provider.search(query, target_count):
            key = (raw.get("name", "").lower(), raw.get("city", "").lower())
            if key not in merged: merged[key] = raw | {"source_names": [provider.name]}
            else: merged[key]["source_names"] = sorted(set(merged[key].get("source_names", []) + [provider.name]))
    return list(merged.values())[:target_count]
