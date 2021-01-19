import React from 'react';
import { Link } from 'react-router-dom';

export defualt function Navbar(){
    return(
        <nav>
            <ul>
                <li>
                    <Link to="/">Home</Link>
                </li>
                <li>
                    <Link to="/bio">Bio</Link>
                </li>
                <li>
                    <Link to="/gallery">Gallery</Link>
                </li>
                <li>
                    <Link to="/live">Live</Link>
                </li>
                <li>
                    <Link to="/videos">Videos</Link>
                </li>
            </ul>
        </nav>
    )
}