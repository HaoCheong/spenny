import { Input } from "@headlessui/react";
import clsx from "clsx";
import FieldLabel from "../../../FieldLabel";

const EventAddInputs = ({ formik }) => {
	return (
		<FieldLabel label="Amount to Add">
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
						amount: parseInt(e.target.value),
					});
				}}
				value={formik.values.properties.amount ?? 0}
			/>
		</FieldLabel>
	);
};

export default EventAddInputs;
