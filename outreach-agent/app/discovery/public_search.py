from __future__ import annotations

from typing import Any


def discover_candidates(city: str, country: str, category: str, keywords: str = "") -> list[dict[str, Any]]:
    """Provider-neutral discovery seam.

    A real search provider can be added here. The default intentionally returns no
    remote results so the tool never silently scrapes a search engine or bypasses
    its terms. Use the UI's mock dataset for safe local testing.
    """
    _ = (city, country, category, keywords)
    return []


def mock_candidates() -> list[dict[str, Any]]:
    return [{"name": "Orda Smile Clinic (DEMO)", "website": "https://demo.orda-smile.example", "city": "Astana", "country": "Kazakhstan", "category": "Dental clinic", "phone": "+7 7172 000 000", "contact_page": "https://demo.orda-smile.example/contact", "description": "Фиктивная клиника для безопасного демонстрационного прогона.", "source_url": "mock://orda-smile"}]
