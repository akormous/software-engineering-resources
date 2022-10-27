# Spring Security

* Powerful and highly customizable **authentication** and **access-control** framework. 
* de-facto standard for securing Spring-based applications.

<details>
    <summary>Features</summary>

* Comprehensive and extensible support for both Authentication and Authorization
* Protection against attacks like session fixation, clickjacking, cross site request forgery etc.
* Servlet API integration
* Optional integration with Spring web MVC
</details>

<details>
    <summary>What can Spring Security do?</summary>

* Username/password authentication
* SSO / Okta / LDAP
* App level authorization
* Intra App authorization like OAuth
* Microservice security (using tokens, JWT)
* Method level security
</details>

---

## Spring Security Concepts

1. **Authentication** - who are you
2. **Authorization** - what do you want
3. **Principal** - currently logged-in account
4. **Granted Authority** - what can this guy do, fine-grained access
5. **Roles** - what sorts of things this guy can do, coarse-grained access