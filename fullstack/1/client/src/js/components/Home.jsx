import React from "react";
import { Button, ButtonGroup, Table } from "react-bootstrap";
import StoreComponent from "./base/StoreComponent.jsx";
import getBtnClickedHandler from "../actions/actionCreators/BtnClicked.js";

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
          {items.reverse().map((item, index) => (
            <tr key={index}>
              <td>{items.length - index}</td>
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
        <ButtonGroup className="mr-2">
          <Button variant="success" onClick={getBtnClickedHandler("addItem")}>
            Add item
          </Button>
        </ButtonGroup>
        <ButtonGroup className="mr-2">
          <Button onClick={getBtnClickedHandler("addItemToTheQueue")}>
            Add item to the queue
          </Button>
        </ButtonGroup>
        <ButtonGroup className="mr-2">
          <Button onClick={getBtnClickedHandler("addItemsFromQueue")}>
            Add items from queue
          </Button>
        </ButtonGroup>
        <ButtonGroup className="mr-2">
          <Button onClick={getBtnClickedHandler("addItemAfterDelay")}>
            Add item after delay
          </Button>
        </ButtonGroup>
        {this.renderItems(this.state.items)}
      </div>
    );
  }
}

export default Home;
