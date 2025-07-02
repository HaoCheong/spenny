import {
	DialogPanel,
	DialogTitle,
	Input,
	Listbox,
	ListboxButton,
	ListboxOption,
	ListboxOptions,
	Textarea,
} from "@headlessui/react";
import clsx from "clsx";
import React from "react";
import Button from "./Button";
import DialogBase from "./DialogBase";
import FieldLabel from "./FieldLabel";

const AddBucketDialog = ({ isOpen, setIsOpen }) => {
	const handleClose = () => {
		setIsOpen(false);
	};

	const bucketTypes = [
		{ id: 1, name: "STORE" },
		{ id: 2, name: "INVISIBLE" },
		{ id: 3, name: "GOALS" },
	];

	const [selected, setSelected] = React.useState(bucketTypes[1]);

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
				<div
					id="add-modal-input-content"
					className="flex flex-col gap-3"
				>
					<FieldLabel label="Name">
						<Input
							className={clsx(
								"mt-2 w-full rounded-lg border-none bg-white/5 p-1.5 text-sm text-white",
								"focus:not-data-focus:outline-none data-focus:outline-2 data-focus:-outline-offset-2 data-focus:outline-white/30"
							)}
						/>
					</FieldLabel>
					<FieldLabel label="Starting Amount">
						<Input
							className={clsx(
								"mt-2 block w-full rounded-lg border-none bg-white/5 px-3 py-1.5 text-sm text-white",
								"focus:not-data-focus:outline-none data-focus:outline-2 data-focus:-outline-offset-2 data-focus:outline-white/30"
							)}
						/>
					</FieldLabel>
					<FieldLabel
						label="Description"
						desc="What is the purpose of this bucket"
					>
						<Textarea
							className={clsx(
								"mt-2 block w-full resize-none rounded-lg border-none bg-white/5 px-3 py-1.5 text-sm text-white",
								"focus:not-data-focus:outline-none data-focus:outline-2 data-focus:-outline-offset-2 data-focus:outline-white/25"
							)}
							rows={3}
						/>
					</FieldLabel>
					<FieldLabel label="Bucket Type">
						<div className="mt-3 w-full h-full">
							<Listbox value={selected} onChange={setSelected}>
								<ListboxButton
									className={clsx(
										"relative block w-full rounded-lg bg-white/5 py-1.5 pr-8 pl-3 text-left text-sm text-white",
										"focus:not-data-focus:outline-none data-focus:outline-2 data-focus:-outline-offset-2 data-focus:outline-white/25"
									)}
								>
									{selected.name}
								</ListboxButton>
								<ListboxOptions
									anchor="bottom"
									transition
									className={clsx(
										"w-(--button-width) rounded-lg border border-white/5 bg-spenny-background p-1 [--anchor-gap:--spacing(1)] focus:outline-none",
										"transition duration-100 ease-in-out data-closed:opacity-0"
									)}
								>
									{bucketTypes.map((type) => (
										<ListboxOption
											key={type.name}
											value={type}
											className="group flex cursor-default items-center gap-2 rounded-lg px-3 py-1.5 select-none data-focus:bg-white/10"
										>
											<div className="text-sm/6 text-white">
												{type.name}
											</div>
										</ListboxOption>
									))}
								</ListboxOptions>
							</Listbox>
						</div>
					</FieldLabel>
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
