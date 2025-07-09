import React from "react";
import { BACKEND_URL } from "../../configs/config";
import Button from "../Button";
import Divider from "../Divider";
import SkeletonCard from "../SkeletonCard";
import Placeholder from "../Structural/Placeholder";
import axiosRequest from "../axiosRequest";
import ActionMenu from "./ActionMenu";
import BucketAmountDisplay from "./BucketAmountDisplay";
import BucketEventCard from "./BucketEventCard";
import BucketLogCard from "./BucketLogCard";

const BucketCard = ({
	bucket_id,
	setFocusBucket,
	setIsAddEventOpen,
	setIsViewBucketOpen,
	setIsEditBucketOpen,
	setIsDeleteBucketOpen,
}) => {
	const [bucket, setBucket] = React.useState({});
	const [nextEvent, setNextEvent] = React.useState(null);
	const [recentLogs, setRecentLogs] = React.useState([]);

	const getNextEvent = (bucket) => {
		const sortedEvents = bucket.events.sort((event_1, event_2) => {
			return (
				new Date(event_2.trigger_datetime) -
				new Date(event_1.trigger_datetime)
			);
		});

		return setNextEvent(sortedEvents[0]);
	};

	const fetchBucket = async () => {
		const data = await axiosRequest(
			"GET",
			`${BACKEND_URL}/bucket/${bucket_id}`
		);
		setBucket(data);
		if (data.events.length !== 0) {
			getNextEvent(data);
		}
	};

	const fetchRecentLogs = async () => {
		const data = await axiosRequest(
			"GET",
			`${BACKEND_URL}/logs/${bucket_id}?skip=0&limit=3`
		);
		setRecentLogs(data.data);
	};

	const handleAddEvent = () => {
		setFocusBucket(bucket);
		setIsAddEventOpen(true);
	};

	const handleViewBucket = () => {
		setFocusBucket(bucket);
		setIsViewBucketOpen(true);
	};

	const handleEditBucket = () => {
		setFocusBucket(bucket);
		setIsEditBucketOpen(true);
	};

	const handleDeleteBucket = () => {
		setFocusBucket(bucket);
		setIsDeleteBucketOpen(true);
	};

	React.useEffect(() => {
		fetchBucket();
		fetchRecentLogs();
	}, []);

	return (
		<div
			id="bucket-card"
			className="flex flex-col gap-3 h-full min-w-[500px] max-w-[700px] rounded-lg p-6 shadow-2xl shadow-spenny-secondary border-2 border-solid border-spenny-secondary"
		>
			<div id="bucket-header" className="h-1/16 flex flex-row gap-3">
				<header
					id="bucket-title"
					className="text-2xl font-semibold text-spenny-text w-3/4"
				>
					{bucket.name}
				</header>
				<Divider vertical />
				<div
					id="bucket-action"
					className="w-1/4 h-full flex flex-row gap-3"
				>
					<ActionMenu
						handleAddEvent={handleAddEvent}
						handleEditBucket={handleEditBucket}
						handleDeleteBucket={handleDeleteBucket}
					/>
				</div>
			</div>

			<Placeholder label="Graph" classStyle="h-7/16" />

			<div
				id="bucket-data-display"
				className="flex flex-row gap-3 w-full h-8/16"
			>
				<div className="w-1/2 flex flex-col gap-3">
					<h1>Amount</h1>
					<BucketAmountDisplay bucket={bucket} />
					<Divider />
					<h1>Upcoming Events</h1>
					{nextEvent === null ? (
						<SkeletonCard
							classStyle="w-full h-1/3"
							label="No Upcoming Events"
						/>
					) : (
						<BucketEventCard event={nextEvent} />
					)}
					<Divider />
					<div
						id="bucket-data-action"
						className="flex flex-row gap-3 h-1/3"
					>
						<Button
							classColor="border-solid border-2 border-spenny-accent-primary bg-spenny-accent-primary text-black hover:bg-spenny-background hover:text-spenny-accent-primary"
							classStyle="w-1/2 text-xl h-full"
							label="View"
							onClick={handleViewBucket}
						/>
						<Button
							classColor="border-solid border-2 border-spenny-accent-warning bg-spenny-accent-warning text-black hover:bg-spenny-background hover:text-spenny-accent-warning"
							classStyle="w-1/2 text-xl h-full"
							label="Entry"
						/>
					</div>
				</div>

				<Divider vertical />
				<div
					id="bucket-event-display"
					className="w-1/2 h-full flex flex-col gap-3"
				>
					<h1>Logs</h1>
					<div
						id="bucket-event-container"
						className="flex flex-col gap-3 h-full"
					>
						{recentLogs.length !== 0 ? (
							recentLogs.map((log, key) => {
								return <BucketLogCard key={key} log={log} />;
							})
						) : (
							<SkeletonCard label="No logs found" />
						)}
					</div>
				</div>
			</div>
		</div>
	);
};

export default BucketCard;
