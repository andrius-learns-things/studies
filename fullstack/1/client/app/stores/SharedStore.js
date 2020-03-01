import { ReduceStore } from 'flux/utils';
import cookie from 'react-cookie';

import constants from '../../Constants.js';
import log from '../../singletons/Log.js';
import ActionTypes from '../../actions/ActionTypes';
import redirectToUrl from '../../actions/actionCreators/navigation/RedirectToUrl.js';
import redirectToErrorPage from '../../actions/actionCreators/navigation/RedirectToErrorPage.js';
import saveUsedLanguage from '../../actions/actionCreators/SaveUsedLanguage.js';
import getConfig from '../../actions/actionCreators/GetConfig.js';
import getClassifiers from '../../actions/actionCreators/classifiers/GetClassifiers.js';
import getAuthInfo from '../../actions/actionCreators/GetAuthInfo.js';
import { localizationHelpers, errorMessageHelpers } from 'stv-utils-frontend';

import prepareUrl from '../../helpers/PrepareUrl.js';

import messagesFi from '../../localizations/fi.json';
import messagesEn from '../../localizations/en.json';
import messagesSv from '../../localizations/sv.json';
import messagesEt from '../../localizations/et.json';

const sessionExpiredForLoggedInUser = 'sessionExpiredForLoggedInUser';

class SharedStore extends ReduceStore {

    getInitialState() {

        // Language & classifiers:

        let getCachedResourceObject = function (messagesFile) {
            return {
                messages: messagesFile
            };
        };

        let cachedResourcesByLanguage = {
            'en': getCachedResourceObject(messagesEn),
            'fi': getCachedResourceObject(messagesFi),
            'sv': getCachedResourceObject(messagesSv),
            'et': getCachedResourceObject(messagesEt)
        };

        let defaultLanguageCode = "en";
        localizationHelpers.setFrontendUILanguage(defaultLanguageCode);

        // Config

        getConfig();

        // Error handling:

        let errorMessage = {
            show: false,
            id: null,
            data: null
        };

        // Async action loading indicator:

        let showLoadingIndicator = false;

        let state = {
            currentRoute: {
                fullPath: "/",
                routeParams: {}
            },
            localizations: {
                locale: 'en',
                messagesLanguage: defaultLanguageCode,
                messages: cachedResourcesByLanguage[defaultLanguageCode].messages,
                cachedResourcesByLanguage: cachedResourcesByLanguage
            },
            classifiers: null,
            classifiersLoading: true,
            reloadclassifiers: false,
            loadingAuthInfo: false,
            savingUsedLanguage: false,
            profile: null,
            representedOrganizationCode: null,
            errorMessage: errorMessage,
            emailToVerify: null,
            showLoadingIndicator: showLoadingIndicator,
            showMinimalRegistrationFlow: false,
            showRedirectBackNotice: null,
            redirectBackOrganizationUrl: null,
            redirectBackOrganizationName: null,
            pageWhereShowingRedirectNotice: null,
            constants: {
                chatScriptUrl: constants.chatScriptUrl,
                chatScriptId: constants.chatScriptId,
                hubSpotScriptUrl: constants.hubSpotScriptUrl,
                hubSpotScriptId: constants.hubSpotScriptId,
                milisecondsToWaitForLoadingIndicatorDisplay: constants.milisecondsToWaitForLoadingIndicatorDisplay
            },
            configIsLoaded: false,
            forceRedirectToUnauthorized: false,
            showOnlyLoadingIndicator: false,
            loadingIndicatorIsVisible: false,
            tosPrefix: "",
            userDoneActionOfAnonymousUser: false,
            showSessionExpiredInfoMsg: false,
            showSessionExpiredInfoMsgForLoggedInUser: false,
            overrideTopMenuSignInBtnAction: null
        };

        // Classifier loading:

        return state;
    }

    reduce(state, action) {

        log.addAction(action);

        let newState = Object.assign({}, state);

        this.reloadWholeAppAfterLanguageChangeIfNeeded(newState, action);

        if (!newState.appWillBeReloaded) {

            this.ensureConfigIsLoaded(newState, action);
            this.parseCurrentRouteParams(newState, action);

            if (newState.configIsLoaded) {

                this.loadAuthInfoWhenPossibleAndWhenNeeded(newState, action);
                this.checkIfNeedToShowRedirectNotice(newState);

                if (!state.savingUsedLanguage && this[action.type]) {
                    this[action.type](newState, action);
                }
            }

            this.handleErrors(newState, action);
        }

        return newState;
    }

