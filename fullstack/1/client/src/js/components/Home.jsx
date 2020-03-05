import React from "react";
import { Button } from "react-bootstrap";
import StoreComponent from "./base/StoreComponent.jsx";
import getItemsBtnClicked from "../actions/actionCreators/GetItemsBtnClicked.js";

class Home extends StoreComponent {
  renderItems(items) {
    return items ? (
      <ul>
        {items.map((item, index) => (
          <li key={index}>{item.name}</li>
        ))}
      </ul>
    ) : null;
  }

  render() {
    return (
      <div>
        <p>
          Home. Navigated{" "}
          {this.state.timesNavigated ? this.state.timesNavigated : "?"} number
          of times.
        </p>
        <p>
          <Button variant="success" onClick={getItemsBtnClicked}>
            Get items
          </Button>
        </p>
        <p>{this.renderItems(this.state.items)}</p>
      </div>
    );
  }
}

export default Home;
