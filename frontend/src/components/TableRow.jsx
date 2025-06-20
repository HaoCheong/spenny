import Divider from "./Divider";

const TableRow = () => {
	return (
		<div class="flex flex-row gap-3 w-full h-1/12">
			<p class="flex items-center w-1/16 h-[60px]">Data</p>
			<Divider vertical />
			<p class="flex items-center w-2/16 h-[60px]">Data</p>
			<Divider vertical />
			<p class="flex items-center w-2/16 h-[60px]">Data</p>
			<Divider vertical />
			<p class="flex items-center w-7/16 h-[60px]">Data</p>
			<Divider vertical />
			<p class="flex items-center w-2/16 h-[60px]">Data</p>
			<Divider vertical />
			<p class="flex items-center w-2/16 h-[60px]">Data</p>
		</div>
	);
};

export default TableRow;
