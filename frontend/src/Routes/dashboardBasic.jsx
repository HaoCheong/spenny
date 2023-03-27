import 'reactflow/dist/style.css';
import React from 'react'
import axios from 'axios'
import { Stack, HStack, VStack, Box, Button, useDisclosure } from '@chakra-ui/react'
import BucketDisplay from '../Components/BucketDisplay';
import CreateBucketModal from '../Components/BucketModal';
const BACKEND_URL = "http://127.0.0.1:8000"

const DashboardBasic = () => {

    return (
        <>

            <VStack sx={{ backgroundColor: "black" }}>
                <Box sx={{ border: "5px solid black" }}>
                    <h1>DashBoard Basic</h1>
                    <CreateBucketModal />
                </Box>

                <Box sx={{ border: "5px solid black", width: "100%", height: "100%", padding: '1em' }}>
                    <h1>Content</h1>
                    <BucketDisplay bucket_id={1} />
                </Box>

            </VStack>


        </>
    )
}

export default DashboardBasic