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
import { useFormik } from "formik";
import * as Yup from "yup";
import Button from "./Button";
import DialogBase from "./DialogBase";
import Divider from "./Divider";
import FieldLabel from "./FieldLabel";

const AddBucketDialog = ({ isOpen, setIsOpen }) => {
	const handleClose = () => {
		setIsOpen(false);
	};

	const handleSubmit = (values) => {
		console.log("New Bucket Values:", values);
	};

	const bucketTypes = [
		{ id: 0, name: "STORE", properties: {} },
		{ id: 1, name: "INVISIBLE", properties: {} },
		{ id: 2, name: "GOALS", properties: { target_amount: 0 } },
	];

	const handleBucketTypeChange = (value) => {
		const bucketType = bucketTypes.find(
			(bucketType) => bucketType.id === value
		);

		formik.setFieldValue("bucket_type", bucketType.name);
		formik.setFieldValue("properties", bucketType.properties);
	};

	const AddBucketValidateSchema = Yup.object().shape({
		name: Yup.string().required(),
		description: Yup.string().required(),
		amount: Yup.number().min(0).required(),
	});

	const formik = useFormik({
		validateSchema: AddBucketValidateSchema,
		initialValues: {
			name: "",
			description: "",
			amount: 0,
			bucket_type: bucketTypes[0].name,
			properties: bucketTypes[0].properties,
		},
		onSubmit: (values) => {
			handleSubmit(values);
		},
	});

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

				<form onSubmit={formik.handleSubmit}>
					<div
						id="add-modal-input-content"
						className="flex flex-col gap-3"
					>
						<FieldLabel label="Name">
							<Input
								id="name"
								name="name"
								className={clsx(
									"mt-2 w-full rounded-lg border-none bg-white/5 p-1.5 text-sm text-white",
									"focus:not-data-focus:outline-none data-focus:outline-2 data-focus:-outline-offset-2 data-focus:outline-white/30"
								)}
								onChange={formik.handleChange}
								value={formik.values.name}
							/>
						</FieldLabel>
						<FieldLabel label="Starting Amount">
							<Input
								id="amount"
								name="amount"
								className={clsx(
									"mt-2 block w-full rounded-lg border-none bg-white/5 px-3 py-1.5 text-sm text-white",
									"focus:not-data-focus:outline-none data-focus:outline-2 data-focus:-outline-offset-2 data-focus:outline-white/30"
								)}
								onChange={formik.handleChange}
								value={formik.values.amount}
							/>
						</FieldLabel>
						<FieldLabel
							label="Description"
							desc="What is the purpose of this bucket"
						>
							<Textarea
								id="description"
								name="description"
								className={clsx(
									"mt-2 block w-full resize-none rounded-lg border-none bg-white/5 px-3 py-1.5 text-sm text-white",
									"focus:not-data-focus:outline-none data-focus:outline-2 data-focus:-outline-offset-2 data-focus:outline-white/25"
								)}
								rows={3}
								onChange={formik.handleChange}
								value={formik.values.description}
							/>
						</FieldLabel>
						<FieldLabel label="Bucket Type">
							<div className="mt-3 w-full h-full">
								<Listbox
									value={formik.values.bucket_type}
									onChange={(value) =>
										handleBucketTypeChange(value)
									}
								>
									<ListboxButton
										className={clsx(
											"relative block w-full rounded-lg bg-white/5 py-1.5 pr-8 pl-3 text-left text-sm text-white",
											"focus:not-data-focus:outline-none data-focus:outline-2 data-focus:-outline-offset-2 data-focus:outline-white/25"
										)}
									>
										{formik.values.bucket_type}
									</ListboxButton>
									<ListboxOptions
										anchor="bottom end"
										transition
										className={clsx(
											"w-(--button-width) rounded-lg border border-white/5 bg-spenny-background p-1 [--anchor-gap:--spacing(1)] focus:outline-none",
											"transition duration-100 ease-in-out data-closed:opacity-0"
										)}
									>
										{bucketTypes.map((type) => (
											<ListboxOption
												key={type.id}
												value={type.id}
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
						{formik.values.bucket_type.name === "GOALS" ? (
							<>
								<Divider />
								<FieldLabel
									label="Target Amount"
									desc="How much are you aiming for?"
								>
									<Input
										id="target_amount"
										name="target_amount"
										className={clsx(
											"mt-2 block w-full rounded-lg border-none bg-white/5 px-3 py-1.5 text-sm text-white",
											"focus:not-data-focus:outline-none data-focus:outline-2 data-focus:-outline-offset-2 data-focus:outline-white/30"
										)}
										onChange={(value) => {
											formik.setFieldValue("properties", {
												target_amount: value,
											});
										}}
										value={
											formik.values.properties
												.target_amount ?? 0
										}
									/>
								</FieldLabel>
							</>
						) : (
							<></>
						)}
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
								type="submit"
								onClick={() => {}}
							/>
						</div>
					</div>
				</form>
			</DialogPanel>
		</DialogBase>
	);
};

export default AddBucketDialog;
