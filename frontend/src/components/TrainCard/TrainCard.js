import React from 'react';
import './TrainCard.css';

class TrainCard extends React.Component {
    state = {

    };

    componentDidMount() {
        this.setState(
            {
                name: this.props.name,
                dest: this.props.dest,
                eta: this.props.eta,
                id: this.props.id
            }
        )
    }

    render() {
        return(
            <a className="train-card" href={'/train/' + this.state.id}>
                <span className="side-color" />
                <span className="train-desc">
                    <h3 className="train-name">{this.state.name}</h3>
                    <p className="train-desc-info">{this.state.dest}</p>
                </span>
                <span className="train-eta">
                    <p className="train-eta-val" style={this.state.eta === 0 ? {paddingTop: '10px'} : {}}>
                        {this.state.eta === 0 ? "due" : this.state.eta}
                        <span className="train-eta-unit">{this.state.eta === 0 ? "" : "mins"}</span>
                    </p>
                    <span className="arr">›</span>
                </span>
            </a>
        );
    }
}

export default TrainCard;