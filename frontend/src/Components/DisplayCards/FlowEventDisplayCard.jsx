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

import ViewFlowEventModal from '../FlowEventModals/ViewFlowEventModal'

const FlowEventDisplayCard = ({ fe }) => {
    const options = {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric',
    }
    let bgColor
    switch (fe.type) {
        case 'ADD':
            bgColor = '#23CE6B'
            break

        case 'SUB':
            bgColor = '#EE4266'
            break

        case 'MOV':
            bgColor = '#FFD23F'
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
                        <Text py="2">
                            Next Date:{' '}
                            {new Date(fe.next_trigger).toLocaleDateString(
                                undefined,
                                options
                            )}
                        </Text>
                    </CardBody>
                    <Text py="2" fontSize="xl">
                        {fe.change_amount}
                    </Text>
                    <CardFooter width="20%">
                        <ViewFlowEventModal fe={fe} />
                    </CardFooter>
                </HStack>
            </Card>
        </>
    )
}

export default FlowEventDisplayCard
