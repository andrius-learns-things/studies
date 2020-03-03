import React, { Component } from "react";
import ReactDOM from "react-dom";
import StoreComponent from "./base/StoreComponent.jsx";

class Form extends StoreComponent {
  constructor() {
    super();

    this.state = {};
  }

  render() {
    return (
      <p>
        <p>Hello world!</p>
        <p>Counter: {this.state.timesNavigated}</p>
      </p>
    );
  }
}

export default Form;

const wrapper = document.getElementById("container");
wrapper ? ReactDOM.render(<Form />, wrapper) : false;
