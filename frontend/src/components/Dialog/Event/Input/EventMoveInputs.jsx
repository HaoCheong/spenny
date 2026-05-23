import { Input } from "@headlessui/react";
import clsx from "clsx";
import FieldLabel from "../../../FieldLabel";
import ListItems from "../../../Input/ListItems";

const EventMoveInputs = ({ disabled = false, formik, buckets }) => {
	const handleBucketChange = (value) => {
		const bucket = buckets.find((buckets) => buckets.id === value);

		formik.setFieldValue("operation", {
			id: formik.values.operation.id,
			value: formik.values.operation.value,
			name: formik.values.operation.name,
			to_bucket: bucket,
			amount: formik.values.operation.amount,
		});
	};
	return (
		<>
			<FieldLabel label="Amount to Transfer">
				<Input
					required
					id="amount"
					name="amount"
					className={clsx(
						"mt-2 w-full rounded-lg border-none bg-white/5 p-1.5 text-sm text-white",
						"focus:not-data-focus:outline-none data-focus:outline-2 data-focus:-outline-offset-2 data-focus:outline-white/30",
					)}
					onChange={(e) => {
						formik.setFieldValue("operation", {
							id: formik.values.operation.id,
							value: formik.values.operation.value,
							name: formik.values.operation.name,
							to_bucket: formik.values.operation.to_bucket,
							amount: parseInt(e.target.value),
						});
					}}
					value={formik.values.operation.amount ?? 0}
				/>
			</FieldLabel>
			<FieldLabel
				label="To Bucket"
				desc="Which bucket are we transferring to"
			>
				<ListItems
					disabled={disabled}
					collection={buckets}
					onChange={(bucket) => {
						handleBucketChange(bucket);
					}}
					formikItem={formik.values.operation.to_bucket}
				/>
			</FieldLabel>
		</>
	);
};

export default EventMoveInputs;
