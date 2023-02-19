
// Importing modules
import React, { useState, useEffect } from "react";
import "./App.css";
import PlayerMatrix from "./components/tests"
import Handler from "./api/Data";
function App() {

	return (
		<div className="App">
			<PlayerMatrix/>
			{/* <Handler></Handler> */}
		</div>
	);
}

export default App;




