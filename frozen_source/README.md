# Reference Computational Instance v2 — English Input Edition

## Contents
A Python research instance for reconstructing curated qualitative assessments under SC1.1. It implements neither an intervention policy nor selection between candidates. D01–D06 are derived from related objects, not supplied as Boolean input labels.

- `baseline/evaluation_matrix.json` and `.csv`: Baseline v1's 18 examination entries.
- `baseline/frozen_sha256.json`: byte hashes of the distributed English matrix and 13 case files. The original frozen map is preserved in `../TRANSLATION_PROVENANCE.json`.
- `cases/`: documentary A-01 and twelve synthetic cases. The documentary r002/r003 tension is part of A-01, not an additional independent study.
- `engine.py`: loading, integrity checks, dependencies, reason reconstruction, limitations, conditions, chains, and traces.
- `run_matrix.py`: records assessments, comparisons, and repetitions without automatically assigning scientific support to CL1–CL5.
- `DESIGN_DECISIONS.md`: computational decisions and dependence on external judgments.

## Execute
Requires Python 3.10 or later and no third-party packages.

```bash
python engine.py cases/A-01.json --output A01_assessment.json
python run_matrix.py --output-dir evaluation_run_01
```

The matrix runner checks the distributed input hashes, produces assessments and parent–variant differences, repeats A-01 in separate processes, and creates a pending human-review form. It refuses to overwrite a nonempty output directory. The engine does not read expected conclusions: it receives only a case. The runner uses the matrix to select cases, not determine conclusions.

## Before Interpreting Results
The original baseline was fixed before v2 implementation and its new checks, but A-01 and eight iteration-1 development checks were already known. This was not public preregistration or independent evaluation. Synthetic cases were developed through the same design process; their expectations examine implications of stated assumptions, not external truth.

Sixteen technical development checks were previously run, exposing the cases before the reported analysis. Those checks are not independent evaluation. No independent human reconstruction of CL2 or empirical examination of domain sufficiency has been completed. The original technical test suite is not included in this evaluation distribution.

## What Is Calculated and What Is Supplied
The instance receives recorded evidence, inferences, methods, relevance, issue criticality, responses, constraints, and plausible alternatives. It follows dependencies and scope, generates practical reasons from supplied relevance warrants, and preserves documentary reasons. It does not independently establish the adequacy of human judgments.

A response requires a directed object, grounds, and an acceptance judgment. Priority-based responses also require W-P with accepted cost and limits. Checking these fields establishes the presence of supplied reasoning, not its legitimacy. Available uncertainty is not converted into missing information. Stability is limited to supplied alternatives, not all possible alternatives.

## Reading Outputs
- `completed`: procedure completed; does not imply favourable justification.
- `invalid`: structurally invalid case; no justification assessment is emitted.
- `supported`, `contradicted`, `not_established`: condition states relative to supplied grounds.
- Conclusions: `favourably_supported`, `unfavourably_supported`, `undetermined`.
- A contrary chain is not inferred from failure of the favourable chain.
- The complete input snapshot retains inferences, sources, methods, and judgments alongside the trace.

Computational repetition differs from reconstruction by another person. A link does not establish inference adequacy.

## Provenance
The integrated specification and documentary dossier informed the original v1-to-v2 migration. Personal drafting links were removed for anonymous review. The migration added structural roles and links rather than new empirical observations. It retained the individual A-01 claim and its limits. Inherited priority correspondence does not establish justificatory force, especially at the individual level. The original article was not re-audited to produce that version.

This edition translates Spanish narrative fields into English. The engine and conceptual judgments remain unchanged. The separately recorded English verification is not a replacement for the historical execution or independent validation. See the root README and provenance file for checksum distinctions.