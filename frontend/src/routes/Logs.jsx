import {
	Input,
	Listbox,
	ListboxButton,
	ListboxOption,
	ListboxOptions,
} from "@headlessui/react";
import clsx from "clsx";
import React from "react";
import Divider from "../components/Divider";
import Button from "../components/Input/Button";
import LogRow from "../components/LogRow";
import Page from "../components/Structural/Page";
import Section from "../components/Structural/Section";
import axiosRequest from "../components/axiosRequest";
import { BACKEND_URL } from "../configs/config";

const Logs = () => {
	const [paginationModel, setPaginationModel] = React.useState({
		page: 0,
		pageSize: 25,
	});

	const [maxLogs, setMaxLogs] = React.useState(0);
	const [logs, setLogs] = React.useState([]);
	const [viewLogs, setViewLogs] = React.useState([]);

	const [buckets, setBuckets] = React.useState([]);

	const [searchBucket, setSearchBucket] = React.useState({ name: "", id: 0 });
	const [searchDateRange, setSearchDateRange] = React.useState({});
	const [searchText, setSearchText] = React.useState("");

	const handleChangeSelectBucket = (value) => {
		const bucket = buckets.find((bucket) => bucket.id === value);
		setSearchBucket(bucket);
	};

	const fetchBuckets = async () => {
		const data = await axiosRequest("GET", `${BACKEND_URL}/buckets`);
		setBuckets(data.data);
	};

	const handleClearSearch = () => {
		setSearchBucket({ name: "", id: 0 });
		setSearchDateRange({ fromDate: "", toDate: "" });
		setSearchText("");
	};

	const fetchLogs = async (paginationModel) => {
		const data = await axiosRequest(
			"GET",
			`${BACKEND_URL}/logs?skip=${
				paginationModel.pageSize * paginationModel.page
			}&limit=${paginationModel.pageSize}`
		);

		const newLogs = [...logs, ...data.data];
		setLogs(newLogs);
		setViewLogs(filterLogs(newLogs));
		setMaxLogs(data.total);
	};

	const handleScroll = (e) => {
		const bottom =
			e.target.scrollHeight - e.target.scrollTop ===
			e.target.clientHeight;
		if (
			(bottom &&
				paginationModel.page * paginationModel.pageSize <= maxLogs) ||
			(e.target.scrollTop === 0 &&
				paginationModel.page * paginationModel.pageSize <= maxLogs)
		) {
			const newPM = {
				page: paginationModel.page + 1,
				pageSize: paginationModel.pageSize,
			};
			setPaginationModel(newPM);
			fetchLogs(newPM);
		}
	};

	const filterLogs = (logs) => {
		let allLogs = logs;

		if (searchBucket.id !== 0) {
			allLogs = logs.filter((log) => {
				return log.bucket_id === searchBucket.id;
			});
		}

		if (searchDateRange.fromDate !== "" && searchDateRange.toDate !== "") {
			allLogs = allLogs.filter((log) => {
				return (
					new Date(log.created_at) >=
						new Date(searchDateRange.fromDate) &&
					new Date(log.created_at) <= new Date(searchDateRange.toDate)
				);
			});
		}

		allLogs = allLogs.filter((log) => {
			return (
				log.bucket_name
					.toLowerCase()
					.includes(searchText.toLowerCase()) ||
				log.description.toLowerCase().includes(searchText.toLowerCase())
			);
		});

		return allLogs;
	};

	React.useEffect(() => {
		fetchBuckets();
		fetchLogs(paginationModel);
	}, []);

	React.useEffect(() => {
		setViewLogs(filterLogs(logs));
	}, [searchBucket, searchDateRange, searchText]);

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
						<Button
							classStyle="rounded-xl w-1/8 text-xl"
							label="Export"
						/>
					</Section>
					<Section
						classSize="h-1/8"
						classStyle="flex flex-row items-center w-full gap-5"
					>
						<div
							id="log-date-range-picker"
							className="w-3/10 flex flex-row gap-3 size-full"
						>
							<Input
								type="date"
								className={clsx(
									"block w-full rounded-lg border-none bg-white/5 px-3 py-1.5 text-sm text-white",
									"focus:not-data-focus:outline-none data-focus:outline-2 data-focus:-outline-offset-2 data-focus:outline-white/30"
								)}
								onChange={(e) => {
									setSearchDateRange({
										fromDate: e.target.value,
										toDate: searchDateRange.toDate,
									});
								}}
								value={searchDateRange.fromDate ?? undefined}
							/>
							<Input
								type="date"
								className={clsx(
									"block w-full rounded-lg border-none bg-white/5 px-3 py-1.5 text-sm text-white",
									"focus:not-data-focus:outline-none data-focus:outline-2 data-focus:-outline-offset-2 data-focus:outline-white/30"
								)}
								onChange={(e) => {
									setSearchDateRange({
										fromDate: searchDateRange.fromDate,
										toDate: e.target.value,
									});
								}}
								value={searchDateRange.toDate ?? undefined}
							/>
						</div>
						<Divider vertical />
						<div
							id="log-bucket-picker"
							className="flex flex-col w-3/10 h-full"
						>
							<Listbox
								onChange={(value) => {
									handleChangeSelectBucket(value);
								}}
							>
								<ListboxButton
									className={clsx(
										"flex items-center w-full h-full rounded-lg bg-white/5 p-5 text-left text-xl text-white",
										"focus:not-data-focus:outline-none data-focus:outline-2 data-focus:-outline-offset-2 data-focus:outline-white/25"
									)}
								>
									{searchBucket.name}
								</ListboxButton>
								<ListboxOptions
									anchor="bottom end"
									transition
									className={clsx(
										"w-(--button-width) rounded-lg border border-white/5 bg-spenny-background p-1 [--anchor-gap:--spacing(1)] focus:outline-none",
										"transition duration-100 ease-in-out data-closed:opacity-0"
									)}
								>
									{buckets.map((bucket) => (
										<ListboxOption
											key={bucket.id}
											value={bucket.id}
											className="group flex cursor-default items-center gap-2 rounded-lg px-3 py-1.5 select-none data-focus:bg-white/10"
										>
											<div className="text-xl text-white">
												{bucket.name}
											</div>
										</ListboxOption>
									))}
								</ListboxOptions>
							</Listbox>
						</div>
						<Divider vertical />
						<div
							id="log-search"
							className="flex flex-col w-3/10 h-full"
						>
							<Input
								className={clsx(
									"block size-full rounded-lg border-none bg-white/5 px-3 py-1.5 text-sm text-white",
									"focus:not-data-focus:outline-none data-focus:outline-2 data-focus:-outline-offset-2 data-focus:outline-white/30"
								)}
								onChange={(e) => {
									setSearchText(e.target.value);
								}}
								value={searchText}
							/>
						</div>

						<Divider vertical />
						<Button
							classStyle="rounded-xl border-solid border-5 border-spenny-accent-error bg-spenny-accent-error text-white hover:bg-spenny-background hover:text-spenny-accent-error"
							classColor="w-1/10 text-xl h-full"
							label="Clear"
							onClick={handleClearSearch}
						/>
					</Section>
					<Section
						classSize="h-6/8 w-full"
						classStyle="text-xl overflow-y-scroll"
					>
						<div className="w-full h-full flex flex-col gap-3">
							<div
								id="log-header"
								className="flex flex-row gap-3 w-full h-1/12"
							>
								<p className="flex items-center text-2xl font-bold w-2/27 h-[60px] ">
									ID
								</p>
								<Divider vertical />
								<p className="flex items-center text-2xl font-bold w-2/27 h-[60px] ">
									Event
								</p>
								<Divider vertical />
								<p className="flex items-center text-2xl font-bold w-2/27 h-[60px] ">
									Bucket
								</p>
								<Divider vertical />
								<p className="flex items-center text-2xl font-bold w-4/27 h-[60px] ">
									Name
								</p>
								<Divider vertical />
								<p className="flex items-center text-2xl font-bold w-11/27 h-[60px] ">
									Description
								</p>
								<Divider vertical />
								<p className="flex items-center text-2xl font-bold w-2/27 h-[60px] ">
									Amount
								</p>

								<Divider vertical />
								<p className="flex items-center text-2xl font-bold w-2/27 h-[60px] ">
									Created
								</p>
								<Divider vertical />
								<p className="flex items-center text-2xl font-bold w-2/27 h-[60px] ">
									View
								</p>
							</div>
							<Divider />
							<div
								id="log-items"
								className="w-full h-full overflow-y-scroll flex flex-col gap-2"
								onWheel={handleScroll}
							>
								{viewLogs.map((log, key) => {
									return <LogRow key={key} log={log} />;
								})}
								{paginationModel.page *
									paginationModel.pageSize <=
									maxLogs && maxLogs !== 0 ? (
									<div
										role="status"
										className="flex justify-center item-center"
									>
										<svg
											aria-hidden="true"
											className="w-8 h-8 text-gray-200 animate-spin dark:text-gray-600 fill-spenny-accent-primary p-2"
											viewBox="0 0 100 101"
											fill="none"
											xmlns="http://www.w3.org/2000/svg"
										>
											<path
												d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
												fill="currentColor"
											/>
											<path
												d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
												fill="currentFill"
											/>
										</svg>
									</div>
								) : (
									<div
										role="status"
										className="flex justify-center item-center"
									>
										<p
											className={
												"cursor-progress text-md font-semibold text-white/30 p-2 border-2 border-dashed border-white/30 rounded-xl w-full flex justify-center"
											}
										>
											No more logs
										</p>
									</div>
								)}
							</div>
						</div>
					</Section>
				</div>
			</Page>
		</>
	);
};

export default Logs;
