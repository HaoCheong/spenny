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
} from '@chakra-ui/react'
import BucketDisplay from '../Components/BucketDisplay'
import CreateBucketModal from '../Components/BucketModal'
import CreateFlowEventModal from '../Components/CreateFlowEventModal'
const BACKEND_URL = 'http://127.0.0.1:8000'

const DashboardBasic = () => {
    const [bucketList, setBucketList] = React.useState([])

    const getAllBucket = async () => {
        const res = await axios.get(`${BACKEND_URL}/buckets`)
        console.log('BUK LIST', res.data)
        setBucketList(res.data)
    }

    React.useEffect(() => {
        getAllBucket()
    }, [])

    return (
        <>
            <Box
                sx={{
                    backgroundColor: '#49416D',
                    width: '100%',
                    height: '100%',
                }}
            >
                <VStack sx={{ margin: '1rem' }}>
                    <CreateBucketModal />
                    <CreateFlowEventModal />
                    <Box
                        sx={{
                            width: '100%',
                            height: '100%',
                            padding: '1em',
                        }}
                    >
                        <HStack sx={{ overflowX: 'scroll' }}>
                            {bucketList.map((bucket) => {
                                return <BucketDisplay bucket_id={bucket.id} />
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
