# Context and Custom Hooks

# Context
React context allows us to pass down and consume data in any component without using props. Makes it easy to share data across components.

It is the equivalent of global variables for our React components.

It avoid prop drilling.

## When to use?
- Theme data (light or dark)
- User data (currently authenticated user)
- Location-specific data (user language or locale)
- **For data that does not need to be updated often**

## How to use?

1. Create context using `createContext` method
2. Wrap the context provider around the component tree
3. Put any value on your context provider with the `value` prop
4. Read the value using `useContext`

## Code Example

```js

import { useEffect, useState, createContext, useContext } from 'react';

interface Pokemon {
  "id": number,
  "name": string,
  "type": string[],
  "hp": number,
  "attack": number,
  "defense": number,
  "special_attack": number,
  "special_defense": number,
  "speed": number
}

const PokemonContext = createContext<ReturnType<typeof usePokemonSource>>(
  {} as unknown as ReturnType<typeof usePokemonSource>
);

function usePokemonSource() {
  const [pokemon, setPokemon] = useState<Pokemon[]>([]);

  useEffect(() => {
    fetch("/pokemon.json")
    .then((response) => response.json())
    .then((data) => setPokemon(data))
  }, [])

  return {pokemon};
}

export function usePokemon() {
  return useContext(PokemonContext);
}

export function PokemonProvider({
    children,
}: {
    children: React.ReactNode;
}) {
    return (
        <PokemonContext.Provider value={usePokemonSource()}>
            {children}
        </PokemonContext.Provider>
    );
}

```

# Custom Hooks

When you have component logic that needs to be used by multiple components, we can extract that logic to a custom hook.

Simply, extract the data fetching logic to a different file and export the function that returns the data and use it in your components.

## Code Example

In this example, the function `usePokemon` can be termed as a custom hook.

```js

import { useEffect, useState, createContext, useContext, useReducer, useCallback, useMemo } from 'react';

interface Pokemon {
  "id": number,
  "name": string,
  "type": string[],
  "hp": number,
  "attack": number,
  "defense": number,
  "special_attack": number,
  "special_defense": number,
  "speed": number
}

const PokemonContext = createContext<ReturnType<typeof usePokemonSource>>(
  {} as unknown as ReturnType<typeof usePokemonSource>
);

function usePokemonSource(): {
  pokemon: Pokemon[];
  search: string;
  setSearch: (search: string) => void;
} {
  //const [pokemon, setPokemon] = useState<Pokemon[]>([]);
  //const [search, setSearch] = useState("");
  type PokemonState = {
    pokemon: Pokemon[],
    search: string;
  }
  type PokemonAction = { type: "setPokemon"; payload: Pokemon[] } | 
  { type: "setSearch"; payload: string };

  const [ {pokemon, search}, dispatch ] = useReducer((state: PokemonState, action: PokemonAction) => {
    switch(action.type) {
      case "setPokemon":
        return { ...state, pokemon: action.payload };
      case "setSearch":
        return { ...state, search: action.payload };
    }
  }, {
    pokemon: [],
    search: ""
  })
  useEffect(() => {
    fetch("/pokemon.json")
    .then((response) => response.json())
    .then((data) => dispatch({
      type: "setPokemon",
      payload: data
    }))
  }, []);

  const setSearch = useCallback((search: string) => {
    dispatch({
      type: "setSearch",
      payload: search,
    });
  }, []);

  const filteredPokemon = useMemo(
    () => pokemon.filter((p) => p.name.toLowerCase().includes(search)).slice(0, 20),
    [pokemon, search]
  )
  
  const sortedPokemon = useMemo(() => 
  [...filteredPokemon].sort((a, b) => a.name.localeCompare(b.name)), [filteredPokemon]);

  return { pokemon: sortedPokemon, search, setSearch };
}

export function usePokemon() {
  return useContext(PokemonContext);
}

export function PokemonProvider({
    children,
}: {
    children: React.ReactNode;
}) {
    return (
        <PokemonContext.Provider value={usePokemonSource()}>
            {children}
        </PokemonContext.Provider>
    );
}

```