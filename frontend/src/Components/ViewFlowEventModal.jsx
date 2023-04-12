import { ViewIcon } from '@chakra-ui/icons'
import {
    Button,
    IconButton,
    ListItem,
    Modal,
    ModalBody,
    ModalCloseButton,
    ModalContent,
    ModalFooter,
    ModalHeader,
    ModalOverlay,
    UnorderedList,
    useDisclosure,
} from '@chakra-ui/react'
import React from 'react'

const ViewFlowEventModal = ({ fe }) => {
    const { isOpen, onOpen, onClose } = useDisclosure()

    //Change the frequency to english text
    const freqToText = () => {
        const interval = fe.frequency.slice(-1)
        const time = fe.frequency.slice(0, -1)
        // console.log(time, interval)
        switch (interval) {
            case 'n':
                return `${time} Minute(s)`
            case 'h':
                return `${time} Hour(s)`
            case 'd':
                return `${time} Days(s)`
            case 'w':
                return `${time} Week(s)`
            case 'm':
                return `${time} Month(s)`
            case 'y':
                return `${time} Year(s)`
            default:
                break
        }
    }

    const amountToText = () => {
        switch (fe.type) {
            case 'ADD':
                return `+${fe.change_amount}`
            case 'SUB':
                return `-${fe.change_amount}`
            case 'MOV':
                return `Moving ${fe.change_amount}`
            default:
                break
        }
    }

    //Given type and amount generate english text

    //Convert Date to Readable standard
    const dateToText = () => {}

    // console.log('FE', fe)
    return (
        <>
            <IconButton icon={<ViewIcon />} onClick={onOpen} />
            <Modal isOpen={isOpen} onClose={onClose}>
                <ModalOverlay />
                <ModalContent>
                    <ModalHeader>{fe.name}</ModalHeader>
                    <ModalCloseButton />
                    <ModalBody>
                        <UnorderedList>
                            <ListItem>Description: {fe.description}</ListItem>
                            <ListItem>Frequency: {freqToText()}</ListItem>
                            <ListItem>Change Amount: {amountToText()}</ListItem>
                            <ListItem>Next date: {fe.next_trigger}</ListItem>
                        </UnorderedList>
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

export default ViewFlowEventModal
