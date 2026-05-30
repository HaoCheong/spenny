import { DialogPanel, DialogTitle, Input } from "@headlessui/react";
import clsx from "clsx";
import React from "react";
import { BACKEND_URL } from "../../../configs/config";
import axiosRequest from "../../axiosRequest";
import FieldLabel from "../../FieldLabel";
import Button from "../../Input/Button";
import ResponseAlert from "../../ResponseAlert";
import DialogBase from "../DialogBase";

const DeleteEventDialog = ({ isOpen, setIsOpen, bucket, event }) => {
	const [error, setError] = React.useState(false);
	const [errorMsg, setErrorMsg] = React.useState("");

	const [alertInfo, setAlertInfo] = React.useState({
		isOpen: false,
		type: "",
		message: "",
	});

	const handleDelete = async () => {
		setError(false);

		try {
			console.log("EVENT", event);
			await axiosRequest("DELETE", `${BACKEND_URL}/event/${event.id}`);

			setAlertInfo({
				isOpen: true,
				type: "success",
				message: `${event.name} event successfully deleted.`,
			});
		} catch (error) {
			setAlertInfo({
				isOpen: true,
				type: "error",
				message: `${error}`,
			});
		}
	};

	const handleClose = () => {
		setError(false);
		setErrorMsg("");
		setIsOpen(false);
	};
	return (
		<DialogBase isOpen={isOpen} setIsOpen={setIsOpen}>
			<DialogPanel
				transition
				className={clsx(
					"w-full max-w-2xl rounded-xl bg-spenny-background shadow-lg p-5",
					"border-solid border-5 border-spenny-accent-primary",
					"transition duration-200",
					"data-closed:scale-90 data-closed:opacity-0",
					"data-leave:duration-200 data-leave:ease-in-out",
				)}
			>
				<DialogTitle
					as="h3"
					className="text-3xl font-bold text-white pb-3"
				>
					Delete Event
				</DialogTitle>

				<div
					id="delete-event-modal"
					className="flex flex-col gap-3 p-3 size-full"
				>
					<div
						id="delete-warning-container"
						className="border-5 border-spenny-accent-error border-solid bg-spenny-accent-error/80 h-12/16 w-full flex flex-col gap-3 rounded-xl p-3"
					>
						<p
							id="delete-warning-message"
							className="text-md text-white text-justify"
						>
							Are you sure you want to delete the following event?
						</p>
						<p
							id="delete-warning-notification"
							className="text-md text-white font-bold"
						>
							All logs will be retained
						</p>
						<p
							id="delete-warning-notification"
							className="text-md text-white font-bold"
						>
							Event Name: {event.name}
						</p>
					</div>
					<ResponseAlert alertInfo={alertInfo} />
					<div
						id="delete-dialog-action-panel"
						className="flex flex-row-reverse w-full pt-3 gap-3"
					>
						<Button
							classColor="border-solid border-2 border-solid rounded-xl bg-spenny-accent-warning text-black hover:bg-spenny-background hover:text-spenny-accent-warning"
							label="Close"
							onClick={handleClose}
						/>
						<Button
							classColor="text-white rounded-xl border-solid border-2 border-solid border-spenny-accent-error bg-spenny-accent-error text-black hover:bg-spenny-background hover:text-spenny-accent-error"
							label="Delete Event"
							onClick={handleDelete}
						/>
					</div>
				</div>
			</DialogPanel>
		</DialogBase>
	);
};

export default DeleteEventDialog;
