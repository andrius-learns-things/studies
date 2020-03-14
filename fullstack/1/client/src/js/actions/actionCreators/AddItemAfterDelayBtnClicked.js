import ActionTypes from "../ActionTypes.js";
import dispatcher from "../../Dispatcher.js";

let addItemAfterDelayBtnClicked = function() {
  dispatcher.dispatch({
    type: ActionTypes.ADD_ITEM_AFTER_DELAY_BTN_CLICKED
  });
};

export default addItemAfterDelayBtnClicked;
