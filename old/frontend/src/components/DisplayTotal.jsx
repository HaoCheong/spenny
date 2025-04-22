import React from "react";

const DisplayTotal = ({ buckets }) => {
	const calculateTotal = (buckets) => {
		if (buckets.length === 0) {
			return 0;
		}

		let total = 0;
		buckets.forEach((bucket) => {
			if (bucket.bucket_type !== "INVSB") {
				total = total + bucket.amount;
			}
		});
		return total;
	};

	const total = React.useMemo(() => {
		return calculateTotal(buckets);
	}, [buckets]);

	return (
		<div
			id="total-amount"
			className="rounded-xl p-3 flex flex-col justify-center items-center border-5 border-solid border-spenny-accent-primary text-white font-semibold text-xl w-2/8"
		>
			Total: ${total}
		</div>
	);
};

export default DisplayTotal;
