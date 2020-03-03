import ActionTypes from '../ActionTypes.js';
import dispatcher from '../../Dispatcher.js';


let routeEntered = function (nextRouterState) {
    dispatcher.dispatch({
        type: ActionTypes.ROUTE_ENTERED,
        nextRouteState: nextRouterState
    });
};

export default routeEntered;