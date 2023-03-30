import React from 'react'
import axios from 'axios'
import { BACKEND_URL } from '../config'
import {
    Area,
    AreaChart,
    CartesianGrid,
    ReferenceLine,
    ResponsiveContainer,
    Tooltip,
    XAxis,
    YAxis,
} from 'recharts'

// Group by days for now, display 10 days

const SpendChart = ({ bucket_id }) => {
    const [logs, setLogs] = React.useState([])
    const [dataPoints, setDataPoints] = React.useState([])

    const getLogs = async () => {
        const res = await axios.get(`${BACKEND_URL}/logs/${1}`)
        console.log('LOG res', res.data)
        setLogs(res.data)
    }

    const logsDataMapper = () => {
        const dateHash = {}
        const today = new Date()
        console.log('TODAY RAW', today)
        console.log('TODAY MID', today.setHours(0, 0, 0, 0))

        //Find the dates of the last 28 days
        //For Each day
        //Group the logs into groups of days, sum the amount, set as data point (You can parse dates from python style to js style directly)
        //Cap until 28 days (you can have a config to set limit)
        //Pass into bucket
    }

    React.useEffect(() => {
        getLogs()
        logsDataMapper()
    }, [])

    const data = [
        {
            name: 'Page A',
            uv: 4000,
            pv: 2400,
            amt: 2400,
        },
        {
            name: 'Page B',
            uv: 3000,
            pv: 1398,
            amt: 2210,
        },
        {
            name: 'Page C',
            uv: 2000,
            pv: 9800,
            amt: 2290,
        },
        {
            name: 'Page D',
            uv: 2780,
            pv: 3908,
            amt: 2000,
        },
        {
            name: 'Page E',
            uv: 1890,
            pv: 4800,
            amt: 2181,
        },
        {
            name: 'Page F',
            uv: 2390,
            pv: 3800,
            amt: 2500,
        },
        {
            name: 'Page G',
            uv: 3490,
            pv: 4300,
            amt: 2100,
        },
    ]

    return (
        <ResponsiveContainer width="100%" height={200}>
            <AreaChart
                data={data}
                margin={{ top: 20, right: 30, left: 0, bottom: 0 }}
            >
                <XAxis dataKey="time" />
                <YAxis />
                <CartesianGrid strokeDasharray="3 3" />
                <Tooltip />
                <ReferenceLine x="Page C" stroke="green" label="Min PAGE" />
                <ReferenceLine
                    y={4000}
                    label="Max"
                    stroke="red"
                    strokeDasharray="3 3"
                />
                <Area
                    type="monotone"
                    dataKey="uv"
                    stroke="#8884d8"
                    fill="#8884d8"
                />
            </AreaChart>
        </ResponsiveContainer>
    )
}

export default SpendChart
