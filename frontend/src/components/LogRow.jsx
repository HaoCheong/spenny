import { centsToDollars } from "../helpers/displayConverter";
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
				className={`flex items-center text-xl w-2/27 h-[60px] ${textColorType}`}
			>
				{log.action_properties.operation.type}
			</p>
			<Divider vertical />
			<p className="flex items-center text-xl w-2/27 h-[60px] ">
				{log.bucket_name}
			</p>
			<Divider vertical />
			<p className="flex items-center text-sm w-6/27 h-[60px] whitespace-nowrap text-ellipsis">
				{log.name}
			</p>
			<Divider vertical />
			<p className="flex items-center text-lg w-11/27 h-[60px] whitespace-nowrap text-ellipsis">
				{log.description}
			</p>
			<Divider vertical />
			{["ADD", "SUB", "MOVE"].includes(
				log.action_properties.operation.type,
			) ? (
				<p
					className={`flex justify-center items-center text-xl w-2/27 h-[60px] p-2 ${textColorType} rounded-xl`}
				>
					$
					{centsToDollars(log.action_properties.operation?.amount) ??
						"N/A"}
				</p>
			) : (
				<></>
			)}
			{["MULT"].includes(log.action_properties.operation.type) ? (
				<p
					className={`flex justify-center items-center text-xl w-2/27 h-[60px] p-2 ${textColorType} rounded-xl`}
				>
					{centsToDollars(
						log.action_properties.operation?.percentage,
					) ?? "N/A"}
					%
				</p>
			) : (
				<></>
			)}

			<Divider vertical />
			<p className="flex items-center text-xl w-2/27 h-[60px] ">
				{datetime_convert(log.created_at)}
			</p>
			<Divider vertical />
			<p className="flex items-center justify-center text-xl w-2/27 h-[60px] ">
				<Button classStyle={"w-full h-full"} label="View" />
			</p>
		</div>
	);
};

export default LogRow;
