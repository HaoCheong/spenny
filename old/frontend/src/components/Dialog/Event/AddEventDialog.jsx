import { DialogPanel, DialogTitle, Input, Textarea } from "@headlessui/react";
import clsx from "clsx";
import { useFormik } from "formik";
import React from "react";
import * as Yup from "yup";
import { BACKEND_URL } from "../../../configs/config";
import axiosRequest from "../../axiosRequest";
import Divider from "../../Divider";
import FieldLabel from "../../FieldLabel";
import Button from "../../Input/Button";
import ListItems from "../../Input/ListItems";
import ResponseAlert from "../../ResponseAlert";
import DialogBase from "../DialogBase";
import EventAddInputs from "./Input/EventAddInputs";
import EventCmvInputs from "./Input/EventCmvInputs";
import EventMoveInputs from "./Input/EventMoveInputs";
import EventMultInputs from "./Input/EventMultInputs";
import EventSubInputs from "./Input/EventSubInputs";

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

		formik.setFieldValue("frequency_type", frequencyType);
	};

	const handleEventTypeChange = (value) => {
		const eventType = eventTypes.find(
			(eventType) => eventType.id === value
		);

		formik.setFieldValue("event_type", eventType);
		formik.setFieldValue("properties", eventType.properties);
	};

	const handleSubmit = async (values) => {
		const newEvent = {
			name: values.name,
			description: values.description,
			trigger_datetime: new Date(values.trigger_datetime),
			frequency: `${values.frequency_qty}${values.frequency_type.value}`,
			event_type: values.event_type.value,
			properties: values.properties,
			bucket_id: bucket.id,
		};

		try {
			const data = await axiosRequest("POST", `${BACKEND_URL}/event`, {
				data: newEvent,
			});

			setAlertInfo({
				isOpen: true,
				type: "success",
				message: `${newEvent.name} event added to ${bucket.name} successfully.`,
			});
		} catch (error) {
			setAlertInfo({
				isOpen: true,
				type: "error",
				message: `${error}`,
			});
		}
	};
	const AddEventValidationSchema = Yup.object().shape({
		name: Yup.string().required("Event name is required"),
		description: Yup.string().required("Event description is required"),
		frequency_qty: Yup.string().required("Frequency is required"),
	});
	const formik = useFormik({
		validationSchema: AddEventValidationSchema,
		initialValues: {
			name: "",
			description: "",
			trigger_datetime: "",
			frequency_qty: 0,
			frequency_type: frequencyTypes[0],
			event_type: eventTypes[0],
			properties: {},
		},
		onSubmit: (values) => {
			handleSubmit(values);
		},
	});

	const EventInputsMap = {
		ADD: <EventAddInputs formik={formik} />,
		SUB: <EventSubInputs formik={formik} />,
		MOVE: <EventMoveInputs formik={formik} buckets={buckets} />,
		MULT: <EventMultInputs formik={formik} />,
		CMV: <EventCmvInputs formik={formik} buckets={buckets} />,
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
								id="bucket"
								name="bucket"
								className={clsx(
									"mt-2 w-full rounded-lg border-none bg-white/5 p-1.5 text-sm text-white",
									"focus:not-data-focus:outline-none data-focus:outline-2 data-focus:-outline-offset-2 data-focus:outline-white/30"
								)}
								disabled
								value={bucket.name}
							/>
						</FieldLabel>
						<Divider />
						<FieldLabel
							label="Event Name"
							error={formik.errors.name !== ""}
							errorMsg={formik.errors.name}
						>
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
							<ListItems
								startItem={formik.values.event_type}
								collection={eventTypes}
								onChange={(value) => {
									handleEventTypeChange(value);
								}}
								formik={formik}
							/>
						</FieldLabel>

						{EventInputsMap[formik.values.event_type.value] || (
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
									<ListItems
										startItem={formik.values.frequency_type}
										collection={frequencyTypes}
										onChange={(value) =>
											handleFrequencyTypeChange(value)
										}
										formik={formik}
									/>
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
							classColor="rounded-xl border-solid border-2 border-solid bg-spenny-accent-warning text-black hover:bg-spenny-background hover:text-spenny-accent-warning"
							label="Close Form"
							onClick={handleClose}
						/>
						<Button
							classColor="rounded-xl border-solid border-2 border-solid bg-spenny-accent-primary text-black hover:bg-spenny-background hover:text-spenny-accent-primary"
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
