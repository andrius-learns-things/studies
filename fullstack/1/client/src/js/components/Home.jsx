import React from "react";
import { Button, Table } from "react-bootstrap";
import StoreComponent from "./base/StoreComponent.jsx";
import getItemsBtnClicked from "../actions/actionCreators/GetItemsBtnClicked.js";

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
          <Button variant="success" onClick={getItemsBtnClicked}>
            Get items
          </Button>
        </p>
        {this.renderItems(this.state.items)}
      </div>
    );
  }
}

export default Home;
