import { useEffect, useState } from "react";

function calculateWinner(gameState: string[][]) : string {
    // check rows
    for(let i = 0; i < 3; i++) {
        if(gameState[i][0] === gameState[i][1] && gameState[i][1] === gameState[i][2]) {
            return gameState[i][0];
        }
    }

    // check cols
    for(let j = 0; j < 3; j++) {
        if(gameState[0][j] === gameState[1][j] && gameState[1][j] === gameState[2][j]) {
            return gameState[0][j];
        }
    }

    // check diags
    if(gameState[0][0] === gameState[1][1] && gameState[1][1] === gameState[2][2]) {
        return gameState[1][1];
    }
    if(gameState[0][2] === gameState[1][1] && gameState[1][1] === gameState[2][0]) {
        return gameState[1][1];
    }

    return "";
}

function Square({val, onSquareClick} : {
    val: string;
    onSquareClick: () => void;
}) {
    return (
        <>
        <button className="square" onClick={onSquareClick}>
            {val}
        </button>
        </>
    );
}

function Board({gameState, currentPlayer, onPlay} : {
    gameState: string[][];
    currentPlayer: string;
    onPlay: (nextPlayer: string, nextGameState: string[][]) => void;
}) {
    const [status, setStatus] = useState("");

    function handleClick(i: number) {
        const row = Math.floor(i/3);
        const col = i%3;

        const nextGameState = gameState.slice();
        if(calculateWinner(nextGameState) != "" || nextGameState[row][col] != '') {
            return;
        }

        nextGameState[row][col] = currentPlayer;
        const nextPlayer = (currentPlayer === 'X' ? 'O' : 'X');

        onPlay(nextPlayer, nextGameState);
    }

    
    
    useEffect(() => {
        const gameWinner = calculateWinner(gameState);
        
        if(gameWinner != "") {
            setStatus("Winner: " + gameWinner + " !!");
        }
        else {
            setStatus("Current turn: " + currentPlayer);
        }
    }, [gameState])

    return (
        <>
        <h3>{status}</h3>
        <div className="board-row">
            <Square val={gameState[0][0]} onSquareClick={() => handleClick(0)} />
            <Square val={gameState[0][1]} onSquareClick={() => handleClick(1)} />
            <Square val={gameState[0][2]} onSquareClick={() => handleClick(2)} />
        </div>
        <div className="board-row">
            <Square val={gameState[1][0]} onSquareClick={() => handleClick(3)} />
            <Square val={gameState[1][1]} onSquareClick={() => handleClick(4)} />
            <Square val={gameState[1][2]} onSquareClick={() => handleClick(5)} />
        </div>
        <div className="board-row">
            <Square val={gameState[2][0]} onSquareClick={() => handleClick(6)} />
            <Square val={gameState[2][1]} onSquareClick={() => handleClick(7)} />
            <Square val={gameState[2][2]} onSquareClick={() => handleClick(8)} />
        </div>
        </>
    );
}

function Game() {
    const [gameState, setGameState] = useState([['','',''],['','',''],['','','']]);
    const [currentPlayer, setCurrentPlayer] = useState('X');

    const handlePlay = (nextPlayer: string, nextGameState: string[][]) => {
        setCurrentPlayer(nextPlayer);
        setGameState(nextGameState);
    }

    const handleReset = () => {
        setCurrentPlayer('X');
        setGameState([['','',''],['','',''],['','','']]);
    }

    return (
        <>
        <div className="game">
            <div>
                <button className="reset-button" onClick={() => handleReset()}>Reset</button>
                <Board gameState={gameState} currentPlayer={currentPlayer} onPlay={handlePlay} />
            </div>
        </div>
        </>
    );
}

export default Game;