//Modal for the action of bringing forward

import {
    Alert,
    AlertIcon,
    Button,
    FormControl,
    FormLabel,
    IconButton,
    ListItem,
    Modal,
    ModalBody,
    ModalCloseButton,
    ModalContent,
    ModalFooter,
    ModalHeader,
    ModalOverlay,
    Switch,
    UnorderedList,
    VStack,
    useDisclosure,
} from '@chakra-ui/react'

import { ArrowForwardIcon, } from '@chakra-ui/icons'
import { useFormik } from 'formik'
import React from 'react'
import FormValidator from '../FormValidator'

import { BACKEND_URL } from '../../config.js'
import axios from 'axios'
import { freqToText, amountToText, dateToText } from './helper.jsx'
import ResponseAlert from '../ResponseAlert.jsx'

/**
 * Notes:
 * - 2 types of bring forward
 *  - Trigger with money: Premptively bring forward cash of that day and do said trasnfer of money
 *  - Trigger without money: Premeptive bring forward cash but do not do said transfer of money. Simply bring date forward
 * */


const BringForwardModal = ({ fe }) => {
    const { isOpen, onOpen, onClose } = useDisclosure()

    const [alertInfo, setAlertInfo] = React.useState({
        isOpen: false,
        type: '',
        message: '',
    })


    const formik = useFormik({
        initialValues: {
            money_include: false,
        },
        onSubmit: async (values) => {
            const newBringForward = {
                money_include: values.money_include,
                flow_event_id: fe.id,
            }
            try {
                await axios.put(`${BACKEND_URL}/api/v1/bringForward`, newBringForward)
                setAlertInfo({
                    isOpen: true,
                    type: 'success',
                    message: 'Successfully brought forward event',
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
            <IconButton icon={<ArrowForwardIcon />} onClick={onOpen} />
            <Modal isOpen={isOpen} onClose={onClose}>
                <ModalOverlay />
                <form onSubmit={formik.handleSubmit}>
                    <ModalContent>
                        <ModalHeader>Bring forward next trigger</ModalHeader>
                        <ModalCloseButton />
                        <ModalBody>
                            <VStack spacing="2em">

                                <Alert status='info'>
                                    <AlertIcon />
                                    This action will bring the date forward up to the next trigger date.
                                </Alert>


                                <UnorderedList>
                                    <ListItem><b>Description</b>: {fe.description}</ListItem>
                                    <ListItem><b>Frequency</b>: {freqToText({ fe })}</ListItem>
                                    <ListItem><b>Change Amount</b>: {amountToText({ fe })}</ListItem>
                                    <ListItem><b>Next date</b>: {fe.next_trigger}</ListItem>
                                </UnorderedList>

                                <FormValidator
                                    formik={formik}
                                    propName="money_include"
                                >
                                    <FormControl
                                        display="flex"
                                        alignItems="center"
                                    >
                                        <FormLabel>
                                            Money Inclusive:
                                        </FormLabel>
                                        <Switch
                                            onChange={(e) => {
                                                formik.setFieldValue(
                                                    'money_include',
                                                    e.target.checked
                                                )
                                            }}
                                            value={formik.values.money_include}
                                        />
                                    </FormControl>
                                </FormValidator>

                                {formik.values.money_include ?
                                    <Alert status='warning'>
                                        <AlertIcon />
                                        Checking this means you will transfer the money as specified as well as move the date. Runs as if you are triggering the flow event pre-emptively
                                    </Alert> : <></>}

                                <ResponseAlert alertInfo={alertInfo} />

                            </VStack>
                        </ModalBody>

                        <ModalFooter>
                            <Button colorScheme="green" type="submit">
                                Forward
                            </Button>
                            <Button
                                colorScheme="blue"
                                ml={3}
                                onClick={() => {
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

export default BringForwardModal
