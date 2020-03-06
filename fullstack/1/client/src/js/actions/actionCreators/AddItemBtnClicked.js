import ActionTypes from "../ActionTypes.js";
import dispatcher from "../../Dispatcher.js";

let addItemBtnClicked = function() {
  dispatcher.dispatch({
    type: ActionTypes.ADD_ITEM_BTN_CLICKED
  });
};

export default addItemBtnClicked;
