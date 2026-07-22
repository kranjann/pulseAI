# PulseAI

> Build a production-style AI-powered CI Failure Analysis System while learning every major AI Engineering concept required for LLM/GenAI interviews.

---

# Vision

PulseAI is **not** a toy chatbot.

It is an end-to-end AI backend application that analyzes CI/CD test failures, retrieves similar historical incidents using semantic search, and produces AI-assisted root cause analysis.

The project is intentionally designed to teach modern AI Engineering concepts through one coherent system instead of isolated tutorials.

---

# Primary Goal

Learn AI Engineering by building one realistic project.

Every feature must teach at least one interview-worthy concept.

The project is **education-first**, not feature-first.

---

# Learning Objectives

By the end of this project, I should be comfortable explaining and implementing:

## Backend Engineering

- Python
- FastAPI
- Pydantic
- Project Architecture
- Dependency Injection
- Logging
- Configuration Management
- Testing (Pytest)
- Error Handling
- API Design

---

## AI Engineering

- Prompt Engineering
- Structured Outputs
- Embeddings
- Semantic Search
- Chunking Strategies
- Vector Databases
- Retrieval-Augmented Generation (RAG)
- Context Construction
- Hallucination Prevention
- LLM Evaluation
- Similarity Scoring
- AI Cost Optimization
- Token Optimization

---

## Production Concepts

- Multi-stage AI Pipelines
- Separation of Deterministic Logic vs AI Reasoning
- AI System Architecture
- Performance Considerations
- Caching
- Observability
- Scaling AI Applications

---

# Core Principle

Use deterministic code whenever possible.

Use AI only when reasoning is required.

Example:

Deterministic:

- Parse logs
- Extract filenames
- Extract assertions
- Extract line numbers

AI:

- Explain probable root cause
- Suggest fixes
- Summarize failures
- Estimate confidence

---

# Final Architecture

```text
                      Historical Incidents
                              │
                     Chunk Documents
                              │
                       Generate Embeddings
                              │
                         Vector Database
                              │
                     Retrieve Top-K Matches
                              ▲
                              │
                     Current Parsed Failure
                              │
                        Prompt Builder
                              │
                              ▼
                            LLM
                              │
                              ▼
                  Structured Root Cause Analysis
                              │
                              ▼
                         FastAPI Endpoint
```

---

# Project Roadmap

## Phase 1 — Deterministic Parsing ✅

Purpose:

Convert noisy pytest logs into structured data.

Concepts:

- Multi-pass parsing
- Stateful parsing
- Pydantic models
- Defensive parsing

Output:

```python
TestReport
```

---

## Phase 2 — Knowledge Base

Purpose:

Create historical CI incidents.

Concepts:

- Dataset design
- Ground truth
- Metadata

Output:

Historical incidents ready for retrieval.

---

## Phase 3 — Chunking

Purpose:

Split long incident reports into meaningful chunks.

Concepts:

- Fixed chunking
- Recursive chunking
- Semantic chunking
- Chunk overlap

Questions this phase answers:

- Why do we chunk?
- What happens if chunks are too large?
- Why overlap?

---

## Phase 4 — Embeddings

Purpose:

Convert chunks into vectors.

Concepts:

- Sentence Transformers
- Embedding models
- Vector dimensions
- Cosine similarity

Questions:

- What is an embedding?
- Why are embeddings semantic?

---

## Phase 5 — Vector Database

Purpose:

Store and search embeddings efficiently.

Concepts:

- FAISS
- ChromaDB (comparison)
- Approximate Nearest Neighbor (ANN)

Questions:

- Why not SQL?
- Why not Python lists?
- Why FAISS?

---

## Phase 6 — Retrieval

Purpose:

Retrieve similar historical failures.

Concepts:

- Top-K retrieval
- Similarity thresholds
- Recall vs Precision

Output:

Top similar incidents.

---

## Phase 7 — Prompt Engineering

Purpose:

Construct prompts using retrieved context.

Concepts:

- Prompt templates
- Context windows
- Token optimization

---

## Phase 8 — LLM Reasoning

Purpose:

Generate root cause analysis.

Concepts:

- Reasoning
- Chain of thought (conceptually)
- Confidence estimation
- Structured outputs

---

## Phase 9 — Evaluation

Purpose:

Measure AI quality.

Concepts:

- Hallucination detection
- Retrieval evaluation
- Prompt evaluation
- Similarity scoring
- Ground truth comparison

---

## Phase 10 — FastAPI

Expose PulseAI as a production-ready API.

Endpoints:

- Upload log
- Parse log
- Retrieve incidents
- Generate RCA
- Health check

---

# Design Principles

Every new feature should answer:

1. What interview concept does this teach?
2. Would this exist in a production AI system?
3. Can deterministic code solve this instead of AI?
4. Is this improving architecture or just adding features?

If the answer is "No" to all four, don't build it.

---

# Tech Stack

Backend

- Python
- FastAPI
- Pydantic
- Pytest

AI

- Sentence Transformers
- OpenAI API
- FAISS
- LangChain (only where it adds value)

Utilities

- pathlib
- logging
- dotenv

---

# What This Project Is NOT

❌ A chatbot

❌ A LangChain demo

❌ An OpenAI wrapper

❌ A collection of AI buzzwords

Instead, it is a realistic AI engineering project that demonstrates how modern production AI systems are built.

---

# Success Criteria

By the end of PulseAI, I should be able to confidently explain:

- Why embeddings work
- Why chunking matters
- Why vector databases exist
- How RAG improves LLM responses
- How retrieval is evaluated
- How prompts are constructed
- Why deterministic parsing should happen before AI
- How an AI backend is architected end-to-end

More importantly, I should have built every one of these concepts myself.