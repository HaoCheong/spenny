const Placeholder = ({ label = "PLACEHOLDER", classStyle = "size-full" }) => {
	return (
		<div
			className={`text-white border-5 border-solid border-white rounded-lg flex justify-center items-center ${classStyle}`}
		>
			{label}
		</div>
	);
};

export default Placeholder;
