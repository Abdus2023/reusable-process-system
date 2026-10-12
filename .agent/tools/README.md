# Tools

## validate_directory.py
Validates internal structure and cross-field consistency for a JSON creator directory. Uses only the Python standard library and makes no network requests.

### Input
UTF-8 JSON object with a top-level `creators` array.

### Checks
- record object, stable identifier, display name;
- supported entity and record statuses;
- HTTP(S) source URLs;
- VERIFIED records include identity evidence, Tunisia-connection evidence, and a verification date;
- populated subscriber/view metrics are non-negative integers with a metric observation date;
- duplicate creator IDs and duplicate primary platform URLs.

### Exit codes
- 0: structural checks passed;
- 1: validation findings;
- 2: input/usage error.

### Limitation
The tool does not open URLs, confirm source independence, prove creator identity, verify nationality/residence, validate source content, or fact-check claims. PASS means only that implemented structural checks passed.

### Tests
Run `python -m unittest discover -s .agent/tests -v`. Record the actual command and output; do not infer execution from test-file existence.