    reloadWholeAppAfterLanguageChangeIfNeeded(state, action) {
        // Exceptional case - when language was changed, need to reload the whole app,
        // in order for chat component to be fully reloaded
        if (action.type === ActionTypes.LANGUAGE_CHANGE_SUCCESS) {
            if (action.reloadAppAfter) {
                state.appWillBeReloaded = true;
                window.location.reload();
            } else {
                state.savingUsedLanguage = false;
            }
        }
    }

    ensureConfigIsLoaded(state, action) {
        if (action.type === ActionTypes.CONFIG_GET_SUCCESS || action.type == ActionTypes.CONFIG_GET_ERROR) {
            state.configIsLoaded = true;
        }
    }

    parseCurrentRouteParams(state, action) {
        if (action.type === ActionTypes.ROUTE_ENTERED) {
            let route = action.route;
            state.currentRoute = route;
            state.representedOrganizationCode = route.params ? route.params.organizationCode : null;
        }
    }

    /* Loading authorization-related info */

    loadAuthInfoWhenPossibleAndWhenNeeded(state, action) {

        if (action.authInfoHash) {
            state.authInfoHash = action.authInfoHash;
        }

        let cookieUsedUiLanguage = cookie.load(constants.cookieNames.usedUiLanguage);

        let languageChangedForAnonymousUser = Boolean(cookieUsedUiLanguage
            && state.authInfo
            && state.authInfo.otherUiInfo
            && !state.authInfo.otherUiInfo.isSignedIn
            && state.authInfo.otherUiInfo.uiLanguage != cookieUsedUiLanguage);

        let needsReloading = !state.authInfoLoadedFor
            || state.authInfoLoadedFor.representedOrganizationCode !== state.representedOrganizationCode
            || state.authInfoLoadedFor.authInfoHash !== state.authInfoHash
            || languageChangedForAnonymousUser;

        if (needsReloading && !state.loadingAuthInfo) {

            state.loadingAuthInfo = true;

            state.authInfoLoadedFor = {
                representedOrganizationCode: state.representedOrganizationCode,
                authInfoHash: state.authInfoHash
            };

            getAuthInfo(state.representedOrganizationCode);
        }

        if (action.type === ActionTypes.AUTH_INFO_GET_SUCCESS) {
            // Set user info:

            state.loadingAuthInfo = false;
            state.authInfo = action.result;
            state.authInfoLoadedFor.authInfoHash = action.authInfoHash;

            // Some fields set in root for convenience:

            state.profile = action.result.userProfile;
            state.isSignedIn = action.result.otherUiInfo.isSignedIn;
            state.isAdmin = action.result.otherUiInfo.isAdmin;
            state.isSuperAdmin = action.result.otherUiInfo.isSuperAdmin;
            state.representedOrgCountry = action.result.otherUiInfo.representedOrgCountry;
            state.representedOrgName = action.result.otherUiInfo.representedOrgName;

            // Set messages and start loading classifiers:

            let lang = action.result.otherUiInfo.uiLanguage;
            let cache = state.localizations.cachedResourcesByLanguage[lang];
            localizationHelpers.setFrontendUILanguage(lang, cache.messages);

            state.localizations.messagesLanguage = lang;
            state.localizations.messages = cache.messages;
            state.tosPrefix = action.result.topMenuParameters.configuration.tosPrefix;

            if (!state.forceRedirectToUnauthorized) {
                let isSessionExpiredForLoggedInUser = sessionStorage.getItem(sessionExpiredForLoggedInUser)
                if (isSessionExpiredForLoggedInUser) {
                    state.showSessionExpiredInfoMsgForLoggedInUser = isSessionExpiredForLoggedInUser.toLowerCase() === 'true';
                }
                sessionStorage.setItem(sessionExpiredForLoggedInUser, false);
            }

            // Set default "Go to home" link url in error messages
            this.setDefaultGoHomeUrlForErrors(action.result);

            // Start loading classifiers:

            if (!state.classifiers || state.reloadclassifiers) {
                state.classifiersLoading = true;
                getClassifiers(state.localizations.messagesLanguage);
            }
        }
    }

