import {
	Dialog,
	DialogBackdrop,
	DialogPanel,
	DialogTitle,
	Transition,
} from "@headlessui/react";
import Button from "./Button";
import clsx from "clsx";

const AddBucketDialog = ({ isOpen, setIsOpen }) => {
	const handleClose = () => {
		setIsOpen(false);
	};
	return (
		<Transition show={isOpen}>
			<Dialog
				open={isOpen}
				as="div"
				className="relative z-10 focus:outline-none"
				onClose={handleClose}
			>
				{/* `fixed inset-0 z-10 w-screen overflow-y-auto backdrop-blur-xl data-enter:backdrop-blur-xl data-enter:opacity-100 data-enter:duration-300 data-enter:ease-in data-leave:backdrop-blur-none data-leave:opacity-0 data-leave:duration-300 data-leave:ease-out` */}
				<div
					className={clsx(
						"fixed inset-0 z-10 w-screen overflow-y-auto transition ease-in-out backdrop-blur-2xl",
						"data-enter:bg-green-300 data-enter:opacity-90 data-enter:duration-500",
						"data-transition:bg-blue-500 data-transition:opacity-20 data-transition:duration-500"
					)}
				>
					<div className="flex min-h-full items-center justify-center p-4">
						<DialogPanel
							transition
							className="w-full max-w-md rounded-xl bg-white/5 p-6 backdrop-blur-xl duration-100 ease-out data-closed:opacity-0"
						>
							<DialogTitle
								as="h3"
								className="text-base/7 font-medium text-white"
							>
								Test
							</DialogTitle>
							<p className="mt-2 text-sm/6 text-white/50">
								Test Content
							</p>
							<div className="mt-4">
								<Button onClick={handleClose} label="Close" />
							</div>
						</DialogPanel>
					</div>
				</div>
			</Dialog>
		</Transition>
	);
};

export default AddBucketDialog;
