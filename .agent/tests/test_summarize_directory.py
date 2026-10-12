import importlib.util
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).parents[1] / "tools" / "summarize_directory.py"
SPEC = importlib.util.spec_from_file_location("summarize_directory", MODULE_PATH)
summarizer = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(summarizer)

class SummarizeDirectoryTests(unittest.TestCase):
    def test_status_category_language_counts(self):
        payload = {"creators": [
            {"record_status": "VERIFIED", "content_categories": ["Gaming", "Gaming"], "primary_language": "Tunisian Arabic", "primary_platform": "YouTube"},
            {"record_status": "PARTIALLY_VERIFIED", "content_categories": ["Education"], "primary_language": "French", "primary_platform": "TikTok"}
        ]}
        result = summarizer.summarize(payload)
        self.assertEqual(result["record_count"], 2)
        self.assertEqual(result["status_counts"]["VERIFIED"], 1)
        self.assertEqual(result["category_counts"]["Gaming"], 2)
        self.assertEqual(result["language_counts"]["French"], 1)

    def test_invalid_payload_fails(self):
        with self.assertRaises(ValueError):
            summarizer.summarize([])

    def test_missing_status_is_counted(self):
        result = summarizer.summarize({"creators": [{"display_name": "No status"}]})
        self.assertEqual(result["status_counts"]["OTHER_OR_MISSING"], 1)

if __name__ == "__main__":
    unittest.main()
