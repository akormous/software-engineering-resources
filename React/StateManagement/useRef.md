# useRef

This hook allows you to persist values between renders.

It can be used to store a mutable value that does not cause a re-render when updated.

It can be used to access a DOM element directly.

`useRef` only returns one item which is an object called `current`

## Code Example 1

```js

import { useRef, useEffect, useState } from 'react'

function App() {
  const [name, setName] = useState("");
  const count = useRef(0);

  useEffect(() => {
    count.current = count.current + 1;
  });
  
  return (
    <div className="App">
      <div>{name}</div>
      <input type="text" onChange={(e) => setName(e.target.value)} />
      <p>This component is rendered {count.current} times</p>
    </div>
  )
}

export default App;


```

## Code Example 2

```js

import { useRef, useEffect, useState } from 'react'

function App() {
  const idRef = useRef(1);
  const inputRef = useRef(null);

  const [names, setNames] = useState([
    {id: 69, alias: "duke"},
    {id: 420, alias: "walter"},
  ]);

  const onAddName = () => {
    setNames([...names, {
      id: idRef.current++,
      alias: inputRef.current.value
    }]);
    inputRef.current.value = "";
  }

  
  useEffect(() => {
    inputRef.current.focus();
  }, []);

  return (
    <div className="App">
      <ul>
      {names.map((name) => (
        <li>{name.id} - {name.alias}</li>
      ))}
      </ul>
      <input type="text" ref={inputRef}/>
      <button onClick={onAddName}>Add Name</button>
    </div>
  )
}

export default App


```