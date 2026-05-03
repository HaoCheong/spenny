import FieldLabel from "../../../FieldLabel";
import ListItems from "../../../Input/ListItems";

const EventCmvInputs = ({ formik, buckets }) => {
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
		<FieldLabel
			label="To Bucket"
			desc="Which bucket are we transferring to"
		>
			<ListItems
				collection={buckets}
				onChange={(bucket) => {
					handleBucketChange(bucket);
				}}
				formikItem={formik.values.operation.to_bucket}
			/>
		</FieldLabel>
	);
};

export default EventCmvInputs;
