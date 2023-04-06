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
import FlowEventDisplayCard from './FlowEventDisplayCard.jsx'
import SpendChart from './SpendChart.jsx'

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
        <Card minWidth="sm" bg="white" variant="elevated" minHeight="md">
            <CardBody>
                <Box bg="white">
                    <SpendChart bucket_id={1} />
                </Box>

                <Stack mt="6" spacing="3">
                    <Heading size="lg">{bucket.name}</Heading>
                    <Text color="blue.600" fontSize="2xl">
                        Current Amount: ${bucket.current_amount}
                    </Text>
                    <Text sx={{ overflowY: 'scroll', maxH: '10em' }}>
                        {bucket.description}
                    </Text>
                    <Divider />
                    <Box
                        sx={{
                            overflowY: 'scroll',
                            maxH: '16em',
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
                    <Button variant="solid" bgColor="#00a6fb" color="white">
                        View Bucket
                    </Button>
                </ButtonGroup>
            </CardFooter>
        </Card>
    )
}

export default BucketDisplay
