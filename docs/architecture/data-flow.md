# Data flow

1. Upstream Retriever sends [Query, List[Candidates]] to Gateway Controller.
2. Gateway Controller forwards payload to Reranker Engine.
3. Reranker Engine computes scores using cross-attention mechanism.
4. Engine sorts candidates by score descending.
5. Gateway Controller returns reordered list.
6. On failure, Fallback Handler returns original order with a warning flag.

```mermaid
flowchart LR
    client([Client]) --> api[HTTP / CLI adapter]
    api --> bus[[Message bus]]
    bus --> orch{{Orchestrator}}
    orch --> s0["Gateway Controller<br/><i>ingest</i>"]
    s0 --> s1["Corpus Retrieval<br/><i>retrieve</i>"]
    s1 --> s2["Metrics Collector<br/><i>enrich</i>"]
    s2 --> s3["Ranking Cache<br/><i>cache</i>"]
    s3 --> s4["Reranker Engine<br/><i>score</i>"]
    s4 --> s5["Fallback Handler<br/><i>fallback</i>"]
    s5 --> s6["Access Policy<br/><i>policy</i>"]
    s6 --> s7["Token Budget Governor<br/><i>budget</i>"]
    s7 --> s8["Answer Assembly<br/><i>answer</i>"]
    s8 --> out([Outcome: answer or abstain])
    orch -.-> obs[(Metrics / traces / audit)]
    orch -.-> store[(Run repository)]
```

The `PipelineContext` is the only mutable object in a run. Stages read the request,
mutate candidates, and append decisions. Nothing else carries run state.
