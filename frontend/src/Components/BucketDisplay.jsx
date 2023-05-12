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
    const [bucket, setBucket] = React.useState({ from_events: [] })

    const getBucketData = async () => {
        const res = await axios.get(`${BACKEND_URL}/bucket/${bucket_id}`)
        setBucket(res.data)
    }

    React.useEffect(() => {
        getBucketData()
    }, [])

    return (
        <Card
            minW="sm"
            bg="#2A1E5C"
            variant="elevated"
            color="white"
            minH="120vh"
        >
            <CardBody>
                <Box bg="white">
                    <SpendChart bucket_id={bucket_id} />
                </Box>

                <Stack mt="6" spacing="3">
                    <Heading size="lg">{bucket.name}</Heading>
                    <BucketStats bucket={bucket} />
                    <Text sx={{ overflowY: 'scroll', maxH: '10em' }}>
                        {bucket.description}
                    </Text>

                    <Divider />
                    <Text fontSize="2xl">Flow Events</Text>
                    <Box
                        sx={{
                            overflowY: 'scroll',
                            maxH: '16rem',
                        }}
                    >
                        {bucket.from_events.map((fe, idx) => {
                            return <FlowEventDisplayCard key={idx} fe={fe} />
                        })}
                    </Box>
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
