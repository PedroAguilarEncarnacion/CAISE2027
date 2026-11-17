# English Edition Verification

## Scope
This is a language edition of the evaluated supplement, not an independent evaluation or a revised justification criterion. Spanish narrative descriptions, reports, matrices, and documentary extraction notes were translated into English. IDs, numeric findings, supplied judgments, inference rules, condition states, conclusions, and trace structure were preserved. AI-assistance disclosures remain explicit.

## Checks Performed
- The evaluated engine is byte-identical to the original engine.
- All thirteen English input files were processed using that unchanged engine.
- For every case, processing status, conclusion, chains, condition assessments, reasons, issues, priorities, constraints, trace, limitations, and translated snapshot matched the translated historical record.
- Two separate-process executions of English A-01 produced equivalent outputs.
- English input byte hashes were regenerated to keep the baseline integrity check executable.
- Historical outputs retain their original assessment IDs and input hashes; these refer to the original evaluated inputs. They are not presented as byte hashes of translated text.
- No independent human reconstruction has been performed.

`ENGLISH_VERIFICATION.json` records the per-case checks. `english_verification/` contains the separate language-edition execution, clearly distinguished from historical records in `execution/`.

## Checksums and Provenance
`TRANSLATION_PROVENANCE.json` records original file hashes and the original frozen baseline map. `ORIGINAL_EVALUATION_SHA256.json` is retained as historical provenance, not a checksum manifest for translated files. `DISTRIBUTION_SHA256.json` verifies the current English distribution. The baseline map in `frozen_source/baseline/frozen_sha256.json` verifies the English input files distributed here.

Translation changes textual bytes and consequently input hashes and hash-derived assessment identifiers. This is a documented language change, not a correction of the observed R-02 explanatory discrepancy. No conclusions or claim-support judgments were upgraded.
