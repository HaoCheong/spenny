const StoreBucketDisplay = ({ bucket }) => {
	return (
		<div
			id="bucket-data-store-amount"
			className="w-full h-1/3 flex justify-center items-center border-solid border-5 border-spenny-accent-primary rounded-xl"
		>
			<h1 className="text-4xl te-spenny-accent-primary">
				${bucket.amount}
			</h1>
		</div>
	);
};

const InvisibleBucketDisplay = ({ bucket }) => {
	return (
		<div
			id="bucket-data-amount"
			className="w-full h-1/3 flex justify-center items-center border-solid border-5 border-[#7d20ab] rounded-xl"
		>
			<h1 className="text-4xl te-spenny-accent-primary">
				${bucket.amount}
			</h1>
		</div>
	);
};

const GoalsBucketDisplay = ({ bucket }) => {
	return (
		<div
			id="bucket-data-amount"
			className="w-full h-1/3 flex justify-center items-center border-solid border-5 border-[#219646] rounded-xl"
		>
			<h1 className="text-4xl te-spenny-accent-primary">
				${bucket.amount}/{bucket.properties.target ?? 0}
			</h1>
		</div>
	);
};

const BucketAmountDisplay = ({ bucket }) => {
	return (
		<>
			{bucket.bucket_type === "STORE" ? (
				<StoreBucketDisplay bucket={bucket} />
			) : (
				<></>
			)}
			{bucket.bucket_type === "INVSB" ? (
				<InvisibleBucketDisplay bucket={bucket} />
			) : (
				<></>
			)}
			{bucket.bucket_type === "GOALS" ? (
				<GoalsBucketDisplay bucket={bucket} />
			) : (
				<></>
			)}
		</>
	);
};

export default BucketAmountDisplay;
