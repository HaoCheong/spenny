import { useLocation } from "react-router";

const Button = ({
	classColor = "border-solid border-2 border-solid bg-white text-black hover:bg-black hover:text-white",
	classStyle,
	onClick = () => {
		alert("Nothing");
	},
	label = "__UNLABEL__",
}) => {
	return (
		<>
			<button
				className={`flex flex-col p-3 rounded-lg text-xl transition duration-300 ease-in-out ${classColor} ${classStyle}`}
				onClick={onClick}
			>
				{label}
			</button>
		</>
	);
};

export default Button;
