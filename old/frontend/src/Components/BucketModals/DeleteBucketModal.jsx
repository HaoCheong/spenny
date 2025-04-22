//Display Modal for creating, updating and deleting buckets

import {
    Alert,
    AlertDescription,
    AlertIcon,
    AlertTitle,
    Button,
    Input,
    Modal,
    ModalBody,
    ModalCloseButton,
    ModalContent,
    ModalFooter,
    ModalHeader,
    ModalOverlay,
    Select,
    Textarea,
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

const DeleteBucketModal = () => {
    const { isOpen, onOpen, onClose } = useDisclosure()
    const [alertInfo, setAlertInfo] = React.useState({
        isOpen: false,
        type: '',
        message: '',
    })

    const [bucketList, setBucketList] = React.useState([])
    const getAllBuckets = async () => {
        const res = await axios.get(`${BACKEND_URL}/api/v1/buckets`)
        setBucketList(res.data)
    }

    React.useEffect(() => {
        getAllBuckets()
    }, [])

    const formik = useFormik({
        initialValues: {
            bucket_remove: 0,
        },
        validationSchema: yup.object({
            bucket_remove: yup.number('Enter Bucket to remove'),
        }),
        onSubmit: async (values) => {
            try {
                await axios.delete(
                    `${BACKEND_URL}/api/v1/bucket/${values.bucket_remove}`
                )
                setAlertInfo({
                    isOpen: true,
                    type: 'success',
                    message: 'Bucket Successfully Removed',
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
                Delete Bucket
            </MenuItem>
            <Modal isOpen={isOpen} onClose={onClose}>
                <ModalOverlay />
                <form onSubmit={formik.handleSubmit}>
                    <ModalContent>
                        <ModalHeader>Delete bucket</ModalHeader>
                        <ModalCloseButton />
                        <ModalBody>
                            <VStack spacing="1em">
                                <FormValidator
                                    formik={formik}
                                    propName="to_bucket_id"
                                >
                                    <Select
                                        placeholder="Select bucket to remove"
                                        onChange={(e) => {
                                            formik.setFieldValue(
                                                'bucket_remove',
                                                parseInt(e.target.value)
                                            )
                                        }}
                                    >
                                        {bucketList.map((bucket, idx) => {
                                            return (
                                                <option
                                                    key={idx}
                                                    value={bucket.id}
                                                >
                                                    {bucket.name}
                                                </option>
                                            )
                                        })}
                                    </Select>
                                </FormValidator>
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

export default DeleteBucketModal
