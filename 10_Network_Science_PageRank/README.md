# Network Science — PageRank and Graph Analysis

**Subject Area:** Graph Theory · Network Science · Algorithm Implementation · Data Analysis

---

## What It Does

This project implements and analyzes **PageRank** and **Personalized PageRank** algorithms on real graph datasets using Python and NetworkX. The notebooks compute node importance scores across multiple convergence iterations, compare simplified vs. personalized variants, and analyze how graph structure (degree distribution, centrality, clustering) shapes the resulting rankings. Convergence behavior is tracked across iterations and output to structured result files for further analysis.

### Contents

| File | Description |
|------|-------------|
| `Assignment_PageRank.ipynb` | PageRank and Personalized PageRank implementation with convergence analysis |
| `Assignment_1_NetworkX.ipynb` | Graph construction, degree/centrality analysis, and network property exploration with NetworkX |
| `simplified_pagerank_iter10.txt` | PageRank scores at 10 iterations |
| `simplified_pagerank_iter25.txt` | PageRank scores at 25 iterations |
| `personalized_pagerank_iter10.txt` | Personalized PageRank (teleportation vector biased) at 10 iterations |
| `personalized_pagerank_iter25.txt` | Personalized PageRank at 25 iterations |

## Problem Addressed

Ranking nodes in a graph by influence is a fundamental problem in network analysis — with applications ranging from web search (Google's original PageRank) to social network influence modeling, malware propagation analysis, and supply chain risk assessment. This project examines how convergence speed and final rankings differ between the simplified (global) PageRank and the personalized variant, and what graph topology properties drive those differences.

## Practical Relevance

Graph-based algorithms appear across cybersecurity and data engineering contexts: network traffic graphs for lateral movement detection, knowledge graphs for threat intelligence, and social graphs for influence operation analysis. Understanding how PageRank and its variants work at the algorithm level — not just as a library call — is foundational for building or auditing any system that reasons about network influence or connectivity.

## Tools, Languages, and Libraries

Python · NetworkX · NumPy · Jupyter Notebook · graph algorithms (PageRank, centrality measures, degree distribution)

## Skills Demonstrated

- Graph algorithm implementation: PageRank power iteration from first principles
- Network analysis: degree centrality, betweenness, clustering coefficient
- Convergence analysis: tracking algorithm behavior across iterations and measuring stability
- Data interpretation: connecting graph structure properties to ranking outcomes
- Reproducible research: Jupyter notebooks with documented methodology and outputs

## Extension Ideas

- Apply Personalized PageRank to a cybersecurity knowledge graph (MITRE ATT&CK) to rank most impactful techniques
- Implement HITS (Hubs and Authorities) as an alternative to PageRank and compare on the same dataset
- Analyze how graph sparsification or targeted node removal affects rank stability
- Extend to temporal graphs: how do rankings evolve as edges are added or removed over time?

---

*Georgia Institute of Technology — MS Computer Science · CS 7280: Network Science*
