import ActionTypes from "../ActionTypes.js";
import { postToBackend } from "./helpers/CallBackend.js";

let addItem = function(item) {
  postToBackend(
    "/items",
    ActionTypes.ADD_ITEM_SUCCESS,
    ActionTypes.ADD_ITEM_ERROR,
    item
  );
};

export default addItem;
