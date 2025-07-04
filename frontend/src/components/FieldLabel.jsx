import { Description, Field, Label } from "@headlessui/react";

const FieldLabel = ({
	label,
	desc,
	children,
	error = false,
	errorMsg = "",
}) => {
	return (
		<Field>
			<Label className="text-md font-medium text-white">{label}</Label>
			{desc && (
				<Description className="text-sm/6 text-white/50">
					{desc}
				</Description>
			)}
			{children}
			{error ? (
				<p
					id={`${label}-field-error-message`}
					className="text-sm text-spenny-accent-error"
				>
					{errorMsg}
				</p>
			) : (
				<></>
			)}
		</Field>
	);
};

export default FieldLabel;
