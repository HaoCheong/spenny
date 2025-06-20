import Button from "../Button";
import Divider from "../Divider";
import Placeholder from "../Placeholder";

const BucketCard = ({ name }) => {
	return (
		<div
			id="bucket-card"
			class="flex flex-col gap-3 h-full min-w-[500px] max-w-[700px] rounded-lg p-6 border-5 border-solid border-green-500"
		>
			<div id="bucket-header" class="h-1/16 flex flex-row gap-3">
				<header id="bucket-title" class="text-5xl text-white w-4/8">
					{name}
				</header>
				<Divider vertical />
				<div
					id="bucket-action"
					class="w-4/8 h-full flex flex-row gap-3"
				>
					<Button classStyle="w-1/2 text-xl h-full" label="View" />
					<Button classStyle="w-1/2 text-xl h-full" label="Action" />
				</div>
			</div>

			<Placeholder label="Graph" classStyle="h-8/16" />

			<div
				id="bucket-data-display"
				class="flex flex-row gap-3 w-full h-7/16"
			>
				<Placeholder label="Amount" classStyle="w-1/2 h-full" />
				<Divider vertical />
				<div
					id="bucket-event-display"
					class="w-1/2 h-full flex flex-col gap-3"
				>
					<Placeholder label="Next Event" classStyle="w-full h-1/4" />
					<Divider />
					<Placeholder
						label="Recent Event 1"
						classStyle="w-full h-1/4"
					/>
					<Placeholder
						label="Recent Event 2"
						classStyle="w-full h-1/4"
					/>
					<Placeholder
						label="Recent Event 3"
						classStyle="w-full h-1/4"
					/>
				</div>
			</div>
		</div>
	);
};

export default BucketCard;
