import React from "react";
import StoreComponent from "./base/StoreComponent.jsx";
import { Button } from "react-bootstrap";

class Home extends StoreComponent {
  render() {
    return (
      <div>
        <p>
          Home. Navigated{" "}
          {this.state.timesNavigated ? this.state.timesNavigated : "?"} number
          of times.
        </p>
        <p>
          <Button variant="success">Great succėss</Button>
        </p>
      </div>
    );
  }
}

export default Home;
