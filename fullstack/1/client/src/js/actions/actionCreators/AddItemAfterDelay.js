import ActionTypes from "../ActionTypes.js";
import { postToBackend } from "./helpers/CallBackend.js";

let addItemAfterDelay = function(item) {
  postToBackend(
    "/add-item-after-delay",
    ActionTypes.ADD_ITEM_AFTER_DELAY_SUCCESS,
    ActionTypes.ADD_ITEM_AFTER_DELAY_ERROR,
    item
  );
};

export default addItemAfterDelay;
