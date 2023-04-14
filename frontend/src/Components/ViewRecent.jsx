import {
    Button,
    Modal,
    ModalBody,
    ModalCloseButton,
    ModalContent,
    ModalFooter,
    ModalHeader,
    ModalOverlay,
    useDisclosure,
    MenuItem,
    VStack,
    Select,
    Divider,
} from '@chakra-ui/react'
import React from 'react'
import { QuestionIcon } from '@chakra-ui/icons'

import { BACKEND_URL } from '../config.js'
import axios from 'axios'
import LogCard from './LogCard'

const ViewRecent = () => {
    const { isOpen, onOpen, onClose } = useDisclosure()

    const [bucketList, setBucketList] = React.useState([])
    const [logList, setLogList] = React.useState([])
    const getAllBuckets = async () => {
        const res = await axios.get(`${BACKEND_URL}/buckets`)
        setBucketList(res.data)
    }
    const getLogs = async (bucket_id) => {
        const cap_date = new Date(0)
        const cap_date_str = `${cap_date.getDate()}-${
            cap_date.getMonth() + 1
        }-${cap_date.getFullYear()}`

        const res = await axios.get(
            `${BACKEND_URL}/logs/${bucket_id}/${cap_date_str}`
        )
        setLogList(res.data)
    }

    React.useEffect(() => {
        getAllBuckets()
    }, [])
    return (
        <>
            <MenuItem onClick={onOpen} icon={<QuestionIcon />}>
                View Recent Transactions
            </MenuItem>
            <Modal isOpen={isOpen} onClose={onClose}>
                <ModalOverlay />
                <ModalContent>
                    <ModalHeader>Recent transactions</ModalHeader>
                    <ModalCloseButton />
                    <ModalBody>
                        <VStack spacing="1em">
                            <Select
                                placeholder="All Buckets"
                                onChange={(e) => {
                                    getLogs(e.target.value)
                                }}
                            >
                                {bucketList.map((bucket, idx) => {
                                    return (
                                        <option key={idx} value={bucket.id}>
                                            {bucket.name}
                                        </option>
                                    )
                                })}
                            </Select>
                            <Divider />
                            <VStack
                                spacing="1em"
                                sx={{
                                    overflowY: 'scroll',
                                    maxH: '30rem',
                                }}
                            >
                                {logList.length === 0 ? (
                                    <></>
                                ) : (
                                    logList.map((log, idx) => {
                                        return <LogCard key={idx} log={log} />
                                    })
                                )}
                            </VStack>
                        </VStack>
                    </ModalBody>
                    <ModalFooter>
                        <Button colorScheme="blue" mr={3} onClick={onClose}>
                            Close
                        </Button>
                    </ModalFooter>
                </ModalContent>
            </Modal>
        </>
    )
}

export default ViewRecent
