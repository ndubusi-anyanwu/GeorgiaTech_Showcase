# Network Protocol Implementations in Python

**Subject Area:** Computer Networks · Distributed Systems · Routing Algorithms · Protocol Design

---

## What It Does

This project contains clean Python implementations of three foundational network protocols — **BGP measurement analysis**, **Distance Vector Routing** (Bellman-Ford), and **Spanning Tree Protocol** (STP) for Ethernet switch loop prevention. Each implementation models the core algorithm driving the protocol, demonstrating how distributed systems converge on consistent network state without centralized coordination.

### Implementations

| File | Protocol | Description |
|------|----------|-------------|
| `bgp_measurements.py` | Border Gateway Protocol | Parses and analyzes BGP routing table measurements; models AS-path propagation and reachability |
| `distance_vector_routing.py` | Distance Vector / Bellman-Ford | Distributed routing algorithm where each node maintains a vector of best-known costs to all destinations and converges through iterative neighbor updates |
| `spanning_tree_switch.py` | Spanning Tree Protocol (STP) | Layer-2 loop prevention algorithm; models root bridge election, port state transitions, and BPDUs |

## Problem Addressed

Real network infrastructure runs on these protocols. Understanding their mechanics — not just their configuration syntax — is essential for diagnosing routing failures, designing resilient network topologies, and identifying protocol-level attack surfaces (BGP hijacking, STP manipulation). Implementing them from scratch builds the deep intuition that separates network engineers from network operators.

## Practical Relevance

These implementations are directly applicable to:

- Network security: BGP hijacking, route poisoning, and STP topology attacks require protocol-level understanding to defend against
- Infrastructure engineering: reasoning about convergence time, routing loops, and failover behavior
- Security architecture: designing segmented, resilient network topologies with STP and routing protocols in mind
- CISSP/CISM exam domains: network security architecture and telecommunications

## Tools, Languages, and Libraries

Python · socket programming concepts · graph algorithms (Bellman-Ford, BFS) · BGP measurement datasets

## Skills Demonstrated

- Protocol implementation: translating RFC-level algorithm descriptions into working code
- Distributed algorithm design: modeling asynchronous, message-passing convergence
- Network topology reasoning: path selection, loop avoidance, root election
- Code clarity: writing implementations that serve as readable protocol documentation

## Extension Ideas

- Implement Dijkstra-based OSPF link-state routing and benchmark convergence against Distance Vector
- Add BGP path preference attributes (local preference, MED) and model policy-based routing decisions
- Simulate a BGP hijacking attack and implement RPKI-style origin validation as a countermeasure
- Visualize spanning tree topology changes using NetworkX and Matplotlib

---

*Georgia Institute of Technology — MS Cybersecurity · CS 6250: Computer Networks*
