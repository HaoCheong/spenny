import Divider from "../Divider";
import SidebarSelector from "./SidebarSelector";

const Sidebar = () => {
	return (
		<>
			<div
				className={`flex flex-col w-1/5 h-full p-5 border-r-white border-solid border-r-4 bg-spenny-background gap-7`}
			>
				<div id="sidebar-header" className="flex flex-col h-1/8 gap-4">
					<h1 className="flex justify-center items-center text-7xl text-spenny-text">
						Spenny
					</h1>
					<h2 className="flex justify-center items-center text-spenny-text text-lg">
						Version: 1.1
					</h2>
				</div>
				<Divider />
				<div
					id="sidebar-selectors"
					className="flex flex-col h-5/8 gap-3"
				>
					<SidebarSelector label="Dashboard" path="/Dashboard" />
					<SidebarSelector label="Logs" path="/Logs" />
				</div>
				<Divider />
				<div id="sidebar-footer" className="h-2/8">
					<h2 className="flex justify-center items-center text-spenny-text">
						@hcheong
					</h2>
				</div>
			</div>
		</>
	);
};

export default Sidebar;
