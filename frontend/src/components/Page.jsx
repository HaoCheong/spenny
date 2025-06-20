import Sidebar from "./Sidebar";

const Page = ({ children }) => {
	return (
		<div class="flex flex-row bg-teal-200 w-screen h-screen">
			<Sidebar />
			<div id="page-container" class="bg-black w-full h-full p-5">
				<div
					id="page-content"
					class="w-full h-full border-2 border-solid"
				>
					{children}
				</div>
			</div>
		</div>
	);
};

export default Page;
