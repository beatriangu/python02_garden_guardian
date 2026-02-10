# 🌱 Python Garden — Data Guard  
### Garden Guardian · Defensive Programming & Error Handling in Python

Repository: **python02_data_guard**

**This repository is part of a personal Python learning journey focused on
clarity, mental models and explainable code.**

This module is part of the Python Garden learning path and focuses on
**robust error handling and defensive programming in Python**, applied to
realistic data engineering scenarios inspired by smart agriculture systems.

Building on the foundations of Python basics (Module 00) and
Object-Oriented Programming (Module 01), this module introduces the mindset
required to design **resilient systems** that continue working when things
go wrong.

---

## 🎯 Learning Objectives

Throughout this module, the learner develops the ability to:

- Understand why errors happen in real-world programs
- Use `try`, `except`, `else`, and `finally` blocks correctly
- Identify and handle different built-in exception types
- Create custom exception classes for domain-specific errors
- Raise meaningful errors with clear, helpful messages
- Design programs that **never crash unexpectedly**
- Build fault-tolerant systems that recover gracefully from failure

The emphasis is **not on avoiding errors**, but on **handling them
intentionally and safely**.

---

## 🧠 Core Concepts Covered

- Exception handling with `try / except`
- Catching specific vs generic exceptions
- Multiple exception handling strategies
- Custom exception classes and inheritance
- The `finally` block and guaranteed cleanup
- Raising errors explicitly with `raise`
- Defensive programming principles
- Designing systems that remain stable under failure

---

## 📐 Rules & Constraints

As defined by the subject and learning goals:

- Python 3.10+
- Code follows `flake8` / PEP 8 standards
- Each exercise is contained in its own file
- Simple docstrings included for functions and classes
- Both normal execution and error scenarios are demonstrated
- Only authorized constructs are used per exercise
- Programs must **never crash**
- Solutions remain intentionally simple and learning-focused

This module prioritizes **clarity, correctness, and robustness**
over complexity.

---

## 🗂️ Exercise Overview & Progression

The exercises follow a clear and incremental progression, each introducing
a new layer of resilience:

### ex0 — Agricultural Data Validation Pipeline
- First contact with `try / except`
- Input validation and type conversion
- Graceful handling of invalid sensor data
- Ensuring the program continues running despite errors

### ex1 — Different Types of Problems
- Exploration of common built-in exceptions:
  - `ValueError`
  - `ZeroDivisionError`
  - `FileNotFoundError`
  - `KeyError`
- Catching errors individually and together
- Understanding why different error types exist

### ex2 — Making Your Own Error Types
- Creation of custom exception classes
- Error hierarchy using inheritance
- Domain-specific errors (`GardenError`, `PlantError`, `WaterError`)
- Catching grouped errors via a base exception

### ex3 — Finally Block: Always Clean Up
- Introduction to the `finally` block
- Guaranteed cleanup regardless of success or failure
- Resource management mindset
- Ensuring system stability during errors

### ex4 — Raising Your Own Errors
- Using `raise` to signal invalid states
- Explicit input validation
- Designing helpful and precise error messages
- Separating error detection from error handling

### ex5 — Garden Management System
- Integration of all previous concepts
- A complete system using:
  - custom exceptions
  - `try / except / finally`
  - recovery strategies
- Demonstrates how resilient systems behave under failure
- Focus on continuity, stability, and clarity

---

## 🧠 Design Philosophy

Across all exercises, the following principles are consistently applied:

- Programs are designed to **fail safely**
- Errors are expected, not exceptional
- Each error has a clear meaning and purpose
- Responsibilities are explicit:
  - detect
  - raise
  - handle
- Cleanup is guaranteed
- Systems remain usable even when operations fail

This module reflects a shift from **“making code work”** to
**“making systems reliable”**.

---

## 🧪 Code Quality

- Fully compliant with `flake8` and PEP 8
- Clear, minimal, and readable code
- No unexpected crashes
- Learning-only documentation excluded via `.gitignore`

---

## 🚀 Conclusion

The Data Guard module introduces a **critical professional skill**:
building software that survives real-world failure.

By the end of this repository, the learner demonstrates not only knowledge
of Python exceptions, but a **defensive programming mindset** essential for:

- data engineering
- backend development
- production-grade systems

---

📌 *Module completed — Python Garden · Data Guard* 🌱
