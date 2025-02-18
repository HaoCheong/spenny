import {
    Button,
    ListItem,
    UnorderedList,
    Modal,
    ModalBody,
    ModalCloseButton,
    ModalContent,
    ModalFooter,
    ModalHeader,
    ModalOverlay,
    useDisclosure,
} from '@chakra-ui/react'
import React from 'react'

const ViewBucketModal = ({ bucket }) => {
    const { isOpen, onOpen, onClose } = useDisclosure()
    return (
        <>
            <Button
                onClick={onOpen}
                variant="solid"
                bgColor="#aedf8b"
                color="black"
            >
                View Bucket
            </Button>
            <Modal isOpen={isOpen} onClose={onClose}>
                <ModalOverlay />
                <ModalContent>
                    <ModalHeader>{bucket.name}</ModalHeader>
                    <ModalCloseButton />
                    <ModalBody>
                        <UnorderedList>
                            <ListItem>
                                Current Amount: {bucket.current_amount}
                            </ListItem>
                            <ListItem>
                                Description: {bucket.description}
                            </ListItem>
                            <ListItem>
                                Invisible (Not counted in total):{' '}
                                {bucket.properties.invisible ? 'True' : 'False'}
                            </ListItem>
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

export default ViewBucketModal
