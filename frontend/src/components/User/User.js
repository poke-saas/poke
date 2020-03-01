import React from 'react';
import './User.css';
import {useSelector, useDispatch} from "react-redux";
import * as pic from '../../profile_davis.jpg'
import FacebookButton from '../ConnectButton/FacebookButton';
import TwitterButton from '../ConnectButton/TwitterButton';
import InstagramButton from '../ConnectButton/InstagramButton';

const User = () => {

    const points = useSelector(state => state.points);
    const dispatch = useDispatch();

    return (
        <>
            <header>
                User
            </header>
            <main className="container">
                <div className="user-info-card">
                    <img className="user-image" src={pic} />
                    <div className="user-info">
                        <h3>Davis Keene</h3>
                        <p style={{opacity: 0.6}}><span>Member of </span><span style={{fontWeight: 600}}>Founders</span></p>
                    </div>
                </div>
                <table>
                    <name>Your Stats</name>
                    <tr>
                        <th>Point Balance</th>
                        <td>{points} pts</td>
                    </tr>
                    <tr>
                        <th>All Time Points</th>
                        <td>63 pts</td>
                    </tr>
                    <tr>
                        <th>Rewards Earned</th>
                        <td>5 Rewards</td>
                    </tr>
                </table>
                <FacebookButton 

                />
                <TwitterButton

                />
                <InstagramButton

                />
            </main>
        </>
    );
}

export default User;