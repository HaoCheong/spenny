import { DialogPanel, DialogTitle, Input } from "@headlessui/react";
import clsx from "clsx";
import React from "react";
import { BACKEND_URL } from "../../../configs/config";
import axiosRequest from "../../axiosRequest";
import FieldLabel from "../../FieldLabel";
import Button from "../../Input/Button";
import ResponseAlert from "../../ResponseAlert";
import DialogBase from "../DialogBase";

const DeleteBucketDialog = ({
	isOpen,
	setIsOpen,
	buckets,
	setBuckets,
	bucket,
}) => {
	const [bucketNameCheck, setBucketNameCheck] = React.useState("");
	const [error, setError] = React.useState(false);
	const [errorMsg, setErrorMsg] = React.useState("");

	const [alertInfo, setAlertInfo] = React.useState({
		isOpen: false,
		type: "",
		message: "",
	});

	const handleDelete = async () => {
		if (bucket.name !== bucketNameCheck) {
			setError(true);
			setErrorMsg(
				"Bucket name does not match. Ensure casing and spacing is accurate"
			);
			return;
		}

		setError(false);

		try {
			await axiosRequest("DELETE", `${BACKEND_URL}/bucket/${bucket.id}`);

			// const remainingBuckets = buckets.filter((b) => b.id !== bucket.id);
			setBuckets((buckets) => buckets.filter((b) => b.id !== bucket.id));

			setAlertInfo({
				isOpen: true,
				type: "success",
				message: `${bucket.name} bucket successfully deleted.`,
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
		setBucketNameCheck("");
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
					"data-leave:duration-200 data-leave:ease-in-out"
				)}
			>
				<DialogTitle
					as="h3"
					className="text-3xl font-bold text-white pb-3"
				>
					Delete Bucket
				</DialogTitle>

				<div
					id="delete-bucket-modal"
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
							Once this bucket is delete, operation is
							irreversible. Events related to it are all deleted
							with it. Logs will be kept
						</p>
						<p
							id="delete-warning-notification"
							className="text-md text-white font-bold"
						>
							To confirm deletion, please type in the name of the
							bucket you want to be deleting in the box and
							confirming.
						</p>
						<p
							id="delete-warning-notification"
							className="text-md text-white font-bold"
						>
							{" "}
							Bucket Name: {bucket.name}
						</p>
					</div>
					<FieldLabel
						label="Bucket to Delete"
						error={error}
						errorMsg={errorMsg}
					>
						<Input
							className={clsx(
								"mt-2 w-full rounded-lg border-none bg-white/5 p-1.5 text-sm text-white",
								"focus:not-data-focus:outline-none data-focus:outline-2 data-focus:-outline-offset-2 data-focus:outline-white/30"
							)}
							onChange={(e) => setBucketNameCheck(e.target.value)}
							value={bucketNameCheck}
						/>
					</FieldLabel>
					<ResponseAlert alertInfo={alertInfo} />
					<div
						id="delete-dialog-action-panel"
						className="flex flex-row-reverse w-full pt-3 gap-3"
					>
						<Button
							classColor="border-solid border-2 border-solid bg-spenny-accent-warning text-black hover:bg-spenny-background hover:text-spenny-accent-warning"
							label="Close Form"
							onClick={handleClose}
						/>
						<Button
							classColor="text-white border-solid border-2 border-solid border-spenny-accent-error bg-spenny-accent-error text-black hover:bg-spenny-background hover:text-spenny-accent-error"
							label="Delete Bucket"
							onClick={handleDelete}
						/>
					</div>
				</div>
			</DialogPanel>
		</DialogBase>
	);
};

export default DeleteBucketDialog;
