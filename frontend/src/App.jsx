import { BrowserRouter, Routes, Route, Navigate } from "react-router";
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
