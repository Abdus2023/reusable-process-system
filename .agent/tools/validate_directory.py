#!/usr/bin/env python3
"""Deterministic structural validator for a creator directory; standard library only.

Usage:
  python .agent/tools/validate_directory.py path/to/directory.json

Input: {"creators": [creator_record, ...]}
Exit codes: 0 = valid, 1 = validation findings, 2 = input/usage error.
This checks internal structure and consistency only. It does not verify factual truth or URL reachability.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

STATUSES = {"VERIFIED", "PARTIALLY_VERIFIED", "UNVERIFIED", "EXCLUDED"}
ENTITY_TYPES = {"individual", "group", "channel_brand", "media_organization", "other"}
CREATOR_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:-]*$")


def is_http_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def validate(payload: object) -> list[str]:
    errors: list[str] = []
    if not isinstance(payload, dict):
        return ["ROOT_NOT_OBJECT: top-level JSON value must be an object"]
    creators = payload.get("creators")
    if not isinstance(creators, list):
        return ["CREATORS_NOT_ARRAY: top-level 'creators' must be an array"]

    seen_ids: set[str] = set()
    seen_platform_urls: dict[str, str] = {}
    for index, creator in enumerate(creators):
        prefix = f"creators[{index}]"
        if not isinstance(creator, dict):
            errors.append(f"RECORD_NOT_OBJECT: {prefix} must be an object")
            continue

        creator_id = creator.get("creator_id")
        if not isinstance(creator_id, str) or not CREATOR_ID.fullmatch(creator_id):
            errors.append(f"INVALID_CREATOR_ID: {prefix}.creator_id must be a non-empty stable identifier")
        elif creator_id in seen_ids:
            errors.append(f"DUPLICATE_CREATOR_ID: {creator_id}")
        else:
            seen_ids.add(creator_id)

        if not isinstance(creator.get("display_name"), str) or not creator["display_name"].strip():
            errors.append(f"MISSING_DISPLAY_NAME: {prefix}.display_name is required")

        if creator.get("entity_type") not in ENTITY_TYPES:
            errors.append(f"INVALID_ENTITY_TYPE: {prefix}.entity_type must be one of {sorted(ENTITY_TYPES)}")

        status = creator.get("record_status")
        if status not in STATUSES:
            errors.append(f"INVALID_STATUS: {prefix}.record_status must be one of {sorted(STATUSES)}")

        sources = creator.get("source_urls")
        if not isinstance(sources, list) or not sources:
            errors.append(f"MISSING_SOURCE_URLS: {prefix}.source_urls must be a non-empty array")
        else:
            for j, url in enumerate(sources):
                if not is_http_url(url):
                    errors.append(f"INVALID_SOURCE_URL: {prefix}.source_urls[{j}] is not an HTTP(S) URL")

        for field in ("primary_platform_url", "official_youtube_channel"):
            value = creator.get(field)
            if value is not None and not is_http_url(value):
                errors.append(f"INVALID_URL: {prefix}.{field} must be null or an HTTP(S) URL")

        if status == "VERIFIED":
            for field in ("identity_evidence_urls", "tunisia_connection_evidence"):
                value = creator.get(field)
                if not isinstance(value, list) or not value or not all(isinstance(x, str) and x.strip() for x in value):
                    errors.append(f"VERIFIED_WITHOUT_EVIDENCE: {prefix} requires non-empty {field}")
            date = creator.get("last_verified_date")
            if not isinstance(date, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
                errors.append(f"VERIFIED_WITHOUT_DATE: {prefix}.last_verified_date must be YYYY-MM-DD")

        metric_fields = ("subscriber_count", "total_views")
        for field in metric_fields:
            value = creator.get(field)
            if value is not None and (not isinstance(value, int) or isinstance(value, bool) or value < 0):
                errors.append(f"INVALID_METRIC: {prefix}.{field} must be a non-negative integer or null")
            if value is not None and not creator.get("metric_observation_date"):
                errors.append(f"UNDATED_METRIC: {prefix}.{field} is populated without metric_observation_date")

        platform_url = creator.get("primary_platform_url")
        if is_http_url(platform_url):
            normalized = platform_url.rstrip("/").lower()
            if normalized in seen_platform_urls:
                errors.append(f"DUPLICATE_PLATFORM_URL: {creator_id} and {seen_platform_urls[normalized]} share {platform_url}")
            else:
                seen_platform_urls[normalized] = creator_id

    return errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("USAGE: validate_directory.py path/to/directory.json", file=sys.stderr)
        return 2
    path = Path(argv[1])
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        print(f"INPUT_ERROR: cannot read {path}: {exc}", file=sys.stderr)
        return 2
    except json.JSONDecodeError as exc:
        print(f"INPUT_ERROR: invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}", file=sys.stderr)
        return 2

    errors = validate(payload)
    if errors:
        for error in errors:
            print(f"FAIL {error}")
        print(f"RESULT FAIL findings={len(errors)} records={len(payload.get('creators', [])) if isinstance(payload, dict) and isinstance(payload.get('creators'), list) else 'unknown'}")
        return 1

    print(f"RESULT PASS records={len(payload['creators'])}")
    print("SCOPE structural consistency only; external factual claims and URL reachability were not checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
