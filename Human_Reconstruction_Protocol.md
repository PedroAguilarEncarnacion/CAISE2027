# Human Reconstruction Protocol — CL2 — v1 — English translation

## Purpose
Examine whether another researcher can reconstruct the condition assessments and conclusion from the recorded grounds without introducing undocumented information. This review examines reconstruction; it does not establish the adequacy of normative or empirical assumptions.

## Status
**Pending.** No independent human review has been conducted. No results, names, or agreement are attributed to evaluators. This protocol was fixed after analysing the executions; it is not presented as preregistered before development.

## Reviewer
A researcher or supervisor who did not encode the cases or implement the engine. Record role, familiarity with the model, and prior exposure to the results. Disclose previous knowledge and do not describe an exposed reviewer as blind. One independent reviewer is proposed for exploratory examination, without claiming inter-rater reliability. If several reviewers participate, preserve their individual responses before discussion.

## Materials
Baseline v1's required case is **A-01**. `reviewer_packet/` contains a redacted assessment, its snapshot, the engine, and a description of the procedure. The computed conclusion, F/U indicators, and derived condition states are removed to prevent copying. All substantive input grounds and judgments remain because they are what the reviewer must reconstruct.

The reviewer must not initially receive expected-result matrices, analysis reports, or development records. A tension cannot be completely concealed from someone reading its grounds; this limitation is disclosed.

## Procedure
1. Record identity/role, experience, and prior exposure in `human_review_form.json`. Do not invent details or complete responses for the reviewer.
2. Read the claim, level, scope, reference, and horizon. Identify its documentary origin and the absence of a recorded individual episode.
3. For D01–D06, propose `supported`, `contradicted`, or `not_established`. Cite IDs and versions of evidence, inferences, reasons, issues, and methods. The reviewer may report a condition as not reconstructable and explain what is missing.
4. Identify the favourable chain and any independent contrary chain. Explain why the absence of the former does not imply the latter.
5. Propose a conclusion and identify any additional assumptions that would be required. Do not fill gaps as facts.
6. Record broken references, hidden steps, scope ambiguities, and judgments whose acceptance is unexplained. Distinguish a documented but disputable judgment from a hidden judgment.
7. Reveal `execution/A-01.assessment.json` only after the initial response has been saved. Compare conditions and conclusion; record matches, differences, and causes. Preserve the first response.
8. Record whether explaining a difference requires changing code, specification, grounds, or interpretation. Do not correct the materials during the initial reconstruction.

## Evidence to Preserve
Original form, consulted IDs, reconstructed conditions, conclusion, chains, missing steps, added assumptions, discrepancies, and subsequent clarifications. Duration is optional and descriptive; it is not an acceptance threshold.

## Interpretation Criterion
The frozen CL2 criterion is reconstruction without hidden information. A required but unavailable premise is evidence against that criterion even if the conclusion happens to match. If the reviewer reconstructs the reasoning but disputes a curated judgment, distinguish traceability from substantive adequacy. If clarification from the authors is required, preserve the issue as a limitation of the initial package and record a new version for later review.

Do not set a passing percentage after seeing responses. Do not treat one review as evidence of generalization or universal comprehensibility.

## Optional Extension
R-01/R-02, U-01/U-02, and P-01/P-02 may subsequently be reviewed as additional contrasts. They are not part of Baseline v1's required human case. Register their inclusion as a later extension rather than retrospectively changing the baseline.

## English Edition
The input narratives and explanatory documents have been translated. Historical assessment identifiers are preserved in the reconstruction materials. Original and translated byte hashes are distinguished in `TRANSLATION_PROVENANCE.json`; translation does not constitute a completed review.
