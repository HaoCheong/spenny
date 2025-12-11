import clsx from "clsx";
import Button from "../Input/Button";
const ViewBucketEventRow = () => {
	return (
		<div
			id="view-bucket-event-row"
			className={clsx(
				"flex flex-row size-full border-3 border-solid border-spenny-accent-primary rounded-xl"
			)}
		>
			<div
				id="view-bucket-event-content"
				className="w-14/16 p-3 h-full flex items-center"
			>
				Test Name
			</div>
			<div
				id="view-bucket-event-content"
				className="w-2/16 h-full flex items-center"
			>
				<Button
					label="View"
					classColor="bg-spenny-accent-primary border-solid border-2 border-spenny-accent-primary text-black hover:bg-spenny-background hover:text-spenny-accent-primary"
					classStyle={"w-1/2 h-full"}
				/>
				<Button
					label="Edit"
					classColor="bg-spenny-accent-warning border-solid border-2 border-spenny-accent-warning text-black hover:bg-spenny-background hover:text-spenny-accent-warning"
					classStyle={"w-1/2 h-full rounded-r-lg"}
				/>
			</div>
		</div>
	);
};

export default ViewBucketEventRow;
