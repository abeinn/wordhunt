import React, { useState, useContext } from "react";
import Letter from "./Letter";
import App, { AppContext } from '../App';
import Xarrow from "react-xarrows";

function Grid() {

  const { grid, connections } = useContext(AppContext);
  

  return (
    <div className="grid">
      {grid.map((row, rowIndex) => (
        <div className="row">
          {row.map((letter, colIndex) => (
            <Letter x={rowIndex} y={colIndex} />
          ))}
        </div>
      ))}

      {connections && connections.map(connection => (
        <Xarrow
          start={connection[0].toString()}
          end={connection[1].toString()}
          startAnchor="middle"
          endAnchor="middle"
          curveness={0}
          showHead={true}
        />
      ))}
    </div>
  )
}

export default Grid;