import React, { useState, createContext } from "react";
import "./App.css";
import Select from "react-select";
import chroma from "chroma-js";
import Grid from "./components/Grid";
import Keyboard from "./components/Keyboard";
import { gridDefault } from "./Words";

export const AppContext = createContext();
  
function App() {
  
  const size = 4;
  const [entered, setEntered] = useState(false);
  const [letters, setLetters] = useState('');
  const [wordPathList, setWordPathList] = useState(null);
  const [options, setOptions] = useState(null);
  const [connections, setConnections] = useState(null);
  const [grid, setGrid] = useState(gridDefault);
  const [currPos, setCurrPos] = useState(0);

  function handleKey(key) {
    if (currPos > Math.pow(size, 2) || entered)  return;
    if (key == "Enter") {
      if (currPos !== 16) return; 
      handleEnter();
    } else if (key == "Backspace") {
      if (currPos === 0) return;
      const newGrid = [...grid];
      const pos = currPos - 1
      newGrid[Math.floor(pos / size)][pos % size] = "";
      setLetters(letters.slice(0, -1));
      setGrid(newGrid);
      setCurrPos(currPos - 1);
    } else if (key.toLowerCase() !== key.toUpperCase() && Keyboard.length === 1 && currPos !== Math.pow(size, 2)) {
      const newGrid = [...grid];
      newGrid[Math.floor(currPos / size)][currPos % size] = key.toUpperCase();
      setLetters(letters + key.toUpperCase());
      setGrid(newGrid);
      setCurrPos(currPos + 1);
    }
  }

  function handleEnter() {
    if (letters.length !== Math.pow(size, 2)) return;
    fetch(`/solve?input_value=${letters}`)
      .then(response => response.json())
      .then(data => {
        setWordPathList(data);
        setOptions(data.map(item => (
          {value: item.id, label: item.word}
          )));
      })
      .catch(error => console.error(error)); 
    setEntered(true);
  }

  function handleChange(event) {
    const path = wordPathList[event.value].path;
    
    const newConnections = [];
    var prev = path[0];
    for (let i = 1; i < path.length; i++) {
      newConnections.push([prev, path[i]]);
      prev = path[i];
    }
    setConnections(newConnections);
  }
  

  const styles = {
    control: styles => ({ ...styles, backgroundColor: "white"}),
    option: (styles, { isFocused, isSelected }) => ({
      ...styles,
      backgroundColor: 
        isSelected ? "blue" :
        isFocused ? chroma("blue").alpha(0.3).css() :
        undefined,
      color:
        isSelected ? "white" :
        "black"
    }),

    singleValue: (styles, state) => ({
      ...styles,
      color:"black"
    })
  }

  return(
    <div className="App">
      <nav>
        <h1>Word Hunt Solver</h1>
      </nav>

      <AppContext.Provider 
        value={{ 
          grid, 
          setGrid,
          handleKey,
          size,
          connections
        }}
      >
        <div className="main">
          <Grid />
          <Keyboard />
          <div className="select">
            {wordPathList && 
              <Select 
                options={options}
                onChange={handleChange}
                styles={styles}
                closeMenuOnSelect={false}
                menuShouldScrollIntoView={false}
            />}
          </div>
        </div>
      </AppContext.Provider>
      
      
    </div>

  ) 
}
  
export default App;