# Go

Go, or golang, is an open-source, compiled, and statically typed programming language designed by Google. It is built to be **simple, high-performing, readable, and efficient**.

This documentation will mainy revolve around creating a web server in Go in the simplest way possible.

<details>
    <summary> <code>net/http</code> </summary>

### ServeMux (Multiplexer)

- `ServeMux` is an HTTP request multiplexer. 
- It is responsible for matching the URL in the request to an appropriate handler and executing it.

### http.HandleFunc

- This method accepts the Handler implementation in the form of a function
```go
http.HandleFunc("/route", func(http.ResponseWriter, *http.Request) {
    // business logic
})
```
</details>