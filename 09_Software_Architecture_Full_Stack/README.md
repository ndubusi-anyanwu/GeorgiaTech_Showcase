# Full-Stack Application with Enterprise Software Architecture

**Subject Area:** Software Architecture · Backend Engineering · Frontend Development · Containerization · System Design

---

## What It Does

This project is a fully deployed, containerized full-stack web application built with a Spring Boot backend, React frontend, and PostgreSQL database — orchestrated with Docker Compose. The system was designed following formal software architecture principles: Architecture Decision Records (ADRs) document every major technical choice, and UML class and sequence diagrams capture both static structure and runtime behavior. The application implements RESTful API design, service-layer separation, and component-based frontend architecture.

## Problem Addressed

Building software that is maintainable, extensible, and communicable to a team requires intentional architectural decision-making — not just working code. This project addresses the challenge of designing a system from requirements through implementation while producing the documentation artifacts (ADRs, UML diagrams) that real engineering teams use to make decisions durable and reviewable. It demonstrates the full software development lifecycle from architecture through containerized deployment.

## Practical Relevance

This project reflects the engineering practices used in production software teams: infrastructure-as-code with Docker Compose for portable deployment, architectural records for team decision transparency, and formal diagram artifacts for onboarding and review. The skills demonstrated are directly applicable to:

- Full-stack product engineering roles
- Platform and DevOps engineering
- Systems design interviews at senior/staff level
- Technical lead roles requiring documentation and architecture ownership

## Project Structure

```
backend/          Spring Boot REST API (Java)
frontend/         React single-page application
ADRs/             Architecture Decision Records
docker-compose.yml  Container orchestration
Makefile          Build and run automation
class_diagram.pdf   UML class diagram
sequence_diagram*.pdf  UML sequence diagrams for key workflows
```

## Tools, Languages, and Libraries

Java · Spring Boot · React · JavaScript · PostgreSQL · Docker · Docker Compose · Make · UML · REST API design

## Skills Demonstrated

- System architecture design: translating requirements into layered, decoupled components
- Backend engineering: REST API development with Spring Boot, service/repository patterns
- Frontend development: component-based UI with React
- Containerization: multi-service Docker Compose orchestration for reproducible environments
- Technical documentation: Architecture Decision Records (ADRs), UML class and sequence diagrams
- Build automation: Makefile targets for common development workflows

## Extension Ideas

- Add JWT-based authentication and authorization to the REST API
- Implement CI/CD pipeline with GitHub Actions for automated test and deploy
- Add Kubernetes Helm chart for cloud deployment (GKE, EKS, or AKS)
- Extend ADRs to cover security architecture decisions (auth, data encryption, API rate limiting)

---

*Georgia Institute of Technology — MS Computer Science · CS 6310: Software Architecture and Design*
