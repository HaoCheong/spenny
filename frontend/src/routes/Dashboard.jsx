import React from "react";
import AddBucketDialog from "../components/AddBucketDialog";
import BucketCard from "../components/Bucket/BucketCard";
import Button from "../components/Button";
import Divider from "../components/Divider";
import Page from "../components/Structural/Page";
import Placeholder from "../components/Structural/Placeholder";
import Section from "../components/Structural/Section";
import axiosRequest from "../components/axiosRequest";
import { BACKEND_URL } from "../configs/config";

const Dashboard = () => {
	const [buckets, setBuckets] = React.useState([]);
	const [isAddBucketOpen, setIsAddBucketOpen] = React.useState(false);

	const fetchBucket = async () => {
		const data = await axiosRequest("GET", `${BACKEND_URL}/api/v1/buckets`);
		setBuckets(data.data);
	};

	const handleAddBucketOpen = () => {
		setIsAddBucketOpen(true);
	};

	React.useEffect(() => {
		fetchBucket();
	}, []);

	return (
		<>
			<Page>
				<div
					id="dashboard-content"
					className="flex flex-col gap-6 h-full w-full"
				>
					<AddBucketDialog
						isOpen={isAddBucketOpen}
						setIsOpen={setIsAddBucketOpen}
					/>
					<Section
						id="dasboard-card-header"
						classSize="h-1/8"
						classStyle="flex flex-row items-center w-full gap-5"
					>
						<h1 className="w-5/8 text-5xl">Dashboard</h1>
						<Divider vertical />
						<Placeholder
							label="TOTAL"
							classStyle="w-2/8 h-full text-xl"
						/>
						<Divider vertical />
						<Button
							classStyle="w-1/8 text-xl"
							classColor="border-solid border-2 border-solid bg-spenny-accent-primary text-black hover:bg-spenny-background hover:text-spenny-accent-primary"
							label="Add Bucket"
							onClick={handleAddBucketOpen}
						/>
					</Section>
					<Section
						id="dasboard-card-display"
						classSize="h-7/8 overflow-x-scroll"
					>
						<div className="flex flex-row gap-5 h-full min-w-max">
							{buckets.map((bucket, key) => {
								return (
									<BucketCard
										key={key}
										bucket_id={bucket.id}
									/>
								);
							})}
						</div>
					</Section>
				</div>
			</Page>
		</>
	);
};

export default Dashboard;
