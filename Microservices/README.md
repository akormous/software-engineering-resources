![Microservices](./static/microservices_title.png)

# Enterprise Service Bus

ESB is fundamentally an architecture. It is a set of rules and principles for integration numerous applications together over a bus-like infrastructure. The core concept of the ESB is that you integrate different applications by putting a communication bus between them and then enable each application to talk to the bus. This <span style="color: cyan">decouples</span> systems from each other, allowing them to communicate without dependency on or knowledge of other systems on the bus.

The ESB performs transformations of data models, handles connectivity, performs message routing, converts communication protocols and potentially manages the composition of multiple requests.

## ESB and SOA

An ESB is an essential component of SOA, or [Service Oriented Architecture](https://en.wikipedia.org/wiki/Service-oriented_architecture), a software architecture emerged in the late 1990s. SOA defines a way to make software components reusable via service interfaces.

## Benefits

In theory, an ESB simplifies communication, messaging, and integration between services across the enterprise. Software application can simply connect to the ESB and leave it to the ESB to transform the protocols, route the messages, and transform into the data formats as required providing the interoperability to get the transactions executed.

## Downsides

While ESBs were deployed successfully in many organizations, in many other organizations the ESB came to be seen as the bottleneck. Making changes or enhancements to ine integration could destabilize others who used that same integration. Updates to the ESB middleware often impacted existing integrations.
Because the ESB was centrally managed, application teams soon found themselves waiting in line for their integrations.

For a deeper dive, read [this article](https://developer.ibm.com/articles/cl-lightweight-integration-1/).

# ESB and Microservices

Microservices architecture enables the internals of a single application to be broken up into small pieces that can be independently changed, scaled, and administered. Microservices emerged and gained steam with the rise of [virtualization](https://www.redhat.com/en/topics/virtualization/what-is-virtualization), [cloud computing](https://www.redhat.com/en/topics/cloud), [Agile development practices](https://www.atlassian.com/agile), and [DevOps](https://www.redhat.com/en/topics/devops).

Microservices offers the following:

- Improved developer agility and productivity
- Simpler, more cost effective scalability
- Greater resilience

Recommended reading:
- [SOA vs. Microservices](https://www.ibm.com/cloud/blog/soa-vs-microservices)
- [The fate of the ESB](https://developer.ibm.com/articles/cl-lightweight-integration-1/)