import { DialogPanel, DialogTitle } from "@headlessui/react";
import { useFormik } from "formik";
import DialogBase from "./DialogBase";

const AddEventDialog = () => {
	const eventTypes = [
		{ id: 0, name: "STORE", properties: {} },
		{ id: 1, name: "INVSB", properties: {} },
		{ id: 2, name: "GOALS", properties: { target_amount: 0 } },
		{ id: 0, name: "STORE", properties: {} },
		{ id: 1, name: "INVSB", properties: {} },
	];

	const [alertInfo, setAlertInfo] = React.useState(() => {});
	const handleClose = () => {};
	const handleSubmit = () => {};
	const AddEventValidationSchema = () => {};
	const formik = useFormik({
		initialValues: {
			name: "",
			description: "",
			trigger_datetime: "",
			frequency: "",
			event_type: "",
			properties: {},
			bucket_id: 0,
		},
		onSubmit: (values) => {
			handleSubmit(values);
		},
	});
	return (
		<DialogBase>
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
					Add Event
				</DialogTitle>
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
			</DialogPanel>
		</DialogBase>
	);
};

export default AddEventDialog;
