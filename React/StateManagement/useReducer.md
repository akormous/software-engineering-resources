# useReducer

This hook is similar to the `useState` but it also allows for custom state logic. If your state relies on some complex logic, `useReducer` may be useful.

`useReducer(reducerFunction, initialState)`

The reducer function contains your custom state logic and the `initialState` is the state object/value.

The `useReducer` hook returns the current `state` and a `dispatch` method.

The `dispatch` is used to call one of your logic written in the `reducerFunction`.

## Code example

```js
import { useReducer } from 'react'

function UserForm() {
  const [ state, dispatch ] = useReducer(
    (state, action) => ({
      ...state,
      ...action
    }), 
    {
      first: "Ben",
      last: "Dover"
    })
  return (
    <div>
      <input type="text"
        value={state.first}
        onChange={(e) => dispatch({ first: e.target.value })}
      />
      <input type="text"
        value={state.last}
        onChange={(e) => dispatch({ last: e.target.value })}
      />
      <div>
        First: {state.first}
      </div>
      <div>
        Last: {state.last}
      </div>
    </div>
  );
}

function NameList() {
  const [ state, dispatch ] = useReducer((state, action) => {
    switch(action.type) {
      case "SET_NAME": 
        return {...state, name: action.payload};
      case "ADD_NAME":
        return {...state, names: [...state.names, state.name], name: ""}
    }
  }, 
    {
      names: [],
      name: ""
    })
  return (
    <div className="App">
      <ul>
        {state.names.map((name, index) => (
          <li key={index}>{name}</li>
        ))}
      </ul>
      <input 
        type="text"
        value={state.name}
        onChange={(e) =>
          dispatch({type: "SET_NAME", payload: e.target.value})
        }
      />
      <button
       onClick={() =>
        dispatch({type: "ADD_NAME"})
       }
      >Add Name</button>
    </div>
  )
}

function App() {
  return (
    <div>
      <NameList />
      <UserForm />
    </div>
  );
}

export default App

```