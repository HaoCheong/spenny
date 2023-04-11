import 'reactflow/dist/style.css'
import React from 'react'
import axios from 'axios'
import {
    Stack,
    HStack,
    VStack,
    Box,
    Button,
    useDisclosure,
    Text,
} from '@chakra-ui/react'
import BucketDisplay from '../Components/BucketDisplay'
import CreateBucketModal from '../Components/CreateBucketModal'
import CreateFlowEventModal from '../Components/CreateFlowEventModal'
import DeleteBucketModal from '../Components/DeleteBucketModal'
import EventTriggerModal from '../Components/EventTriggerModal'
const BACKEND_URL = 'http://127.0.0.1:8000'

const DashboardBasic = () => {
    const [bucketList, setBucketList] = React.useState([])

    const getAllBucket = async () => {
        const res = await axios.get(`${BACKEND_URL}/buckets`)
        setBucketList(res.data)
    }

    const handleUpdate = async () => {
        try {
            await axios.put(`${BACKEND_URL}/updateValues`)
            console.log('Running update')
        } catch (err) {
            console.error('Error', err)
        }
    }

    React.useEffect(() => {
        getAllBucket()
    }, [])

    return (
        <>
            <Box
                sx={{
                    width: '100vw',
                    height: '100vh',
                }}
            >
                <HStack gap={5} margin="2rem">
                    <Text fontSize="5xl">Spenny V1.0</Text>
                    <CreateBucketModal />
                    <CreateFlowEventModal />
                    <DeleteBucketModal />
                    <EventTriggerModal />
                    <Button colorScheme="green" onClick={handleUpdate}>
                        Run Update
                    </Button>
                </HStack>
                <VStack sx={{ margin: '1rem' }}>
                    <Box
                        sx={{
                            width: '100%',
                            height: '100%',
                            padding: '1em',
                        }}
                    >
                        <HStack sx={{ overflowX: 'scroll' }}>
                            {bucketList.map((bucket, idx) => {
                                return (
                                    <BucketDisplay
                                        key={idx}
                                        bucket_id={bucket.id}
                                    />
                                )
                            })}
                        </HStack>
                        {/* <BucketDisplay bucket_id={1} /> */}
                    </Box>
                </VStack>
            </Box>
        </>
    )
}

export default DashboardBasic
