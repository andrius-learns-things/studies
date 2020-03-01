import routeEntered from '../actions/actionCreators/RouteEntered.js';


let routeOnEnterHook = function (nextRouterState) {

    // HERE stores are informed about react router navigation

    routeEntered(nextRouterState);
};

export default routeOnEnterHook;
