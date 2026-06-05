import Divider from "../Divider";

const BucketLogCard = ({ log }) => {
	const datetime_convert = (date) => {
		const dateObj = new Date(date);
		return dateObj.toLocaleDateString("en-GB");
	};
	let colorType;
	if (log.action_properties.operation.type === "MOVE") {
		colorType = "spenny-accent-warning";
	} else if (log.action_properties.operation.type === "ADD") {
		colorType = "spenny-accent-base";
	} else if (log.action_properties.operation.type === "SUB") {
		colorType = "spenny-accent-error";
	} else {
		colorType = "white";
	}

	return (
		<div
			className={`w-full h-1/3 border-5 border-solid rounded-lg p-2 border-${colorType} flex flex-col justify-center`}
		>
			<h1 className="text-md h-1/2 overflow-hidden text-ellipsis whitespace-nowrap">
				{log.action_name}
			</h1>
			<Divider />
			<div id="bucket-log-card-bottom" className="w-full h-1/2">
				<h2 className="float-left">
					{datetime_convert(log.created_at)}
				</h2>
				<p className={`float-right font-bold text-${colorType}`}>
					${log.action_properties.operation.amount}
				</p>
			</div>
		</div>
	);
};

export default BucketLogCard;
