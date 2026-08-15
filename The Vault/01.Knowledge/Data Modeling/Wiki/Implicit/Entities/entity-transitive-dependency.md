---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: entity
tags: [entity, database, Data Modeling]
---

# Transitive Dependency

<!-- A data dependency pattern where Field A determines Field B and Field B determines Field C, but Field C should only depend on Field A. This creates update anomalies when B changes. -->

## Definition

A data dependency pattern where Field A determines Field B and Field B determines Field C, but Field C should only depend on Field A. This creates update anomalies when B changes.
