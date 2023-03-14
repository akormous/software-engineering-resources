# HTTP (Hypertext Transfer Protocol)

* HTTP is an application-layer protocol for transmitting hypermedia documents, such as HTML.
* It is designed for communication between web browsers and web servers
* It follows a *client-server* model, with a client opening a connection to make a request, then waiting until it gets a response
* It is a stateless protocol

# HTTP request
Each HTTP request carries with it a series of encoded data that carries different types of information. A typical HTTP request contains:

1. **HTTP version type**: HTTP/1.0, HTTP/1.1, HTTP/2.0, HTTP/3.0
2. **URL**: Uniform Resource Locator, address of a given unique resource on the web
3. **HTTP method**: it indicates the action that the HTTP request expects from the queried server. For ex, GET, POST, PUT etc.
4. **HTTP headers**: It contains text information stored in key-value pairs. These can be grouped according to their contexts:
    * *Request Headers*: information about the resource to be fetched, or about the client requesting the resource
    * *Response Headers*: information about the response, like its location or about the server providing it
    * *Representation Headers*: contain information about the body of the resource, like its MIME type, or encoding/compression type
    * *Payload Headers*: representation-independent information about payload data, including content-length and the encoding used for transport
5. **HTTP Request body**: it contains any information being submitted to the web server, such as username and password, or any other data entered into a form
6. **HTTP Response**: it is the response that web clients receive from an Internet server in answer to an HTTP request. It contains:
    * *HTTP status code*: 3-digit status codes most often used to indicate whether an HTTP request has been successfully completed
    * *HTTP response headers*: a response comes with headers that convey important information such as the language and format of the data being sent
    * *optional HTTP body*: 'GET' requests generally have a body that contains the requested information. In most requests, this is HTML data 