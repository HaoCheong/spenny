import { useLocation, useNavigate } from "react-router";

const SidebarSelector = ({ label, path }) => {
	const currPath = useLocation();
	const navigate = useNavigate();

	const handleNavigation = (path) => {
		navigate(`${path}`);
	};

	return (
		<>
			{currPath.pathname === path ? (
				<button
					class="flex bg-white text-black flex-col w-full p-3 rounded-sm text-xl"
					onClick={() => {
						handleNavigation(path);
					}}
				>
					{label}
				</button>
			) : (
				<button
					class="flex bg-black text-white flex-col w-full p-3 rounded-sm text-xl transition duration-350 ease-in-out hover:bg-white hover:text-black "
					onClick={() => {
						handleNavigation(path);
					}}
				>
					{label}
				</button>
			)}
		</>
	);
};

export default SidebarSelector;
