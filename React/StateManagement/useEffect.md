# useEffect

The `useEffect` hook allows you to perform side effects in your components.

Some of the examples of side effects are: fetching data, directly updating the DOM, and timers.

`useEffect(<function>, <dependency>)`

# Effect cleanup

Some effect require cleanup to reduce memory leaks. This can be done by a return function at the end of the `useEffect` hook.

## Code Example

```js

import { useState, useEffect } from 'react'

const Stopwatch = () => {
  const [time, setTime] = useState(0);
  useEffect(() => {
    const interval = setInterval(() => {
      setTime((t) => {
        return t + 1;
      });
    }, 1000);
    return () => clearInterval(interval);
  }, [])
  
  return (
    <div>Time: {time}</div>
  );
}

function App() {
  const [names, setNames] = useState([]);

  useEffect(() => {
    fetch("/public/names.json")
    .then((response) => response.json())
    .then((data) => setNames(data));
  }, []);

  
  const [selectedNameDetails, setSelectedNameDetails] = useState(null);

  const onSelectedNameChange = (name) => {
    fetch(`/${name}.json`)
    .then((response) => response.json())
    .then((data) => setSelectedNameDetails(data));
  }

  return (
    <div className="App">
      <Stopwatch />
      {names.map((name) => (
        <button key={name} onClick={() => onSelectedNameChange(name)}>{name}</button>
      ))}
      <div>Details: {JSON.stringify(selectedNameDetails)}</div>
    </div>
  )
}

export default App

```

[Explanation for beginners](https://www.freecodecamp.org/news/react-useeffect-absolute-beginners/)