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

const EditBucketDialog = ({
	isOpen,
	setIsOpen,
	buckets,
	setBuckets,
	bucket,
}) => {
	const [alertInfo, setAlertInfo] = React.useState({
		isOpen: false,
		type: "",
		message: "",
	});

	const handleClose = () => {
		setIsOpen(false);
	};

	const handleSubmit = async (values) => {
		const edittedBucket = {
			name: values.name,
			description: values.description,
			amount: values.amount,
			bucket_type: values.bucket_type,
			properties: values.properties,
		};

		try {
			const data = await axiosRequest(
				"PATCH",
				`${BACKEND_URL}/bucket/${bucket.id}`,
				{
					data: edittedBucket,
				}
			);

			const updatedBuckets = buckets.filter((b) => b.id !== bucket.id);
			const newBuckets = [data, ...updatedBuckets];
			setBuckets(newBuckets);

			setAlertInfo({
				isOpen: true,
				type: "success",
				message: `${values.name} bucket edited successfully.`,
			});
		} catch (error) {
			setAlertInfo({
				isOpen: true,
				type: "error",
				message: `${error}`,
			});
		}
	};

	const bucketTypes = [
		{ id: 0, name: "STORE", properties: {} },
		{ id: 1, name: "INVSB", properties: {} },
		{ id: 2, name: "GOALS", properties: { target: 0 } },
	];

	const handleBucketTypeChange = (value) => {
		const bucketType = bucketTypes.find(
			(bucketType) => bucketType.id === value
		);

		formik.setFieldValue("bucket_type", bucketType.name);
		formik.setFieldValue("properties", bucketType.properties);
	};

	const EditBucketValidateSchema = Yup.object().shape({
		name: Yup.string().required("Bucket name is required"),
		description: Yup.string().required("A short description is required"),
		amount: Yup.number().required("Starting amount is required"),
	});

	const formik = useFormik({
		validateSchema: EditBucketValidateSchema,
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

	React.useEffect(() => {
		formik.setFieldValue("name", bucket.name);
		formik.setFieldValue("description", bucket.description);
		formik.setFieldValue("amount", bucket.amount);
		formik.setFieldValue("bucket_type", bucket.bucket_type);
		formik.setFieldValue("properties", bucket.properties);
	}, [bucket]);

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
					Edit Bucket
				</DialogTitle>

				<form onSubmit={formik.handleSubmit}>
					<div
						id="edit-modal-input-content"
						className="flex flex-col gap-3"
					>
						<FieldLabel
							label="Name"
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
							label="Starting Amount"
							error={formik.errors.amount !== ""}
							errorMsg={formik.errors.amount}
						>
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
						<FieldLabel label="Bucket Type">
							<div className="mt-3 w-full h-full">
								<ListItems
									startItem={formik.values.bucket_type}
									collection={bucketTypes}
									onChange={(value) =>
										handleBucketTypeChange(value)
									}
									formik={formik}
								/>
							</div>
						</FieldLabel>
						{formik.values.bucket_type === "GOALS" ? (
							<>
								<Divider />
								<FieldLabel
									label="Target Amount"
									desc="How much are you aiming for?"
								>
									<Input
										id="target_amount"
										name="target_amount"
										type="number"
										className={clsx(
											"mt-2 block w-full rounded-lg border-none bg-white/5 px-3 py-1.5 text-sm text-white",
											"focus:not-data-focus:outline-none data-focus:outline-2 data-focus:-outline-offset-2 data-focus:outline-white/30"
										)}
										onChange={(e) => {
											formik.setFieldValue("properties", {
												target: parseInt(
													e.target.value
												),
											});
										}}
										value={
											formik.values.properties.target ?? 0
										}
									/>
								</FieldLabel>
							</>
						) : (
							<></>
						)}
						<ResponseAlert alertInfo={alertInfo} />
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
								label="Edit Bucket"
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

export default EditBucketDialog;
