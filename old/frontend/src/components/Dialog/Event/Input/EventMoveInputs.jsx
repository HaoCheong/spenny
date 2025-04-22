import { Input } from "@headlessui/react";
import clsx from "clsx";
import FieldLabel from "../../../FieldLabel";
import ListItems from "../../../Input/ListItems";

const EventMoveInputs = ({ formik, buckets }) => {
	return (
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
							to_bucket: formik.values.properties.to_bucket,
							amount: parseInt(e.target.value),
						});
					}}
					value={formik.values.properties.amount ?? 0}
				/>
			</FieldLabel>
			<FieldLabel
				label="To Bucket"
				desc="Which bucket are we transferring to"
			>
				<ListItems
					startItem={buckets[0]}
					collection={buckets}
					onChange={(bucket) => {
						formik.setFieldValue("properties", {
							to_bucket: bucket,
							amount: formik.values.properties.amount,
						});
					}}
					formik={formik}
				/>
			</FieldLabel>
		</>
	);
};

export default EventMoveInputs;
