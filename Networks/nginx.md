NGINX at its core is a reverse proxy server.
- high-performance web server
- can handle high-concurrency
- low resource usage
- faster static content delivery than Apache httpd

## Installation on linux
`sudo apt install nginx -y`

To check if its running:
`sudo systemctl status nginx`

To run::
`sudo systemctl start nginx`

## NGINX configuration file

Everything in an nginx configuration file is either a **Directive** or a **Context**

### Directives
Directives are of 2 types
- **Simple directives**: it consists of the directive name and the space delimited parameters, like `listen`, `return` and others, and are terminated by semicolons
- **Block directives**: similar to simple directives, except that instead of ending with semicolons, they end with a pair of curly braces `{ }` enclosing additional instructions

A **Block Directive** capable of containing other directives inside it is called a context. There are 4 core contexts in NGINX
1. `events { }` - this context is used for settings global configuration regarding how NGINX is going to handle requests on a general level. There can only be one `events` context in a valid configuration file
2. `http { }` - this is used for defining configuration regarding how the server is going to handle HTTP and HTTPS requests, specifically. There can be only one `http` context in a valid configuration file
3. `server { }` - this context is nested inside the `http` context and used for configuring specific virtual servers within a single host. There can be multiple `server` contexts in a valid configuration file nested inside the `http` context. Each `server` context is considered a virtual host
4. `main { }` - it is the configuration file itself, anything written outside of the 3 previously mentioned contexts is on the `main` context
When a request reaches the nginx server, the `listen` directive is one of the ways to identify the correct `server` context to hit.



