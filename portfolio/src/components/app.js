import React, { Component } from 'react';
import ReactDOM from 'react-dom';
class app extends Component {
    render() {
        return <h1>Hellow World</h1>;
    }
}

ReactDOM.render(<app />, document.getElementById('app'));