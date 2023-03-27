import {
    Alert,
    AlertDescription,
    AlertIcon,
    AlertTitle,
} from '@chakra-ui/react'
import React from 'react'

const ResponseAlert = ({ alertInfo }) => {
    if (alertInfo.isOpen) {
        return (
            <>
                <Alert status={alertInfo.type}>
                    <AlertIcon />
                    {alertInfo.type === 'success' ? (
                        <AlertTitle>Success</AlertTitle>
                    ) : (
                        <AlertTitle>Error</AlertTitle>
                    )}
                    <AlertDescription>{alertInfo.message}</AlertDescription>
                </Alert>
            </>
        )
    } else {
        return <></>
    }
}

export default ResponseAlert
