"""Print a safe end-to-end mock workflow without SMTP or external web access."""
import json
from app.server import run_pipeline, DB
from app.discovery.public_search import mock_candidates

candidate = mock_candidates()[0]
result = run_pipeline(candidate, use_mock=True)
print(json.dumps(result, ensure_ascii=False, indent=2))
if result.get("draft_id"):
    DB.update_draft(result["draft_id"], status="APPROVED")
    print("APPROVED draft:", result["draft_id"])
    print("Next step is simulated send through the local dashboard; SMTP was not used.")
