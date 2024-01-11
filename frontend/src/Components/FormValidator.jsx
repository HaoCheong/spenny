//Wrapper for FormControl and inputs for cleaner management

import { FormControl, FormErrorMessage } from '@chakra-ui/react'
import React from 'react';

const FormValidator = ({ children, propName, formik }) => {
    return (
        <>
            <FormControl
                isInvalid={
                    !!formik.errors[propName] && formik.touched[propName]
                }
            >
                {children}
                <FormErrorMessage>{formik.errors[propName]}</FormErrorMessage>
            </FormControl>
        </>
    )
}

export default FormValidator
