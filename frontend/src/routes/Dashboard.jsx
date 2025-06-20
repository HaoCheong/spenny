import React from "react";
import Page from "../components/Page";
import Section from "../components/Section";
import Button from "../components/Button";

const Dashboard = () => {
	return (
		<>
			<Page>
				<div
					id="dashboard-content"
					class="flex flex-col gap-3 h-full w-full"
				>
					<Section
						classSize="h-1/8"
						classStyle="flex flex-row items-center w-full gap-5"
					>
						<h1 class="w-5/8 text-5xl items-center">Dashboard</h1>
						<Button classStyle="w-3/16" label="Add Bucket" />
						<Button classStyle="w-3/16" label="Manual Trigger" />
					</Section>
					<Section classSize="h-7/8"></Section>
				</div>
			</Page>
		</>
	);
};

export default Dashboard;
