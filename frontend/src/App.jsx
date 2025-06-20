import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import { BrowserRouter, Routes, Route, Navigate } from "react-router";
// import "./App.css";
import Dashboard from "./routes/Dashboard";
import Logs from "./routes/Logs";

const App = () => {
	return (
		<BrowserRouter>
			<Routes>
				<Route path="/Dashboard" element={<Dashboard />} />
				<Route path="/Logs" element={<Logs />} />
				<Route
					path="*"
					element={<Navigate to="/Dashboard" replace />}
				/>
			</Routes>
		</BrowserRouter>
	);
};

export default App;
