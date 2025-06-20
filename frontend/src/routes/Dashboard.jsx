import React from "react";
import Page from "../components/Page";
import Section from "../components/Section";
import Button from "../components/Button";
import Divider from "../components/Divider";
import Placeholder from "../components/Placeholder";
import BucketCard from "../components/Bucket/BucketCard";

const Dashboard = () => {
	return (
		<>
			<Page>
				<div
					id="dashboard-content"
					class="flex flex-col gap-6 h-full w-full"
				>
					<Section
						id="dasboard-card-header"
						classSize="h-1/8"
						classStyle="flex flex-row items-center w-full gap-5"
					>
						<h1 class="w-4/8 text-5xl">Dashboard</h1>
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
						<div class="flex flex-row gap-5 h-full min-w-max">
							<BucketCard name="Test" />
							<BucketCard name="Test" />
							<BucketCard name="Test" />
							<BucketCard name="Test" />
						</div>
					</Section>
				</div>
			</Page>
		</>
	);
};

export default Dashboard;
