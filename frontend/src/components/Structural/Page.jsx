import Sidebar from "./Sidebar";

const Page = ({ children }) => {
	return (
		<div className="flex flex-row w-screen h-screen">
			<Sidebar />
			<div
				id="page-container"
				className="bg-spenny-background w-4/5 h-full p-5"
			>
				<div id="page-content" className="h-full w-1500px">
					{children}
				</div>
			</div>
		</div>
	);
};

export default Page;
