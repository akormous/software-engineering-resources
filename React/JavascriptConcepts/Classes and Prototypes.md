```js
class Student {
	constructor(name, roll) {
		this.name = name;
		this.roll = roll;
	}
	greet() {
		console.log("My name is ", this.name);
	}
}
```

JavaScript implements classes with special objects called `prototypes`. All the methods of the class are stored on the object's prototype. The above code is similar to the following:
```js
const s1 = {
	name: "Tom",
	roll: "2",
	"__proto__": {
		greet: function() {
			console.log("My name is ", this.name);
		}
	}
};
```
How is the greet function called even though it is not a key on the s1 object? 
There is an algorithm that traverses the *prototype chain*
First, javascript looks at the keys of the object, if it is not found, it then looks on the keys of the prototype object, if it still doesn't find the key, it looks on the keys of the prototype's prototype, and so on.
But why?
Efficiency, only a single reference of the prototype object is stored in the memory and all the instances have reference to this prototype object.

# Proxies
It allows you to override default behavior of objects.
```js
const s1 = new Proxy({name: "Tom", roll: "2"}, {
	get: (target, key) => {
		if(key === 'greet') {
			return () => console.log("My name is ", target.name);
		}
		else {
			return target[key];
		}
	},
})
```
### Use case of Proxy
1. Perform validation on input data
2. Create a log every time a key is accessed
3. Throw an error if an attempt was made to write to a readonly value
4. Create a modified version of an immutable object by writing to it's proxy