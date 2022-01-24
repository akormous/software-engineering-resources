# Go

Go, or golang, is an open-source, compiled, and statically typed programming language designed by Google. It is built to be **simple, high-performing, readable, and efficient**.

This documentation will mainy revolve around creating a web server in Go (and learning the syntax) in the simplest way possible.

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

---

## Syntax

All syntax related stuff is here

<details>
    <summary>Functions</summary>

- Declaration
```go
func function_name(Parameter-list)(Return_type) {
    // function body
}
```
- Example
```go
func doSomething(num1, num2 int, action string) int {
    return num1 + num2
}
```
- By default, Go language uses call by value method to pass arguments in function
</details>

<details>
    <summary><code>struct</code></summary>

- `struct` in Go is a user-defined type that allows to group/combine items of different types into a single type
- It is analogous to classes in OOP (there are no classes in Go btw)
- `struct` does not support inheritance but supports composition
```go
type Employee struct {
    name, designation string
    id int
}
```
</details>