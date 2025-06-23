import axios from "axios";

/**
 * Axios Interface function. Handles request errors and data handling
 *
 * @param {string} method - The Method that is being used to call
 * @param {string} url - The route objects that require prior authorisation checks
 * @param {Object} options - The route objects that require prior authorisation checks
 *
 * @return {Object} The requested data object
 * @throws API Error - API was unable to handle the request
 * @throws Network Error - The network was unable to handle the request
 * @throws Unexpected Error - The request was unable to be processed
 */
const axiosRequest = async (method = "GET", url, options = {}) => {
	// Attempt to call via axios
	try {
		const res = await axios({
			url: url,
			method: method.toUpperCase(),
			timeout: 10000,
			...options,
		});

		return res.data;
	} catch (error) {
		if (axios.isAxiosError(error)) {
			// If the response is an error, its an API Error
			if (error.response) {
				const new_error = new Error(
					`API Error - Status: ${error.response.status} - Message: ${
						error.response.data?.message || "Unknown Error"
					}`
				);
				new_error.code = error.response.status;
				throw new_error;

				// If the response is an error, its an Network Error
			} else if (error.request) {
				const new_error = new Error(
					`Network Error - No response from the server`
				);
				new_error.code = 404;
				throw new_error;

				// Else it is an unknown error
			} else {
				const new_error = new Error(
					`Unexpected Error: ${error.message}`
				);
				new_error.code = 500;
				throw new_error;
			}
		} else {
			const new_error = new Error(
				`Unexpected Error: ${error.message || error}`
			);
			new_error.code = 500;
			throw new_error;
		}
	}
};

export default axiosRequest;
