from __future__ import annotations

import json
from ..analysis.lm_studio import LMStudioClient


def generate_draft(client: LMStudioClient, clinic: dict, analysis: dict, config: dict) -> dict:
    prompt = {"task": "Сгенерируй короткое профессиональное B2B-письмо на русском языке", "clinic": clinic, "analysis": analysis, "sender": config, "rules": ["Используй только наблюдения из входных данных.", "Не называй клинику устаревшей без доказательств.", "Упомяни ссылку на DENTARA demo, если она задана.", "Добавь простой opt-out текст.", "Верни JSON: subject, body, rationale, source_observations, confidence."]}
    result = client.chat_json(prompt)
    result.setdefault("source_observations", analysis.get("observations", [])); result.setdefault("confidence", analysis.get("confidence", 0))
    return result
