import { DialogPanel, DialogTitle, Input, Textarea } from "@headlessui/react";
import clsx from "clsx";
import { FormikConsumer, useFormik } from "formik";
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

const ViewEventDialog = ({ isOpen, setIsOpen, buckets, bucket, event }) => {
	const eventTypes = [
		{ id: 0, value: "ADD", name: "Add", amount: 0 },
		{ id: 1, value: "SUB", name: "Deduct", amount: 0 },
		{
			id: 2,
			value: "MOVE",
			name: "Transfer",
			to_bucket: buckets[0],
			amount: 0,
		},
		{
			id: 3,
			value: "MULT",
			name: "Multiply",
			to_bucket: buckets[0],
			percentage: 0,
		},
		{
			id: 4,
			value: "CMV",
			name: "Clear and Move",
			to_bucket: buckets[0],
		},
	];

	const frequencyTypes = [
		{ id: 0, value: "d", name: "Day(s)" },
		{ id: 1, value: "w", name: "Week(s)" },
		{ id: 2, value: "m", name: "Month(s)" },
		{ id: 3, value: "y", name: "Year(s)" },
	];

	//PFIX: This is not great, we should really pick a standard especially in the backend. There is no reason for translation between them
	const convertFrequencyToType = (freq) => {
		if (freq == undefined) {
			return {
				frequencyValue: 0,
				frequencyType: {},
			};
		}

		const frequencyContent = freq?.split("");
		console.log("frequencyContent", frequencyContent);
		const frequencyValue = frequencyContent[0];

		const frequencyItem = frequencyTypes.find(
			(frequencyType) => frequencyType.value === frequencyContent[1],
		);

		return {
			frequencyValue: frequencyValue,
			frequencyItem: frequencyItem,
		};
	};

	const handleClose = () => {
		setIsOpen(false);
	};

	const formik = useFormik({
		initialValues: {
			name: "",
			description: "",
			bucket_id: 0,
			operation: eventTypes[0],
			trigger: {
				type: "timed",
				frequencyValue: 0,
				frequencyItem: frequencyTypes[0],
				next_trigger_date: new Date(),
			},
		},
	});

	const EventInputsMap = {
		ADD: <EventAddInputs formik={formik} />,
		SUB: <EventSubInputs formik={formik} />,
		MOVE: <EventMoveInputs formik={formik} buckets={buckets} />,
		MULT: <EventMultInputs formik={formik} />,
		CMV: <EventCmvInputs formik={formik} buckets={buckets} />,
	};

	React.useEffect(() => {
		const eventType = eventTypes.find(
			(eventType) => eventType.value === event.operation?.type,
		);

		console.log("VIEW EVENT DIALOG EVENT", event);
		formik.setFieldValue("name", event.name);
		formik.setFieldValue("description", event.name);
		formik.setFieldValue("bucket_id", event.name);
		formik.setFieldValue("operation", eventType);

		const frequency = convertFrequencyToType(event.trigger?.frequency);
		formik.setFieldValue("trigger", {
			type: "timed",
			frequencyValue: frequency.frequencyValue,
			frequencyItem: frequency.frequencyItem,
			next_trigger_date: event.trigger?.next_trigger_date,
		});
	}, [event]);

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
				<form onSubmit={formik.handleSubmit}>
					<DialogTitle
						as="h3"
						className="text-3xl font-bold text-white pb-3"
					>
						View Event
					</DialogTitle>
					<div
						id="add-event-input-content"
						className="flex flex-col gap-3 h-[700px] overflow-y-scroll"
					>
						<FieldLabel label="Owning Bucket">
							<Input
								id="bucket"
								name="bucket"
								className={clsx(
									"mt-2 w-full rounded-lg border-none bg-white/5 p-1.5 text-sm text-white opacity-50",
									"focus:not-data-focus:outline-none data-focus:outline-2 data-focus:-outline-offset-2 data-focus:outline-white/30",
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
									"mt-2 w-full rounded-lg border-none bg-white/5 p-1.5 text-sm text-white opacity-50",
									"focus:not-data-focus:outline-none data-focus:outline-2 data-focus:-outline-offset-2 data-focus:outline-white/30",
								)}
								onChange={formik.handleChange}
								value={formik.values.name}
							/>
						</FieldLabel>
						<FieldLabel
							required
							label="Description"
							desc="What is the purpose of this event"
						>
							<Textarea
								id="description"
								name="description"
								className={clsx(
									"mt-2 block w-full resize-none rounded-lg border-none bg-white/5 px-3 py-1.5 text-sm text-white opacity-50",
									"focus:not-data-focus:outline-none data-focus:outline-2 data-focus:-outline-offset-2 data-focus:outline-white/25",
								)}
								rows={3}
								value={formik.values.description}
							/>
						</FieldLabel>
						<FieldLabel required label="Event Type">
							<ListItems
								collection={eventTypes}
								formikItem={formik.values.operation}
								disabled
							/>
						</FieldLabel>
						{EventInputsMap[formik.values.operation?.value] || (
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
									className={clsx(
										"w-full rounded-lg border-none bg-white/5 p-1.5 text-sm text-white opacity-50",
										"focus:not-data-focus:outline-none data-focus:outline-2 data-focus:-outline-offset-2 data-focus:outline-white/30",
									)}
									disabled
									value={formik.values.trigger.frequencyValue}
								/>
								<div className="size-full">
									<ListItems
										disabled
										collection={frequencyTypes}
										formikItem={
											formik.values.trigger.frequencyItem
										}
									/>
								</div>
							</div>
						</FieldLabel>
						<FieldLabel required label="Next Date">
							<Input
								id="trigger_datetime"
								name="trigger_datetime"
								className={clsx(
									"mt-2 w-full rounded-lg border-none bg-white/5 p-1.5 text-sm text-white",
									"focus:not-data-focus:outline-none data-focus:outline-2 data-focus:-outline-offset-2 data-focus:outline-white/30",
								)}
								value={formik.values.trigger.next_trigger_date}
							/>
						</FieldLabel>
					</div>
					<div
						id="dialog-action-panel"
						className="flex flex-row-reverse h-1/10 w-full pt-3 gap-3"
					>
						<Button
							classColor="rounded-xl border-solid border-2 border-solid bg-spenny-accent-warning text-black hover:bg-spenny-background hover:text-spenny-accent-warning"
							label="Close Form"
							onClick={handleClose}
						/>
					</div>
				</form>
			</DialogPanel>
		</DialogBase>
	);
};

export default ViewEventDialog;
