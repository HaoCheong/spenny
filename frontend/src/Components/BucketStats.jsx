import {
    Card,
    CardBody,
    Stat,
    StatArrow,
    StatGroup,
    StatHelpText,
    StatLabel,
    StatNumber,
    Text,
} from '@chakra-ui/react'
import React from 'react'

const BucketStats = ({ bucket }) => {
    return (
        <Card bg="#3AAED8" color="white">
            <CardBody>
                <StatGroup>
                    <Stat>
                        <StatLabel>Current Amount</StatLabel>
                        <StatNumber>${bucket.current_amount}</StatNumber>
                    </Stat>
                    <Stat>
                        <StatLabel>Out/Inflow Events Ratio</StatLabel>

                        {bucket.from_events && bucket.to_events ? (
                            <StatNumber>
                                {bucket.from_events.length}:
                                {bucket.to_events.length}
                            </StatNumber>
                        ) : (
                            <></>
                        )}
                    </Stat>
                </StatGroup>
            </CardBody>
        </Card>
    )
}

export default BucketStats
