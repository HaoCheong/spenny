const Placeholder = ({ label = "PLACEHOLDER", classStyle }) => {
	return (
		<div
			className={`bg-green-600 rounded-xl w-full h-full flex justify-center items-center ${classStyle}`}
		>
			{label}
		</div>
	);
};

export default Placeholder;
