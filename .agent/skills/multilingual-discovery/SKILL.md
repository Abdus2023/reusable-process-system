---
name: multilingual-discovery
description: Discover candidate content creators using structured, multilingual searches across web search and YouTube. Use before verification and when coverage gaps remain.
---

# Multilingual Discovery

## Scope
Discover candidates; do not certify them. Search is a lead-generation step.

## Procedure
1. Turn the research objective into explicit inclusion/exclusion criteria.
2. Build query families in relevant languages and writing systems. For Tunisia, consider Tunisian Arabic/Darija, Arabic script, French, English, and transliteration variants where useful.
3. Search multiple query patterns: creator categories, platform-native terms, regional terms, niche topics, interviews, collaborations, and creator self-descriptions.
4. Search YouTube directly where available and inspect channel pages or video descriptions rather than relying only on snippets.
5. Log query, platform, observation date, candidate, candidate URL, discovery source, and next verification action.
6. Search for under-covered categories/regions/languages based on a coverage matrix, not arbitrary quotas.
7. Deduplicate candidate leads conservatively; unresolved aliases remain linked candidates until identity is resolved.
8. Pass candidates to `identity-resolution`; do not mark VERIFIED from search results alone.

## Query design
Use multiple spellings and aliases. Distinguish searches for Tunisian creators from searches for content about Tunisia. Avoid assuming language proves nationality or residence.

## Output
Candidate ledger, query log, coverage gaps, duplicate hypotheses, and next verification actions.

## Failure conditions
If search is unavailable, state which sources were not queried. If a source is inaccessible, record the access failure; do not replace it with invented evidence.