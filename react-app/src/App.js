import React, { Component } from 'react'
import './App.css';
import UserSupervisor from './forms/UserSupervisor';
import AlertMessage from './components/AlertMessage';

export default class App extends Component{
  constructor(props) {
      super(props);
      this.state = {
          message: null,
          category: null,
      }
  }

  flashMessage = (message, category) => {
    this.setState({message,category})
  }


  render() {
    return (
      <>
      <div className='container mt-5'>
      {this.state.message ? <AlertMessage category={this.state.category} message={this.state.message} flashMessage={this.flashMessage}/> : null}
        <UserSupervisor flashMessage={this.flashMessage}/>
      </div>
      </>
    );
  }
}

