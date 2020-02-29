import React from 'react';
import './BottomNav.css';
import {NavLink} from "react-router-dom";
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {faUserCircle, faHandPointRight, faTrophy as faMedal} from '@fortawesome/free-solid-svg-icons'

class BottomNav extends React.Component {
  render() {
        return (
          <nav>
            <NavLink to="/pokes" className="nav-item" activeClassName="active" >
                <FontAwesomeIcon icon={faHandPointRight} />
                <div className="label">Pokes</div>
            </NavLink>
            <NavLink to="/rewards" className="nav-item" activeClassName="active" >
                <FontAwesomeIcon icon={faMedal} />
                <div className="label">Rewards</div>
            </NavLink>
            <NavLink to="/user" className="nav-item" activeClassName="active" >
                <FontAwesomeIcon icon={faUserCircle} />
                <div className="label">User</div>
            </NavLink>
          </nav>
        );
    }
}

export default BottomNav;