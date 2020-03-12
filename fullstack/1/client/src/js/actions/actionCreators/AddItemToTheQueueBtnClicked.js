import ActionTypes from "../ActionTypes.js";
import dispatcher from "../../Dispatcher.js";

let addItemToTheQueueBtnClicked = function() {
  dispatcher.dispatch({
    type: ActionTypes.ADD_ITEM_TO_THE_QUEUE_BTN_CLICKED
  });
};

export default addItemToTheQueueBtnClicked;
