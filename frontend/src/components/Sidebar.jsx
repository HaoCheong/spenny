import Divider from "./Divider";
import SidebarSelector from "./SidebarSelector";
const Sidebar = () => {
	return (
		<>
			<div class="flex flex-col w-1/4 h-full p-5 border-r-white border-solid border-r-4 bg-black gap-7">
				<div id="sidebar-header" class="flex flex-col h-1/8 gap-4">
					<h1 class="flex justify-center items-center text-7xl text-white">
						Spenny
					</h1>
					<h2 class="flex justify-center items-center text-white text-lg">
						Version: 1.1
					</h2>
				</div>
				<Divider />
				<div id="sidebar-selectors" class="flex flex-col h-5/8 gap-1">
					<SidebarSelector label="Dashboard" path="/Dashboard" />
					<SidebarSelector label="Logs" path="/Logs" />
				</div>
				<Divider />
				<div id="sidebar-footer" class="h-2/8">
					<h2 class="flex justify-center items-center text-white">
						@github
					</h2>
				</div>
			</div>
		</>
	);
};

export default Sidebar;
