import ActionTypes from "../ActionTypes.js";
import { postToBackend } from "./helpers/CallBackend.js";

let addItemsFromQueue = function() {
  postToBackend(
    "/add-items-from-queue",
    ActionTypes.ADD_ITEMS_FROM_QUEUE_SUCCESS,
    ActionTypes.ADD_ITEMS_FROM_QUEUE_ERROR
  );
};

export default addItemsFromQueue;
