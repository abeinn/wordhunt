import React, { useState, useContext } from "react";
import App, { AppContext } from '../App';

function Letter({x, y}) {
  const { grid, size } = useContext(AppContext);
  const letter = grid[x][y];
  return (
    <div id={(x * size + y).toString()} className="letter">
      {letter}
    </div>
  )
}

export default Letter;