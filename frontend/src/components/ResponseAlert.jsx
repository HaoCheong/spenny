const ResponseAlert = ({ alertInfo }) => {
	if (alertInfo.isOpen) {
		return (
			<>
				{alertInfo.type === "error" ? (
					<div
						id="response-alert-error"
						className="rounded-xl flex flex-col justify-center items-center bg-spenny-accent-error/10 border-2 border-solid border-spenny-accent-error/65 text-white p-3"
					>
						{alertInfo.message}
					</div>
				) : (
					<></>
				)}
				{alertInfo.type === "success" ? (
					<div
						id="response-alert-error"
						className="rounded-xl flex flex-col justify-center items-center bg-spenny-accent-base/10 border-2 border-solid border-spenny-accent-base/65 text-white p-3"
					>
						{alertInfo.message}
					</div>
				) : (
					<></>
				)}
				{alertInfo.type === "warning" ? (
					<div
						id="response-alert-error"
						className="rounded-xl flex flex-col justify-center items-center bg-spenny-accent-warning/10 border-2 border-solid border-spenny-accent-warning/65 text-white p-3"
					>
						{alertInfo.message}
					</div>
				) : (
					<></>
				)}
			</>
		);
	}
};

export default ResponseAlert;
