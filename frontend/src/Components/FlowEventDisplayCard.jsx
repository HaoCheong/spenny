import {
    Card,
    CardBody,
    CardFooter,
    Heading,
    HStack,
    Text,
    IconButton,
} from '@chakra-ui/react'
import React from 'react'
import { ViewIcon } from '@chakra-ui/icons'

const FlowEventDisplayCard = ({ fe }) => {
    let bgColor
    switch (fe.type) {
        case 'ADD':
            bgColor = '#5c940d'
            break

        case 'SUB':
            bgColor = '#c92a2a'
            break

        case 'MOV':
            bgColor = '#e67700'
            break

        default:
            break
    }

    return (
        <>
            <Card
                direction={{ base: 'column', sm: 'row' }}
                overflow="hidden"
                variant="elevated"
                bg={bgColor}
                mt="2"
            >
                <HStack width="100%">
                    <CardBody width="80%" color="white">
                        <Heading size="md">{fe.name}</Heading>
                        <Text py="2">{fe.description}</Text>
                    </CardBody>
                    <Text py="2" fontSize="xl">
                        {fe.change_amount}
                    </Text>
                    <CardFooter width="20%">
                        <IconButton
                            aria-label="Search database"
                            icon={<ViewIcon />}
                        />
                    </CardFooter>
                </HStack>
            </Card>
        </>
    )
}

export default FlowEventDisplayCard
