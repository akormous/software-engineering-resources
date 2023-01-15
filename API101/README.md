# API
This document describes some of the best practices to use when designing an API.

For a quick introduction to REST design, read this PDF: [REST_Design_101.pdf](./REST_Design_101.pdf)

## Basic stuff, good to know
<details>
    <summary>Data Contract</summary>

- It is an agreement on the shape and general content of the request and/or response data
- It is the documentation of an API, where the behavior of the API is described
- The document includes endpoint urls, action of each endpoint, arguments, examples and any other details that you think is interesting to be documented
- Check out: [OpenAPI](https://oai.github.io/Documentation/)
</details>

---

## Versioning
API versioning is the practice of transparently managing changes to your API. 

It is the ability to enhance an API without disintegrating the client's application when new versions are developed. Versioning permits clients to keep on using an existing REST API and only migrate or update their applications to the latest API version when they are ready.

### When to API version?
Whenever a breaking change is made. Some of the scenarios of breaking change:
- Renaming fields or resources paths
- Changing payload structure to incorporate maybe a different data type or something
- Removing parts of the API endpoints either to improve design or fix poor choices of HTTP verbs

# OpenAPI Specification

The OpenAPI Specification (OAS) defines a standard, language-agnostic interface to HTTP APIs which allows both humans and computers to discover and understand the capabilities of the service without access to source code, documentation, or through network traffic inspection.

An OpenAPI defintion can then be used by documentation generation tools to display the API, code generation tools to generate servers and clients in various programming languages, testing tools, and many other use cases.

## OpenAPI Document

A self-contained or composite resource which defines or describes an API or elements of an API.

**Design your API first instead of code first. Because it sucks when you have to change your API after you complete coding.**

## Editors

- https://stoplight.io/welcome (for zoomers)
- https://editor.swagger.io/ (for boomers)