import React, { Component } from 'react';

class Counter extends Component {
    state = {
        count: this.props.value
    };

    increment = () => {
        this.setState({ count: this.state.count + 1 });
    }

    decrement = () => {
        this.setState({ count: this.state.count - 1 });
    }

    render() {
        return (
            <div className="counter">
                <span>{this.state.count}</span>
                <button className="danger" onClick={this.decrement}>-</button>
                <button className="success" onClick={this.increment}>+</button>
            </div>
        );
    }
}

export default Counter;