import Divider from "../Divider";

const BucketEventCard = ({ event }) => {
	const datetime_convert = (date) => {
		const dateObj = new Date(date);
		return dateObj.toLocaleDateString("en-GB");
	};

	//PFIX: Must be a better way to do conditional colours

	let borderColorType;
	let textColorType;

	if (event.event_type === "MOVE") {
		borderColorType = "border-spenny-accent-warning";
		textColorType = "text-spenny-accent-warning";
	} else if (event.event_type === "ADD") {
		borderColorType = "border-spenny-accent-base";
		textColorType = "text-spenny-accent-base";
	} else if (event.event_type === "SUB") {
		borderColorType = "border-spenny-accent-error";
		textColorType = "text-spenny-accent-error";
	} else {
		borderColorType = "border-white";
		textColorType = "text-white";
	}

	return (
		<div
			className={`w-full h-1/3 border-5 border-solid rounded-lg p-2 ${borderColorType} flex flex-col justify-center`}
		>
			<h1 className="text-md h-1/2 overflow-hidden text-ellipsis whitespace-nowrap">
				{event.name}
			</h1>
			<Divider />
			<div id="bucket-event-card-bottom" className="w-full h-1/2">
				<h2 className="float-left">
					{datetime_convert(event.trigger_datetime)}
				</h2>
				<p className={`float-right font-bold ${textColorType}`}>
					{event.properties.amount}
				</p>
			</div>
		</div>
	);
};

export default BucketEventCard;
