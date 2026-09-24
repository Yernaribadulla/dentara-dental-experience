# DENTARA Outreach Assistant

Локальный B2B outreach-инструмент для проекта DENTARA. Он помогает собрать публичные бизнес-контакты стоматологических клиник, исследовать доступный сайт, локально проанализировать наблюдения через LM Studio, подготовить персонализированный draft и провести его через review queue до симулированной или явно разрешённой отправки.

## Архитектура

```text
discovery → extraction → local LM Studio analysis → draft generation
          → review/approve → simulated or SMTP send → send log
```

- `app/discovery` — безопасный provider-neutral discovery seam и mock-кандидаты.
- `app/extraction` — ограниченный public-page fetch, видимый текст и публичные business emails.
- `app/analysis` — OpenAI-compatible client для локального LM Studio (`127.0.0.1:1234`).
- `app/generation` — structured JSON draft generation.
- `app/storage` — SQLite-схема для clinics, contacts, analyses, drafts, send logs и suppression list.
- `app/email` — simulated provider и отключённый по умолчанию SMTP provider.
- `app/ui` — локальный review dashboard.

## Установка и запуск

Нужен Python 3.11+. Внешние пакеты не требуются.

```powershell
cd outreach-agent
Copy-Item .env.example .env
python -m app.server
```

Откройте `http://127.0.0.1:8765`.

## LM Studio

Запустите локальный LM Studio server на `http://127.0.0.1:1234`, укажите загруженную модель в `.env`:

```env
LM_STUDIO_BASE_URL=http://127.0.0.1:1234/v1
LM_STUDIO_MODEL=название-локальной-модели
```

Website content и clinic facts не отправляются во внешние AI API. Если LM Studio недоступен, обычный pipeline не подменяет анализ выдуманными данными: draft получает ошибку/нулевую confidence. Mock-пайплайн — отдельный безопасный демонстрационный режим.

## Review queue и отправка

Dashboard показывает клиники, контакты, анализы, drafts, approved, sent, failed и suppression list. Для каждого draft можно отредактировать тему и текст, approve, добавить адрес в suppression list или запустить `Simulated send`.

Отправка возможна только если:

1. draft имеет статус `APPROVED`;
2. email отсутствует в suppression list;
3. выбран simulated provider или явно настроен SMTP.

SMTP по умолчанию выключен. Секреты хранятся только в `.env`, который не коммитится.

```env
SMTP_ENABLED=false
SMTP_HOST=
SMTP_PORT=587
SMTP_USERNAME=
SMTP_PASSWORD=
SMTP_FROM=
SMTP_USE_TLS=true
SEND_DELAY_SECONDS=30
```

Каждое письмо должно содержать opt-out sentence. При ручной фиксации отказа адрес попадает в `data/outreach.db` и не может быть отправлен повторно. Список также можно экспортировать/синхронизировать с `data/suppression.json` при добавлении внешнего адаптера.

## Discovery и приватность

Автоматический web search намеренно не реализован как скрытый scraper: `discover_candidates` — явный provider seam. При добавлении поискового адаптера соблюдайте terms, robots.txt, rate limits и законодательство. Система не обходит CAPTCHA, авторизацию, paywall или anti-bot, не угадывает личные адреса и не использует утечки/купленные базы. Сбор ограничен публичными business contact emails и точным source URL.

## Безопасный mock-прогон

В dashboard нажмите `Запустить mock-пайплайн`:

```text
mock clinic → public contact → extracted info → local mock analysis
→ personalized draft → review → explicit Approve → Simulated send
```

Реальные письма во время разработки не отправляются.

## Тесты

```powershell
python -m unittest discover -s tests -v
```

Тесты проверяют approval boundary, suppression list и отсутствие сетевой отправки у simulated provider.
