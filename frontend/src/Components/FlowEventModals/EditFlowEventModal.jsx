///Display Modal for creating, updating and deleting buckets

import {
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
    IconButton
} from '@chakra-ui/react'
import { EditIcon } from '@chakra-ui/icons'
import { useFormik } from 'formik'
import * as yup from 'yup'
import React from 'react'
import FormValidator from '../FormValidator'

import { BACKEND_URL } from '../../config.js'
import axios from 'axios'
import ResponseAlert from '../ResponseAlert'

const EditFlowEventModal = ({fe}) => {
    const { isOpen, onOpen, onClose } = useDisclosure()
    const [alertInfo, setAlertInfo] = React.useState({
        isOpen: false,
        type: '',
        message: '',
    })
    const [bucketList, setBucketList] = React.useState([])

    const getAllBuckets = async () => {
        const res = await axios.get(`${BACKEND_URL}/buckets`)
        setBucketList(res.data)
    }

    React.useEffect(() => {
        getAllBuckets()
    }, [])

    

    const formik = useFormik({
        initialValues: {
            name: '',
            description: '',
            change_amount: 0,
            type: '',
            frequency: '',
            next_trigger: '',
            from_bucket_id: null,
            to_bucket_id: null,
        },
        validationSchema: yup.object({
            name: yup
                .string('Enter Bucket Name')
                .required('Bucket Name Required'),
            description: yup
                .string('Enter Bucket Description')
                .required('Bucket Description Required'),
            change_amount: yup.number('Enter a valid starting amount'),
            type: yup
                .string('Enter flow event type')
                .matches('^(ADD|SUB|MOV)$', 'Has to either ADD, SUB, MOV'),
            frequency: yup
                .string('Enter your frequency of trigger')
                .matches(
                    '^[0-9]+(n|h|d|w|m|y){1}$',
                    'It does not match expected format. (I.E 1n = 1 Minute, 3h = 3 Hours)'
                ),
        }),
        onSubmit: async (values) => {
            const newFlowEvent = {
                name: values.name,
                description: values.description,
                change_amount: parseFloat(values.change_amount),
                type: values.type,
                frequency: values.frequency,
                next_trigger: values.next_trigger,
                from_bucket_id: values.from_bucket_id,
                to_bucket_id: values.to_bucket_id,
            }
            console.log("newFlowEvent", newFlowEvent)
            try {
                await axios.patch(`${BACKEND_URL}/flowEvent/${fe.id}`, newFlowEvent)
                setAlertInfo({
                    isOpen: true,
                    type: 'success',
                    message: 'Flow Event Successfully Created',
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

    const handleOpen = () => {
        formik.setFieldValue('name',fe.name)
        formik.setFieldValue('description',fe.description)
        formik.setFieldValue('change_amount',fe.change_amount)
        formik.setFieldValue('type',fe.type)
        formik.setFieldValue('frequency',fe.frequency)
        formik.setFieldValue('next_trigger',fe.next_trigger)
        formik.setFieldValue('from_bucket_id',fe.from_bucket_id)
        formik.setFieldValue('to_bucket_id',fe.to_bucket_id)
        onOpen()
    }

    return (
        <>
            <IconButton icon={<EditIcon />} onClick={handleOpen} />
            <Modal isOpen={isOpen} onClose={onClose}>
                <ModalOverlay />
                <form onSubmit={formik.handleSubmit}>
                    <ModalContent>
                        <ModalHeader>Edit New Flow Event</ModalHeader>
                        <ModalCloseButton />
                        <ModalBody>
                            <VStack spacing="1em">
                                <FormValidator formik={formik} propName="name">
                                    <Input
                                        id="name"
                                        placeholder="Flow Event Name"
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
                                        placeholder="Flow Event Description"
                                        focusBorderColor="blue.500"
                                        onChange={formik.handleChange}
                                        value={formik.values.description}
                                        sx={{ height: '10em' }}
                                        resize="none"
                                    />
                                </FormValidator>

                                <FormValidator
                                    formik={formik}
                                    propName="change_amount"
                                >
                                    <Input
                                        id="change_amount"
                                        placeholder="Amount to change"
                                        focusBorderColor="blue.500"
                                        onChange={formik.handleChange}
                                        value={formik.values.change_amount}
                                    />
                                </FormValidator>
                                <FormValidator formik={formik} propName="type">
                                    <Select
                                        placeholder="Select Flow Event Type"
                                        onChange={(e) => {
                                            formik.setFieldValue(
                                                'type',
                                                e.target.value
                                            )
                                        }}
                                        value={formik.values.type}
                                    >
                                        <option value="ADD">
                                            ADD: Add Money into a Bucket
                                        </option>
                                        <option value="SUB">
                                            SUB: Substract Money from a Bucket
                                        </option>
                                        <option value="MOV">
                                            MOV: Move Money from one Bucket to
                                            another
                                        </option>
                                    </Select>
                                </FormValidator>
                                <FormValidator
                                    formik={formik}
                                    propName="Frequency"
                                >
                                    <Input
                                        id="frequency"
                                        placeholder="Flow Event Frequency"
                                        focusBorderColor="blue.500"
                                        onChange={formik.handleChange}
                                        value={formik.values.frequency}
                                    />
                                </FormValidator>
                                <FormValidator
                                    formik={formik}
                                    propName="next_trigger"
                                >
                                    <Input
                                        id="next_trigger"
                                        placeholder="Start Date and time"
                                        focusBorderColor="blue.500"
                                        onChange={formik.handleChange}
                                        value={formik.values.next_trigger}
                                        type="datetime-local"
                                    />
                                </FormValidator>
                                {formik.values.type === 'ADD' ? (
                                    <></>
                                ) : (
                                    <FormValidator
                                        formik={formik}
                                        propName="from_bucket_id"
                                    >
                                        <Select
                                            placeholder="Select Bucket to flow from"
                                            onChange={(e) => {
                                                formik.setFieldValue(
                                                    'from_bucket_id',
                                                    parseInt(e.target.value)
                                                )
                                            }}
                                            value={formik.values.from_bucket_id}
                                            
                                        >
                                            {bucketList.map((bucket, idx) => {
                                                return (
                                                    <option
                                                        key={idx}
                                                        value={parseInt(
                                                            bucket.id
                                                        )}
                                                    >
                                                        {bucket.name}
                                                    </option>
                                                )
                                            })}
                                        </Select>
                                    </FormValidator>
                                )}

                                {formik.values.type === 'SUB' ? (
                                    <></>
                                ) : (
                                    <FormValidator
                                        formik={formik}
                                        propName="to_bucket_id"
                                    >
                                        <Select
                                            placeholder="Select bucket to flow to"
                                            onChange={(e) => {
                                                formik.setFieldValue(
                                                    'to_bucket_id',
                                                    parseInt(e.target.value)
                                                )
                                            }}
                                            value={formik.valuesto_bucket_id}
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
                                )}
                                <ResponseAlert alertInfo={alertInfo} />
                            </VStack>
                        </ModalBody>

                        <ModalFooter>
                            <Button colorScheme="green" type="submit">
                                Edit
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

export default EditFlowEventModal
