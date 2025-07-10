import {
	Listbox,
	ListboxButton,
	ListboxOption,
	ListboxOptions,
} from "@headlessui/react";
import clsx from "clsx";

const ListItems = ({ startItem, collection, onChange, formik }) => {
	// Collection must be a minimal of {id: 0, name: "Display Name", value: "DB backend value"}
	return (
		<Listbox value={startItem.id} onChange={onChange}>
			<ListboxButton
				className={clsx(
					"w-full rounded-lg bg-white/5 p-1.5 text-left text-sm text-white",
					"focus:not-data-focus:outline-none data-focus:outline-2 data-focus:-outline-offset-2 data-focus:outline-white/25"
				)}
			>
				{startItem.name}
			</ListboxButton>
			<ListboxOptions
				anchor="bottom end"
				transition
				className={clsx(
					"w-(--button-width) rounded-lg border border-white/5 bg-spenny-background p-1 [--anchor-gap:--spacing(1)] focus:outline-none",
					"transition duration-100 ease-in-out data-closed:opacity-0"
				)}
			>
				{collection.map((item) => (
					<ListboxOption
						key={item.id}
						value={item.id}
						className="group flex cursor-default items-center gap-2 rounded-lg px-3 py-1.5 select-none data-focus:bg-white/10"
					>
						<div className="text-sm/6 text-white">{item.name}</div>
					</ListboxOption>
				))}
			</ListboxOptions>
		</Listbox>
	);
};

export default ListItems;
