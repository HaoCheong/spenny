import Button from "../components/Button";
import Divider from "../components/Divider";
import Page from "../components/Structural/Page";
import Placeholder from "../components/Structural/Placeholder";
import Section from "../components/Structural/Section";
import TableRow from "../components/TableRow";

const Logs = () => {
	return (
		<>
			<Page>
				<div
					id="log-content"
					className="flex flex-col gap-6 h-full w-full"
				>
					<Section
						classSize="h-1/8"
						classStyle="flex flex-row items-center w-full gap-5"
					>
						<h1 className="w-7/8 text-5xl items-center">Logs</h1>
						<Divider vertical={true} />
						<Button classStyle="w-1/8 text-xl" label="Export" />
					</Section>
					<Section
						classSize="h-1/8"
						classStyle="flex flex-row items-center w-full gap-5"
					>
						<Placeholder
							classStyle="w-1/3 h-full"
							label="Datetime"
						/>
						<Divider vertical />
						<Placeholder
							classStyle="w-1/3 h-full"
							label="Bucket Drop Down"
						/>
						<Divider vertical />
						<Placeholder classStyle="w-1/3 h-full" label="Search" />
					</Section>
					<Section
						classSize="h-6/8 w-full"
						classStyle="text-xl overflow-y-scroll"
					>
						<div className="w-full h-full flex flex-col gap-3 overflow-y-scroll">
							<div className="flex flex-row gap-3 w-full h-1/12">
								<p className="flex items-center text-2xl font-bold w-1/16 h-[60px] ">
									ID
								</p>
								<Divider vertical />
								<p className="flex items-center text-2xl font-bold w-2/16 h-[60px] ">
									Type
								</p>
								<Divider vertical />
								<p className="flex items-center text-2xl font-bold w-2/16 h-[60px] ">
									Name
								</p>
								<Divider vertical />
								<p className="flex items-center text-2xl font-bold w-7/16 h-[60px] ">
									Description
								</p>
								<Divider vertical />
								<p className="flex items-center text-2xl font-bold w-2/16 h-[60px] ">
									Created
								</p>
								<Divider vertical />
								<p className="flex items-center text-2xl font-bold w-2/16 h-[60px] ">
									View
								</p>
							</div>
							<Divider />
							<TableRow />
							<TableRow />
							<TableRow />
							<TableRow />
							<TableRow />
							<TableRow />
							<TableRow />
							<TableRow />
							<TableRow />
							<TableRow />
							<TableRow />
							<TableRow />
						</div>
					</Section>
				</div>
			</Page>
		</>
	);
};

export default Logs;
