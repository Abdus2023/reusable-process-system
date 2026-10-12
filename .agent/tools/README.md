# Tools

## validate_directory.py
Validates internal structure and cross-field consistency for a JSON creator directory. Uses only the Python standard library and makes no network requests.

Input: UTF-8 JSON object with a top-level `creators` array.

Checks:
- record object, stable identifier, display name;
- supported entity and record statuses;
- HTTP(S) source URLs;
- VERIFIED records include identity evidence, Tunisia-connection evidence, and a verification date;
- populated subscriber/view metrics are non-negative integers with a metric observation date;
- duplicate creator IDs and duplicate primary platform URLs.

Exit codes: 0 = checks pass; 1 = validation findings; 2 = input/usage error.

Limitation: it does not open URLs, confirm source independence, prove identity, verify nationality/residence, validate source content, or fact-check claims.

## summarize_directory.py
Counts record statuses, categories, languages, platforms, and records with undated populated metrics. Output is deterministic JSON and summarizes supplied fields only; it does not establish truth or evidence quality.

Exit codes: 0 = summary produced; 2 = input/usage error.

## Tests
Run `python -m unittest discover -s .agent/tests -v`. Record the actual command and output; do not infer execution from test-file existence.