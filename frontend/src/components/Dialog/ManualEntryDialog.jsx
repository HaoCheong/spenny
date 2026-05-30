import { DialogPanel, DialogTitle, Input, Textarea } from "@headlessui/react";
import clsx from "clsx";
import { FormikConsumer, useFormik } from "formik";
import React from "react";
import * as Yup from "yup";
import { BACKEND_URL } from "../../configs/config";
import axiosRequest from "../axiosRequest";
import Divider from "../Divider";
import FieldLabel from "../FieldLabel";
import Button from "../Input/Button";
import ListItems from "../Input/ListItems";
import ResponseAlert from "../ResponseAlert";
import EventAddInputs from "./Event/Input/EventAddInputs";
import EventCmvInputs from "./Event/Input/EventCmvInputs";
import EventMoveInputs from "./Event/Input/EventMoveInputs";
import EventMultInputs from "./Event/Input/EventMultInputs";
import EventSubInputs from "./Event/Input/EventSubInputs";
import DialogBase from "./DialogBase";

const ManualEntryDialog = ({ isOpen, setIsOpen, bucket, buckets }) => {
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

	const [alertInfo, setAlertInfo] = React.useState({
		isOpen: false,
		type: "",
		message: "",
	});
	const handleClose = () => {
		setIsOpen(false);
	};

	const handleEventTypeChange = (value) => {
		const eventType = eventTypes.find(
			(eventType) => eventType.id === value,
		);

		formik.setFieldValue("operation", eventType);
	};

	// TODO: Can be converted into a class for each operation instead of ham fisting code with ifs
	const operationSchema = (operation) => {
		switch (operation.value) {
			case "ADD":
				return {
					type: operation.value,
					amount: operation.amount,
				};
			case "SUB":
				return {
					type: operation.value,
					amount: operation.amount,
				};
				break;
			case "MOVE":
				return {
					to_bucket_id: operation.to_bucket.id,
					type: operation.value,
					amount: operation.amount,
				};
				break;
			case "MULT":
				return {
					type: operation.value,
					percentage: operation.amount,
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
			},
			operation: operationSchema(values.operation),
		};
	};

	const handleSubmit = async (values) => {
		const newEntry = valuesToSchema(formik.values);

		console.log("NEW ENTRY", newEntry);

		try {
			const data = await axiosRequest("POST", `${BACKEND_URL}/trigger`, {
				data: newEntry,
			});

			setAlertInfo({
				isOpen: true,
				type: "success",
				message: `${newEntry.name} entry processed successfully.`,
			});
		} catch (error) {
			setAlertInfo({
				isOpen: true,
				type: "error",
				message: `${error}`,
			});
		}
	};

	const ManualEntryValidationSchema = Yup.object().shape({
		name: Yup.string().required("Event name is required"),
		description: Yup.string().required("Event description is required"),
	});

	const formik = useFormik({
		validationSchema: ManualEntryValidationSchema,
		initialValues: {
			name: "",
			description: "",
			bucket_id: 0,
			operation: eventTypes[0],
			trigger: {
				type: "manual",
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
						Manual Entry
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
								disableda
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
						{EventInputsMap[formik.values.operation.value] || <></>}
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
							label="Submit Entry"
							type="submit"
							onClick={() => {}}
						/>
					</div>
				</form>
			</DialogPanel>
		</DialogBase>
	);
};

export default ManualEntryDialog;
