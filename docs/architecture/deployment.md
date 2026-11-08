# Deployment

```mermaid
flowchart LR
    lb[Ingress / load balancer] --> svc[Service]
    svc --> p1[reranking-gateway pod 1]
    svc --> p2[reranking-gateway pod 2]
    svc --> p3[reranking-gateway pod N]
    hpa[HorizontalPodAutoscaler] -. scales .-> p1
    cm[(ConfigMap: TOML profile)] -.-> p1
    prom[(Prometheus)] -. scrapes /metrics .-> svc
    pvc[(Volume: jsonl runs + audit)] -.-> p1
```

- Stateless replicas behind a Service; scale on CPU via HPA.
- Configuration is a TOML profile mounted from a ConfigMap and selected with `RERANKING_GATEWAY_CONFIG`.
- Readiness uses `/readyz`; liveness uses `/healthz`.
- PodDisruptionBudget keeps at least one replica during voluntary disruptions.
- NetworkPolicy allows ingress only from the gateway namespace.
