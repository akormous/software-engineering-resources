# useMemo

This hook returns a memoized value. It only runs when one of its dependencies update. This can improve performance.

`useMemo` can be used to keep expensive, resource intensive functions from needlessly running.


`const result = useMemo(() => {expensiveCalculation}, [dependencies])`

## Code Example

```js

import { useState, useMemo } from 'react'

function App() {
  const [numbers, setNumbers] = useState([11,22,33]);

  const total = useMemo(
    () => numbers.reduce((acc, number) => acc + number, 0), 
    [numbers]);


  const [names] = useState(["Reyna", "Jett", "Sova", "KAYO"]);
  const sortedNames = useMemo(() => [...names].sort(), [names]);

  return (
    <div className="App">
      <div>Total = {total}</div>
      <div>Names = {names.join(", ")}</div>
      <div>Sorted Names = {sortedNames.join(", ")}</div>

    </div>
  )
}

export default App


```



# useCallback

This hook returns a memoized callback function. This allows us to isolate resource intensive functions so that they will not automatically run on every render. The `useCallback` hook only runs when one of its dependcies update.

NOTE: The difference is that `useMemo` returns a memoized value and `useCallback` returns a memoized function.

This prevents a component from re-rendering unless its props have changed.


`const someFunc = useCallback(() => someIntructions, [dependencies])`

## Code Example

```js

import { useState, useMemo, useCallback } from 'react'

function SortedList({ list, comparator }) {
  console.log("Sorted List render");
  const sortedList = useMemo(() => {
    console.log("Running sort");
    return [...list].sort(comparator);
  }, [list]);
  return (
    <div>
      {sortedList.join(", ")}
    </div>
  );
}

function App() {
  const [numbers, setNumbers] = useState([11,22,33]);

  const total = useMemo(
    () => numbers.reduce((acc, number) => acc + number, 0), 
    [numbers]);


  const [names] = useState(["Reyna", "Jett", "Sova", "KAYO"]);
  const [count, setCount] = useState(0);
  const descSort = useCallback((a, b) => a.localeCompare(b)*-1, []);
  return (
    <div className="App">
      <div>Total = {total}</div>
      <div>Names = {names.join(", ")}</div>
      <SortedList list={names} comparator={descSort}/>
      <button onClick={() => setCount(count+1)}>Count = {count}</button>
    </div>
  )
}

export default App


```