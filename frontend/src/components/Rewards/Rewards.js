import React, {useState} from 'react';
import RewardCard from '../RewardCard/RewardCard';
import './Rewards.css';

const Rewards = () => {

    let initPoints = 23;

    const [points, updatePoints] = useState(initPoints);

    return (
        <>
            <header>
                Rewards
            </header>
            <div className="point-display">
                <img src="" alt=""/>
                <div className="info">
                    { points === 0
                        ?
                            <h2>Try to earn some points by doing pokes!</h2>
                        :
                            <h2>You currently have {points} points!</h2>
                    }
                    
                </div>
            </div>
            <main className="container">
                <RewardCard 
                    name="Reward Name"
                    cost={4}
                    image="hi"
                />
            </main>
        </>
    );
}

export default Rewards;