import React from "react";
import Page from "../components/Page";
import Section from "../components/Section";
import Button from "../components/Button";
import Divider from "../components/Divider";
import Placeholder from "../components/Placeholder";
import BucketCard from "../components/Bucket/BucketCard";
import axiosRequest from "../components/axiosRequest";
import { BACKEND_URL } from "../configs/config";

const Dashboard = () => {
	const [buckets, setBuckets] = React.useState([]);

	const fetchBucket = async () => {
		const data = await axiosRequest("GET", `${BACKEND_URL}/api/v1/buckets`);
		setBuckets(data.data);
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
					<Section
						id="dasboard-card-header"
						classSize="h-1/8"
						classStyle="flex flex-row items-center w-full gap-5"
					>
						<h1 className="w-4/8 text-5xl">Dashboard</h1>
						<Divider vertical />
						<Placeholder
							label="TOTAL"
							classStyle="w-2/8 h-full text-xl"
						/>
						<Divider vertical />
						<Button classStyle="w-1/8 text-xl" label="Add Bucket" />
						<Button classStyle="w-1/8 text-xl" label="Manual" />
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
