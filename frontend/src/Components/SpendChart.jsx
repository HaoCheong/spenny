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

// Group by days for now, display 28 days
const DATE_CAP = 28

const SpendChart = ({ bucket_id }) => {
    const [logs, setLogs] = React.useState([])
    const [dataPoints, setDataPoints] = React.useState([])

    const getLogs = async () => {
        const cap_date = new Date(new Date().setHours(0, 0, 0, 0))
        cap_date.setDate(cap_date.getDate() - DATE_CAP)
        const cap_date_str = `${cap_date.getDate()}-${
            cap_date.getMonth() + 1
        }-${cap_date.getFullYear()}`

        const res = await axios.get(`${BACKEND_URL}/logs/${1}/${cap_date_str}`)
        setLogs(res.data)
        // console.log('BRUH')
    }

    const logsDataMapper = async () => {
        const dateHash = {}
        console.log('LOGS', logs)
        logs.forEach((log) => {
            const curr_date = new Date(Date.parse(log.date_created))
            const date_key = `${curr_date.getDate()}-${curr_date.getMonth()}-${curr_date.getFullYear()}`

            if (dateHash[date_key]) {
                dateHash[date_key] += log.amount
            } else {
                dateHash[date_key] = log.amount
            }
        })

        let points = []
        Object.entries(dateHash).forEach(([key, value]) => {
            points.push({ name: key, amt: value })
        })
        console.log('POINTS', points)
        setDataPoints(points)
    }

    // startup()

    React.useEffect(() => {
        getLogs()
    }, [])

    React.useEffect(() => {
        logsDataMapper()
    }, [logs])

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
        {
            name: 'Page H',
            uv: 4000,
            pv: 2400,
            amt: 2400,
        },
        {
            name: 'Page I',
            uv: 3000,
            pv: 1398,
            amt: 2210,
        },
        {
            name: 'Page J',
            uv: 2000,
            pv: 9800,
            amt: 2290,
        },
        {
            name: 'Page K',
            uv: 2780,
            pv: 3908,
            amt: 2000,
        },
        {
            name: 'Page L',
            uv: 1890,
            pv: 4800,
            amt: 2181,
        },
        {
            name: 'Page M',
            uv: 2390,
            pv: 3800,
            amt: 2500,
        },
        {
            name: 'Page N',
            uv: 3490,
            pv: 4300,
            amt: 2100,
        },
        {
            name: 'Page O',
            uv: 4000,
            pv: 2400,
            amt: 2400,
        },
        {
            name: 'Page P',
            uv: 3000,
            pv: 1398,
            amt: 2210,
        },
        {
            name: 'Page Q',
            uv: 2000,
            pv: 9800,
            amt: 2290,
        },
        {
            name: 'Page R',
            uv: 2780,
            pv: 3908,
            amt: 2000,
        },
        {
            name: 'Page S',
            uv: 1890,
            pv: 4800,
            amt: 2181,
        },
        {
            name: 'Page T',
            uv: 2390,
            pv: 3800,
            amt: 2500,
        },
        {
            name: 'Page U',
            uv: 3490,
            pv: 4300,
            amt: 2100,
        },
    ]

    return (
        <ResponsiveContainer width="100%" height={200}>
            <AreaChart
                data={dataPoints}
                margin={{ top: 20, right: 30, left: 0, bottom: 0 }}
            >
                <XAxis dataKey="name" />
                <YAxis />
                <CartesianGrid strokeDasharray="3 3" />
                <Tooltip />
                <Area
                    type="monotone"
                    dataKey="amt"
                    stroke="#8884d8"
                    fill="#8884d8"
                />
            </AreaChart>
        </ResponsiveContainer>
    )
}

export default SpendChart
