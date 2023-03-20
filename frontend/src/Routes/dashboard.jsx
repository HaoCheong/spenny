import { AddIcon, ChevronDownIcon } from '@chakra-ui/icons'
import { Box, Button, Menu, MenuButton, MenuItem, MenuList } from '@chakra-ui/react'
import ReactFlow, { Background, Controls, applyNodeChanges, applyEdgeChanges } from 'reactflow';
import 'reactflow/dist/style.css';
import React from 'react'
import axios from 'axios'

const BACKEND_URL = "http://127.0.0.1:8000"
let pos_x = 10
let pos_y = 10


const Dashboard = () => {
    
    const [BucketNodes, setBucketNodes] = React.useState([])
    const [FlowEventNodes, setFlowEventNodes] = React.useState([])

    const [allNodes, setAllNodes] = React.useState([])

    const bucketGenerator = (bucket) => {
        pos_x += 10
        pos_y += 10
        const bucketRFNode = {
            id: `B_${bucket.id}`,
            position: {x: pos_x, y: pos_y},
            data: { label: `Bucket: ${bucket.name}` },
        }
        console.log(bucketRFNode)
        return bucketRFNode
    }

    const flowEventGenerator = (fe) => {
        pos_x += 10
        pos_y += 10
        const flowEventRFNode = {
            id: `FE_${fe.id}`,
            position: {x: pos_x, y: pos_y},
            data: { label: `Flow Event: ${fe.name}` },
        }
        console.log(flowEventRFNode)
        return flowEventRFNode
    }

    const getNodes = async () => {
        const bucketRFNodes = await getBucketNodes()
        const flowEventRFNodes = await getFlowEventNodes()
        const allRFNodes = bucketRFNodes.concat(flowEventRFNodes)
        console.log("ALL NODES",bucketRFNodes, flowEventRFNodes)
        setAllNodes(allRFNodes)
    }

    // Generate all bucket nodes
    const getBucketNodes = async () => {
        console.log("Creating all bucket nodes")
        const res = await axios.get(`${BACKEND_URL}/buckets`)
        const data = res.data
        
        const bucketRFNodes = data.map((bucket) => {
            return bucketGenerator(bucket)
        })

        return bucketRFNodes
    }
    // Generate all flow event nodes
    const getFlowEventNodes = async () => {
        console.log("Creating all flow event nodes")
        const res = await axios.get(`${BACKEND_URL}/flowEvents`)
        const data = res.data
        const flowEventRFNodes = data.map((fe) => {
            return flowEventGenerator(fe)
        })
        return flowEventRFNodes
    }

    const onNodesChange = React.useCallback(
        (changes) => setAllNodes((nds) => applyNodeChanges(changes, nds)),
    []);

    React.useEffect(() => {
        getNodes()
    },[])


    return (
        <>
            <Box sx={{margin: "1em", width: "100%"}}>
                <Menu>
                    <MenuButton as={Button} rightIcon={<ChevronDownIcon />}>
                        Actions
                    </MenuButton>
                    <MenuList>
                        <MenuItem icon={<AddIcon/>}>Add Bucket</MenuItem>
                        <MenuItem icon={<AddIcon/>}>Add Flow</MenuItem>
                    </MenuList>
                </Menu>
            </Box>
            <Box sx={{height: "90vh", width: "100vw"}}>
                <ReactFlow nodes={allNodes} onNodesChange={onNodesChange}>
                    <Background />
                    <Controls />
                </ReactFlow>
            </Box>
        </>
    )
}

export default Dashboard