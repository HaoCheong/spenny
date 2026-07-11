import { Input } from "@headlessui/react";
import clsx from "clsx";
import FieldLabel from "../../../FieldLabel";

const EventAddInputs = ({ formik }) => {
	return (
		<FieldLabel
			label="Amount to Add"
			error={!!formik.errors.operation?.amount}
			errorMsg={formik.errors.operation?.amount}
		>
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
						amount: e.target.value,
					});
				}}
				value={formik.values.operation?.amount ?? ""}
			/>
		</FieldLabel>
	);
};

export default EventAddInputs;
