import React, {useState, useEffect} from 'react';

const Square = ({user1Move, setUser1Move, x, y, setBoard, board, setGameWinner, gameWinner}) => {
    const [color, setColor] = useState("white")

    const checkBoard = () => {
    
    // Checking columns
    for (let x = 0; x < 3; x++) {
      var winner = false;
      var curr_state = board[x][0]
      if (curr_state != 0){
        for (let y = 1; y < 3; y++) {
          if (board[x][y] != curr_state){
            winner = false;
            break;
          }
          else 
          {winner = true;}
        }
      }
      if (winner){
        setGameWinner(curr_state)
      }
    }

    // Checking rows
    for (let y = 0; y < 3; y++) {
        var winner = false;
        var curr_state = board[0][y]
        if (curr_state != 0){
          for (let x = 1; x < 3; x++) {
            if (board[x][y] != curr_state){
              winner = false;
              break;
            }
            else 
            {winner = true;}
          }
        }
        if (winner){
          setGameWinner(curr_state)
        }
      }

      // Checking diagonal 1
      
        var winner = false;
        var curr_state = board[0][0]
        if (curr_state != 0){
          for (let i = 1; i < 3; i++) {
            if (board[i][i] != curr_state){
              winner = false;
              break;
            }
            else 
            {winner = true;}
          }
        }
        if (winner){
          setGameWinner(curr_state)
        }

      // Checking diagonal 2
      
        var winner = false;
        var curr_state = board[0][2]
        if (curr_state != 0){
          for (let i = 1; i < 3; i++) {
            if (board[i][2-i] != curr_state){
              winner = false;
              break;
            }
            else 
            {winner = true;}
          }
        }
        if (winner){
          setGameWinner(curr_state)
        }

        // Checking for a tie
        else {
            let tie = false;
            for (let i = 1; i < 3; i++) {
                if (board[i].indexOf(0) == -1){
                    tie = true;
                }
                else {
                    tie = false
                    break
                }
            }
            if (tie){
                setGameWinner(3)
            }
        }
    }

    const changeBoard = (x, y, value) => {
        let new_board = board
        board[x][y] = value
        setBoard(new_board);
        checkBoard();
      }

    return (
    <div onClick = {() => {
        if (color == "white" && gameWinner === null){
            if (user1Move){
                setColor("green")
                setUser1Move(false)
                changeBoard(x, y, 1)
                
            }
            else {
                setColor("blue")
                setUser1Move(true)
                changeBoard(x, y, 2)
                
            }
        }
        
    }}
        style = {{
            borderStyle: "solid",
            borderRadius: "5px",
            height: "20vh", 
            width: "33vw",
            backgroundColor: color
        }}>
            
        </div>
    )
}
export default Square;