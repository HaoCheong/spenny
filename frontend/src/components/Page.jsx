import Sidebar from "./Sidebar";

const Page = ({ children }) => {
	return (
		<div class="flex flex-roww-screen h-screen">
			<Sidebar />
			<div id="page-container" class="bg-black w-4/5 h-full p-5">
				<div id="page-content" class="h-full w-1500px">
					{children}
				</div>
			</div>
		</div>
	);
};

export default Page;
