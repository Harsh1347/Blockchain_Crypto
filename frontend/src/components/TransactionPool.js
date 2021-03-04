import React, { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { Button } from 'react-bootstrap'

import Transaction from './Transaction'
import history from '../history'

import { API_BASE_URL, SECONDS_JS } from '../config'


const POLL_INTERVAL = 10 * SECONDS_JS

function TransactionPool() {
    const [transactions, setTransactions] = useState([])

    const fetchTransaction = () => {
        fetch(`${API_BASE_URL}/transactions`)
            .then(response => response.json())
            .then(json => setTransactions(json))
    }

    useEffect(() => {
        fetchTransaction()

        const intervalId = setInterval(fetchTransaction, POLL_INTERVAL)

        return () => clearInterval(intervalId)
    }, [])

    const fetchMineBlock = () => {
        fetch(`${API_BASE_URL}/blockchain/mine`)
            .then(() => {
                alert('Success!')

                history.push('/blockchain')
            })
    }

    return (
        <div className='TransactionPool'>
            <Link to='/'>Home</Link>
            <hr />
            <h3>Transaction Pool</h3>
            <div>
                {
                    transactions.map(transaction => (
                        <div key={transaction.id}>
                            <hr />
                            <Transaction transaction={transaction} />
                        </div>
                    ))
                }
            </div>
            <hr />
            <Button variant='danger' size='sm' onClick={fetchMineBlock}>
                Mine a block of these transaction
                </Button>
        </div>
    )
}

export default TransactionPool
