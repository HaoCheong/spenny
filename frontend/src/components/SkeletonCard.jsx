const SkeletonCard = ({ label = "Nothing", classStyle = "w-full h-full" }) => {
	return (
		<div
			className={`border-5 border-dashed border-gray-700 rounded-lg flex justify-center items-center ${classStyle}`}
		>
			{label}
		</div>
	);
};

export default SkeletonCard;
