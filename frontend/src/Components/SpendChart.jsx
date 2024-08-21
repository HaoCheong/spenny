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
    const [bucket, setBucket] = React.useState({})

    const getLogs = async () => {
        const cap_date = new Date(new Date().setHours(0, 0, 0, 0))
        cap_date.setDate(cap_date.getDate() - DATE_CAP)
        const cap_date_str = `${cap_date.getDate()}-${cap_date.getMonth() + 1
            }-${cap_date.getFullYear()}`

        const res = await axios.get(
            `${BACKEND_URL}/api/v1/logs/${bucket_id}/${cap_date_str}`
        )
        setLogs(res.data)
    }

    const getBucketData = async () => {
        const res = await axios.get(`${BACKEND_URL}/api/v1/bucket/${bucket_id}`)
        setBucket(res.data)
    }

    const spendingMapper = async () => {
        const dateHash = {}
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
        setDataPoints(points)
    }

    const changeInAmountMapper = async () => {
        const dateHash = {}
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
        let curr_amount = bucket.current_amount
        Object.entries(dateHash)
            .slice()
            .reverse()
            .forEach(([key, value]) => {
                curr_amount -= value
                points.push({ name: key, amt: curr_amount })
            })
        setDataPoints(points.slice().reverse())
    }

    // startup()

    React.useEffect(() => {
        getLogs()
        getBucketData()
    }, [])

    React.useEffect(() => {
        changeInAmountMapper()
    }, [logs])

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
