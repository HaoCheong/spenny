const Divider = ({ vertical = false }) => {
	return (
		<>
			{vertical ? (
				<div className="w-1px h-full border-solid border-1 border-gray-600"></div>
			) : (
				<hr className="border-1 border-gray-600" />
			)}
		</>
	);
};

export default Divider;
