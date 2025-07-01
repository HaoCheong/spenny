import { Description, Field, Label } from "@headlessui/react";

const FieldLabel = ({ label, desc, children }) => {
	return (
		<Field>
			<Label className="text-md font-medium text-white">{label}</Label>
			{desc && (
				<Description className="text-sm/6 text-white/50">
					{desc}
				</Description>
			)}
			{children}
		</Field>
	);
};

export default FieldLabel;
