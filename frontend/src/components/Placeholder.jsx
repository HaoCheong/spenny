const Placeholder = ({
	label = "PLACEHOLDER",
	classStyle = "w-full h-full",
}) => {
	return (
		<div
			className={`border-5 border-solid border-white rounded-lg flex justify-center items-center ${classStyle}`}
		>
			{label}
		</div>
	);
};

export default Placeholder;
