const Section = ({ id, classSize, classStyle, children }) => {
	return (
		<div
			id={`${id}`}
			className={`border-solid border-4 border-green-400 p-6 ${classSize} rounded-xl text-white ${classStyle}`}
		>
			{children}
		</div>
	);
};
export default Section;
