import React from "react";
import Button from "../Button";
import Divider from "../Divider";
import Placeholder from "../Placeholder";
import axiosRequest from "../axiosRequest";
import { BACKEND_URL } from "../../configs/config";
import BucketLogCard from "./BucketLogCard";
import SkeletonCard from "../SkeletonCard";
import BucketEventCard from "./BucketEventCard";

const BucketCard = ({ bucket_id }) => {
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
			`${BACKEND_URL}/api/v1/bucket/${bucket_id}`
		);
		setBucket(data);
		if (data.events.length !== 0) {
			getNextEvent(data);
		}
	};

	const fetchRecentLogs = async () => {
		const data = await axiosRequest(
			"GET",
			`${BACKEND_URL}/api/v1/logs/${bucket_id}?skip=0&limit=3`
		);
		setRecentLogs(data.data);
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
					className="text-2xl font-semibold text-spenny-text w-4/8"
				>
					{bucket.name}
				</header>
				<Divider vertical />
				<div
					id="bucket-action"
					className="w-4/8 h-full flex flex-row gap-3"
				>
					<Button
						classColor="border-solid border-2 border-spenny-accent-primary bg-spenny-accent-primary text-black hover:bg-spenny-background hover:text-spenny-accent-primary"
						classStyle="w-1/2 text-xl h-full"
						label="View"
					/>
					<Button
						classColor="border-solid border-2 border-spenny-accent-warning bg-spenny-accent-warning text-black hover:bg-spenny-background hover:text-spenny-accent-warning"
						classStyle="w-1/2 text-xl h-full"
						label="Action"
					/>
				</div>
			</div>

			<Placeholder label="Graph" classStyle="h-8/16" />

			<div
				id="bucket-data-display"
				className="flex flex-row gap-3 w-full h-7/16"
			>
				<div className="w-1/2 flex flex-col gap-4">
					<Placeholder label="Amount" classStyle="w-full h-2/3" />
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
				</div>

				<Divider vertical />
				<div
					id="bucket-event-display"
					className="w-1/2 h-full flex flex-col gap-3"
				>
					<h1>Logs</h1>
					{recentLogs.length !== 0 ? (
						recentLogs.map((log, key) => {
							return <BucketLogCard log={log} />;
						})
					) : (
						<SkeletonCard label="No logs found" />
					)}
				</div>
			</div>
		</div>
	);
};

export default BucketCard;
