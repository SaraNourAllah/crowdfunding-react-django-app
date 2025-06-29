import React from 'react'
import Api from '../endpoints/Api.jsx'

export default function About() {
    return (
        <div>
            <h1>From About Page{Api.message}</h1>

        </div>
    )
}
