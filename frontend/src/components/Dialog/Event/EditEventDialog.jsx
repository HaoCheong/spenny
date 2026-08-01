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
import { dollarsToCents } from "../../../helpers/displayConverter";

const EditEventDialog = ({ isOpen, setIsOpen, bucket, buckets, event }) => {
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
			(frequencyType) => frequencyType.id === value,
		);

		formik.setFieldValue("trigger", {
			type: "timed",
			frequencyValue: formik.values.trigger.frequencyValue,
			frequencyItem: frequencyType,
			next_trigger_date: formik.values.trigger.next_trigger_date,
		});
	};

	const handleFrequencyValueChange = (value) => {
		formik.setFieldValue("trigger", {
			type: formik.values.trigger.type,
			frequencyValue: parseInt(value),
			frequencyItem: formik.values.trigger.frequencyItem,
			next_trigger_date: formik.values.trigger.next_trigger_date,
		});
	};

	const handleEventTypeChange = (value) => {
		const eventType = eventTypes.find(
			(eventType) => eventType.id === value,
		);

		formik.setFieldValue("operation", eventType);
	};

	const handleDateChange = (value) => {
		formik.setFieldValue("trigger", {
			type: formik.values.trigger.type,
			frequencyValue: formik.values.trigger.frequencyValue,
			frequencyItem: formik.values.trigger.frequencyItem,
			next_trigger_date: value,
		});
	};

	// TODO: Can be converted into a class for each operation instead of ham fisting code with ifs
	const operationSchema = (operation) => {
		switch (operation.value) {
			case "ADD":
				return {
					type: operation.value,
					amount: dollarsToCents(parseFloat(operation.amount)),
				};
			case "SUB":
				return {
					type: operation.value,
					amount: dollarsToCents(parseFloat(operation.amount)),
				};
				break;
			case "MOVE":
				return {
					to_bucket_id: operation.to_bucket.id,
					type: operation.value,
					amount: dollarsToCents(parseFloat(operation.amount)),
				};
				break;
			case "MULT":
				return {
					type: operation.value,
					percentage: operation.percentage,
				};
				break;
			case "CMV":
				return {
					type: operation.value,
					to_bucket_id: operation.to_bucket.id,
				};
			default:
				throw new Error(`Type ${operation.value} does not exist`);
		}
	};

	const valuesToSchema = (values) => {
		return {
			name: values.name,
			description: values.description,
			bucket_id: bucket.id,
			trigger: {
				type: values.trigger.type,
				frequency: `${values.trigger.frequencyValue}${values.trigger.frequencyItem.value}`,
				next_trigger_date: new Date(values.trigger.next_trigger_date),
			},
			operation: operationSchema(values.operation),
		};
	};

	const handleSubmit = async (values) => {
		const newEvent = valuesToSchema(formik.values);

		try {
			const data = await axiosRequest(
				"PATCH",
				`${BACKEND_URL}/event/${bucket.id}`,
				{
					data: newEvent,
				},
			);

			setAlertInfo({
				isOpen: true,
				type: "success",
				message: `${newEvent.name} event editted successfully.`,
			});
		} catch (error) {
			setAlertInfo({
				isOpen: true,
				type: "error",
				message: `${error}`,
			});
		}
	};

	const EditEventValidationSchema = Yup.object().shape({
		name: Yup.string().required("Event name is required"),
		description: Yup.string().required("Event description is required"),
		operation: Yup.object().shape({
			value: Yup.string(),
			amount: Yup.number()
				// treat empty field as "missing" so .required fires instead of a cast error
				.transform((val, orig) => (orig === "" ? undefined : val))
				.when("value", {
					is: (v) => ["ADD", "SUB", "MOVE"].includes(v),
					then: (s) =>
						s
							.typeError("Amount must be a number")
							.positive("Amount must be greater than 0")
							.required("Amount is required"),
					otherwise: (s) => s.notRequired(),
				}),
			percentage: Yup.number()
				.transform((val, orig) => (orig === "" ? undefined : val))
				.when("value", {
					is: "MULT",
					then: (s) =>
						s
							.typeError("Percentage must be a number")
							.required("Percentage is required"),
					otherwise: (s) => s.notRequired(),
				}),
		}),
	});

	const formik = useFormik({
		validationSchema: EditEventValidationSchema,
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

	React.useEffect(() => {
		const eventType = eventTypes.find(
			(eventType) => eventType.value === event.operation?.type,
		);

		// PFIX: Terrible, do better
		if (!eventType) {
			return;
		}

		// PFIX: I feel like we should be populate on render
		// PFIX: Terrible conditional
		// PFIX: Currently showing in cent form. Need to update the input to use dollar. Automatically add the decimal point?
		if (eventType.value === "MULT") {
			eventType.amount = event.operation?.percentage;
		} else {
			eventType.amount = event.operation?.amount;
		}

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
						Edit Event
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
									"mt-2 w-full rounded-lg border-none bg-white/5 p-1.5 text-sm text-white",
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
							error={formik.errors.description !== ""}
							errorMsg={formik.errors.description}
						>
							<Textarea
								id="description"
								name="description"
								className={clsx(
									"mt-2 block w-full resize-none rounded-lg border-none bg-white/5 px-3 py-1.5 text-sm text-white",
									"focus:not-data-focus:outline-none data-focus:outline-2 data-focus:-outline-offset-2 data-focus:outline-white/25",
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
						>
							<ListItems
								collection={eventTypes}
								onChange={(value) => {
									handleEventTypeChange(value);
								}}
								formikItem={formik.values.operation}
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
									type="number"
									className={clsx(
										"w-full rounded-lg border-none bg-white/5 p-1.5 text-sm text-white",
										"focus:not-data-focus:outline-none data-focus:outline-2 data-focus:-outline-offset-2 data-focus:outline-white/30",
									)}
									onChange={(e) =>
										handleFrequencyValueChange(
											e.target.value,
										)
									}
									value={formik.values.trigger.frequencyValue}
								/>
								<div className="size-full">
									<ListItems
										collection={frequencyTypes}
										onChange={(value) =>
											handleFrequencyTypeChange(value)
										}
										formikItem={
											formik.values.trigger.frequencyItem
										}
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
									"focus:not-data-focus:outline-none data-focus:outline-2 data-focus:-outline-offset-2 data-focus:outline-white/30",
								)}
								onChange={(e) =>
									handleDateChange(e.target.value)
								}
								value={formik.values.trigger.next_trigger_date}
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
							label="Close"
							onClick={handleClose}
						/>
						<Button
							classColor="rounded-xl border-solid border-2 border-solid bg-spenny-accent-primary text-black hover:bg-spenny-background hover:text-spenny-accent-primary"
							label="Edit Event"
							type="submit"
							onClick={() => {}}
						/>
					</div>
				</form>
			</DialogPanel>
		</DialogBase>
	);
};

export default EditEventDialog;
