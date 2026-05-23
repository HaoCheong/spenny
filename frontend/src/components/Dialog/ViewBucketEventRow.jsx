import clsx from "clsx";
import Button from "../Input/Button";
const ViewBucketEventRow = ({
	setIsViewOpen,
	setIsEditOpen,
	setIsDeleteOpen,
	setEvent,
	event,
}) => {
	return (
		<div
			id="view-bucket-event-row"
			className={clsx(
				"flex flex-row w-1/1 h-2/5 border-3 border-solid border-spenny-accent-primary rounded-xl",
			)}
		>
			<div
				id="view-bucket-event-content"
				className="w-14/16 p-3 h-full flex items-center text-white"
			>
				{event.name}
			</div>
			<div
				id="view-bucket-event-content"
				className="w-3/16 h-full flex items-center"
			>
				<Button
					label="View"
					classColor="bg-spenny-accent-primary border-solid border-2 border-spenny-accent-primary text-black hover:bg-spenny-background hover:text-spenny-accent-primary"
					classStyle={"w-1/3 h-full"}
					onClick={() => {
						setEvent(event);
						setIsViewOpen(true);
					}}
				/>
				<Button
					label="Edit"
					classColor="bg-spenny-accent-warning border-solid border-2 border-spenny-accent-warning text-black hover:bg-spenny-background hover:text-spenny-accent-warning"
					classStyle={"w-1/3 h-full"}
					onClick={() => {
						setEvent(event);
						setIsEditOpen(true);
					}}
				/>

				{/* PFIX: Have the removal of events be reactive (Man Solid would have been great for this alas) */}
				<Button
					label="Delete"
					classColor="bg-spenny-accent-error border-solid border-2 border-spenny-accent-warning text-black hover:bg-spenny-background hover:text-spenny-accent-warning"
					classStyle={"w-1/3 h-full rounded-r-lg"}
					onClick={() => {
						setEvent(event);
						setIsDeleteOpen(true);
					}}
				/>
			</div>
		</div>
	);
};

export default ViewBucketEventRow;
