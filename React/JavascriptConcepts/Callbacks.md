A callback is defined as a function passes as an argument to another function. It's a pretty popular concept and is essential to writing reusable code.
### Why use callbacks?
They allow you to write code that can be reused across different use-cases

```ts
function map(arr: number[], fn: (n : number, i: number) => number): number[] {
	for(let i = 0; i < arr.length; i++) {
		arr[i] = fn(arr[i], i);
	}
	return arr;
}
```
In the above example, `fn` is the callback function