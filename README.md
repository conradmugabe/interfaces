# Interfaces
![build workflow](https://github.com/conradmugabe/interfaces/actions/workflows/testing.yml/badge.svg)
[![codecov](https://codecov.io/github/conradmugabe/interfaces/branch/main/graph/badge.svg?token=5F3GTE485A)](https://codecov.io/github/conradmugabe/interfaces)

Implementation of interfaces using python.

## Why use interfaces?

Interfaces help us reduce coupling within our code. Interfaces help us

So, instead of depending on an actual implementation of a class, we can switch to an abstraction.

We do this through depedency injection. Which is one of the SOLID principles.

## Implementations

The concept of the interfaces are demonstrated here with databases. All full tested. Each database instance can be swapped out for another since they all implement the same interface.

1. In Memory Database
1. NoSQL (Mongo Database)
1. SQL (Postgres Database)

## References

This is an interesting [blog](https://blog.cleancoder.com/uncle-bob/2015/01/08/InterfaceConsideredHarmful.html) by Robert C Martin on the difference between `interfaces` and `abstract classes` or should I say similarities.