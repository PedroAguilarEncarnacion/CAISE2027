# Evaluation Matrix Execution — Reference v2 — English Edition

## Start Here
This package presents an English-language edition of the analysed Baseline v1 execution using reference instance v2. The engine is unchanged. Narrative translations do not alter judgments, inference rules, condition states, or conclusions. This package does not validate real-world intervention decisions.

## Four Deliverables
1. `Evaluation_Execution_Report.md`: recorded execution and D01–D06 assessments for each case.
2. `Claim_Analysis_Report.md`: evidence and interpretation for CL1–CL5.
3. `Human_Reconstruction_Protocol.md`: procedure for independent CL2 reconstruction, which remains pending.
4. `Limitations_Register.md`: limitations and the explanatory discrepancy observed in R-02.

`Matrix_Observed_Results.csv` and `.json` link the 18 original entries to observed results. `execution/` contains English translations of the historical assessment records, two repeated executions, and change records. `frozen_source/` contains the unchanged engine and English-language inputs. `english_verification/` contains a separately labelled verification run, not the original reported execution.

## What the Evidence Shows
All cases completed the procedure while preserving distinctions between opposition, constraints, missing information, and uncertainty. Changes in grounds can leave the conclusion unchanged. Separate-process A-01 executions matched in the recorded environment. Judgments about relevance, criticality, acceptance, and the sufficiency of alternatives remain researcher-supplied inputs.

R-02 requires further examination: its snapshot records the absent exclusion warrant, but its output lacks a specific explanation of why no contrary chain was constructed. The translation preserves this discrepancy rather than retrospectively correcting it.

## What to Do
Read the Claim Analysis Report first. Examine case fidelity and assumptions. For independent reconstruction, provide **only `Reviewer_Packet_CL2.zip`**, not the complete package with expectations and analysis reports. The reviewer must save an initial reconstruction before seeing the computed conditions and conclusion. Compare results according to the protocol. No independent human review has been completed and no human evaluation results have been fabricated.

## Repeat the Execution
From `frozen_source/`, with Python 3.10 or later:

```bash
python run_matrix.py --output-dir ../another_execution
```

The destination must be empty or must not exist. No third-party packages are required. Repetition does not provide independent corroboration or validate the grounds. Prior development exposure is disclosed in the reports.

## Language Edition and Checksums
Translation changes file bytes. Historical assessment IDs, input hashes, and Python-version records in `execution/` identify the original evaluated records; they are not hashes of the translated snapshot text. `TRANSLATION_PROVENANCE.json` preserves original file hashes and the original frozen baseline map. `frozen_source/baseline/frozen_sha256.json` identifies the English input edition so the runner remains executable. `DISTRIBUTION_SHA256.json` identifies the files distributed in this English package. See `ENGLISH_VERIFICATION.md` for the comparison with the original results.