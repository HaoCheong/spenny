import { Input } from "@headlessui/react";
import clsx from "clsx";
import FieldLabel from "../../../FieldLabel";

const EventMultInputs = ({ formik }) => {
	return (
		<FieldLabel label="Amount to Multiply (%)">
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
	);
};

export default EventMultInputs;
