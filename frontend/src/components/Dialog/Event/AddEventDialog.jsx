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
import React from "react";
import * as Yup from "yup";
import Divider from "../../Divider";
import FieldLabel from "../../FieldLabel";
import Button from "../../Input/Button";
import ResponseAlert from "../../ResponseAlert";
import DialogBase from "../DialogBase";

const AddEventDialog = ({ isOpen, setIsOpen, bucket, buckets }) => {
	const eventTypes = [
		{ id: 0, value: "ADD", name: "Add", properties: { amount: 0 } },
		{ id: 1, value: "SUB", name: "Deduct", properties: { amount: 0 } },
		{
			id: 2,
			value: "MOVE",
			name: "Transfer",
			properties: { to_bucket: buckets[0], amount: 0 },
		},
		{
			id: 3,
			value: "MULT",
			name: "Multiply",
			properties: { to_bucket: buckets[0], percentage: 0 },
		},
		{
			id: 4,
			value: "CMV",
			name: "Clear and Move",
			properties: { to_bucket: buckets[0] },
		},
	];

	const frequencyTypes = [
		{ id: 0, value: "d", name: "Day(s)" },
		{ id: 1, value: "w", name: "Week(s)" },
		{ id: 2, value: "m", name: "Month(s)" },
		{ id: 3, value: "y", name: "Year(s)" },
	];

	const [alertInfo, setAlertInfo] = React.useState({
		isOpen: false,
		type: "",
		message: "",
	});
	const handleClose = () => {
		setIsOpen(false);
	};

	const handleFrequencyTypeChange = (value) => {
		const frequencyType = frequencyTypes.find(
			(frequencyType) => frequencyType.id === value
		);

		console.log("FREQ TYPE", frequencyType);
		formik.setFieldValue("frequency_type", frequencyType);
	};

	const handleEventTypeChange = (value) => {
		const eventType = eventTypes.find(
			(eventType) => eventType.id === value
		);

		console.log("EVENT TYPE", eventType);
		formik.setFieldValue("event_type", eventType);
		formik.setFieldValue("properties", eventType.properties);
	};

	const handleSubmit = async (values) => {
		console.log("NEW EVENT", values);
	};

	const AddEventValidationSchema = Yup.object().shape({
		name: Yup.string().required("Event name is required"),
		description: Yup.string().required("Event description is required"),
		frequency_qty: Yup.string().required("Frequency is required"),
		event_type: Yup.string().required("Event name is required"),
	});
	const formik = useFormik({
		// validationSchema: AddEventValidationSchema,
		initialValues: {
			name: "",
			description: "",
			trigger_datetime: "",
			frequency_qty: 0,
			frequency_type: frequencyTypes[0],
			event_type: eventTypes[0],
			properties: {},
			bucket_id: bucket.id,
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
				<form onSubmit={formik.handleSubmit}>
					<DialogTitle
						as="h3"
						className="text-3xl font-bold text-white pb-3"
					>
						Add Event
					</DialogTitle>
					<div
						id="add-event-input-content"
						className="flex flex-col gap-3 h-[700px] overflow-y-scroll"
					>
						<FieldLabel label="Bucket to Add">
							<Input
								id="bucket_id"
								name="bucket_id"
								className={clsx(
									"mt-2 w-full rounded-lg border-none bg-white/5 p-1.5 text-sm text-white",
									"focus:not-data-focus:outline-none data-focus:outline-2 data-focus:-outline-offset-2 data-focus:outline-white/30"
								)}
								disabled
								value={bucket.name}
							/>
						</FieldLabel>
						<Divider />
						<FieldLabel label="Event Name">
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
						<FieldLabel
							required
							label="Description"
							desc="What is the purpose of this event"
							error={formik.errors.description !== ""}
							errorMsg={formik.errors.description}
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
						<FieldLabel
							required
							label="Event Type"
							desc="What is the type of event that this is?"
							error={formik.errors.event_type !== ""}
							errorMsg={formik.errors.event_type}
						>
							<Listbox
								value={formik.values.event_type.id}
								onChange={(value) =>
									handleEventTypeChange(value)
								}
							>
								<ListboxButton
									className={clsx(
										"w-full rounded-lg bg-white/5 p-1.5 text-left text-sm text-white",
										"focus:not-data-focus:outline-none data-focus:outline-2 data-focus:-outline-offset-2 data-focus:outline-white/25"
									)}
								>
									{formik.values.event_type.name}
								</ListboxButton>
								<ListboxOptions
									anchor="bottom end"
									transition
									className={clsx(
										"w-(--button-width) rounded-lg border border-white/5 bg-spenny-background p-1 [--anchor-gap:--spacing(1)] focus:outline-none",
										"transition duration-100 ease-in-out data-closed:opacity-0"
									)}
								>
									{eventTypes.map((evt_type) => (
										<ListboxOption
											key={evt_type.id}
											value={evt_type.id}
											className="group flex cursor-default items-center gap-2 rounded-lg px-3 py-1.5 select-none data-focus:bg-white/10"
										>
											<div className="text-sm/6 text-white">
												{evt_type.name}
											</div>
										</ListboxOption>
									))}
								</ListboxOptions>
							</Listbox>
						</FieldLabel>
						{formik.values.event_type.value === "ADD" ? (
							<FieldLabel label="Amount to Add">
								<Input
									required
									id="amount"
									name="amount"
									className={clsx(
										"mt-2 w-full rounded-lg border-none bg-white/5 p-1.5 text-sm text-white",
										"focus:not-data-focus:outline-none data-focus:outline-2 data-focus:-outline-offset-2 data-focus:outline-white/30"
									)}
									onChange={(e) => {
										formik.setFieldValue("properties", {
											amount: parseInt(e.target.value),
										});
									}}
									value={formik.values.properties.amount ?? 0}
								/>
							</FieldLabel>
						) : (
							<></>
						)}
						{formik.values.event_type.value === "SUB" ? (
							<FieldLabel label="Amount to Deduct">
								<Input
									required
									id="amount"
									name="amount"
									className={clsx(
										"mt-2 w-full rounded-lg border-none bg-white/5 p-1.5 text-sm text-white",
										"focus:not-data-focus:outline-none data-focus:outline-2 data-focus:-outline-offset-2 data-focus:outline-white/30"
									)}
									onChange={(e) => {
										formik.setFieldValue("properties", {
											amount: parseInt(e.target.value),
										});
									}}
									value={formik.values.properties.amount ?? 0}
								/>
							</FieldLabel>
						) : (
							<></>
						)}
						{formik.values.event_type.value === "MOVE" ? (
							<>
								<FieldLabel label="Amount to Transfer">
									<Input
										required
										id="amount"
										name="amount"
										className={clsx(
											"mt-2 w-full rounded-lg border-none bg-white/5 p-1.5 text-sm text-white",
											"focus:not-data-focus:outline-none data-focus:outline-2 data-focus:-outline-offset-2 data-focus:outline-white/30"
										)}
										onChange={(e) => {
											formik.setFieldValue("properties", {
												to_bucket:
													formik.values.properties
														.to_bucket,
												amount: parseInt(
													e.target.value
												),
											});
										}}
										value={
											formik.values.properties.amount ?? 0
										}
									/>
								</FieldLabel>
								<FieldLabel
									label="To Bucket"
									desc="Which bucket are we transferring to"
								>
									<Listbox
										value={
											formik.values.properties.to_bucket
												.id
										}
										onChange={(bucket) => {
											formik.setFieldValue("properties", {
												to_bucket: bucket,
												amount: formik.values.properties
													.amount,
											});
										}}
									>
										<ListboxButton
											className={clsx(
												"w-full rounded-lg bg-white/5 p-1.5 text-left text-sm text-white",
												"focus:not-data-focus:outline-none data-focus:outline-2 data-focus:-outline-offset-2 data-focus:outline-white/25"
											)}
										>
											{
												formik.values.properties
													.to_bucket.name
											}
										</ListboxButton>
										<ListboxOptions
											anchor="bottom end"
											transition
											className={clsx(
												"w-(--button-width) rounded-lg border border-white/5 bg-spenny-background p-1 [--anchor-gap:--spacing(1)] focus:outline-none",
												"transition duration-100 ease-in-out data-closed:opacity-0"
											)}
										>
											{buckets.map((bucket) => (
												<ListboxOption
													key={bucket.id}
													value={bucket}
													className="group flex cursor-default items-center gap-2 rounded-lg px-3 py-1.5 select-none data-focus:bg-white/10"
												>
													<div className="text-sm/6 text-white">
														{bucket.name}
													</div>
												</ListboxOption>
											))}
										</ListboxOptions>
									</Listbox>
								</FieldLabel>
							</>
						) : (
							<></>
						)}
						{formik.values.event_type.value === "MULT" ? (
							<FieldLabel label="Amount to Multiply (%)">
								<Input
									required
									id="amount"
									name="amount"
									className={clsx(
										"mt-2 w-full rounded-lg border-none bg-white/5 p-1.5 text-sm text-white",
										"focus:not-data-focus:outline-none data-focus:outline-2 data-focus:-outline-offset-2 data-focus:outline-white/30"
									)}
									onChange={(e) => {
										formik.setFieldValue("properties", {
											percentage: parseInt(
												e.target.value
											),
										});
									}}
									value={
										formik.values.properties.percentage ?? 0
									}
								/>
							</FieldLabel>
						) : (
							<></>
						)}
						{formik.values.event_type.value === "CMV" ? (
							<FieldLabel
								label="To Bucket"
								desc="Which bucket are we transferring to"
							>
								<Listbox
									value={
										formik.values.properties.to_bucket.id
									}
									onChange={(bucket) => {
										formik.setFieldValue("properties", {
											to_bucket: bucket,
										});
									}}
								>
									<ListboxButton
										className={clsx(
											"w-full rounded-lg bg-white/5 p-1.5 text-left text-sm text-white",
											"focus:not-data-focus:outline-none data-focus:outline-2 data-focus:-outline-offset-2 data-focus:outline-white/25"
										)}
									>
										{
											formik.values.properties.to_bucket
												.name
										}
									</ListboxButton>
									<ListboxOptions
										anchor="bottom end"
										transition
										className={clsx(
											"w-(--button-width) rounded-lg border border-white/5 bg-spenny-background p-1 [--anchor-gap:--spacing(1)] focus:outline-none",
											"transition duration-100 ease-in-out data-closed:opacity-0"
										)}
									>
										{buckets.map((bucket) => (
											<ListboxOption
												key={bucket.id}
												value={bucket}
												className="group flex cursor-default items-center gap-2 rounded-lg px-3 py-1.5 select-none data-focus:bg-white/10"
											>
												<div className="text-sm/6 text-white">
													{bucket.name}
												</div>
											</ListboxOption>
										))}
									</ListboxOptions>
								</Listbox>
							</FieldLabel>
						) : (
							<></>
						)}
						<Divider />
						<FieldLabel
							required
							label="Frequency"
							desc="How often do you want this event to occur?"
						>
							<div
								id="event-frequency-input"
								className="flex flex-row gap-3"
							>
								<Input
									id="frequency_qty"
									name="frequency_qty"
									type="number"
									className={clsx(
										"w-full rounded-lg border-none bg-white/5 p-1.5 text-sm text-white",
										"focus:not-data-focus:outline-none data-focus:outline-2 data-focus:-outline-offset-2 data-focus:outline-white/30"
									)}
									onChange={formik.handleChange}
									value={formik.values.frequency_qty}
								/>
								<div className="size-full">
									<Listbox
										value={formik.values.frequency_type.id}
										onChange={(value) =>
											handleFrequencyTypeChange(value)
										}
									>
										<ListboxButton
											className={clsx(
												"size-full rounded-lg bg-white/5 p-1.5 text-left text-sm text-white",
												"focus:not-data-focus:outline-none data-focus:outline-2 data-focus:-outline-offset-2 data-focus:outline-white/25"
											)}
										>
											{formik.values.frequency_type.name}
										</ListboxButton>
										<ListboxOptions
											anchor="bottom end"
											transition
											className={clsx(
												"w-(--button-width) rounded-lg border border-white/5 bg-spenny-background p-1 [--anchor-gap:--spacing(1)] focus:outline-none",
												"transition duration-100 ease-in-out data-closed:opacity-0"
											)}
										>
											{frequencyTypes.map((freq_type) => (
												<ListboxOption
													key={freq_type.id}
													value={freq_type.id}
													className="group flex cursor-default items-center gap-2 rounded-lg px-3 py-1.5 select-none data-focus:bg-white/10"
												>
													<div className="text-sm/6 text-white">
														{freq_type.name}
													</div>
												</ListboxOption>
											))}
										</ListboxOptions>
									</Listbox>
								</div>
							</div>
						</FieldLabel>
						<FieldLabel
							required
							label="Next Date"
							desc="When do you want this to next run?"
						>
							<Input
								id="trigger_datetime"
								name="trigger_datetime"
								className={clsx(
									"mt-2 w-full rounded-lg border-none bg-white/5 p-1.5 text-sm text-white",
									"focus:not-data-focus:outline-none data-focus:outline-2 data-focus:-outline-offset-2 data-focus:outline-white/30"
								)}
								onChange={formik.handleChange}
								value={formik.values.trigger_datetime}
								type="date"
							/>
						</FieldLabel>
					</div>
					<ResponseAlert alertInfo={alertInfo} />
					<div
						id="dialog-action-panel"
						className="flex flex-row-reverse h-1/10 w-full pt-3 gap-3"
					>
						<Button
							classColor="border-solid border-2 border-solid bg-spenny-accent-warning text-black hover:bg-spenny-background hover:text-spenny-accent-warning"
							label="Close Form"
							onClick={handleClose}
						/>
						<Button
							classColor="border-solid border-2 border-solid bg-spenny-accent-primary text-black hover:bg-spenny-background hover:text-spenny-accent-primary"
							label="Add Event"
							type="submit"
							onClick={() => {}}
						/>
					</div>
				</form>
			</DialogPanel>
		</DialogBase>
	);
};

export default AddEventDialog;
