---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [dax, spatial, graph, transitive-closure, network]
---

# Transitive Closure in DAX

Finding all pairs of entities within a given distance threshold — a graph connectivity problem solved with DAX.

## Concept

Transitive closure = for every pair of points (A, B), determine if there exists a path from A to B through intermediate nodes, where each edge in the path satisfies a distance threshold. In geographic terms: "find all locations reachable from this origin within N kilometers, jumping through intermediate waypoints."

## The Problem

Naive approach: compare every pair. For N locations, that's N² comparisons. With transitive closure through intermediate nodes, the complexity grows.

Deckler's approach: build an adjacency matrix (all pairs within threshold) and then compute the transitive closure using DAX iterations.

## Pattern Structure

```dax
Transitive Closure =
    // Step 1: All direct pairs within threshold
    VAR __DirectPairs =
        FILTER(
            CROSSJOIN( 'Locations', 'Locations' ),
            'Locations_1'[LocationKey] <> 'Locations_2'[LocationKey]
            && [HaversineDistance] <= __Threshold
        )
    // Step 2: Iteratively find indirect connections
    VAR __Closure = ... (recursive expansion through intermediaries)
    RETURN __Closure
```

This is an advanced pattern typically requiring multiple DAX iterations or a pre-computed bridge table.

## Use Cases

- Delivery zone coverage (all addresses reachable within 50km)
- Service area analysis
- Network/path connectivity in DAX models
- Social network distance (friends-of-friends)

## Related

- [[haversine-distance-dax]] — underlying distance calculation
- [[nearest-point-dax]] — single nearest point
- [[dax-index-pattern-deckler]] — row numbering for iteration