    setDefaultGoHomeUrlForErrors(authInfo) {
        if (authInfo && authInfo.topMenuParameters && authInfo.topMenuParameters.configuration) {
            let uiConfiguration = authInfo.topMenuParameters.configuration;
            let servicePortalCode = uiConfiguration['servicePortalServiceCode'];
            let servicePortalUrl = uiConfiguration.services[servicePortalCode].url;
            if (servicePortalUrl) {
                errorMessageHelpers.setGoHomeLink(servicePortalUrl);
            }
        }
    }

    forceReloadAuthInfo(state, action) {
        state.authInfoLoadedFor = null;
        this.loadAuthInfoWhenPossibleAndWhenNeeded(state, action);
    }

    [ActionTypes.AUTH_INFO_GET_ERROR](state) {
        state.loadingAuthInfo = false;
        if (!state.authInfo) {
            state.authInfo = {
                currentPermissions: [],
                otherUiInfo: {
                    uiLanguage: "en"
                },
                topMenuParameters: {
                    configuration: {
                        servicePortal: {
                            registrationSettings: {
                                registrationFlow: "flow",
                                flow: {
                                    tosType: ""
                                }
                            }
                        }
                    },
                    menuItemsVisibility: {
                        showSignedInUserProfileLinks: false,
                        showUnverifiedSignedInUserProfileLinks: false,
                        showSignedInUserOrganizationInfoLink: null,
                        showSignedInUserManageUsersLink: null,
                        showSignedInUserManageCardsLink: null
                    },
                    selectedLanguageCode: "en",
                    servicesVisibilityInTopMenu: {},
                    servicesEnabilityInTopMenu: {}
                },
                userProfile: null
            };
        }
        if (!state.classifiers || state.reloadclassifiers) {
            state.classifiersLoading = true;
            getClassifiers(state.authInfo.otherUiInfo.uiLanguage);
        }
    }

    [ActionTypes.CLASSIFIERS_GET_ALL_SUCCESS](state, action) {
        state.classifiersLoading = false;
        state.reloadclassifiers = false;
        state.classifiers = action.result;
    }

    [ActionTypes.CLASSIFIERS_GET_ALL_ERROR](state) {
        state.classifiersLoading = false;
        state.reloadclassifiers = false;

        if (!state.classifiers) {
            state.classifiers = {
                countries: []
            };
        }
    }

    /* Redirect notices: */

    [ActionTypes.CLOSE_REDIRECT_NOTICE_BTN_CLICKED](state) {
        state.showRedirectBackNotice = false;
        this.clearRedirectNotice();
    }

    checkIfNeedToShowRedirectNotice(state) {
        if (state.isSignedIn) {
            let route = state.currentRoute;
            let firstRoutePath = route.paths ? route.paths[0] : null;

            state.pageWhereShowingRedirectNotice = cookie.load(constants.cookieNames.redirectNoticePageWhereShowing);
            state.redirectBackOrganizationUrl = cookie.load(constants.cookieNames.redirectNoticeBackToServiceUrl);
            state.redirectBackOrganizationName = cookie.load(constants.cookieNames.redirectNoticeRedirectedFrom);

            if (state.pageWhereShowingRedirectNotice && firstRoutePath && state.pageWhereShowingRedirectNotice === firstRoutePath) {
                state.showRedirectBackNotice = true;
            } else {
                state.showRedirectBackNotice = false;
                this.clearRedirectNotice();
            }
        }
    }

    clearRedirectNotice() {
        cookie.remove(constants.cookieNames.redirectNoticePageWhereShowing);
        cookie.remove(constants.cookieNames.redirectNoticeBackToServiceUrl);
        cookie.remove(constants.cookieNames.redirectNoticeRedirectedFrom);
    }

    /* Language change: */

    [ActionTypes.LANGUAGE_SELECT_BTN_CLICKED](state, action) {
        let chatComponentIsEnabled = state.authInfo.topMenuParameters.configuration.loadChatComponent;
        // Reload classifiers if app will not be reloaded because language
        // changed and classifiers should be served with different language
        state.reloadclassifiers = !chatComponentIsEnabled;

        this.initiateLanguageSaving(state, action.lang, chatComponentIsEnabled);
    }

    initiateLanguageSaving(state, lang, reloadAppAfter) {
        state.savingUsedLanguage = true;
        saveUsedLanguage(lang, reloadAppAfter);
    }

    [ActionTypes.LANGUAGE_CHANGE_ERROR](state) {
        state.savingUsedLanguage = false;
    }

    /* Auth: */

