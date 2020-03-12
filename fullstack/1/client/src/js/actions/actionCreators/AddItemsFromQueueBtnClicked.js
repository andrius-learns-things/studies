import ActionTypes from "../ActionTypes.js";
import dispatcher from "../../Dispatcher.js";

let addItemsFromQueueBtnClicked = function() {
  dispatcher.dispatch({
    type: ActionTypes.ADD_ITEMS_FROM_QUEUE_BTN_CLICKED
  });
};

export default addItemsFromQueueBtnClicked;
