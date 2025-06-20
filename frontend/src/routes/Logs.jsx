import React from "react";
import Page from "../components/Page";
import Section from "../components/Section";
import Button from "../components/Button";
import Divider from "../components/Divider";
import Placeholder from "../components/Placeholder";

const Logs = () => {
	return (
		<>
			<Page>
				<div id="log-content" class="flex flex-col gap-3 h-full w-full">
					<Section
						classSize="h-1/8"
						classStyle="flex flex-row items-center w-full gap-5"
					>
						<h1 class="w-7/8 text-5xl items-center">Logs</h1>
						<Divider vertical={true} />
						<Button classStyle="w-1/8" label="Export" />
					</Section>
					<Section
						classSize="h-1/8"
						classStyle="flex flex-row items-center w-full gap-5"
					>
						<Placeholder classStyle="w-1/3" />
						<Divider vertical />
						<Placeholder classStyle="w-1/3" />
						<Divider vertical />
						<Placeholder classStyle="w-1/3" />
					</Section>
					<Section classSize="h-6/8">Log</Section>
				</div>
			</Page>
		</>
	);
};

export default Logs;
