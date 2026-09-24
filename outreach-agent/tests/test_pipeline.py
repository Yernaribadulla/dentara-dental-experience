import tempfile
import unittest
from pathlib import Path

from app.storage.db import Database
from app.email.sender import SMTPProvider, SendError, SimulatedProvider


class OutreachSafetyTests(unittest.TestCase):
    def test_sending_requires_approval_at_storage_boundary(self):
        with tempfile.TemporaryDirectory() as folder:
            db = Database(Path(folder) / "test.db")
            clinic = db.add_clinic({"name": "Demo", "website": "https://example.invalid"})
            contact = db.add_contact(clinic, "info@example.invalid", "mock://contact")
            draft = db.add_draft(clinic, contact, {"subject": "Test", "body": "Test", "rationale": "Mock", "source_observations": [], "confidence": .9})
            row = db.get_draft(draft)
            self.assertEqual(row["status"], "DRAFTED")
            self.assertRaises(SendError, SMTPProvider({"SMTP_ENABLED": "false"}).send, row["email"], row["subject"], row["body"])
            db.close()

    def test_suppression_is_checked(self):
        with tempfile.TemporaryDirectory() as folder:
            db = Database(Path(folder) / "test.db")
            db.suppress("info@example.invalid", "opt-out")
            self.assertTrue(db.is_suppressed("INFO@EXAMPLE.INVALID"))
            db.close()

    def test_simulated_provider_does_not_send_network_requests(self):
        provider = SimulatedProvider(); provider.send("info@example.invalid", "Subject", "Body")
        self.assertEqual(provider.name, "simulated")
        self.assertEqual(provider.sent[0]["recipient"], "info@example.invalid")


if __name__ == "__main__": unittest.main()
