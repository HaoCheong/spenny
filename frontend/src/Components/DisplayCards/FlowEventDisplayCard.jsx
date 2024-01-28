import {
    Card,
    CardBody,
    CardFooter,
    Heading,
    HStack,
    VStack,
    Text,
} from '@chakra-ui/react'
import React from 'react'

import ViewFlowEventModal from '../FlowEventModals/ViewFlowEventModal'
import EditFlowEventModal from '../FlowEventModals/EditFlowEventModal'

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
                borderWidth="5px"
                borderColor={bgColor}
                bg="#0a1c09"
                width="100%"
                minH="150px"
                padding="10px"
            >
                <HStack spacing={1}>
                    <CardBody color="white" padding="0">
                        <Heading size="md">{fe.name}</Heading>
                        <Text>
                            Next Date:{' '}
                            {new Date(fe.next_trigger).toLocaleDateString(
                                undefined,
                                options
                            )}
                        </Text>
                    </CardBody>
                    <Text fontSize="xl">
                        ${fe.change_amount}
                    </Text>
                    <CardFooter width="20%">
                       <VStack>
                            <ViewFlowEventModal fe={fe} />
                            <EditFlowEventModal fe={fe} />
                        </VStack> 
                        
                    </CardFooter>
                </HStack>
            </Card>
        </>
    )
}

export default FlowEventDisplayCard
