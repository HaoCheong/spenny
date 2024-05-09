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
    Textarea,
    useDisclosure,
    VStack,
    MenuItem,
    Switch,
    FormControl,
    FormLabel,
} from '@chakra-ui/react'
import { AddIcon } from '@chakra-ui/icons'
import { useFormik } from 'formik'
import * as yup from 'yup'
import React from 'react'
import FormValidator from '../FormValidator'

import { BACKEND_URL } from '../../config.js'
import axios from 'axios'
import ResponseAlert from '../ResponseAlert'

const CreateBucketModal = () => {
    const { isOpen, onOpen, onClose } = useDisclosure()
    const [alertInfo, setAlertInfo] = React.useState({
        isOpen: false,
        type: '',
        message: '',
    })

    const formik = useFormik({
        initialValues: {
            name: '',
            description: '',
            curr_amount: 0,
            invisible: false,
        },
        validationSchema: yup.object({
            name: yup
                .string('Enter Bucket Name')
                .required('Bucket Name Required'),
            description: yup
                .string('Enter Bucket Description')
                .required('Bucket Description Required'),
            curr_amount: yup
                .number('Enter a valid starting amount')
                .required("Please enter a valid starting amount, 0 at the minimum"),
        }),
        onSubmit: async (values) => {
            const newBucket = {
                name: values.name,
                description: values.description,
                current_amount: parseFloat(values.curr_amount),
                properties: {
                    invisible: values.invisible,
                },
            }
            try {
                await axios.post(`${BACKEND_URL}/bucket`, newBucket)
                setAlertInfo({
                    isOpen: true,
                    type: 'success',
                    message: 'Bucket Successfully Created',
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
            <MenuItem onClick={onOpen} icon={<AddIcon />}>
                Add Bucket
            </MenuItem>
            <Modal isOpen={isOpen} onClose={onClose}>
                <ModalOverlay />
                <form onSubmit={formik.handleSubmit}>
                    <ModalContent>
                        <ModalHeader>Create New Bucket</ModalHeader>
                        <ModalCloseButton />
                        <ModalBody>
                            <VStack spacing="1em">
                                <FormValidator formik={formik} propName="name">
                                    <Input
                                        id="name"
                                        placeholder="Bucket Name"
                                        focusBorderColor="blue.500"
                                        onChange={formik.handleChange}
                                        value={formik.values.name}
                                    />
                                </FormValidator>

                                <FormValidator
                                    formik={formik}
                                    propName="description"
                                >
                                    <Textarea
                                        id="description"
                                        placeholder="Bucket Description"
                                        focusBorderColor="blue.500"
                                        onChange={formik.handleChange}
                                        value={formik.values.description}
                                        sx={{ height: '10em' }}
                                        resize="none"
                                    />
                                </FormValidator>

                                <FormValidator
                                    formik={formik}
                                    propName="curr_amount"
                                >
                                    <Input
                                        id="curr_amount"
                                        placeholder="Current Amount"
                                        focusBorderColor="blue.500"
                                        onChange={formik.handleChange}
                                        value={formik.values.curr_amount}
                                    />
                                </FormValidator>
                                <FormValidator
                                    formik={formik}
                                    propName="invisible"
                                >
                                    <FormControl
                                        display="flex"
                                        alignItems="center"
                                    >
                                        <FormLabel>
                                            Invisible (Not counted in total)
                                        </FormLabel>
                                        <Switch
                                            onChange={(e) => {
                                                formik.setFieldValue(
                                                    'invisible',
                                                    e.target.checked
                                                )
                                            }}
                                            value={formik.values.invisible}
                                        />
                                    </FormControl>
                                </FormValidator>

                                <ResponseAlert alertInfo={alertInfo} />
                            </VStack>
                        </ModalBody>

                        <ModalFooter>
                            <Button colorScheme="green" type="submit">
                                Create
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

export default CreateBucketModal
