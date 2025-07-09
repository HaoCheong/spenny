import React from "react";
import BucketCard from "../components/Bucket/BucketCard";
import Button from "../components/Button";
import AddBucketDialog from "../components/Dialog/AddBucketDialog";
import EditBucketDialog from "../components/Dialog/EditBucketDialog";
import ViewBucketDialog from "../components/Dialog/ViewBucketDialog";
import DisplayTotal from "../components/DisplayTotal";
import Divider from "../components/Divider";
import Page from "../components/Structural/Page";
import Section from "../components/Structural/Section";
import axiosRequest from "../components/axiosRequest";
import { BACKEND_URL } from "../configs/config";
import DeleteBucketDialog from "../components/Dialog/DeleteBucketDialog";

const Dashboard = () => {
	const [buckets, setBuckets] = React.useState([]);
	const [isAddBucketOpen, setIsAddBucketOpen] = React.useState(false);

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
										setFocusBucket={setFocusBucket}
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
