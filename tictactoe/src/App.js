import logo from './logo.svg';
import './App.css';
import Square from './Square.js'
import {useState, useEffect} from "react";

function App() {
  const [user1Move, setUser1Move] = useState(true);
  const [board, setBoard] = useState([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
  const [gameWinner, setGameWinner] = useState(null);

  return (
    <div className="App">
      
      <h1> Tic Tac Toe </h1>
      <h3> Player 1 is green and Player 2 is blue. </h3>
      {[0, 1, 2].map((y, index) => {
        return (
          <div style = {{
            display: 'flex',
            flexDirection: 'row',
            flex: 1
          }}>
          {[0, 1, 2].map((x, index) => {
              return (
                <Square user1Move = {user1Move} setUser1Move = {setUser1Move} 
                x={x} y = {y} setBoard = {setBoard} board = {board} setGameWinner = {setGameWinner}
                gameWinner = {gameWinner}
                />
              );
            })}
            </div>
        )})}
        <h1 style = {{color: "purple"}}> {gameWinner ? 
        (gameWinner == 3? "There was a tie :(" : "Player " + gameWinner + " won the game!") : ""} </h1>
    </div>
  )}

export default App;
