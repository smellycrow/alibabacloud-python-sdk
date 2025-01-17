# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ims20190815 import models as ims_20190815_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('ims', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(
        self,
        product_id: str,
        region_id: str,
        endpoint_rule: str,
        network: str,
        suffix: str,
        endpoint_map: Dict[str, str],
        endpoint: str,
    ) -> str:
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_client_id_to_oidcprovider_with_options(
        self,
        request: ims_20190815_models.AddClientIdToOIDCProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.AddClientIdToOIDCProviderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.AddClientIdToOIDCProviderResponse(),
            self.do_rpcrequest('AddClientIdToOIDCProvider', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_client_id_to_oidcprovider_with_options_async(
        self,
        request: ims_20190815_models.AddClientIdToOIDCProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.AddClientIdToOIDCProviderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.AddClientIdToOIDCProviderResponse(),
            await self.do_rpcrequest_async('AddClientIdToOIDCProvider', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_client_id_to_oidcprovider(
        self,
        request: ims_20190815_models.AddClientIdToOIDCProviderRequest,
    ) -> ims_20190815_models.AddClientIdToOIDCProviderResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_client_id_to_oidcprovider_with_options(request, runtime)

    async def add_client_id_to_oidcprovider_async(
        self,
        request: ims_20190815_models.AddClientIdToOIDCProviderRequest,
    ) -> ims_20190815_models.AddClientIdToOIDCProviderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_client_id_to_oidcprovider_with_options_async(request, runtime)

    def add_fingerprint_to_oidcprovider_with_options(
        self,
        request: ims_20190815_models.AddFingerprintToOIDCProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.AddFingerprintToOIDCProviderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.AddFingerprintToOIDCProviderResponse(),
            self.do_rpcrequest('AddFingerprintToOIDCProvider', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_fingerprint_to_oidcprovider_with_options_async(
        self,
        request: ims_20190815_models.AddFingerprintToOIDCProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.AddFingerprintToOIDCProviderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.AddFingerprintToOIDCProviderResponse(),
            await self.do_rpcrequest_async('AddFingerprintToOIDCProvider', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_fingerprint_to_oidcprovider(
        self,
        request: ims_20190815_models.AddFingerprintToOIDCProviderRequest,
    ) -> ims_20190815_models.AddFingerprintToOIDCProviderResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_fingerprint_to_oidcprovider_with_options(request, runtime)

    async def add_fingerprint_to_oidcprovider_async(
        self,
        request: ims_20190815_models.AddFingerprintToOIDCProviderRequest,
    ) -> ims_20190815_models.AddFingerprintToOIDCProviderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_fingerprint_to_oidcprovider_with_options_async(request, runtime)

    def add_user_to_group_with_options(
        self,
        request: ims_20190815_models.AddUserToGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.AddUserToGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.AddUserToGroupResponse(),
            self.do_rpcrequest('AddUserToGroup', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_user_to_group_with_options_async(
        self,
        request: ims_20190815_models.AddUserToGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.AddUserToGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.AddUserToGroupResponse(),
            await self.do_rpcrequest_async('AddUserToGroup', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_user_to_group(
        self,
        request: ims_20190815_models.AddUserToGroupRequest,
    ) -> ims_20190815_models.AddUserToGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_user_to_group_with_options(request, runtime)

    async def add_user_to_group_async(
        self,
        request: ims_20190815_models.AddUserToGroupRequest,
    ) -> ims_20190815_models.AddUserToGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_user_to_group_with_options_async(request, runtime)

    def bind_mfadevice_with_options(
        self,
        request: ims_20190815_models.BindMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.BindMFADeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.BindMFADeviceResponse(),
            self.do_rpcrequest('BindMFADevice', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def bind_mfadevice_with_options_async(
        self,
        request: ims_20190815_models.BindMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.BindMFADeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.BindMFADeviceResponse(),
            await self.do_rpcrequest_async('BindMFADevice', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def bind_mfadevice(
        self,
        request: ims_20190815_models.BindMFADeviceRequest,
    ) -> ims_20190815_models.BindMFADeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_mfadevice_with_options(request, runtime)

    async def bind_mfadevice_async(
        self,
        request: ims_20190815_models.BindMFADeviceRequest,
    ) -> ims_20190815_models.BindMFADeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_mfadevice_with_options_async(request, runtime)

    def change_password_with_options(
        self,
        request: ims_20190815_models.ChangePasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ChangePasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.ChangePasswordResponse(),
            self.do_rpcrequest('ChangePassword', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def change_password_with_options_async(
        self,
        request: ims_20190815_models.ChangePasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ChangePasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.ChangePasswordResponse(),
            await self.do_rpcrequest_async('ChangePassword', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def change_password(
        self,
        request: ims_20190815_models.ChangePasswordRequest,
    ) -> ims_20190815_models.ChangePasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.change_password_with_options(request, runtime)

    async def change_password_async(
        self,
        request: ims_20190815_models.ChangePasswordRequest,
    ) -> ims_20190815_models.ChangePasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.change_password_with_options_async(request, runtime)

    def create_access_key_with_options(
        self,
        request: ims_20190815_models.CreateAccessKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateAccessKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateAccessKeyResponse(),
            self.do_rpcrequest('CreateAccessKey', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_access_key_with_options_async(
        self,
        request: ims_20190815_models.CreateAccessKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateAccessKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateAccessKeyResponse(),
            await self.do_rpcrequest_async('CreateAccessKey', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_access_key(
        self,
        request: ims_20190815_models.CreateAccessKeyRequest,
    ) -> ims_20190815_models.CreateAccessKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_access_key_with_options(request, runtime)

    async def create_access_key_async(
        self,
        request: ims_20190815_models.CreateAccessKeyRequest,
    ) -> ims_20190815_models.CreateAccessKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_access_key_with_options_async(request, runtime)

    def create_app_secret_with_options(
        self,
        request: ims_20190815_models.CreateAppSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateAppSecretResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateAppSecretResponse(),
            self.do_rpcrequest('CreateAppSecret', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_app_secret_with_options_async(
        self,
        request: ims_20190815_models.CreateAppSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateAppSecretResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateAppSecretResponse(),
            await self.do_rpcrequest_async('CreateAppSecret', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_app_secret(
        self,
        request: ims_20190815_models.CreateAppSecretRequest,
    ) -> ims_20190815_models.CreateAppSecretResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_app_secret_with_options(request, runtime)

    async def create_app_secret_async(
        self,
        request: ims_20190815_models.CreateAppSecretRequest,
    ) -> ims_20190815_models.CreateAppSecretResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_app_secret_with_options_async(request, runtime)

    def create_application_with_options(
        self,
        request: ims_20190815_models.CreateApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateApplicationResponse(),
            self.do_rpcrequest('CreateApplication', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_application_with_options_async(
        self,
        request: ims_20190815_models.CreateApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateApplicationResponse(),
            await self.do_rpcrequest_async('CreateApplication', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_application(
        self,
        request: ims_20190815_models.CreateApplicationRequest,
    ) -> ims_20190815_models.CreateApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_application_with_options(request, runtime)

    async def create_application_async(
        self,
        request: ims_20190815_models.CreateApplicationRequest,
    ) -> ims_20190815_models.CreateApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_application_with_options_async(request, runtime)

    def create_group_with_options(
        self,
        request: ims_20190815_models.CreateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateGroupResponse(),
            self.do_rpcrequest('CreateGroup', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_group_with_options_async(
        self,
        request: ims_20190815_models.CreateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateGroupResponse(),
            await self.do_rpcrequest_async('CreateGroup', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_group(
        self,
        request: ims_20190815_models.CreateGroupRequest,
    ) -> ims_20190815_models.CreateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_group_with_options(request, runtime)

    async def create_group_async(
        self,
        request: ims_20190815_models.CreateGroupRequest,
    ) -> ims_20190815_models.CreateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_group_with_options_async(request, runtime)

    def create_login_profile_with_options(
        self,
        request: ims_20190815_models.CreateLoginProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateLoginProfileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateLoginProfileResponse(),
            self.do_rpcrequest('CreateLoginProfile', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_login_profile_with_options_async(
        self,
        request: ims_20190815_models.CreateLoginProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateLoginProfileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateLoginProfileResponse(),
            await self.do_rpcrequest_async('CreateLoginProfile', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_login_profile(
        self,
        request: ims_20190815_models.CreateLoginProfileRequest,
    ) -> ims_20190815_models.CreateLoginProfileResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_login_profile_with_options(request, runtime)

    async def create_login_profile_async(
        self,
        request: ims_20190815_models.CreateLoginProfileRequest,
    ) -> ims_20190815_models.CreateLoginProfileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_login_profile_with_options_async(request, runtime)

    def create_oidcprovider_with_options(
        self,
        request: ims_20190815_models.CreateOIDCProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateOIDCProviderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateOIDCProviderResponse(),
            self.do_rpcrequest('CreateOIDCProvider', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_oidcprovider_with_options_async(
        self,
        request: ims_20190815_models.CreateOIDCProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateOIDCProviderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateOIDCProviderResponse(),
            await self.do_rpcrequest_async('CreateOIDCProvider', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_oidcprovider(
        self,
        request: ims_20190815_models.CreateOIDCProviderRequest,
    ) -> ims_20190815_models.CreateOIDCProviderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_oidcprovider_with_options(request, runtime)

    async def create_oidcprovider_async(
        self,
        request: ims_20190815_models.CreateOIDCProviderRequest,
    ) -> ims_20190815_models.CreateOIDCProviderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_oidcprovider_with_options_async(request, runtime)

    def create_samlprovider_with_options(
        self,
        request: ims_20190815_models.CreateSAMLProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateSAMLProviderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateSAMLProviderResponse(),
            self.do_rpcrequest('CreateSAMLProvider', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_samlprovider_with_options_async(
        self,
        request: ims_20190815_models.CreateSAMLProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateSAMLProviderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateSAMLProviderResponse(),
            await self.do_rpcrequest_async('CreateSAMLProvider', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_samlprovider(
        self,
        request: ims_20190815_models.CreateSAMLProviderRequest,
    ) -> ims_20190815_models.CreateSAMLProviderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_samlprovider_with_options(request, runtime)

    async def create_samlprovider_async(
        self,
        request: ims_20190815_models.CreateSAMLProviderRequest,
    ) -> ims_20190815_models.CreateSAMLProviderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_samlprovider_with_options_async(request, runtime)

    def create_user_with_options(
        self,
        request: ims_20190815_models.CreateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateUserResponse(),
            self.do_rpcrequest('CreateUser', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_user_with_options_async(
        self,
        request: ims_20190815_models.CreateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateUserResponse(),
            await self.do_rpcrequest_async('CreateUser', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_user(
        self,
        request: ims_20190815_models.CreateUserRequest,
    ) -> ims_20190815_models.CreateUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_user_with_options(request, runtime)

    async def create_user_async(
        self,
        request: ims_20190815_models.CreateUserRequest,
    ) -> ims_20190815_models.CreateUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_user_with_options_async(request, runtime)

    def create_virtual_mfadevice_with_options(
        self,
        request: ims_20190815_models.CreateVirtualMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateVirtualMFADeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateVirtualMFADeviceResponse(),
            self.do_rpcrequest('CreateVirtualMFADevice', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_virtual_mfadevice_with_options_async(
        self,
        request: ims_20190815_models.CreateVirtualMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateVirtualMFADeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateVirtualMFADeviceResponse(),
            await self.do_rpcrequest_async('CreateVirtualMFADevice', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_virtual_mfadevice(
        self,
        request: ims_20190815_models.CreateVirtualMFADeviceRequest,
    ) -> ims_20190815_models.CreateVirtualMFADeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_virtual_mfadevice_with_options(request, runtime)

    async def create_virtual_mfadevice_async(
        self,
        request: ims_20190815_models.CreateVirtualMFADeviceRequest,
    ) -> ims_20190815_models.CreateVirtualMFADeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_virtual_mfadevice_with_options_async(request, runtime)

    def delete_access_key_with_options(
        self,
        request: ims_20190815_models.DeleteAccessKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteAccessKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteAccessKeyResponse(),
            self.do_rpcrequest('DeleteAccessKey', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_access_key_with_options_async(
        self,
        request: ims_20190815_models.DeleteAccessKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteAccessKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteAccessKeyResponse(),
            await self.do_rpcrequest_async('DeleteAccessKey', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_access_key(
        self,
        request: ims_20190815_models.DeleteAccessKeyRequest,
    ) -> ims_20190815_models.DeleteAccessKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_access_key_with_options(request, runtime)

    async def delete_access_key_async(
        self,
        request: ims_20190815_models.DeleteAccessKeyRequest,
    ) -> ims_20190815_models.DeleteAccessKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_access_key_with_options_async(request, runtime)

    def delete_app_secret_with_options(
        self,
        request: ims_20190815_models.DeleteAppSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteAppSecretResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteAppSecretResponse(),
            self.do_rpcrequest('DeleteAppSecret', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_app_secret_with_options_async(
        self,
        request: ims_20190815_models.DeleteAppSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteAppSecretResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteAppSecretResponse(),
            await self.do_rpcrequest_async('DeleteAppSecret', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_app_secret(
        self,
        request: ims_20190815_models.DeleteAppSecretRequest,
    ) -> ims_20190815_models.DeleteAppSecretResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_app_secret_with_options(request, runtime)

    async def delete_app_secret_async(
        self,
        request: ims_20190815_models.DeleteAppSecretRequest,
    ) -> ims_20190815_models.DeleteAppSecretResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_secret_with_options_async(request, runtime)

    def delete_application_with_options(
        self,
        request: ims_20190815_models.DeleteApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteApplicationResponse(),
            self.do_rpcrequest('DeleteApplication', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_application_with_options_async(
        self,
        request: ims_20190815_models.DeleteApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteApplicationResponse(),
            await self.do_rpcrequest_async('DeleteApplication', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_application(
        self,
        request: ims_20190815_models.DeleteApplicationRequest,
    ) -> ims_20190815_models.DeleteApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_application_with_options(request, runtime)

    async def delete_application_async(
        self,
        request: ims_20190815_models.DeleteApplicationRequest,
    ) -> ims_20190815_models.DeleteApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_application_with_options_async(request, runtime)

    def delete_group_with_options(
        self,
        request: ims_20190815_models.DeleteGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteGroupResponse(),
            self.do_rpcrequest('DeleteGroup', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_group_with_options_async(
        self,
        request: ims_20190815_models.DeleteGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteGroupResponse(),
            await self.do_rpcrequest_async('DeleteGroup', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_group(
        self,
        request: ims_20190815_models.DeleteGroupRequest,
    ) -> ims_20190815_models.DeleteGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_group_with_options(request, runtime)

    async def delete_group_async(
        self,
        request: ims_20190815_models.DeleteGroupRequest,
    ) -> ims_20190815_models.DeleteGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_group_with_options_async(request, runtime)

    def delete_login_profile_with_options(
        self,
        request: ims_20190815_models.DeleteLoginProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteLoginProfileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteLoginProfileResponse(),
            self.do_rpcrequest('DeleteLoginProfile', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_login_profile_with_options_async(
        self,
        request: ims_20190815_models.DeleteLoginProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteLoginProfileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteLoginProfileResponse(),
            await self.do_rpcrequest_async('DeleteLoginProfile', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_login_profile(
        self,
        request: ims_20190815_models.DeleteLoginProfileRequest,
    ) -> ims_20190815_models.DeleteLoginProfileResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_login_profile_with_options(request, runtime)

    async def delete_login_profile_async(
        self,
        request: ims_20190815_models.DeleteLoginProfileRequest,
    ) -> ims_20190815_models.DeleteLoginProfileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_login_profile_with_options_async(request, runtime)

    def delete_oidcprovider_with_options(
        self,
        request: ims_20190815_models.DeleteOIDCProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteOIDCProviderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteOIDCProviderResponse(),
            self.do_rpcrequest('DeleteOIDCProvider', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_oidcprovider_with_options_async(
        self,
        request: ims_20190815_models.DeleteOIDCProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteOIDCProviderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteOIDCProviderResponse(),
            await self.do_rpcrequest_async('DeleteOIDCProvider', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_oidcprovider(
        self,
        request: ims_20190815_models.DeleteOIDCProviderRequest,
    ) -> ims_20190815_models.DeleteOIDCProviderResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_oidcprovider_with_options(request, runtime)

    async def delete_oidcprovider_async(
        self,
        request: ims_20190815_models.DeleteOIDCProviderRequest,
    ) -> ims_20190815_models.DeleteOIDCProviderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_oidcprovider_with_options_async(request, runtime)

    def delete_samlprovider_with_options(
        self,
        request: ims_20190815_models.DeleteSAMLProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteSAMLProviderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteSAMLProviderResponse(),
            self.do_rpcrequest('DeleteSAMLProvider', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_samlprovider_with_options_async(
        self,
        request: ims_20190815_models.DeleteSAMLProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteSAMLProviderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteSAMLProviderResponse(),
            await self.do_rpcrequest_async('DeleteSAMLProvider', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_samlprovider(
        self,
        request: ims_20190815_models.DeleteSAMLProviderRequest,
    ) -> ims_20190815_models.DeleteSAMLProviderResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_samlprovider_with_options(request, runtime)

    async def delete_samlprovider_async(
        self,
        request: ims_20190815_models.DeleteSAMLProviderRequest,
    ) -> ims_20190815_models.DeleteSAMLProviderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_samlprovider_with_options_async(request, runtime)

    def delete_user_with_options(
        self,
        request: ims_20190815_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteUserResponse(),
            self.do_rpcrequest('DeleteUser', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_user_with_options_async(
        self,
        request: ims_20190815_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteUserResponse(),
            await self.do_rpcrequest_async('DeleteUser', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_user(
        self,
        request: ims_20190815_models.DeleteUserRequest,
    ) -> ims_20190815_models.DeleteUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_user_with_options(request, runtime)

    async def delete_user_async(
        self,
        request: ims_20190815_models.DeleteUserRequest,
    ) -> ims_20190815_models.DeleteUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_with_options_async(request, runtime)

    def delete_virtual_mfadevice_with_options(
        self,
        request: ims_20190815_models.DeleteVirtualMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteVirtualMFADeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteVirtualMFADeviceResponse(),
            self.do_rpcrequest('DeleteVirtualMFADevice', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_virtual_mfadevice_with_options_async(
        self,
        request: ims_20190815_models.DeleteVirtualMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteVirtualMFADeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteVirtualMFADeviceResponse(),
            await self.do_rpcrequest_async('DeleteVirtualMFADevice', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_virtual_mfadevice(
        self,
        request: ims_20190815_models.DeleteVirtualMFADeviceRequest,
    ) -> ims_20190815_models.DeleteVirtualMFADeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_virtual_mfadevice_with_options(request, runtime)

    async def delete_virtual_mfadevice_async(
        self,
        request: ims_20190815_models.DeleteVirtualMFADeviceRequest,
    ) -> ims_20190815_models.DeleteVirtualMFADeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_virtual_mfadevice_with_options_async(request, runtime)

    def disable_virtual_mfawith_options(
        self,
        request: ims_20190815_models.DisableVirtualMFARequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DisableVirtualMFAResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.DisableVirtualMFAResponse(),
            self.do_rpcrequest('DisableVirtualMFA', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_virtual_mfawith_options_async(
        self,
        request: ims_20190815_models.DisableVirtualMFARequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DisableVirtualMFAResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.DisableVirtualMFAResponse(),
            await self.do_rpcrequest_async('DisableVirtualMFA', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_virtual_mfa(
        self,
        request: ims_20190815_models.DisableVirtualMFARequest,
    ) -> ims_20190815_models.DisableVirtualMFAResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_virtual_mfawith_options(request, runtime)

    async def disable_virtual_mfa_async(
        self,
        request: ims_20190815_models.DisableVirtualMFARequest,
    ) -> ims_20190815_models.DisableVirtualMFAResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_virtual_mfawith_options_async(request, runtime)

    def generate_credential_report_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GenerateCredentialReportResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ims_20190815_models.GenerateCredentialReportResponse(),
            self.do_rpcrequest('GenerateCredentialReport', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def generate_credential_report_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GenerateCredentialReportResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ims_20190815_models.GenerateCredentialReportResponse(),
            await self.do_rpcrequest_async('GenerateCredentialReport', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def generate_credential_report(self) -> ims_20190815_models.GenerateCredentialReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_credential_report_with_options(runtime)

    async def generate_credential_report_async(self) -> ims_20190815_models.GenerateCredentialReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_credential_report_with_options_async(runtime)

    def get_access_key_last_used_with_options(
        self,
        request: ims_20190815_models.GetAccessKeyLastUsedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetAccessKeyLastUsedResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.GetAccessKeyLastUsedResponse(),
            self.do_rpcrequest('GetAccessKeyLastUsed', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_access_key_last_used_with_options_async(
        self,
        request: ims_20190815_models.GetAccessKeyLastUsedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetAccessKeyLastUsedResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.GetAccessKeyLastUsedResponse(),
            await self.do_rpcrequest_async('GetAccessKeyLastUsed', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_access_key_last_used(
        self,
        request: ims_20190815_models.GetAccessKeyLastUsedRequest,
    ) -> ims_20190815_models.GetAccessKeyLastUsedResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_access_key_last_used_with_options(request, runtime)

    async def get_access_key_last_used_async(
        self,
        request: ims_20190815_models.GetAccessKeyLastUsedRequest,
    ) -> ims_20190815_models.GetAccessKeyLastUsedResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_access_key_last_used_with_options_async(request, runtime)

    def get_account_mfainfo_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetAccountMFAInfoResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ims_20190815_models.GetAccountMFAInfoResponse(),
            self.do_rpcrequest('GetAccountMFAInfo', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_account_mfainfo_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetAccountMFAInfoResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ims_20190815_models.GetAccountMFAInfoResponse(),
            await self.do_rpcrequest_async('GetAccountMFAInfo', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_account_mfainfo(self) -> ims_20190815_models.GetAccountMFAInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_account_mfainfo_with_options(runtime)

    async def get_account_mfainfo_async(self) -> ims_20190815_models.GetAccountMFAInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_account_mfainfo_with_options_async(runtime)

    def get_account_security_practice_report_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetAccountSecurityPracticeReportResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ims_20190815_models.GetAccountSecurityPracticeReportResponse(),
            self.do_rpcrequest('GetAccountSecurityPracticeReport', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_account_security_practice_report_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetAccountSecurityPracticeReportResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ims_20190815_models.GetAccountSecurityPracticeReportResponse(),
            await self.do_rpcrequest_async('GetAccountSecurityPracticeReport', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_account_security_practice_report(self) -> ims_20190815_models.GetAccountSecurityPracticeReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_account_security_practice_report_with_options(runtime)

    async def get_account_security_practice_report_async(self) -> ims_20190815_models.GetAccountSecurityPracticeReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_account_security_practice_report_with_options_async(runtime)

    def get_account_summary_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetAccountSummaryResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ims_20190815_models.GetAccountSummaryResponse(),
            self.do_rpcrequest('GetAccountSummary', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_account_summary_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetAccountSummaryResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ims_20190815_models.GetAccountSummaryResponse(),
            await self.do_rpcrequest_async('GetAccountSummary', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_account_summary(self) -> ims_20190815_models.GetAccountSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_account_summary_with_options(runtime)

    async def get_account_summary_async(self) -> ims_20190815_models.GetAccountSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_account_summary_with_options_async(runtime)

    def get_app_secret_with_options(
        self,
        request: ims_20190815_models.GetAppSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetAppSecretResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.GetAppSecretResponse(),
            self.do_rpcrequest('GetAppSecret', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_app_secret_with_options_async(
        self,
        request: ims_20190815_models.GetAppSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetAppSecretResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.GetAppSecretResponse(),
            await self.do_rpcrequest_async('GetAppSecret', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_app_secret(
        self,
        request: ims_20190815_models.GetAppSecretRequest,
    ) -> ims_20190815_models.GetAppSecretResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_app_secret_with_options(request, runtime)

    async def get_app_secret_async(
        self,
        request: ims_20190815_models.GetAppSecretRequest,
    ) -> ims_20190815_models.GetAppSecretResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_app_secret_with_options_async(request, runtime)

    def get_application_with_options(
        self,
        request: ims_20190815_models.GetApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.GetApplicationResponse(),
            self.do_rpcrequest('GetApplication', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_application_with_options_async(
        self,
        request: ims_20190815_models.GetApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.GetApplicationResponse(),
            await self.do_rpcrequest_async('GetApplication', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_application(
        self,
        request: ims_20190815_models.GetApplicationRequest,
    ) -> ims_20190815_models.GetApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_application_with_options(request, runtime)

    async def get_application_async(
        self,
        request: ims_20190815_models.GetApplicationRequest,
    ) -> ims_20190815_models.GetApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_application_with_options_async(request, runtime)

    def get_credential_report_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetCredentialReportResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ims_20190815_models.GetCredentialReportResponse(),
            self.do_rpcrequest('GetCredentialReport', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_credential_report_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetCredentialReportResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ims_20190815_models.GetCredentialReportResponse(),
            await self.do_rpcrequest_async('GetCredentialReport', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_credential_report(self) -> ims_20190815_models.GetCredentialReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_credential_report_with_options(runtime)

    async def get_credential_report_async(self) -> ims_20190815_models.GetCredentialReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_credential_report_with_options_async(runtime)

    def get_default_domain_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetDefaultDomainResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ims_20190815_models.GetDefaultDomainResponse(),
            self.do_rpcrequest('GetDefaultDomain', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_default_domain_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetDefaultDomainResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ims_20190815_models.GetDefaultDomainResponse(),
            await self.do_rpcrequest_async('GetDefaultDomain', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_default_domain(self) -> ims_20190815_models.GetDefaultDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_default_domain_with_options(runtime)

    async def get_default_domain_async(self) -> ims_20190815_models.GetDefaultDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_default_domain_with_options_async(runtime)

    def get_group_with_options(
        self,
        request: ims_20190815_models.GetGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.GetGroupResponse(),
            self.do_rpcrequest('GetGroup', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_group_with_options_async(
        self,
        request: ims_20190815_models.GetGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.GetGroupResponse(),
            await self.do_rpcrequest_async('GetGroup', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_group(
        self,
        request: ims_20190815_models.GetGroupRequest,
    ) -> ims_20190815_models.GetGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_group_with_options(request, runtime)

    async def get_group_async(
        self,
        request: ims_20190815_models.GetGroupRequest,
    ) -> ims_20190815_models.GetGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_group_with_options_async(request, runtime)

    def get_login_profile_with_options(
        self,
        request: ims_20190815_models.GetLoginProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetLoginProfileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.GetLoginProfileResponse(),
            self.do_rpcrequest('GetLoginProfile', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_login_profile_with_options_async(
        self,
        request: ims_20190815_models.GetLoginProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetLoginProfileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.GetLoginProfileResponse(),
            await self.do_rpcrequest_async('GetLoginProfile', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_login_profile(
        self,
        request: ims_20190815_models.GetLoginProfileRequest,
    ) -> ims_20190815_models.GetLoginProfileResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_login_profile_with_options(request, runtime)

    async def get_login_profile_async(
        self,
        request: ims_20190815_models.GetLoginProfileRequest,
    ) -> ims_20190815_models.GetLoginProfileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_login_profile_with_options_async(request, runtime)

    def get_oidcprovider_with_options(
        self,
        request: ims_20190815_models.GetOIDCProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetOIDCProviderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.GetOIDCProviderResponse(),
            self.do_rpcrequest('GetOIDCProvider', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_oidcprovider_with_options_async(
        self,
        request: ims_20190815_models.GetOIDCProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetOIDCProviderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.GetOIDCProviderResponse(),
            await self.do_rpcrequest_async('GetOIDCProvider', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_oidcprovider(
        self,
        request: ims_20190815_models.GetOIDCProviderRequest,
    ) -> ims_20190815_models.GetOIDCProviderResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oidcprovider_with_options(request, runtime)

    async def get_oidcprovider_async(
        self,
        request: ims_20190815_models.GetOIDCProviderRequest,
    ) -> ims_20190815_models.GetOIDCProviderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oidcprovider_with_options_async(request, runtime)

    def get_password_policy_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetPasswordPolicyResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ims_20190815_models.GetPasswordPolicyResponse(),
            self.do_rpcrequest('GetPasswordPolicy', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_password_policy_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetPasswordPolicyResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ims_20190815_models.GetPasswordPolicyResponse(),
            await self.do_rpcrequest_async('GetPasswordPolicy', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_password_policy(self) -> ims_20190815_models.GetPasswordPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_password_policy_with_options(runtime)

    async def get_password_policy_async(self) -> ims_20190815_models.GetPasswordPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_password_policy_with_options_async(runtime)

    def get_samlprovider_with_options(
        self,
        request: ims_20190815_models.GetSAMLProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetSAMLProviderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.GetSAMLProviderResponse(),
            self.do_rpcrequest('GetSAMLProvider', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_samlprovider_with_options_async(
        self,
        request: ims_20190815_models.GetSAMLProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetSAMLProviderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.GetSAMLProviderResponse(),
            await self.do_rpcrequest_async('GetSAMLProvider', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_samlprovider(
        self,
        request: ims_20190815_models.GetSAMLProviderRequest,
    ) -> ims_20190815_models.GetSAMLProviderResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_samlprovider_with_options(request, runtime)

    async def get_samlprovider_async(
        self,
        request: ims_20190815_models.GetSAMLProviderRequest,
    ) -> ims_20190815_models.GetSAMLProviderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_samlprovider_with_options_async(request, runtime)

    def get_security_preference_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetSecurityPreferenceResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ims_20190815_models.GetSecurityPreferenceResponse(),
            self.do_rpcrequest('GetSecurityPreference', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_security_preference_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetSecurityPreferenceResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ims_20190815_models.GetSecurityPreferenceResponse(),
            await self.do_rpcrequest_async('GetSecurityPreference', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_security_preference(self) -> ims_20190815_models.GetSecurityPreferenceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_security_preference_with_options(runtime)

    async def get_security_preference_async(self) -> ims_20190815_models.GetSecurityPreferenceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_security_preference_with_options_async(runtime)

    def get_user_with_options(
        self,
        request: ims_20190815_models.GetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.GetUserResponse(),
            self.do_rpcrequest('GetUser', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_user_with_options_async(
        self,
        request: ims_20190815_models.GetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.GetUserResponse(),
            await self.do_rpcrequest_async('GetUser', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_user(
        self,
        request: ims_20190815_models.GetUserRequest,
    ) -> ims_20190815_models.GetUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_with_options(request, runtime)

    async def get_user_async(
        self,
        request: ims_20190815_models.GetUserRequest,
    ) -> ims_20190815_models.GetUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_with_options_async(request, runtime)

    def get_user_mfainfo_with_options(
        self,
        request: ims_20190815_models.GetUserMFAInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetUserMFAInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.GetUserMFAInfoResponse(),
            self.do_rpcrequest('GetUserMFAInfo', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_user_mfainfo_with_options_async(
        self,
        request: ims_20190815_models.GetUserMFAInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetUserMFAInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.GetUserMFAInfoResponse(),
            await self.do_rpcrequest_async('GetUserMFAInfo', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_user_mfainfo(
        self,
        request: ims_20190815_models.GetUserMFAInfoRequest,
    ) -> ims_20190815_models.GetUserMFAInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_mfainfo_with_options(request, runtime)

    async def get_user_mfainfo_async(
        self,
        request: ims_20190815_models.GetUserMFAInfoRequest,
    ) -> ims_20190815_models.GetUserMFAInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_mfainfo_with_options_async(request, runtime)

    def get_user_sso_settings_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetUserSsoSettingsResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ims_20190815_models.GetUserSsoSettingsResponse(),
            self.do_rpcrequest('GetUserSsoSettings', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_user_sso_settings_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetUserSsoSettingsResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ims_20190815_models.GetUserSsoSettingsResponse(),
            await self.do_rpcrequest_async('GetUserSsoSettings', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_user_sso_settings(self) -> ims_20190815_models.GetUserSsoSettingsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_sso_settings_with_options(runtime)

    async def get_user_sso_settings_async(self) -> ims_20190815_models.GetUserSsoSettingsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_sso_settings_with_options_async(runtime)

    def list_access_keys_with_options(
        self,
        request: ims_20190815_models.ListAccessKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListAccessKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.ListAccessKeysResponse(),
            self.do_rpcrequest('ListAccessKeys', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_access_keys_with_options_async(
        self,
        request: ims_20190815_models.ListAccessKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListAccessKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.ListAccessKeysResponse(),
            await self.do_rpcrequest_async('ListAccessKeys', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_access_keys(
        self,
        request: ims_20190815_models.ListAccessKeysRequest,
    ) -> ims_20190815_models.ListAccessKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_access_keys_with_options(request, runtime)

    async def list_access_keys_async(
        self,
        request: ims_20190815_models.ListAccessKeysRequest,
    ) -> ims_20190815_models.ListAccessKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_access_keys_with_options_async(request, runtime)

    def list_app_secret_ids_with_options(
        self,
        request: ims_20190815_models.ListAppSecretIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListAppSecretIdsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.ListAppSecretIdsResponse(),
            self.do_rpcrequest('ListAppSecretIds', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_app_secret_ids_with_options_async(
        self,
        request: ims_20190815_models.ListAppSecretIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListAppSecretIdsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.ListAppSecretIdsResponse(),
            await self.do_rpcrequest_async('ListAppSecretIds', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_app_secret_ids(
        self,
        request: ims_20190815_models.ListAppSecretIdsRequest,
    ) -> ims_20190815_models.ListAppSecretIdsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_app_secret_ids_with_options(request, runtime)

    async def list_app_secret_ids_async(
        self,
        request: ims_20190815_models.ListAppSecretIdsRequest,
    ) -> ims_20190815_models.ListAppSecretIdsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_app_secret_ids_with_options_async(request, runtime)

    def list_applications_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListApplicationsResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ims_20190815_models.ListApplicationsResponse(),
            self.do_rpcrequest('ListApplications', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_applications_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListApplicationsResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ims_20190815_models.ListApplicationsResponse(),
            await self.do_rpcrequest_async('ListApplications', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_applications(self) -> ims_20190815_models.ListApplicationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_applications_with_options(runtime)

    async def list_applications_async(self) -> ims_20190815_models.ListApplicationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_applications_with_options_async(runtime)

    def list_groups_with_options(
        self,
        request: ims_20190815_models.ListGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.ListGroupsResponse(),
            self.do_rpcrequest('ListGroups', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_groups_with_options_async(
        self,
        request: ims_20190815_models.ListGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.ListGroupsResponse(),
            await self.do_rpcrequest_async('ListGroups', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_groups(
        self,
        request: ims_20190815_models.ListGroupsRequest,
    ) -> ims_20190815_models.ListGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_groups_with_options(request, runtime)

    async def list_groups_async(
        self,
        request: ims_20190815_models.ListGroupsRequest,
    ) -> ims_20190815_models.ListGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_groups_with_options_async(request, runtime)

    def list_groups_for_user_with_options(
        self,
        request: ims_20190815_models.ListGroupsForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListGroupsForUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.ListGroupsForUserResponse(),
            self.do_rpcrequest('ListGroupsForUser', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_groups_for_user_with_options_async(
        self,
        request: ims_20190815_models.ListGroupsForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListGroupsForUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.ListGroupsForUserResponse(),
            await self.do_rpcrequest_async('ListGroupsForUser', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_groups_for_user(
        self,
        request: ims_20190815_models.ListGroupsForUserRequest,
    ) -> ims_20190815_models.ListGroupsForUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_groups_for_user_with_options(request, runtime)

    async def list_groups_for_user_async(
        self,
        request: ims_20190815_models.ListGroupsForUserRequest,
    ) -> ims_20190815_models.ListGroupsForUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_groups_for_user_with_options_async(request, runtime)

    def list_oidcproviders_with_options(
        self,
        request: ims_20190815_models.ListOIDCProvidersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListOIDCProvidersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.ListOIDCProvidersResponse(),
            self.do_rpcrequest('ListOIDCProviders', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_oidcproviders_with_options_async(
        self,
        request: ims_20190815_models.ListOIDCProvidersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListOIDCProvidersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.ListOIDCProvidersResponse(),
            await self.do_rpcrequest_async('ListOIDCProviders', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_oidcproviders(
        self,
        request: ims_20190815_models.ListOIDCProvidersRequest,
    ) -> ims_20190815_models.ListOIDCProvidersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_oidcproviders_with_options(request, runtime)

    async def list_oidcproviders_async(
        self,
        request: ims_20190815_models.ListOIDCProvidersRequest,
    ) -> ims_20190815_models.ListOIDCProvidersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_oidcproviders_with_options_async(request, runtime)

    def list_predefined_scopes_with_options(
        self,
        request: ims_20190815_models.ListPredefinedScopesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListPredefinedScopesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.ListPredefinedScopesResponse(),
            self.do_rpcrequest('ListPredefinedScopes', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_predefined_scopes_with_options_async(
        self,
        request: ims_20190815_models.ListPredefinedScopesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListPredefinedScopesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.ListPredefinedScopesResponse(),
            await self.do_rpcrequest_async('ListPredefinedScopes', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_predefined_scopes(
        self,
        request: ims_20190815_models.ListPredefinedScopesRequest,
    ) -> ims_20190815_models.ListPredefinedScopesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_predefined_scopes_with_options(request, runtime)

    async def list_predefined_scopes_async(
        self,
        request: ims_20190815_models.ListPredefinedScopesRequest,
    ) -> ims_20190815_models.ListPredefinedScopesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_predefined_scopes_with_options_async(request, runtime)

    def list_samlproviders_with_options(
        self,
        request: ims_20190815_models.ListSAMLProvidersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListSAMLProvidersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.ListSAMLProvidersResponse(),
            self.do_rpcrequest('ListSAMLProviders', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_samlproviders_with_options_async(
        self,
        request: ims_20190815_models.ListSAMLProvidersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListSAMLProvidersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.ListSAMLProvidersResponse(),
            await self.do_rpcrequest_async('ListSAMLProviders', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_samlproviders(
        self,
        request: ims_20190815_models.ListSAMLProvidersRequest,
    ) -> ims_20190815_models.ListSAMLProvidersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_samlproviders_with_options(request, runtime)

    async def list_samlproviders_async(
        self,
        request: ims_20190815_models.ListSAMLProvidersRequest,
    ) -> ims_20190815_models.ListSAMLProvidersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_samlproviders_with_options_async(request, runtime)

    def list_user_basic_infos_with_options(
        self,
        request: ims_20190815_models.ListUserBasicInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListUserBasicInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.ListUserBasicInfosResponse(),
            self.do_rpcrequest('ListUserBasicInfos', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_user_basic_infos_with_options_async(
        self,
        request: ims_20190815_models.ListUserBasicInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListUserBasicInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.ListUserBasicInfosResponse(),
            await self.do_rpcrequest_async('ListUserBasicInfos', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_user_basic_infos(
        self,
        request: ims_20190815_models.ListUserBasicInfosRequest,
    ) -> ims_20190815_models.ListUserBasicInfosResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_user_basic_infos_with_options(request, runtime)

    async def list_user_basic_infos_async(
        self,
        request: ims_20190815_models.ListUserBasicInfosRequest,
    ) -> ims_20190815_models.ListUserBasicInfosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_user_basic_infos_with_options_async(request, runtime)

    def list_users_with_options(
        self,
        request: ims_20190815_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.ListUsersResponse(),
            self.do_rpcrequest('ListUsers', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_users_with_options_async(
        self,
        request: ims_20190815_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.ListUsersResponse(),
            await self.do_rpcrequest_async('ListUsers', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_users(
        self,
        request: ims_20190815_models.ListUsersRequest,
    ) -> ims_20190815_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    async def list_users_async(
        self,
        request: ims_20190815_models.ListUsersRequest,
    ) -> ims_20190815_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_users_with_options_async(request, runtime)

    def list_users_for_group_with_options(
        self,
        request: ims_20190815_models.ListUsersForGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListUsersForGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.ListUsersForGroupResponse(),
            self.do_rpcrequest('ListUsersForGroup', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_users_for_group_with_options_async(
        self,
        request: ims_20190815_models.ListUsersForGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListUsersForGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.ListUsersForGroupResponse(),
            await self.do_rpcrequest_async('ListUsersForGroup', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_users_for_group(
        self,
        request: ims_20190815_models.ListUsersForGroupRequest,
    ) -> ims_20190815_models.ListUsersForGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_users_for_group_with_options(request, runtime)

    async def list_users_for_group_async(
        self,
        request: ims_20190815_models.ListUsersForGroupRequest,
    ) -> ims_20190815_models.ListUsersForGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_users_for_group_with_options_async(request, runtime)

    def list_virtual_mfadevices_with_options(
        self,
        request: ims_20190815_models.ListVirtualMFADevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListVirtualMFADevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.ListVirtualMFADevicesResponse(),
            self.do_rpcrequest('ListVirtualMFADevices', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_virtual_mfadevices_with_options_async(
        self,
        request: ims_20190815_models.ListVirtualMFADevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListVirtualMFADevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.ListVirtualMFADevicesResponse(),
            await self.do_rpcrequest_async('ListVirtualMFADevices', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_virtual_mfadevices(
        self,
        request: ims_20190815_models.ListVirtualMFADevicesRequest,
    ) -> ims_20190815_models.ListVirtualMFADevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_virtual_mfadevices_with_options(request, runtime)

    async def list_virtual_mfadevices_async(
        self,
        request: ims_20190815_models.ListVirtualMFADevicesRequest,
    ) -> ims_20190815_models.ListVirtualMFADevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_virtual_mfadevices_with_options_async(request, runtime)

    def remove_client_id_from_oidcprovider_with_options(
        self,
        request: ims_20190815_models.RemoveClientIdFromOIDCProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.RemoveClientIdFromOIDCProviderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.RemoveClientIdFromOIDCProviderResponse(),
            self.do_rpcrequest('RemoveClientIdFromOIDCProvider', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_client_id_from_oidcprovider_with_options_async(
        self,
        request: ims_20190815_models.RemoveClientIdFromOIDCProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.RemoveClientIdFromOIDCProviderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.RemoveClientIdFromOIDCProviderResponse(),
            await self.do_rpcrequest_async('RemoveClientIdFromOIDCProvider', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_client_id_from_oidcprovider(
        self,
        request: ims_20190815_models.RemoveClientIdFromOIDCProviderRequest,
    ) -> ims_20190815_models.RemoveClientIdFromOIDCProviderResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_client_id_from_oidcprovider_with_options(request, runtime)

    async def remove_client_id_from_oidcprovider_async(
        self,
        request: ims_20190815_models.RemoveClientIdFromOIDCProviderRequest,
    ) -> ims_20190815_models.RemoveClientIdFromOIDCProviderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_client_id_from_oidcprovider_with_options_async(request, runtime)

    def remove_fingerprint_from_oidcprovider_with_options(
        self,
        request: ims_20190815_models.RemoveFingerprintFromOIDCProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.RemoveFingerprintFromOIDCProviderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.RemoveFingerprintFromOIDCProviderResponse(),
            self.do_rpcrequest('RemoveFingerprintFromOIDCProvider', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_fingerprint_from_oidcprovider_with_options_async(
        self,
        request: ims_20190815_models.RemoveFingerprintFromOIDCProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.RemoveFingerprintFromOIDCProviderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.RemoveFingerprintFromOIDCProviderResponse(),
            await self.do_rpcrequest_async('RemoveFingerprintFromOIDCProvider', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_fingerprint_from_oidcprovider(
        self,
        request: ims_20190815_models.RemoveFingerprintFromOIDCProviderRequest,
    ) -> ims_20190815_models.RemoveFingerprintFromOIDCProviderResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_fingerprint_from_oidcprovider_with_options(request, runtime)

    async def remove_fingerprint_from_oidcprovider_async(
        self,
        request: ims_20190815_models.RemoveFingerprintFromOIDCProviderRequest,
    ) -> ims_20190815_models.RemoveFingerprintFromOIDCProviderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_fingerprint_from_oidcprovider_with_options_async(request, runtime)

    def remove_user_from_group_with_options(
        self,
        request: ims_20190815_models.RemoveUserFromGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.RemoveUserFromGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.RemoveUserFromGroupResponse(),
            self.do_rpcrequest('RemoveUserFromGroup', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_user_from_group_with_options_async(
        self,
        request: ims_20190815_models.RemoveUserFromGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.RemoveUserFromGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.RemoveUserFromGroupResponse(),
            await self.do_rpcrequest_async('RemoveUserFromGroup', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_user_from_group(
        self,
        request: ims_20190815_models.RemoveUserFromGroupRequest,
    ) -> ims_20190815_models.RemoveUserFromGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_user_from_group_with_options(request, runtime)

    async def remove_user_from_group_async(
        self,
        request: ims_20190815_models.RemoveUserFromGroupRequest,
    ) -> ims_20190815_models.RemoveUserFromGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_user_from_group_with_options_async(request, runtime)

    def set_default_domain_with_options(
        self,
        request: ims_20190815_models.SetDefaultDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.SetDefaultDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.SetDefaultDomainResponse(),
            self.do_rpcrequest('SetDefaultDomain', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_default_domain_with_options_async(
        self,
        request: ims_20190815_models.SetDefaultDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.SetDefaultDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.SetDefaultDomainResponse(),
            await self.do_rpcrequest_async('SetDefaultDomain', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_default_domain(
        self,
        request: ims_20190815_models.SetDefaultDomainRequest,
    ) -> ims_20190815_models.SetDefaultDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_default_domain_with_options(request, runtime)

    async def set_default_domain_async(
        self,
        request: ims_20190815_models.SetDefaultDomainRequest,
    ) -> ims_20190815_models.SetDefaultDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_default_domain_with_options_async(request, runtime)

    def set_password_policy_with_options(
        self,
        request: ims_20190815_models.SetPasswordPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.SetPasswordPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.SetPasswordPolicyResponse(),
            self.do_rpcrequest('SetPasswordPolicy', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_password_policy_with_options_async(
        self,
        request: ims_20190815_models.SetPasswordPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.SetPasswordPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.SetPasswordPolicyResponse(),
            await self.do_rpcrequest_async('SetPasswordPolicy', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_password_policy(
        self,
        request: ims_20190815_models.SetPasswordPolicyRequest,
    ) -> ims_20190815_models.SetPasswordPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_password_policy_with_options(request, runtime)

    async def set_password_policy_async(
        self,
        request: ims_20190815_models.SetPasswordPolicyRequest,
    ) -> ims_20190815_models.SetPasswordPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_password_policy_with_options_async(request, runtime)

    def set_security_preference_with_options(
        self,
        tmp_req: ims_20190815_models.SetSecurityPreferenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.SetSecurityPreferenceResponse:
        UtilClient.validate_model(tmp_req)
        request = ims_20190815_models.SetSecurityPreferenceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.verification_types):
            request.verification_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.verification_types, 'VerificationTypes', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.SetSecurityPreferenceResponse(),
            self.do_rpcrequest('SetSecurityPreference', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_security_preference_with_options_async(
        self,
        tmp_req: ims_20190815_models.SetSecurityPreferenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.SetSecurityPreferenceResponse:
        UtilClient.validate_model(tmp_req)
        request = ims_20190815_models.SetSecurityPreferenceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.verification_types):
            request.verification_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.verification_types, 'VerificationTypes', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.SetSecurityPreferenceResponse(),
            await self.do_rpcrequest_async('SetSecurityPreference', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_security_preference(
        self,
        request: ims_20190815_models.SetSecurityPreferenceRequest,
    ) -> ims_20190815_models.SetSecurityPreferenceResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_security_preference_with_options(request, runtime)

    async def set_security_preference_async(
        self,
        request: ims_20190815_models.SetSecurityPreferenceRequest,
    ) -> ims_20190815_models.SetSecurityPreferenceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_security_preference_with_options_async(request, runtime)

    def set_user_sso_settings_with_options(
        self,
        request: ims_20190815_models.SetUserSsoSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.SetUserSsoSettingsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.SetUserSsoSettingsResponse(),
            self.do_rpcrequest('SetUserSsoSettings', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_user_sso_settings_with_options_async(
        self,
        request: ims_20190815_models.SetUserSsoSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.SetUserSsoSettingsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.SetUserSsoSettingsResponse(),
            await self.do_rpcrequest_async('SetUserSsoSettings', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_user_sso_settings(
        self,
        request: ims_20190815_models.SetUserSsoSettingsRequest,
    ) -> ims_20190815_models.SetUserSsoSettingsResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_user_sso_settings_with_options(request, runtime)

    async def set_user_sso_settings_async(
        self,
        request: ims_20190815_models.SetUserSsoSettingsRequest,
    ) -> ims_20190815_models.SetUserSsoSettingsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_user_sso_settings_with_options_async(request, runtime)

    def unbind_mfadevice_with_options(
        self,
        request: ims_20190815_models.UnbindMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UnbindMFADeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.UnbindMFADeviceResponse(),
            self.do_rpcrequest('UnbindMFADevice', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unbind_mfadevice_with_options_async(
        self,
        request: ims_20190815_models.UnbindMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UnbindMFADeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.UnbindMFADeviceResponse(),
            await self.do_rpcrequest_async('UnbindMFADevice', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unbind_mfadevice(
        self,
        request: ims_20190815_models.UnbindMFADeviceRequest,
    ) -> ims_20190815_models.UnbindMFADeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.unbind_mfadevice_with_options(request, runtime)

    async def unbind_mfadevice_async(
        self,
        request: ims_20190815_models.UnbindMFADeviceRequest,
    ) -> ims_20190815_models.UnbindMFADeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unbind_mfadevice_with_options_async(request, runtime)

    def update_access_key_with_options(
        self,
        request: ims_20190815_models.UpdateAccessKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UpdateAccessKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.UpdateAccessKeyResponse(),
            self.do_rpcrequest('UpdateAccessKey', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_access_key_with_options_async(
        self,
        request: ims_20190815_models.UpdateAccessKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UpdateAccessKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.UpdateAccessKeyResponse(),
            await self.do_rpcrequest_async('UpdateAccessKey', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_access_key(
        self,
        request: ims_20190815_models.UpdateAccessKeyRequest,
    ) -> ims_20190815_models.UpdateAccessKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_access_key_with_options(request, runtime)

    async def update_access_key_async(
        self,
        request: ims_20190815_models.UpdateAccessKeyRequest,
    ) -> ims_20190815_models.UpdateAccessKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_access_key_with_options_async(request, runtime)

    def update_application_with_options(
        self,
        request: ims_20190815_models.UpdateApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UpdateApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.UpdateApplicationResponse(),
            self.do_rpcrequest('UpdateApplication', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_application_with_options_async(
        self,
        request: ims_20190815_models.UpdateApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UpdateApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.UpdateApplicationResponse(),
            await self.do_rpcrequest_async('UpdateApplication', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_application(
        self,
        request: ims_20190815_models.UpdateApplicationRequest,
    ) -> ims_20190815_models.UpdateApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_application_with_options(request, runtime)

    async def update_application_async(
        self,
        request: ims_20190815_models.UpdateApplicationRequest,
    ) -> ims_20190815_models.UpdateApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_application_with_options_async(request, runtime)

    def update_group_with_options(
        self,
        request: ims_20190815_models.UpdateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UpdateGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.UpdateGroupResponse(),
            self.do_rpcrequest('UpdateGroup', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_group_with_options_async(
        self,
        request: ims_20190815_models.UpdateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UpdateGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.UpdateGroupResponse(),
            await self.do_rpcrequest_async('UpdateGroup', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_group(
        self,
        request: ims_20190815_models.UpdateGroupRequest,
    ) -> ims_20190815_models.UpdateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_group_with_options(request, runtime)

    async def update_group_async(
        self,
        request: ims_20190815_models.UpdateGroupRequest,
    ) -> ims_20190815_models.UpdateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_group_with_options_async(request, runtime)

    def update_login_profile_with_options(
        self,
        request: ims_20190815_models.UpdateLoginProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UpdateLoginProfileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.UpdateLoginProfileResponse(),
            self.do_rpcrequest('UpdateLoginProfile', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_login_profile_with_options_async(
        self,
        request: ims_20190815_models.UpdateLoginProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UpdateLoginProfileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.UpdateLoginProfileResponse(),
            await self.do_rpcrequest_async('UpdateLoginProfile', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_login_profile(
        self,
        request: ims_20190815_models.UpdateLoginProfileRequest,
    ) -> ims_20190815_models.UpdateLoginProfileResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_login_profile_with_options(request, runtime)

    async def update_login_profile_async(
        self,
        request: ims_20190815_models.UpdateLoginProfileRequest,
    ) -> ims_20190815_models.UpdateLoginProfileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_login_profile_with_options_async(request, runtime)

    def update_oidcprovider_with_options(
        self,
        request: ims_20190815_models.UpdateOIDCProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UpdateOIDCProviderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.UpdateOIDCProviderResponse(),
            self.do_rpcrequest('UpdateOIDCProvider', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_oidcprovider_with_options_async(
        self,
        request: ims_20190815_models.UpdateOIDCProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UpdateOIDCProviderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.UpdateOIDCProviderResponse(),
            await self.do_rpcrequest_async('UpdateOIDCProvider', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_oidcprovider(
        self,
        request: ims_20190815_models.UpdateOIDCProviderRequest,
    ) -> ims_20190815_models.UpdateOIDCProviderResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_oidcprovider_with_options(request, runtime)

    async def update_oidcprovider_async(
        self,
        request: ims_20190815_models.UpdateOIDCProviderRequest,
    ) -> ims_20190815_models.UpdateOIDCProviderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_oidcprovider_with_options_async(request, runtime)

    def update_samlprovider_with_options(
        self,
        request: ims_20190815_models.UpdateSAMLProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UpdateSAMLProviderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.UpdateSAMLProviderResponse(),
            self.do_rpcrequest('UpdateSAMLProvider', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_samlprovider_with_options_async(
        self,
        request: ims_20190815_models.UpdateSAMLProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UpdateSAMLProviderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.UpdateSAMLProviderResponse(),
            await self.do_rpcrequest_async('UpdateSAMLProvider', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_samlprovider(
        self,
        request: ims_20190815_models.UpdateSAMLProviderRequest,
    ) -> ims_20190815_models.UpdateSAMLProviderResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_samlprovider_with_options(request, runtime)

    async def update_samlprovider_async(
        self,
        request: ims_20190815_models.UpdateSAMLProviderRequest,
    ) -> ims_20190815_models.UpdateSAMLProviderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_samlprovider_with_options_async(request, runtime)

    def update_user_with_options(
        self,
        request: ims_20190815_models.UpdateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UpdateUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.UpdateUserResponse(),
            self.do_rpcrequest('UpdateUser', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_user_with_options_async(
        self,
        request: ims_20190815_models.UpdateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UpdateUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ims_20190815_models.UpdateUserResponse(),
            await self.do_rpcrequest_async('UpdateUser', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_user(
        self,
        request: ims_20190815_models.UpdateUserRequest,
    ) -> ims_20190815_models.UpdateUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_user_with_options(request, runtime)

    async def update_user_async(
        self,
        request: ims_20190815_models.UpdateUserRequest,
    ) -> ims_20190815_models.UpdateUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_user_with_options_async(request, runtime)
