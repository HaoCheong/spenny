import React from 'react'

import {
    Card,
    CardBody,
    Stat,
    StatHelpText,
    StatLabel,
    StatNumber,
    HStack,
    ListItem,
    UnorderedList,
} from '@chakra-ui/react'

const LogCard = ({ log }) => {
    const date = new Date(log.date_created)
    const date_created_str = `${date.getDate()}-${
        date.getMonth() + 1
    }-${date.getFullYear()}`

    let bgColor
    switch (log.type) {
        case 'ADD':
            bgColor = '#5c940d'
            break

        case 'SUB':
            bgColor = '#ff5154'
            break

        case 'MOV':
            bgColor = '#FFD23F'
            break
        default:
            break
    }

    return (
        <Card variant="filled" width="100%" bgColor={bgColor}>
            <CardBody>
                <HStack spacing="1em">
                    <UnorderedList width="80%">
                        <ListItem>Name: {log.name}</ListItem>
                        <ListItem>Description: {log.description}</ListItem>
                    </UnorderedList>
                    <Stat width="20%">
                        <StatLabel>Amount</StatLabel>
                        <StatNumber>{log.amount}$</StatNumber>
                        <StatHelpText>{date_created_str}</StatHelpText>
                    </Stat>
                </HStack>
            </CardBody>
        </Card>
    )
}

export default LogCard
