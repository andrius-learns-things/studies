import React from "react";
import { Button, Table } from "react-bootstrap";
import StoreComponent from "./base/StoreComponent.jsx";
import addItemBtnClicked from "../actions/actionCreators/AddItemBtnClicked.js";
import addItemToTheQueueBtnClicked from "../actions/actionCreators/AddItemToTheQueueBtnClicked.js";
import addItemsFromQueueBtnClicked from "../actions/actionCreators/AddItemsFromQueueBtnClicked.js";

class Home extends StoreComponent {
  renderItems(items) {
    return items ? (
      <Table striped bordered hover size="sm">
        <thead>
          <tr>
            <th>#</th>
            <th>Item name</th>
          </tr>
        </thead>
        <tbody>
          {items.map((item, index) => (
            <tr key={index}>
              <td>{index + 1}</td>
              <td>{item.name}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    ) : null;
  }

  render() {
    return (
      <div>
        <p>
          <Button variant="success" onClick={addItemBtnClicked}>
            Add item
          </Button>
          <Button onClick={addItemToTheQueueBtnClicked}>
            Add item to the queue
          </Button>
          <Button onClick={addItemsFromQueueBtnClicked}>
            Add items from queue
          </Button>
        </p>
        {this.renderItems(this.state.items)}
      </div>
    );
  }
}

export default Home;
