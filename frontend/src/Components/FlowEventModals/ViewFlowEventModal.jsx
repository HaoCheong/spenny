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

import { freqToText, amountToText, dateToText } from './helper.jsx'

const ViewFlowEventModal = ({ fe }) => {
    const { isOpen, onOpen, onClose } = useDisclosure()
    
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
                            <ListItem><b>Description</b>: {fe.description}</ListItem>
                            <ListItem><b>Frequency</b>: {freqToText({fe})}</ListItem>
                            <ListItem><b>Change Amount</b>: {amountToText({fe})}</ListItem>
                            <ListItem><b>Next date</b>: {fe.next_trigger}</ListItem>
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
