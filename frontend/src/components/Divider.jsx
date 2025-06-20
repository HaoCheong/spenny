const Divider = ({ vertical = false }) => {
	return (
		<>
			{vertical ? (
				<div class="w-1px h-full border-solid border-1 border-gray-600"></div>
			) : (
				<hr class="border-1 border-gray-600" />
			)}
		</>
	);
};

export default Divider;
