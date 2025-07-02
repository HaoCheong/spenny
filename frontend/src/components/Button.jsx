const Button = ({
	classColor = "border-solid border-2 border-solid bg-white text-black hover:bg-spenny-background hover:text-spenny-text",
	classStyle,
	onClick = () => {
		alert("Nothing");
	},
	label = "__UNLABEL__",
}) => {
	return (
		<>
			<button
				className={`flex flex-col p-3 h-full justify-center items-center rounded-lg text-md transition duration-300 ease-in-out ${classColor} ${classStyle}`}
				onClick={onClick}
			>
				{label}
			</button>
		</>
	);
};

export default Button;
