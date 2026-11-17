# Evaluation Execution Report — v1 — English translation

## Scope and Provenance
Baseline v1 was executed using Reference Computational Instance v2 without changing the evaluated engine, cases, or expectations. One case (A-01) is documentary and twelve are synthetic. The 18 entries reuse cases; they are not 18 independent observations. This is internal examination of applicability and conformance relative to curated grounds, not a user study.

The original baseline was fixed before v2 implementation, but A-01 and prior development were already known. All cases had also been exercised in v2 development checks. The reported execution is a documented and analysed repetition, not a blind or independent evaluation. A new execution directory does not establish independence.

This document translates the historical report. The historical records in `execution/` retain their original identifiers and input hashes; these refer to original evaluated bytes, not translated narrative bytes. A separate run of the English inputs is stored in `english_verification/`. Its equivalence checks are reported separately.

## Execution Summary

S = supported; NE = not_established; C = contradicted. States are relative to the supplied case grounds.

| Case | Origin | D01 | D02 | D03 | D04 | D05 | D06 | Conclusion | Reasons | Issues | Edges |

|---|---|---|---|---|---|---|---|---|---|---|---|

| A-01 | documentary | NE | NE | S | NE | S | NE | undetermined | 3 | 9 | 129 |

| B-00 | synthetic | S | S | S | S | S | S | favourably_supported | 1 | 0 | 62 |

| M-01 | synthetic | NE | NE | S | S | S | NE | undetermined | 1 | 1 | 64 |

| O-01 | synthetic | S | NE | S | NE | S | S | undetermined | 1 | 1 | 66 |

| O-02 | synthetic | S | S | S | S | S | S | favourably_supported | 1 | 1 | 71 |

| P-01 | synthetic | S | S | S | NE | S | S | undetermined | 2 | 1 | 84 |

| P-02 | synthetic | S | S | S | S | S | S | favourably_supported | 2 | 1 | 96 |

| R-01 | synthetic | S | S | S | S | C | S | unfavourably_supported | 1 | 0 | 78 |

| R-02 | synthetic | S | S | S | S | C | S | undetermined | 1 | 0 | 71 |

| S-01 | synthetic | S | S | S | S | S | S | favourably_supported | 1 | 0 | 65 |

| S-02 | synthetic | S | S | S | NE | S | S | undetermined | 2 | 1 | 78 |

| U-01 | synthetic | S | NE | S | S | S | NE | undetermined | 1 | 1 | 69 |

| U-02 | synthetic | S | S | S | S | S | S | favourably_supported | 1 | 1 | 69 |

## Analysis by Case

### A-01

Identical canonical JSON; other environments and evaluator agreement were not examined.

Input: `frozen_source/cases/A-01.json`. Historical assessment translation: `execution/A-01.assessment.json`. Historical canonical input SHA-256: `94c93d4f5c56d7fb0b643d918dd2e13fe059522605b22bfe5885839ff9e8e164`.

Recorded reasons: r002 (supporting), r003 (opposing), r006 (limiting).

Recorded issues: G01 [missing_information], G02 [missing_information], G03 [missing_information], G04 [missing_information], O01 [objection], O02 [objection], O03 [tension], O04 [objection], O05 [objection].

The output preserves the input snapshot, sources, inferences, methods, conditions, grounds, and trace. Counts are not measures of justification quality.

### B-00

Synthetic case with stipulated grounds and review. All six conditions are supported; the conclusion depends on these input judgments.

Input: `frozen_source/cases/B-00.json`. Historical assessment translation: `execution/B-00.assessment.json`. Historical canonical input SHA-256: `7f4acd28efd6427215a1428c62e63ec533581b548ddc9b1236854e925bcdde38`.

Recorded reasons: GEN:REASON:WR (supporting).

Recorded issues: none within declared coverage.

The output preserves the input snapshot, sources, inferences, methods, conditions, grounds, and trace. Counts are not measures of justification quality.

