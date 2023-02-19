

import React, { useState, useEffect, useRef } from 'react';
import './matrix.css';
import Handler from '../api/Data';

const Matrix = () => {


  const [rows_cols,setRowsCols] = useState(5)

  // const [rows, setRows] = useState(rows_cols);
  // const [columns, setColumns] = useState(5);
  const rows = rows_cols
  const columns = rows_cols;
  const [grid, setGrid] = useState([]);

  const [sizeplayer, setSize] = useState(0);
  

  // --------------------------------


  //data grid
  const [data, setData] = useState(null);
  //reference
  const matrixRef = useRef([]);
  //winner checker
  const [ifwin, setIfwin] = useState(0);

 

  useEffect(() => {
    let newGrid = [];
    for (let i = 0; i < rows; i++) {
      let row = [];
      for (let j = 0; j < columns; j++) {
        row.push(0);
      }
      newGrid.push(row);
    }
    setGrid(newGrid);
  }, [rows, columns]);

 

  useEffect(() => {
    async function fetchData() {
      const response = await fetch("http://localhost:5000/grid");
      const jsonData = await response.json();
      setData(jsonData);
      console.log(jsonData)
    }


    fetchData();
  }, []);


  const handleBoxClick = (row, col) => {
    let newGrid = [...grid];
    newGrid[row][col] = newGrid[row][col] === 0 ? 1 : 0;
    setGrid(newGrid);
  };

  const renderMatrix = () => {
    let matrix = [];
    for (let i = 0; i < rows; i++) {
      let row = [];
      for (let j = 0; j < columns; j++) {
        if (grid[i] && grid[i][j] !== undefined) {
          row.push(
            <div
              className="grid-square"
              style={{ backgroundColor: grid[i][j] === 0 ? "white" : "black" }}
              onClick={() => handleBoxClick(i, j)}
              key={`${i}-${j}`}
              //To avoid interfering with the rendering of the matrix in React, you should not manipulate the DOM directly. Instead, you can use React refs to access the DOM elements.
              ref={el => (matrixRef.current[i * columns + j] = el)}

            />
          );
        }
      }
      matrix.push(
      <div className="grid-row" style={{ display: 'flex', flexDirection: 'column' }}
       key={i}>{row}
      </div>
      );
    }


    return matrix;

    
  };
// // !!!!!!!!!!!!!!!!!!!!!!!
//   // Use different hook or make a custom one so this part of the code comparing the matrixes works properly 
//   // and the matrix in the matrix component from above is being rendered without issues from the useEffect function here:


//GENERATE BUTTON FEATURE

const handleSetClick = () => {
  setSize(sizeplayer + 1);
}

useEffect(() => {
  const checkGrid = () => {
    let index = 0;
    for (let i = 0; i < rows; i++) {
      for (let j = 0; j < columns; j++) {
        const matrixValue = matrixRef.current[index].style.backgroundColor === "black" ? 1 : 0;
        if (data[i][j] !== matrixValue) {
          console.log("Grids are changed");
          setIfwin("Still Not Winning...")

          // setIfwin(1);
          return;
        }
        index++;
      }
    }
    console.log("Grids are the same");
    setIfwin("You Win")

  };

  const intervalId = setInterval(checkGrid, 1000);

  return () => clearInterval(intervalId);

}, [data, rows, columns]);






  return (
    <div className="nonogram-container">
      <h1>Nonogram Puzzle Game</h1>
      <p>Set the Matrix size: {sizeplayer}</p> 
      <button onClick={e => setSize(parseInt(rows_cols,10))}>Set</button>
      {/* <button onClick={}>GENERATE</button> */}
      <button onClick={handleSetClick}>Generate</button>


     

      <div className="input-container">
        <label>Rows/Cols:</label>
        
       {/* Change so the user inputs only one value on rows_cols and the setRows and setColumns are set so they are rendered correclty 
       When the set button is clicked the matrix is regenerated and starts listening to hook if the matrix from the flask app imported from component Handlerd
       and the newGrid matched the player wins and is able to play again or choose different size of the grid which sends POST reques
       to the flask app to change the generated grid size  */}

        <input type="number" value={rows_cols} onChange={e => setRowsCols(parseInt(e.target.value, 10)) } ></input>
        {/* <label>Rows:</label> */}
        {/* <input type="number" value={rows} onChange={e => setRows(parseInt(e.target.value, 10)) } /> */}
        {/* <label>Columns:</label> */}
        {/* <input type="number" value={columns} onChange={e => setColumns(parseInt(e.target.value, 10))} /> */}
      </div>
      <div className="grid-container">{renderMatrix()}</div>
      {/* <Handler /> */}
      <div><p></p>{}</div>
      <p>PLAYER</p>
      <div className='winning'>{ifwin}</div>



      <div>
      {data && (
        <div>
          <h2>Handler Data:</h2>
          <pre>{JSON.stringify(data, null, 2)}</pre>
          <p>{data}</p>
          {/* <table ></table> */}
        </div>
      )}
    </div>
    </div>


    
  );
};

export default Matrix;
