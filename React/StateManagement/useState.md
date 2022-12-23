# useState

It is a hook that allows us to track state in a function component. It can keep track of strings, numbers, booleans, arrays, objects, and any combination of these.

`const [variable, setterFunc] = useState(defaultValue)`

## Code example

```javascript

import { useState } from 'react'

function NameList() {
  const [list, setList] = useState(["Andy","Larry","Daniel"]);
  const [name, setName] = useState(() => "Default");

  function onAddName() {
    setList([...list, name]);
    setName("");
  }

  return (
    <div>
      <ul>
      {list.map((name) => (
        <li key={name}>{name}</li>
      ))}
      </ul>
      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <button
       onClick={onAddName}
      >Add Name</button>
    </div>
  );
}

function Counter() {
  const [count, setCount] = useState(1);

  function addOne() {
    setCount(count+1);
  }
  return (
    <div className="App">
      <button
      onClick={addOne}
      >Count = {count}</button>
    </div>
  )
}

function App() {
  return (
    <div>
      <Counter />
      <NameList />
    </div>
  );
}

export default App

```