### M-01

E remains an existing object whose information is now absent. An informational issue is generated; shared dependencies leave D01, D02, and D06 not established. This is not a broken-reference error.

Input: `frozen_source/cases/M-01.json`. Historical assessment translation: `execution/M-01.assessment.json`. Historical canonical input SHA-256: `453b74017ddba2f3b2b4fbd74169b032eeebf434c73c9665d61732d154dbcc7c`.

Recorded reasons: GEN:REASON:WR (supporting).

Recorded issues: GEN:INFO:E [missing_information].

The output preserves the input snapshot, sources, inferences, methods, conditions, grounds, and trace. Counts are not measures of justification quality.

### O-01

OBJ targets IC. D02 and D04 are not established; D06 remains supported. Opposition does not automatically imply missing information.

Input: `frozen_source/cases/O-01.json`. Historical assessment translation: `execution/O-01.assessment.json`. Historical canonical input SHA-256: `1bdfd8272babc878cfa63c905a0625053057a29a1fb0dd8bde8903c8cc96ec35`.

Recorded reasons: GEN:REASON:WR (supporting).

Recorded issues: OBJ [objection].

The output preserves the input snapshot, sources, inferences, methods, conditions, grounds, and trace. Counts are not measures of justification quality.

### O-02

ANS contains a directed response and stipulated acceptance. OBJ is retained: resolution_supported distinguishes treatment from deletion.

Input: `frozen_source/cases/O-02.json`. Historical assessment translation: `execution/O-02.assessment.json`. Historical canonical input SHA-256: `8c77c6846b5bf690f6cdd432821364c8afdbe13a06dc6fd1c09b119d4f28fc22`.

Recorded reasons: GEN:REASON:WR (supporting).

Recorded issues: OBJ [objection].

The output preserves the input snapshot, sources, inferences, methods, conditions, grounds, and trace. Counts are not measures of justification quality.

### P-01

PRI adds a declared and applicable priority without W-P. The tension remains open and the conclusion remains undetermined.

Input: `frozen_source/cases/P-01.json`. Historical assessment translation: `execution/P-01.assessment.json`. Historical canonical input SHA-256: `1c6ca7d44033efab23a59461597209cb063f19b73403db125033480b00e53ec8`.

Recorded reasons: GEN:REASON:WCOST (opposing), GEN:REASON:WR (supporting).

Recorded issues: TEN [tension].

The output preserves the input snapshot, sources, inferences, methods, conditions, grounds, and trace. Counts are not measures of justification quality.

### P-02

W-P, its limit, and a directed response with stipulated acceptance allow TEN to be addressed. This does not establish legitimate precedence in a real-world case.

Input: `frozen_source/cases/P-02.json`. Historical assessment translation: `execution/P-02.assessment.json`. Historical canonical input SHA-256: `ded5f296b591d516a30c014f315af1ceefa39401490629fb99ac727e98d06a88`.

Recorded reasons: GEN:REASON:WCOST (opposing), GEN:REASON:WR (supporting).

Recorded issues: TEN [tension].

The output preserves the input snapshot, sources, inferences, methods, conditions, grounds, and trace. Counts are not measures of justification quality.

### R-01

RULE is declared applicable, binding, and violated. WB and WX enable EXCLUDING-CONSTRAINT-1. Its authority is hypothetical, not an empirically established domain prohibition.

Input: `frozen_source/cases/R-01.json`. Historical assessment translation: `execution/R-01.assessment.json`. Historical canonical input SHA-256: `31215233fc3ad4114103cc39224975fb3c63acbc2166a59e0fcf0b266424b48d`.

Recorded reasons: GEN:REASON:WR (supporting).

Recorded issues: none within declared coverage.

The output preserves the input snapshot, sources, inferences, methods, conditions, grounds, and trace. Counts are not measures of justification quality.

### R-02

Removing WX leaves D05 contradicted, but no contrary chain is constructed. The absence of WX is visible as a null value in the snapshot; a specific explanation of why U is not constructed is missing.

