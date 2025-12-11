const Button = ({
	classColor = "border-solid border-2 border-solid bg-white text-black hover:bg-spenny-background hover:text-spenny-text",
	classStyle,
	onClick = () => {
		alert("Nothing");
	},
	label = "__UNLABEL__",
	type = "",
}) => {
	return (
		<>
			<button
				className={`cursor-pointer flex flex-col p-3 h-full justify-center items-center text-md transition duration-300 ease-in-out ${classColor} ${classStyle}`}
				onClick={onClick}
				type={type}
			>
				{label}
			</button>
		</>
	);
};

export default Button;
