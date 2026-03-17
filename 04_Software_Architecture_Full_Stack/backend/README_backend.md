# Spring Boot Backend — Pokémon Tournament Application

*CS 6310 Software Architecture and Design*

## Overview

This is the RESTful API backend for a team-built Pokémon tournament simulation platform, developed as a multi-iteration software architecture project. The backend is a **Spring Boot 3** Java application connected to a **PostgreSQL** database, fully containerized with Docker, and secured with **JWT-based authentication and role-based access control (RBAC)**.

The project was built incrementally across multiple architecture assignments, each adding new subsystems with formal Architectural Decision Records (ADRs) documenting every major design choice.

---

## Architecture

The backend follows a **layered Spring Boot architecture** with strict separation of concerns:

```
Controller Layer  →  receives HTTP requests, validates input, returns ResponseEntity
Service Layer     →  business logic, transaction management, cross-entity coordination
Repository Layer  →  Spring Data JPA interfaces for database access (zero boilerplate)
Model/DTO Layer   →  JPA entities for persistence; DTOs for clean API contracts
Security Layer    →  JWT filter chain, BCrypt password hashing, @PreAuthorize annotations
```

Each domain (Battle, Pokémon, User, Item) is organized as its own package with its own Controller, Service, Repository, and DTO — a clean vertical-slice structure that scales linearly as features are added.

---

## Key Components

### `BattleService.java` — Core Game Logic
The heart of the application. `BattleService` orchestrates full battle initialization and execution:
- Accepts a `BattleRequest` containing Pokémon IDs, random seed, and max turns
- Hydrates each Pokémon via `BattlePokemonService`, assigns items via `ItemService`
- Delegates turn-by-turn execution to `Battle.execute()`, which runs the full simulation
- Persists battle results and win records back to the database
- Returns a fully assembled `BattleDto` including per-Pokémon sprite URLs fetched live from the PokéAPI

The service layer cleanly abstracts all business logic away from the controller — the controller performs no computation, only HTTP boundary handling.

### `JwtService.java` — JWT Authentication
Implements the full JWT lifecycle: token generation, refresh token issuance, claims extraction, and validation. Key design choices:
- HS256 HMAC signing with a Base64-encoded secret key
- Short-lived access tokens (2 hours) with separate long-lived refresh tokens (24 hours)
- Stateless authentication — no server-side session storage; every request is self-contained
- Token parsing via the `io.jsonwebtoken` (JJWT) library with a fluent builder API

### `SecurityConfiguration.java` + `JwtAuthenticationFilter.java` — Filter Chain
Every incoming request passes through a custom `JwtAuthenticationFilter` that extracts and validates the JWT before Spring Security's authorization layer runs. Stateless session management (`SessionCreationPolicy.STATELESS`) ensures horizontal scalability.

### `PokemonController.java` — Role-Based Access Control
REST endpoints are annotated with `@PreAuthorize` to enforce fine-grained RBAC:
- `ROLE_USER`, `ROLE_TRAINER`, `ROLE_ADMIN` — can view Pokémon and initiate battles
- `ROLE_TRAINER`, `ROLE_ADMIN` — can create new Pokémon entries
- `ROLE_ADMIN` — can manage user permissions

This pattern decouples authorization logic from business logic entirely — adding a new role requires only an annotation change, not a code restructure.

### `docker-compose.yml` — Full-Stack Container Orchestration
A three-container setup deployable with a single command:
- `api` — Spring Boot JAR on port 8080, connected to `db` via Docker's internal bridge network (`gatech_internal`, subnet `10.17.0.0/16`)
- `site` — React frontend on port 3001
- `db` — PostgreSQL 16.2

The internal bridge network demonstrates proper network isolation: the database is not exposed to the host, only reachable by the API container using Docker DNS (`DB_HOST=db`). The API container uses a startup delay (`sleep 5`) to handle database readiness — a pragmatic solution documented in inline comments.

---

## Architectural Decision Records (ADRs)

The `ADRs/` folder contains formal architecture decisions written in standard ADR format (Title / Status / Context / Decision / Consequences). The authentication ADR captures the full reasoning behind the RBAC model: three distinct roles, four seeded initial users, and a deliberate trade-off acknowledging the increased scope and future maintenance cost of the auth subsystem.

Writing ADRs is a professional engineering practice that creates an auditable record of *why* the architecture looks the way it does — invaluable for onboarding, code review, and long-term maintainability.

---

## Design Decisions Worth Noting

**DTO pattern throughout** — API responses never expose JPA entity objects directly. Every endpoint returns a DTO, preventing accidental data leakage (e.g., password hashes, internal IDs) and decoupling the database schema from the API contract.

**Spring Data JPA repositories** — Every entity has a typed `JpaRepository` interface with zero implementation code. Spring generates all SQL at startup, making data access consistent and type-safe across the entire codebase.

**`@Autowired` dependency injection** — All service dependencies are injected by Spring's IoC container. No static singletons, no manual instantiation. Swapping implementations (e.g., for testing) requires only a configuration change.

**`GlobalExceptionHandler.java`** — A `@ControllerAdvice` class centralizes all exception handling. Rather than scattering try-catch blocks through controllers, all errors surface through one handler that maps exceptions to appropriate HTTP status codes.

---

## Reusability

The security package (`JwtService`, `JwtAuthenticationFilter`, `SecurityConfiguration`, `ApplicationConfiguration`) is largely domain-agnostic and can be lifted directly into any new Spring Boot project as a JWT auth starter. The DTO + Controller + Service + Repository pattern is the standard Spring Boot project structure used across the industry.
