import React from 'react'
import { fetch } from 'react-fetch'
export default function ShowsScreen(){
    const upcomingShows = fetch('http://localhost:3000/api/news').json()

    return(
        <div>
            <h1>Shows Screen</h1>
            <ul className="shows-list">
                {upcomingShows.map((show) => (
                    <li key={show.id}>
                        <p>{show}</p>
                    </li>
                ))}
            </ul>
        </div>
    )}