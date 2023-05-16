import React, { useEffect, useCallback, useContext } from "react";
import { AppContext } from "../App";

function Keyboard() {

  const { handleKey } = useContext(AppContext);

  const handleKeyboard = useCallback((event) => {
    handleKey(event.key);
  })

  useEffect(() => {
    document.addEventListener("keydown", handleKeyboard);

    return () => {
      document.removeEventListener("keydown", handleKeyboard);
    };
  }, [handleKeyboard])

  return (
    <div className="keyboard" onKeyDown={handleKeyboard}></div>
  )
}

export default Keyboard;