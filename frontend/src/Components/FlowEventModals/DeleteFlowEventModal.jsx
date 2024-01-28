//Display Modal for creating, updating and deleting buckets

import {
    Button,
    Modal,
    ModalBody,
    ModalCloseButton,
    ModalContent,
    ModalFooter,
    ModalHeader,
    ModalOverlay,
    Select,
    useDisclosure,
    VStack,
    MenuItem,
} from '@chakra-ui/react'
import { DeleteIcon } from '@chakra-ui/icons'
import { useFormik } from 'formik'
import * as yup from 'yup'
import React from 'react'
import FormValidator from '../FormValidator'

import { BACKEND_URL } from '../../config.js'
import axios from 'axios'
import ResponseAlert from '../ResponseAlert'

const DeleteFlowEventModal = () => {
    const { isOpen, onOpen, onClose } = useDisclosure()
    const [alertInfo, setAlertInfo] = React.useState({
        isOpen: false,
        type: '',
        message: '',
    })

    const [bucketList, setBucketList] = React.useState([])
    const [flowEventList, setFlowEventList] = React.useState([])
    const getAllBuckets = async () => {
        const res = await axios.get(`${BACKEND_URL}/buckets`)
        setBucketList(res.data)
    }

    const getBucketFlowEvents = async (bucket_id) => {
        const res = await axios.get(`${BACKEND_URL}/bucket/${bucket_id}`)
        const allFlowEvents = res.data.from_events.concat(res.data.to_events)
        console.log('ALL FE', allFlowEvents)
        setFlowEventList(allFlowEvents)
    }

    React.useEffect(() => {
        getAllBuckets()
    }, [])

    const formik = useFormik({
        initialValues: {
            flowEvent_remove: 0,
        },
        validationSchema: yup.object({
            flowEvent_remove: yup.number('Enter flowEvent to remove'),
        }),
        onSubmit: async (values) => {
            // console.log('Values', values
            try {
                await axios.delete(
                    `${BACKEND_URL}/flowEvent/${values.flowEvent_remove}`
                )
                setAlertInfo({
                    isOpen: true,
                    type: 'success',
                    message: 'Flow Event Successfully Removed',
                })
            } catch (err) {
                setAlertInfo({
                    isOpen: true,
                    type: 'error',
                    message: err.response.data.detail,
                })
            }
        },
    })

    return (
        <>
            <MenuItem onClick={onOpen} icon={<DeleteIcon />}>
                Delete Flow Event
            </MenuItem>
            <Modal isOpen={isOpen} onClose={onClose}>
                <ModalOverlay />
                <form onSubmit={formik.handleSubmit}>
                    <ModalContent>
                        <ModalHeader>Delete flow event</ModalHeader>
                        <ModalCloseButton />
                        <ModalBody>
                            <VStack spacing="1em">
                                <Select
                                    placeholder="Select bucket to remove flow event from"
                                    onChange={(e) => {
                                        getBucketFlowEvents(e.target.value)
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

                                {flowEventList.length === 0 ? (
                                    <></>
                                ) : (
                                    <FormValidator
                                        formik={formik}
                                        propName="flowEvent_remove"
                                    >
                                        <Select
                                            placeholder="Select Flow Event to Remove"
                                            onChange={(e) => {
                                                formik.setFieldValue(
                                                    'flowEvent_remove',
                                                    parseInt(e.target.value)
                                                )
                                            }}
                                        >
                                            {flowEventList.map((fe, idx) => {
                                                return (
                                                    <option
                                                        key={idx}
                                                        value={fe.id}
                                                    >
                                                        {fe.name}
                                                    </option>
                                                )
                                            })}
                                        </Select>
                                    </FormValidator>
                                )}

                                <ResponseAlert alertInfo={alertInfo} />
                            </VStack>
                        </ModalBody>

                        <ModalFooter>
                            <Button colorScheme="red" type="submit">
                                Delete
                            </Button>
                            <Button
                                colorScheme="blue"
                                ml={3}
                                onClick={() => {
                                    setAlertInfo({ isOpen: false })
                                    onClose()
                                }}
                            >
                                Close
                            </Button>
                        </ModalFooter>
                    </ModalContent>
                </form>
            </Modal>
        </>
    )
}

export default DeleteFlowEventModal
