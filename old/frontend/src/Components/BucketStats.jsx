import {
    Card,
    CardBody,
    Stat,
    StatArrow,
    StatGroup,
    StatLabel,
    StatNumber,
} from '@chakra-ui/react'
import React from 'react'

const BucketStats = ({ bucket }) => {
    const get_fe_amount = (bucket_list) => {
        let total_flow_amount = 0
        bucket_list.forEach((bucket_item) => {
            total_flow_amount += bucket_item.change_amount
        })
        return total_flow_amount
    }

    return (
        <Card
            bg="#123d16"
            color="white"
            borderWidth="2px"
            borderColor="#7bcf3f"
        >
            <CardBody>
                <StatGroup>
                    <Stat m="2">
                        <StatLabel>Current</StatLabel>
                        <StatNumber>${bucket.current_amount}</StatNumber>
                    </Stat>

                    <Stat>
                        <StatLabel>Inflow</StatLabel>
                        {bucket.to_events ? (
                            <>
                                <StatNumber>
                                    ${get_fe_amount(bucket.to_events)}
                                </StatNumber>
                                <StatArrow type="increase" />
                            </>
                        ) : (
                            <></>
                        )}
                    </Stat>

                    <Stat>
                        <StatLabel>Outflow</StatLabel>
                        {bucket.from_events ? (
                            <>
                                <StatNumber>
                                    ${get_fe_amount(bucket.from_events)}
                                </StatNumber>
                                <StatArrow type="decrease" />
                            </>
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
