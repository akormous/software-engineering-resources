
## Basic
```js
function f(a, b) {
	return a + b;
}
```

## Anonymous
```js
var f = function(a, b) {
	return a + b;
}
```

## Immediately Invoked Function Expression (IIFE)
```js
const result = (function(a, b) {
	return a + b;
})(5, 7);
```

## Functions within functions
```js
function createFunction() {
	function sum(a, b) {
		return a+b;	
	}
	return sum;
}
```

## Arrow Syntax
It is the preferred syntax across many projects.
```js
const f = (a, b) => {
	return a+b;
}
```
You don't even need return statement
```js
const f = (a, b) => a+b;
```


# Function Hoisting
A function can be used before it is initialized/defined. This only happens for functions created with `function()` syntax. It is sometimes considered as a bad practice since it reduces readability.
```js
function createFunction() {
	return f;
	function f(a, b) {
		return a+b;
	}
}
```

# Closures
When a function is created, it has access to a reference to all the variables declared around it, which is called it's **lexical enviroment**. 
The combination of the function and its environment is called a **closure**.

```js
function createAdder(a) {
	function f(b) {
		return a+b;
	}
	return f;
}
```
In the above example, function `f` has access to variable `a`


## Difference between arrow syntax and function syntax
1. Arrow syntax is more minimalistic, it is perfect for anonymous and single-line functions
2. No automatic hoisting, it forces you to use it after it has been declared
3. Can't be bound to `this`, `super`, and `arguments` or be used as a constructor. Basically, arrow functions are simpler in their feature set

# Rest / Spread syntax
`(...args)` can be used to access all the passed arguments as an array. The primary use case is for creating generic factory functions that accept any function as input and return a new version of the function with some specific modification.
```js
function f(...args) {
	return args[0] + args[1];
}
f(3, 4);
```

# Higher-Order functions
A functions that accepts a function as an argument and/or returns a function is called a ***Higher-Order function***
```js
function log(f) {
	return function(..args) {
		console.log("input ", args);
		const result = f(args);
		console.log("output ", result);
		return result;
	}
}
const g = log((a, b) => a + b);
```