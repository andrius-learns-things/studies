import React from "react";

import StoreComponent from "./base/StoreComponent.jsx";
import { FormattedMessage } from "react-intl";

class MainPage extends StoreComponent {
  render() {
    return (
      <p>
        <FormattedMessage id="hello" defaultMessage="Hello" />
      </p>
    );
  }
}

export default MainPage;