# Supplementary Material: Intervention Justification Model

This English-language package contains the evaluated engine, translated case narratives, baseline matrix, translated historical execution records, analyses, and pending reconstruction protocol.

Read `README.md` for navigation and reporting limits. See `ENGLISH_VERIFICATION.md` for checks that the language edition preserves the condition states, conclusions, and dependency structure. Translation changes byte hashes; historical hashes and the current distribution checksums are distinguished in `TRANSLATION_PROVENANCE.json`.

From `frozen_source/`, use Python 3.10 or later:

```bash
python run_matrix.py --output-dir ../new_execution
```

Use a new or empty destination. No third-party packages are required. For human reconstruction, give the reviewer only `Reviewer_Packet_CL2.zip` before revealing expected results. Independent reconstruction remains pending.
