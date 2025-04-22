import { createContext } from "react";

const theme = {
	text: "#ffffff",
	background: "#1f2937",
	primary: "#4ade80",
	secondary: "#3e6054",
	accent: "#46fa22",
};

const ThemeContext = createContext(theme);

export default ThemeContext;
