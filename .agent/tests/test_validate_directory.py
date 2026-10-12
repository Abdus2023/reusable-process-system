import importlib.util
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).parents[1] / "tools" / "validate_directory.py"
SPEC = importlib.util.spec_from_file_location("validate_directory", MODULE_PATH)
validator = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(validator)


def valid_record():
    return {
        "creator_id": "TN-0001",
        "display_name": "Example Creator",
        "entity_type": "individual",
        "record_status": "VERIFIED",
        "source_urls": ["https://example.org/source"],
        "identity_evidence_urls": ["https://example.org/channel"],
        "tunisia_connection_evidence": ["https://example.org/about"],
        "last_verified_date": "2026-10-12",
        "primary_platform_url": "https://www.youtube.com/@example",
        "subscriber_count": 100,
        "metric_observation_date": "2026-10-12"
    }


class ValidateDirectoryTests(unittest.TestCase):
    def test_valid_record_passes(self):
        self.assertEqual(validator.validate({"creators": [valid_record()]}), [])

    def test_duplicate_ids_fail(self):
        record = valid_record()
        duplicate = dict(record)
        self.assertTrue(any("DUPLICATE_CREATOR_ID" in e for e in validator.validate({"creators": [record, duplicate]})))

    def test_verified_without_evidence_fails(self):
        record = valid_record()
        record["identity_evidence_urls"] = []
        self.assertTrue(any("VERIFIED_WITHOUT_EVIDENCE" in e for e in validator.validate({"creators": [record]})))

    def test_undated_metric_fails(self):
        record = valid_record()
        record.pop("metric_observation_date")
        self.assertTrue(any("UNDATED_METRIC" in e for e in validator.validate({"creators": [record]})))

    def test_invalid_source_url_fails(self):
        record = valid_record()
        record["source_urls"] = ["not-a-url"]
        self.assertTrue(any("INVALID_SOURCE_URL" in e for e in validator.validate({"creators": [record]})))

    def test_non_object_root_fails(self):
        self.assertTrue(any("ROOT_NOT_OBJECT" in e for e in validator.validate([])))

    def test_missing_creator_array_fails(self):
        self.assertTrue(any("CREATORS_NOT_ARRAY" in e for e in validator.validate({})))

    def test_duplicate_primary_platform_url_fails(self):
        first = valid_record()
        second = valid_record()
        second["creator_id"] = "TN-0002"
        self.assertTrue(any("DUPLICATE_PLATFORM_URL" in e for e in validator.validate({"creators": [first, second]})))


if __name__ == "__main__":
    unittest.main()
