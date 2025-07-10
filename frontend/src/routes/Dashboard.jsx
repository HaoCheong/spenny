import React from "react";
import BucketCard from "../components/Bucket/BucketCard";
import AddBucketDialog from "../components/Dialog/Bucket/AddBucketDialog";
import DeleteBucketDialog from "../components/Dialog/Bucket/DeleteBucketDialog";
import EditBucketDialog from "../components/Dialog/Bucket/EditBucketDialog";
import ViewBucketDialog from "../components/Dialog/Bucket/ViewBucketDialog";
import AddEventDialog from "../components/Dialog/Event/AddEventDialog";
import DisplayTotal from "../components/DisplayTotal";
import Divider from "../components/Divider";
import Button from "../components/Input/Button";
import Page from "../components/Structural/Page";
import Section from "../components/Structural/Section";
import axiosRequest from "../components/axiosRequest";
import { BACKEND_URL } from "../configs/config";

const Dashboard = () => {
	const [buckets, setBuckets] = React.useState([]);
	const [isAddBucketOpen, setIsAddBucketOpen] = React.useState(false);

	const [isAddEventOpen, setIsAddEventOpen] = React.useState(false);
	const [isViewBucketOpen, setIsViewBucketOpen] = React.useState(false);
	const [isEditBucketOpen, setIsEditBucketOpen] = React.useState(false);
	const [isDeleteBucketOpen, setIsDeleteBucketOpen] = React.useState(false);

	const [focusBucket, setFocusBucket] = React.useState({});

	const fetchBuckets = async () => {
		const data = await axiosRequest("GET", `${BACKEND_URL}/buckets`);
		setBuckets(data.data);
	};

	const handleAddBucketOpen = () => {
		setIsAddBucketOpen(true);
	};

	React.useEffect(() => {
		fetchBuckets();
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
						buckets={buckets}
						setBuckets={setBuckets}
					/>
					<ViewBucketDialog
						isOpen={isViewBucketOpen}
						setIsOpen={setIsViewBucketOpen}
						bucket={focusBucket}
					/>
					<EditBucketDialog
						isOpen={isEditBucketOpen}
						setIsOpen={setIsEditBucketOpen}
						buckets={buckets}
						setBuckets={setBuckets}
						bucket={focusBucket}
					/>
					<DeleteBucketDialog
						isOpen={isDeleteBucketOpen}
						setIsOpen={setIsDeleteBucketOpen}
						buckets={buckets}
						setBuckets={setBuckets}
						bucket={focusBucket}
					/>
					<AddEventDialog
						isOpen={isAddEventOpen}
						setIsOpen={setIsAddEventOpen}
						bucket={focusBucket}
						buckets={buckets}
					/>
					<Section
						id="dasboard-card-header"
						classSize="h-1/8"
						classStyle="flex flex-row items-center w-full gap-5"
					>
						<h1 className="w-5/8 text-5xl">Dashboard</h1>
						<Divider vertical />
						<DisplayTotal buckets={buckets} />
						<Divider vertical />
						<Button
							classStyle="w-1/8 text-xl"
							classColor="rounded-xl border-solid border-2 border-solid bg-spenny-accent-primary text-black hover:bg-spenny-background hover:text-spenny-accent-primary"
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
										setFocusBucket={setFocusBucket}
										setIsAddEventOpen={setIsAddEventOpen}
										setIsViewBucketOpen={
											setIsViewBucketOpen
										}
										setIsEditBucketOpen={
											setIsEditBucketOpen
										}
										setIsDeleteBucketOpen={
											setIsDeleteBucketOpen
										}
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
