import { DialogPanel, DialogTitle } from "@headlessui/react";
import clsx from "clsx";
import Divider from "../../Divider";
import Button from "../../Input/Button";
import Placeholder from "../../Structural/Placeholder";
import DialogBase from "../DialogBase";
import ViewBucketEventRow from "../ViewBucketEventRow";
import React from "react";
import ViewEventDialog from "../Event/ViewEventDialog";
import EditEventDialog from "../Event/EditEventDialog";
import DeleteEventDialog from "../Event/DeleteEventDialog";
import { centsToDollars } from "../../../helpers/displayConverter";

const ViewBucketDialog = ({ isOpen, setIsOpen, buckets, bucket }) => {
	const [isViewEventOpen, setIsViewEventOpen] = React.useState(false);
	const [isEditEventOpen, setIsEditEventOpen] = React.useState(false);
	const [isDeleteEventOpen, setIsDeleteEventOpen] = React.useState(false);

	const [focusedEvent, setFocusedEvent] = React.useState({});

	const handleClose = () => {
		setIsOpen(false);
	};

	return (
		<>
			<DialogBase isOpen={isOpen} setIsOpen={setIsOpen}>
				<ViewEventDialog
					isOpen={isViewEventOpen}
					setIsOpen={setIsViewEventOpen}
					buckets={buckets}
					bucket={bucket}
					event={focusedEvent}
				/>
				<EditEventDialog
					isOpen={isEditEventOpen}
					setIsOpen={setIsEditEventOpen}
					buckets={buckets}
					bucket={bucket}
					event={focusedEvent}
				/>
				<DeleteEventDialog
					isOpen={isDeleteEventOpen}
					setIsOpen={setIsDeleteEventOpen}
					bucket={bucket}
					event={focusedEvent}
				/>
				<DialogPanel
					transition
					className={clsx(
						"w-full h-full max-w-5xl rounded-xl bg-spenny-background shadow-lg p-5",
						"border-solid border-5 border-spenny-accent-primary",
						"transition duration-200",
						"data-closed:scale-90 data-closed:opacity-0",
						"data-leave:duration-200 data-leave:ease-in-out",
					)}
				>
					<DialogTitle
						as="h3"
						className="w-full h-1/18 text-3xl font-bold text-white pb-3"
					>
						View: {bucket.name}
					</DialogTitle>
					<div
						id="view-modal-content"
						className="flex flex-col gap-3 h-17/18 w-full"
					>
						<div
							id="view-modal-display"
							className="h-15/16 w-full flex flex-col gap-3"
						>
							<Placeholder
								label="Graph"
								classStyle="h-5/17 w-full"
							/>
							<div
								id="view-modal-base-info"
								className="flex flex-row gap-3 w-full h-2/17"
							>
								<div
									id="view-amount"
									className="w-1/2 h-full flex items-center justify-center"
								>
									<p className="text-5xl text-spenny-text font-semibold p-3">
										{centsToDollars(bucket.amount)}
									</p>
								</div>
								<Divider vertical />
								<div
									id="view-description"
									className="w-1/2 h-full flex items-center border-solid border-5 border-spenny-accent-primary rounded-xl p-3"
								>
									<p className="text-xl text-spenny-text font-semibold">
										{bucket.description}
									</p>
								</div>
							</div>
							<Divider />
							<div
								id="view-flow-event-container"
								className={clsx(
									"h-5/17 w-full p-3 border-solid border-5 border-spenny-accent-primary overflow-y-scroll flex flex-col gap-3 rounded-xl",
								)}
							>
								{bucket.events?.map((event) => {
									console.log(
										"EVENTS from ViewBucketDialog",
										event,
									);
									return (
										<ViewBucketEventRow
											setIsViewOpen={setIsViewEventOpen}
											setIsEditOpen={setIsEditEventOpen}
											setIsDeleteOpen={
												setIsDeleteEventOpen
											}
											setEvent={setFocusedEvent}
											event={event}
										/>
									);
								})}
							</div>
							<Divider />
							<Placeholder
								label="Logs"
								classStyle="w-full h-5/17"
							/>
						</div>
						<div
							id="dialog-action-panel"
							className="flex flex-row-reverse h-1/18 w-full"
						>
							<Button
								classColor="rounded-xl border-solid border-2 border-solid bg-spenny-accent-warning text-black hover:bg-spenny-background hover:text-spenny-accent-warning"
								label="Close"
								onClick={handleClose}
							/>
						</div>
					</div>
				</DialogPanel>
			</DialogBase>
		</>
	);
};

export default ViewBucketDialog;
