import React, {Component} from 'react'

export default class Button extends React.Component{
    
    constructor(props){
        super(props);
        this.state = {
            counter : 0,
        };
    }

    Increment(){
        this.setState({
            counter: this.state.counter + 1
            });
    };

    render(){
        return(
            <div>
                <button onClick={(e) => this.Increment(e)}>
                    Click me!
                </button>
                <p> 
                    The button was clicked {this.state.counter} times
                </p>
            </div>
        );
    }
}