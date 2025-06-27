import { Field, Label } from "@headlessui/react";

const Textfield = ({ children }) => {
	return (
		<Field>
			<Label className="text-md font-medium text-white">{children}</Label>
			<Input
				className={clsx(
					"mt-3 block w-full rounded-lg border-none bg-white/5 px-3 py-1.5 text-sm/6 text-white",
					"focus:not-data-focus:outline-none data-focus:outline-2 data-focus:-outline-offset-2 data-focus:outline-white/30"
				)}
			/>
		</Field>
	);
};

export default Textfield;
