import { Menu, MenuButton, MenuItem, MenuItems } from "@headlessui/react";
import Divider from "../Divider";

const ActionMenu = ({ handleEditBucket, handleDeleteBucket }) => {
	return (
		<Menu>
			<MenuButton className="flex flex-col p-3 h-full justify-center items-center rounded-lg text-md transition duration-300 ease-in-out w-full text-xl border-solid border-2 border-spenny-accent-warning bg-spenny-accent-warning text-black hover:bg-spenny-background hover:text-spenny-accent-warning">
				Action
			</MenuButton>

			<MenuItems
				transition
				anchor="bottom end"
				className="w-52 origin-top-right rounded-xl border border-white/5 bg-spenny-background p-1 text-sm/6 text-white transition duration-100 ease-out [--anchor-gap:--spacing(1)] focus:outline-none data-closed:scale-95 data-closed:opacity-0 flex flex-col gap-2"
			>
				<MenuItem>
					<button className="flex w-full items-center gap-2 rounded-lg p-1.5 transition duration-300 ease-in-out bg-spenny-accent-base/60 data-focus:bg-spenny-background data-focus:border-1 data-focus:border-solid data-focus:border-spenny-accent-base/60 data-focus:text-spenny-accent-base/60">
						Add Event
					</button>
				</MenuItem>
				<Divider />
				<MenuItem>
					<button
						onClick={handleEditBucket}
						className="flex w-full items-center gap-2 rounded-lg p-1.5 transition duration-300 ease-in-out bg-spenny-accent-warning/80 data-focus:bg-spenny-background data-focus:border-1 data-focus:border-solid data-focus:border-spenny-accent-warning/80 data-focus:text-spenny-accent-warning/80"
					>
						Edit
					</button>
				</MenuItem>
				<MenuItem>
					<button
						onClick={handleDeleteBucket}
						className="flex w-full items-center gap-2 rounded-lg p-1.5 transition duration-300 ease-in-out bg-spenny-accent-error/80 data-focus:bg-spenny-background data-focus:border-1 data-focus:border-solid data-focus:border-spenny-accent-error/80 data-focus:text-spenny-accent-error/80"
					>
						Delete
					</button>
				</MenuItem>
			</MenuItems>
		</Menu>
	);
};

export default ActionMenu;
