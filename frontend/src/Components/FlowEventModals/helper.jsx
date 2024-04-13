//Change the frequency to english text
export const freqToText = ({fe}) => {
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

// Converts the type and amount to a textual response
export const amountToText = ({fe}) => {
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

//Convert Date to Readable standard TODO
export const dateToText = ({fe}) => {}