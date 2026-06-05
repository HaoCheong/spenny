import Divider from "./Divider";
import Button from "./Input/Button";

const datetime_convert = (date) => {
	const dateObj = new Date(date);
	return dateObj.toLocaleDateString("en-GB");
};

const LogRow = ({ log }) => {
	let textColorType;
	if (log.action_properties.operation.type === "MOVE") {
		textColorType = "text-spenny-accent-warning";
	} else if (log.action_properties.operation.type === "ADD") {
		textColorType = "text-spenny-accent-base";
	} else if (log.action_properties.operation.type === "SUB") {
		textColorType = "text-spenny-accent-error";
	} else {
		textColorType = "text-white";
	}

	return (
		<div className="flex flex-row gap-3 w-full h-1/11">
			<Divider vertical />
			<p
				className={`flex items-center text-m w-2/27 h-[60px] ${textColorType}`}
			>
				{log.action_properties.operation.type}
			</p>
			<Divider vertical />
			<p className="flex items-center text-sm w-2/27 h-[60px] ">
				{log.bucket_name}
			</p>
			<Divider vertical />
			<p className="flex items-center text-sm w-4/27 h-[60px] whitespace-nowrap text-ellipsis">
				{log.action_name}
			</p>
			<Divider vertical />
			<p className="flex items-center text-sm w-11/27 h-[60px] whitespace-nowrap text-ellipsis">
				{log.action_description}
			</p>
			<Divider vertical />
			<p
				className={`flex justify-center items-center text-l w-2/27 h-[60px] p-2 ${textColorType} rounded-xl`}
			>
				${log.action_properties.operation?.amount ?? "N/A"}
			</p>

			<Divider vertical />
			<p className="flex items-center text-sm w-2/27 h-[30px] ">
				{datetime_convert(log.created_at)}
			</p>
			<Divider vertical />
			<p className="flex items-center justify-center text-lg w-2/27 h-[30px] ">
				<Button classStyle={"w-full"} label="View" />
			</p>
		</div>
	);
};

export default LogRow;
