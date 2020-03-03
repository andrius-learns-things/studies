import React, { Component } from "react";
import ReactDOM from "react-dom";
import StoreComponent from "./base/StoreComponent.jsx";

class MainPage extends StoreComponent {
  render() {
    return (
      <p>
        <p>Hello world!</p>
        <p>Counter: {this.state ? this.state.timesNavigated : "?"}</p>
      </p>
    );
  }
}

const wrapper = document.getElementById("container");
wrapper ? ReactDOM.render(<MainPage />, wrapper) : false;
