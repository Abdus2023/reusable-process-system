---
name: collaboration-mapping
description: Map publicly evidenced collaborations and co-appearances between creators as a provenance-backed graph. Use when creator relationships or network structure are in scope.
---

# Collaboration Mapping

## Procedure
1. Define collaboration types: co-created video, guest appearance, interview, explicit mutual promotion, event appearance, or other documented interaction.
2. Require a public source for each edge and record its date and type.
3. Distinguish a direct collaboration from mere mention, shared topic, repost, or co-occurrence in a search result.
4. Store edge direction only when meaningful and supported; otherwise represent an undirected relation.
5. Record evidence URL, event/video identifier, observation date, and confidence.
6. Treat absence of observed collaboration as unknown, not proof that none exists.
7. Do not infer friendship, endorsement, political alignment, audience overlap, or private relationships from collaboration evidence.
8. Visualize only the verified edges and identify incomplete coverage.

## Output
Node registry, evidence-backed edge list, collaboration types, time window, and graph limitations.

## Failure conditions
Do not add edges based on speculation or inferred relationships.