Input: `frozen_source/cases/R-02.json`. Historical assessment translation: `execution/R-02.assessment.json`. Historical canonical input SHA-256: `2441d6cc333ae21a41ceadd4aa5fe383d4dec786157a66829d991a6e785e3f47`.

Recorded reasons: GEN:REASON:WR (supporting).

Recorded issues: none within declared coverage.

The output preserves the input snapshot, sources, inferences, methods, conditions, grounds, and trace. Counts are not measures of justification quality.

### S-01

E2 is added to IN and appears in the grounds and trace of D01; the favourable conclusion remains unchanged. No probabilistic strength or quantitative increase in support is calculated.

Input: `frozen_source/cases/S-01.json`. Historical assessment translation: `execution/S-01.assessment.json`. Historical canonical input SHA-256: `45938f6d69f32b13ced33b9b5800c7ea403e85369bc706ec5a26654450d2a0d8`.

Recorded reasons: GEN:REASON:WR (supporting).

Recorded issues: none within declared coverage.

The output preserves the input snapshot, sources, inferences, methods, conditions, grounds, and trace. Counts are not measures of justification quality.

### S-02

COST and WCOST generate an opposing reason. TEN blocks D04. The cost is not arithmetically aggregated with the benefit and does not by itself produce an unfavourable conclusion.

Input: `frozen_source/cases/S-02.json`. Historical assessment translation: `execution/S-02.assessment.json`. Historical canonical input SHA-256: `8987282eac4a1d0526f17ae7c0ff21d85454b7fa9ad732e42f360be20062c8f8`.

Recorded reasons: GEN:REASON:WCOST (opposing), GEN:REASON:WR (supporting).

Recorded issues: TEN [tension].

The output preserves the input snapshot, sources, inferences, methods, conditions, grounds, and trace. Counts are not measures of justification quality.

### U-01

C is available but uncertain. Stipulated alternatives differ in support. An uncertainty issue, rather than missing_information, is generated; D02 and D06 are not established.

Input: `frozen_source/cases/U-01.json`. Historical assessment translation: `execution/U-01.assessment.json`. Historical canonical input SHA-256: `e11c0d327486f51def9cae804c648b4dfa394795a9c08ebfff642b5f00ac501f`.

Recorded reasons: GEN:REASON:WR (supporting).

Recorded issues: GEN:UNC:C [uncertainty].

The output preserves the input snapshot, sources, inferences, methods, conditions, grounds, and trace. Counts are not measures of justification quality.

### U-02

Uncertainty is preserved. Both supplied alternatives support the premise; D06 is supported relative to these alternatives, without claiming exhaustive coverage.

Input: `frozen_source/cases/U-02.json`. Historical assessment translation: `execution/U-02.assessment.json`. Historical canonical input SHA-256: `921c812f1aa982f69e6bbabd9667e4ea7873f0d4b94d21d9356a16a5b2ed58a7`.

Recorded reasons: GEN:REASON:WR (supporting).

Recorded issues: GEN:UNC:C [uncertainty].

The output preserves the input snapshot, sources, inferences, methods, conditions, grounds, and trace. Counts are not measures of justification quality.

## Repetition and Identity Checks

A-01 was assessed once in the main execution and twice more in separate Python processes. Canonical JSON comparisons matched the entire content. No varying timestamps were present, so no fields required removal. This establishes repetition for this implementation, case, and environment, not agreement between researchers or universal portability.

Historical Python version: `3.12.14 (main, Aug 25 2026, 14:00:49) [Clang 22.1.3 ]`. Engine hash: `45817877346cec83e12252c33db80c68ce204a50b63c898fa014ebc4570d72ef`. Historical baseline-map digest: `e8532bc1a758ffa8d96146806e407813d4109c61a8bc5f26b111f4984f62b097`. The English edition has separate input checksums and a separately labelled verification run.
