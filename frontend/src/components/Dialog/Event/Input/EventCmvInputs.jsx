import FieldLabel from "../../../FieldLabel";
import ListItems from "../../../Input/ListItems";

const EventCmvInputs = ({ formik, buckets }) => {
	return (
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
					});
				}}
				formik={formik}
			/>
		</FieldLabel>
	);
};

export default EventCmvInputs;
