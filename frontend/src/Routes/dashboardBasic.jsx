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
    Menu,
    MenuButton,
    MenuList,
    Divider,
} from '@chakra-ui/react'
import { ChevronDownIcon } from '@chakra-ui/icons'
import BucketDisplay from '../Components/BucketDisplay'
import CreateBucketModal from '../Components/BucketModals/CreateBucketModal'
import DeleteBucketModal from '../Components/BucketModals/DeleteBucketModal'
import CreateFlowEventModal from '../Components/FlowEventModals/CreateFlowEventModal'
import DeleteFlowEventModal from '../Components/FlowEventModals/DeleteFlowEventModal'
import EventTriggerModal from '../Components/EventTriggerModal'
import ViewRecent from '../Components/StatisticModals/ViewRecent'
import ViewStats from '../Components/StatisticModals/ViewStats'
import ViewUpcoming from '../Components/StatisticModals/ViewUpcoming'

import { BACKEND_URL } from '../config.js'

const DashboardBasic = () => {
    const [bucketList, setBucketList] = React.useState([])
    const [totalAmount, setTotalAmount] = React.useState(0)
    const getAllBucket = async () => {
        const res = await axios.get(`${BACKEND_URL}/buckets`)
        setBucketList(res.data)
    }

    const getTotalAmount = async () => {
        let final = 0
        bucketList.forEach((bucket) => {
            final += bucket.current_amount
        })
        setTotalAmount(final)
    }

    const handleUpdate = async () => {
        try {
            await axios.put(`${BACKEND_URL}/updateValues`)
        } catch (err) {
            console.error('Error', err)
        }
    }

    React.useEffect(() => {
        getAllBucket()
    }, [])

    React.useEffect(() => {
        getTotalAmount()
    }, [bucketList])

    return (
        <>
            <Box
                sx={{
                    width: '100vw',
                    height: '100vh',
                    backgroundColor: '#B892FF',
                }}
            >
                <HStack gap={5} margin="2rem">
                    <Text fontSize="5xl">Spenny V1.0</Text>
                    <Menu>
                        <MenuButton as={Button} rightIcon={<ChevronDownIcon />}>
                            Actions
                        </MenuButton>
                        <MenuList>
                            <CreateBucketModal />
                            <DeleteBucketModal />
                            <Divider />
                            <CreateFlowEventModal />
                            <DeleteFlowEventModal />
                        </MenuList>
                    </Menu>
                    <Menu>
                        <MenuButton as={Button} rightIcon={<ChevronDownIcon />}>
                            Statistics
                        </MenuButton>
                        <MenuList>
                            <ViewStats />
                            <ViewRecent />
                            <ViewUpcoming />
                        </MenuList>
                    </Menu>

                    <EventTriggerModal />
                    <Button colorScheme="green" onClick={handleUpdate}>
                        Run Update
                    </Button>
                    <Text fontSize="3xl">Total In Account: {totalAmount}</Text>
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
                    </Box>
                </VStack>
            </Box>
        </>
    )
}

export default DashboardBasic
