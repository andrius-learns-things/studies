import dispatcher from '../Dispatcher.js';
import SharedStore from './base/SharedStore.js';
import CounterStore from './base/CounterStore.js';

import MenuItemsStore from './MenuItemsStore.js';
import Organizationstore from './organizations/OrganizationsStore.js';
import CompaniesWhitelistedSignatoriesStore from './organizations/CompaniesWhitelistedSignatoriesStore.js';
import CompanyRegistryManualManagementStore from './organizations/CompanyRegistryManualManagementStore.js';
import PageLoaderStore from './PageLoaderStore.js';
import OrganizationInfoStore from './organization/OrganizationInfoStore.js';
import OrganizationBasicInfoStore from './organization/OrganizationBasicInfoStore.js';
import OrganizationContactDetailsStore from './organization/OrganizationContactDetailsStore.js';
import OrganizationInvoicingInfoStore from './organization/OrganizationInvoicingInfoStore.js';
import PendingOrgInvitationStore from './organizations/PendingOrgInvitationStore.js';
import CompanyNameIsTooLongStore from './organization/CompanyNameIsTooLongStore.js';
import OrganisationCardSupplierStore from './organization/OrganisationCardSupplierStore.js';
import CompaniesWithoutFTAXWhitelistStore from './organizations/CompaniesWithoutFTAXWhitelistStore.js';

import RegistrationSuccessStore from './registration/common/SuccessStore.js';
import FindCompanyInRegistryStore from './registration/company/FindCompanyInRegistryStore.js';
import Step4Store from './registration/company/Step4Store.js';
import InviteSignatoryStore from './registration/company/InviteSignatoryStore.js';
import ServiceContractSignStepStore from './registration/company/ServiceContractSignStepStore.js';
import NotAllowedToSignStore from './registration/company/NotAllowedToSignStore.js';

import SaveCSPasswordStore from './services/bol/SaveCSPasswordStore.js';
import CreditsafeTermsAndConditionsStore from './services/bol/CreditsafeTermsAndConditionsStore.js';

/* This list must be maintained: */

let allStoreClasses = {
    menuItems: MenuItemsStore,
    home: PageLoaderStore,
    organizationInfo: OrganizationInfoStore,
    organizationBasicInfo: OrganizationBasicInfoStore,
    organizationContactDetails: OrganizationContactDetailsStore,
    organizationInvoicingInfo: OrganizationInvoicingInfoStore,
    organizations: Organizationstore,
    pendingOrgInvitationStore: PendingOrgInvitationStore,
    companyNameIsTooLongStore: CompanyNameIsTooLongStore,
    companiesWhitelistedSignatoriesStore: CompaniesWhitelistedSignatoriesStore,
    companyRegistryManualManagementStore: CompanyRegistryManualManagementStore,
    organisationCardSupplierStore: OrganisationCardSupplierStore,
    companiesWithoutFTAXWhitelistStore: CompaniesWithoutFTAXWhitelistStore,
    registrationSuccess: RegistrationSuccessStore,
    registrationFindInRegistryStore: FindCompanyInRegistryStore,
    Step4Store: Step4Store,
    inviteSignatoryStore: InviteSignatoryStore,
    serviceContractSignStepStore: ServiceContractSignStepStore,
    notAllowedToSignStore: NotAllowedToSignStore,
    saveCSPassword: SaveCSPasswordStore,
    bolCreditsafeTermsAndConditionsStore: CreditsafeTermsAndConditionsStore
};

/* Create all FLUX stores: */

let allStores = {};

let sharedStore = new SharedStore(dispatcher);
allStores['shared'] = sharedStore;

Object.keys(allStoreClasses).forEach((storeKey) => {
    let storeClass = allStoreClasses[storeKey];
    allStores[storeKey] = new storeClass(dispatcher, sharedStore);
});

allStores['counter'] = new CounterStore(dispatcher, sharedStore);

export default allStores;
