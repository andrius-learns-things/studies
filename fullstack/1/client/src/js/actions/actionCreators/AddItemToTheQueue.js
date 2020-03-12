import ActionTypes from "../ActionTypes.js";
import { postToBackend } from "./helpers/CallBackend.js";

let addItemToTheQueue = function(item) {
  postToBackend(
    "/queued-items",
    ActionTypes.ADD_ITEM_TO_THE_QUEUE_SUCCESS,
    ActionTypes.ADD_ITEM_TO_THE_QUEUE_ERROR,
    item
  );
};

export default addItemToTheQueue;
