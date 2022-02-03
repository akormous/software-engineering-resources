# API
This document describes some of the best practices to use when designing an API.

For a quick introduction, read this PDF: [API_Design_101.pdf](https://github.com/akormous/software-engineering-resources/API101/API_Design_101.pdf)

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