//The display card for bucket

// Displays stats table on the top
// Displays the total and daily use
// Displays all its relevant flow events
// Displays a list of logs and transactions

import {
    Box,
    Button,
    ButtonGroup,
    Card,
    CardBody,
    CardFooter,
    Divider,
    HStack,
    VStack,
    Heading,
    Image,
    Stack,
    Text,
} from '@chakra-ui/react'
import React from 'react'
import axios from 'axios'
import { BACKEND_URL } from '../config.js'
import FlowEventDisplayCard from './DisplayCards/FlowEventDisplayCard.jsx'
import SpendChart from './SpendChart.jsx'
import ViewBucketModal from './BucketModals/ViewBucketModal.jsx'
import BucketStats from './BucketStats.jsx'

const BucketDisplay = ({ bucket_id }) => {
    const [bucket, setBucket] = React.useState({
        properties: {
            invisible: false,
        },
        from_events: [],
        to_events: [],
    })

    const getBucketData = async () => {
        const res = await axios.get(`${BACKEND_URL}/bucket/${bucket_id}`)
        console.log(res.data)
        setBucket(res.data)
    }

    React.useEffect(() => {
        getBucketData()
    }, [])

    return (
        <Card
            minW="sm"
            minH="300px"
            maxH="1500px"
            height="100%"
            bg="black"
            borderWidth="2px"
            // borderColor='#7bcf3f'
            borderColor={bucket.properties.invisible ? '#CD02D9' : '#7bcf3f'}
            variant="elevated"
            color="white"
        >
            <CardBody height="70%">
                <Box bg="white">
                    <SpendChart bucket_id={bucket_id} />
                </Box>

                <Stack height="75%" spacing="5px">
                    <Heading size="lg">{bucket.name}</Heading>
                    <BucketStats bucket={bucket} />
                    <Text minH="30px" sx={{ overflowY: 'scroll' }}>
                        {bucket.description}
                    </Text>

                    <Divider />

                    <Text fontSize="2xl">Flow Events</Text>
                    {/* <Box height="100%" bg='green'>TEST</Box> */}
                    <VStack
                        gap={1}
                        overflowY="scroll"
                        padding={3}
                        minH="50px"
                        height="100%"
                    >
                        {bucket.from_events.map((fe, idx) => {
                            return <FlowEventDisplayCard key={idx} fe={fe} />
                        })}

                        {bucket.to_events.map((fe, idx) => {
                            return <FlowEventDisplayCard key={idx} fe={fe} />
                        })}
                    </VStack>
                </Stack>
            </CardBody>
            <Divider />
            <CardFooter>
                <ButtonGroup spacing="2">
                    <ViewBucketModal bucket={bucket} />
                </ButtonGroup>
            </CardFooter>
        </Card>
    )
}

export default BucketDisplay
