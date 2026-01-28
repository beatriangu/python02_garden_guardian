🌱 Python Garden — Data Guard
Garden Guardian · Data Engineering for Smart Agriculture

Repository: python02_data_guard

This repository is part of the Python Garden learning path and contains the exercises developed in the Data Guard module (also known as Garden Guardian).

The focus of this module is robust error handling and defensive programming in Python, applied to realistic data engineering scenarios inspired by smart agriculture systems.

Building on the foundations of Python basics (Module 00) and Object-Oriented Programming (Module 01), this module introduces the mindset required to design resilient systems that continue working when things go wrong.

🎯 Learning Objectives

Throughout this module, the learner develops the ability to:

Understand why errors happen in real-world programs

Use try, except, else, and finally blocks correctly

Identify and handle different built-in exception types

Create custom exception classes for domain-specific errors

Raise meaningful errors with clear, helpful messages

Design programs that never crash unexpectedly

Build fault-tolerant data pipelines that recover gracefully from failure

The emphasis is not on avoiding errors, but on handling them intentionally and safely.

🧠 Core Concepts Covered

Exception handling with try / except

Catching specific vs generic exceptions

Multiple exception handling strategies

Custom exception classes and inheritance

The finally block and guaranteed cleanup

Raising errors with raise

Defensive programming principles

Designing systems that remain stable under failure

📐 General Rules & Constraints

As defined by the official subject:

All programs are written in Python 3.10+

Code follows flake8 / PEP 8 standards

Each exercise is contained in its own file

Simple docstrings are included for functions and classes

Both normal execution and error scenarios must be demonstrated

Only authorized functions and constructs are used per exercise

Programs must never crash

Solutions are intentionally simple and focused on learning

This module prioritizes clarity, correctness, and robustness over complexity.

🗂️ Exercise Overview & Progression

The exercises follow a clear and incremental progression, each introducing a new layer of resilience:

ex0 — Agricultural Data Validation Pipeline

First contact with try / except

Input validation and type conversion

Graceful handling of invalid sensor data

Ensuring the program keeps running despite errors

ex1 — Different Types of Problems

Exploration of common built-in exceptions:

ValueError

ZeroDivisionError

FileNotFoundError

KeyError

Catching errors individually and together

Understanding why different error types exist

ex2 — Making Your Own Error Types

Creation of custom exception classes

Error hierarchy using inheritance

Domain-specific errors (GardenError, PlantError, WaterError)

Catching grouped errors via a base exception

ex3 — Finally Block: Always Clean Up

Introduction to the finally block

Guaranteed cleanup regardless of success or failure

Resource management mindset

Ensuring system stability even during errors

ex4 — Raising Your Own Errors

Using raise to signal invalid states

Validating inputs explicitly

Designing helpful and precise error messages

Differentiating between detection and handling of errors

ex5 — Garden Management System

Integration of all previous concepts

A complete system using:

Custom exceptions

try / except / finally

Error recovery strategies

Demonstrates how resilient systems behave under failure

Focus on continuity, stability, and clarity

🧠 Design Philosophy

Across all exercises, the following principles are consistently applied:

Programs are designed to fail safely

Errors are expected, not exceptional

Each error has a clear meaning and purpose

Responsibility is explicit: detect, raise, handle

Cleanup is guaranteed

Systems remain usable even when operations fail

This module reflects a shift from “making code work” to making systems reliable.

🧪 Code Quality

Fully compliant with flake8 and PEP 8

Clear, minimal, and readable code

No unexpected crashes

Learning-only documentation excluded via .gitignore

🚀 Conclusion

The Data Guard module introduces a critical professional skill:
building software that survives real-world failure.

By the end of this repository, the learner demonstrates not only knowledge of Python exceptions, but a defensive programming mindset essential for data engineering, backend development, and production systems.

This module forms a direct bridge toward:

More advanced data pipelines

File and stream management

Backend robustness

Production-grade error handling

📌 Module completed — Python Garden · Data Guard 🌱