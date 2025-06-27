import {
	Dialog,
	DialogPanel,
	DialogTitle,
	Transition,
	TransitionChild,
} from "@headlessui/react";
import Button from "./Button";
import clsx from "clsx";
import { Fragment } from "react";

const DialogBase = ({ isOpen, setIsOpen, children }) => {
	const handleClose = () => {
		setIsOpen(false);
	};
	return (
		<Dialog
			open={isOpen}
			as="div"
			className="relative z-10 focus:outline-none"
			onClose={handleClose}
		>
			<Transition show={isOpen} as={Fragment} appear>
				<TransitionChild as={Fragment}>
					<div
						id="dialog-backdrop"
						className={clsx(
							"fixed inset-0 w-screen h-screen rounded-xl bg-spenny-background/30 backdrop-blur-sm shadow-2xl transition duration-200", // There is a transition of 200ms. This is the final rendered state
							"data-closed:backdrop-blur-sm data-closed:opacity-0", // You can treat as the same as assigning values for data-enter and data-leave. Assigned to scale down to 90% then opacity to 0
							"data-leave:duration-200 data-leave:ease-in-out" // Set the leave duration
						)}
					/>
				</TransitionChild>
				<TransitionChild as={Fragment}>
					<div
						id="dialog-panel"
						className="fixed inset-0 flex items-center justify-center p-4"
					>
						{children}
					</div>
				</TransitionChild>
			</Transition>
		</Dialog>
	);
};

export default DialogBase;
