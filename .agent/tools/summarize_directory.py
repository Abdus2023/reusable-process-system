#!/usr/bin/env python3
"""Produce deterministic status and coverage counts from a creator directory."""
from __future__ import annotations
import json
import sys
from collections import Counter
from pathlib import Path

STATUSES = ("VERIFIED", "PARTIALLY_VERIFIED", "UNVERIFIED", "EXCLUDED")

def summarize(payload: object) -> dict:
    if not isinstance(payload, dict) or not isinstance(payload.get("creators"), list):
        raise ValueError("input must be an object with a top-level creators array")
    records = payload["creators"]
    if not all(isinstance(r, dict) for r in records):
        raise ValueError("every creators[] item must be an object")
    statuses = Counter(r.get("record_status", "MISSING_STATUS") for r in records)
    categories = Counter()
    languages = Counter()
    platforms = Counter()
    for record in records:
        cats = record.get("content_categories", [])
        if isinstance(cats, list):
            categories.update(x for x in cats if isinstance(x, str) and x.strip())
        langs = [record.get("primary_language")] + (record.get("other_languages", []) if isinstance(record.get("other_languages", []), list) else [])
        languages.update(x for x in langs if isinstance(x, str) and x.strip())
        platform = record.get("primary_platform")
        platforms[platform if isinstance(platform, str) and platform.strip() else "NOT_SPECIFIED"] += 1
    return {
        "record_count": len(records),
        "status_counts": {status: statuses.get(status, 0) for status in STATUSES} | ({"OTHER_OR_MISSING": sum(v for k, v in statuses.items() if k not in STATUSES)}),
        "category_counts": dict(sorted(categories.items())),
        "language_counts": dict(sorted(languages.items())),
        "platform_counts": dict(sorted(platforms.items())),
        "missing_metric_observation_date_count": sum(1 for r in records if (r.get("subscriber_count") is not None or r.get("total_views") is not None) and not r.get("metric_observation_date")),
        "scope_note": "Counts summarize supplied fields only; they do not validate identity, evidence quality, or source reachability."
    }

def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("USAGE: summarize_directory.py path/to/directory.json", file=sys.stderr)
        return 2
    try:
        payload = json.loads(Path(argv[1]).read_text(encoding="utf-8"))
        result = summarize(payload)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"INPUT_ERROR: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
