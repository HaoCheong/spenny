import {
	Description,
	Dialog,
	DialogPanel,
	DialogTitle,
	Field,
	Input,
	Label,
	Textarea,
	Transition,
	TransitionChild,
} from "@headlessui/react";
import Button from "./Button";
import clsx from "clsx";
import { Fragment } from "react";
import DialogBase from "./DialogBase";
import Textfield from "./Textfield";

const AddBucketDialog = ({ isOpen, setIsOpen }) => {
	const handleClose = () => {
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
					Add Bucket
				</DialogTitle>
				<div id="add-modal-input-content" class="flex flex-col gap-3">
					<Field>
						<Label className="text-md font-medium text-white">
							Name
						</Label>
						<Input
							className={clsx(
								"mt-3 block w-full rounded-lg border-none bg-white/5 px-3 py-1.5 text-sm/6 text-white",
								"focus:not-data-focus:outline-none data-focus:outline-2 data-focus:-outline-offset-2 data-focus:outline-white/30"
							)}
						/>
					</Field>
					<Field>
						<Label className="text-md font-medium text-white">
							Starting Amount
						</Label>
						<Input
							className={clsx(
								"mt-3 block w-full rounded-lg border-none bg-white/5 px-3 py-1.5 text-sm/6 text-white",
								"focus:not-data-focus:outline-none data-focus:outline-2 data-focus:-outline-offset-2 data-focus:outline-white/30"
							)}
						/>
					</Field>
					<Field>
						<Label className="text-md font-medium text-white">
							Description
						</Label>
						<Description className="text-sm/6 text-white/50">
							Short Description of what the bucket purpose is.
						</Description>
						<Textarea
							className={clsx(
								"mt-3 block w-full resize-none rounded-lg border-none bg-white/5 px-3 py-1.5 text-sm/6 text-white",
								"focus:not-data-focus:outline-none data-focus:outline-2 data-focus:-outline-offset-2 data-focus:outline-white/25"
							)}
							rows={3}
						/>
					</Field>
				</div>
				<div
					id="dialog-action-panel"
					className="flex flex-row-reverse w-full pt-3 gap-3"
				>
					<Button
						classColor="border-solid border-2 border-solid bg-spenny-accent-warning text-black hover:bg-spenny-background hover:text-spenny-accent-warning"
						label="Close Form"
						onClick={handleClose}
					/>
					<Button
						classColor="border-solid border-2 border-solid bg-spenny-accent-primary text-black hover:bg-spenny-background hover:text-spenny-accent-primary"
						label="Add Bucket"
					/>
				</div>
			</DialogPanel>
		</DialogBase>
	);
};

export default AddBucketDialog;
