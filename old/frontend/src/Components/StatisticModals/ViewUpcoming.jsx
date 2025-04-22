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
} from '@chakra-ui/react'
import React from 'react'
import { QuestionIcon } from '@chakra-ui/icons'

const ViewUpcoming = () => {
    const { isOpen, onOpen, onClose } = useDisclosure()
    return (
        <>
            <MenuItem onClick={onOpen} icon={<QuestionIcon />}>
                View Upcoming Transactions
            </MenuItem>
            <Modal isOpen={isOpen} onClose={onClose}>
                <ModalOverlay />
                <ModalContent>
                    <ModalHeader>In Progress</ModalHeader>
                    <ModalCloseButton />
                    <ModalBody>In Progress</ModalBody>
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

export default ViewUpcoming