    [ActionTypes.SIGN_IN_BTN_CLICKED](state) {
        if (state.overrideTopMenuSignInBtnAction && typeof state.overrideTopMenuSignInBtnAction === 'function') {
            state.overrideTopMenuSignInBtnAction();
        } else {
            redirectToUrl(prepareUrl.getSignInRelativeUrl());
        }
    }

    [ActionTypes.SIGN_OUT_BTN_CLICKED](state) {
        redirectToUrl(prepareUrl.getSignOutRelativeUrl(state.config.urlAfterSignOut));
    }

    /* Config */

    [ActionTypes.CONFIG_GET_SUCCESS](state, action) {
        log.setConfig(action.result.extensiveLogging);
        state.config = action.result;
    }

    [ActionTypes.CONFIG_GET_ERROR](state) {
        state.config = {
            "extensiveLogging": false,
            "urlAfterSignOut": null
        };
        log.setConfig(state.config.extensiveLogging);
    }

    /* Handle errors: */

    handleErrors(newState, action) {
        // Show user unauthorized or redirect to login
        if (action.type === ActionTypes.AUTH_INFO_GET_SUCCESS) {
            if (newState.forceRedirectToUnauthorized) {
                if (newState.isSignedIn) {
                    redirectToErrorPage('unauthorized');
                } else {
                    if (newState.userDoneActionOfAnonymousUser) {
                        newState.showSessionExpiredInfoMsg = true;
                    } else {
                        let returnUrl = prepareUrl.prepareRouteUrl(newState.currentRoute.fullUrl, false, newState.currentRoute.params.organizationCode);
                        returnUrl = prepareUrl.prepareAbsoluteFrontendUrl(newState, returnUrl);
                        let returnUrlEncoded = encodeURIComponent(returnUrl);
                        redirectToUrl(prepareUrl.getSignInRelativeUrl(returnUrlEncoded));
                    }
                }
                newState.forceRedirectToUnauthorized = false;
                newState.userDoneActionOfAnonymousUser = false;
            }
        }
        // Check for error
        if (action.errorMessageId) {

            if (action.httpErrorStatus === 403) {

                // If got 403 Forbidden - need to redirect out of

                log.addBackendCallForbiddenInfo(action.type);

                // 1. Get new auth state from server:
                this.forceReloadAuthInfo(newState, action);

                // 2. Force user redirect after checking if he is logedin or no
                newState.forceRedirectToUnauthorized = true;

                newState.userDoneActionOfAnonymousUser = action.sessionTokenIsMissing && !newState.isSignedIn;

                let userDoneActionOfLoggedInUser = action.sessionTokenIsMissing && newState.isSignedIn;

                if (userDoneActionOfLoggedInUser) {
                    sessionStorage.setItem(sessionExpiredForLoggedInUser, userDoneActionOfLoggedInUser);
                }

            } else {
                // If action has errorMessageId set, show passed error message:

                let errorMessageId = action.errorMessageId;

                if (!errorMessageId) {
                    errorMessageId = constants.generalErrorMessageId;
                }

                newState.errorMessage.show = true;
                newState.errorMessage.id = constants.errorMessageIdPrefix + action.errorMessageId;
                newState.errorMessage.data = action.additionalData ? action.additionalData : {};
                newState.showSessionExpiredInfoMsg = false;
                newState.showSessionExpiredInfoMsgForLoggedInUser = false;
            }
        } else if (action.type == ActionTypes.ROUTE_ENTERED
            && action.route.fullPath == '/error/:key') {

            // When separate error page is opening, show error message by route params:

            let errorMessageId = action.route.params['key'];

            if (!errorMessageId) {
                errorMessageId = constants.generalErrorMessageId;
            }

            newState.errorMessage.show = true;
            newState.showSessionExpiredInfoMsg = false;
            newState.showSessionExpiredInfoMsgForLoggedInUser = false;
            newState.errorMessage.id = constants.errorMessageIdPrefix + errorMessageId;
            newState.errorMessage.data = action.additionalData ? action.additionalData : {};
        } else if (action.type == ActionTypes.ROUTE_ENTERED
            || action.clearPreviousErrors) {
            // Hide error message on route change:
            newState.showSessionExpiredInfoMsg = false;
            newState.showSessionExpiredInfoMsgForLoggedInUser = false;
            newState.errorMessage.show = false;
            newState.errorMessage.id = null;
            newState.errorMessage.data = {};
        }
    }
}

export default SharedStore;
