const Section = ({ id, classSize, classStyle, children }) => {
	return (
		<div
			id={`${id}`}
			className={`border-solid border-4 border-green-400 p-5 ${classSize} rounded-lg text-white ${classStyle}`}
		>
			{children}
		</div>
	);
};
export default Section;
