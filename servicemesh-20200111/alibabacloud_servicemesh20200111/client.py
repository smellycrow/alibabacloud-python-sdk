# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_servicemesh20200111 import models as servicemesh_20200111_models
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
        self._endpoint = self.get_endpoint('servicemesh', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def run_diagnosis_with_options(
        self,
        request: servicemesh_20200111_models.RunDiagnosisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.RunDiagnosisResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.RunDiagnosisResponse(),
            self.do_rpcrequest('RunDiagnosis', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def run_diagnosis_with_options_async(
        self,
        request: servicemesh_20200111_models.RunDiagnosisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.RunDiagnosisResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.RunDiagnosisResponse(),
            await self.do_rpcrequest_async('RunDiagnosis', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def run_diagnosis(
        self,
        request: servicemesh_20200111_models.RunDiagnosisRequest,
    ) -> servicemesh_20200111_models.RunDiagnosisResponse:
        runtime = util_models.RuntimeOptions()
        return self.run_diagnosis_with_options(request, runtime)

    async def run_diagnosis_async(
        self,
        request: servicemesh_20200111_models.RunDiagnosisRequest,
    ) -> servicemesh_20200111_models.RunDiagnosisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_diagnosis_with_options_async(request, runtime)

    def describe_guest_cluster_access_log_dashboards_with_options(
        self,
        request: servicemesh_20200111_models.DescribeGuestClusterAccessLogDashboardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeGuestClusterAccessLogDashboardsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeGuestClusterAccessLogDashboardsResponse(),
            self.do_rpcrequest('DescribeGuestClusterAccessLogDashboards', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_guest_cluster_access_log_dashboards_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeGuestClusterAccessLogDashboardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeGuestClusterAccessLogDashboardsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeGuestClusterAccessLogDashboardsResponse(),
            await self.do_rpcrequest_async('DescribeGuestClusterAccessLogDashboards', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_guest_cluster_access_log_dashboards(
        self,
        request: servicemesh_20200111_models.DescribeGuestClusterAccessLogDashboardsRequest,
    ) -> servicemesh_20200111_models.DescribeGuestClusterAccessLogDashboardsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_guest_cluster_access_log_dashboards_with_options(request, runtime)

    async def describe_guest_cluster_access_log_dashboards_async(
        self,
        request: servicemesh_20200111_models.DescribeGuestClusterAccessLogDashboardsRequest,
    ) -> servicemesh_20200111_models.DescribeGuestClusterAccessLogDashboardsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_guest_cluster_access_log_dashboards_with_options_async(request, runtime)

    def list_builtin_envoy_filter_with_options(
        self,
        request: servicemesh_20200111_models.ListBuiltinEnvoyFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.ListBuiltinEnvoyFilterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.ListBuiltinEnvoyFilterResponse(),
            self.do_rpcrequest('ListBuiltinEnvoyFilter', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_builtin_envoy_filter_with_options_async(
        self,
        request: servicemesh_20200111_models.ListBuiltinEnvoyFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.ListBuiltinEnvoyFilterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.ListBuiltinEnvoyFilterResponse(),
            await self.do_rpcrequest_async('ListBuiltinEnvoyFilter', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_builtin_envoy_filter(
        self,
        request: servicemesh_20200111_models.ListBuiltinEnvoyFilterRequest,
    ) -> servicemesh_20200111_models.ListBuiltinEnvoyFilterResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_builtin_envoy_filter_with_options(request, runtime)

    async def list_builtin_envoy_filter_async(
        self,
        request: servicemesh_20200111_models.ListBuiltinEnvoyFilterRequest,
    ) -> servicemesh_20200111_models.ListBuiltinEnvoyFilterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_builtin_envoy_filter_with_options_async(request, runtime)

    def describe_service_meshes_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshesResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshesResponse(),
            self.do_rpcrequest('DescribeServiceMeshes', '2020-01-11', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_service_meshes_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshesResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshesResponse(),
            await self.do_rpcrequest_async('DescribeServiceMeshes', '2020-01-11', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_service_meshes(self) -> servicemesh_20200111_models.DescribeServiceMeshesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_service_meshes_with_options(runtime)

    async def describe_service_meshes_async(self) -> servicemesh_20200111_models.DescribeServiceMeshesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_service_meshes_with_options_async(runtime)

    def modify_builtin_envoy_filter_with_options(
        self,
        request: servicemesh_20200111_models.ModifyBuiltinEnvoyFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.ModifyBuiltinEnvoyFilterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.ModifyBuiltinEnvoyFilterResponse(),
            self.do_rpcrequest('ModifyBuiltinEnvoyFilter', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_builtin_envoy_filter_with_options_async(
        self,
        request: servicemesh_20200111_models.ModifyBuiltinEnvoyFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.ModifyBuiltinEnvoyFilterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.ModifyBuiltinEnvoyFilterResponse(),
            await self.do_rpcrequest_async('ModifyBuiltinEnvoyFilter', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_builtin_envoy_filter(
        self,
        request: servicemesh_20200111_models.ModifyBuiltinEnvoyFilterRequest,
    ) -> servicemesh_20200111_models.ModifyBuiltinEnvoyFilterResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_builtin_envoy_filter_with_options(request, runtime)

    async def modify_builtin_envoy_filter_async(
        self,
        request: servicemesh_20200111_models.ModifyBuiltinEnvoyFilterRequest,
    ) -> servicemesh_20200111_models.ModifyBuiltinEnvoyFilterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_builtin_envoy_filter_with_options_async(request, runtime)

    def describe_available_nacos_instances_with_options(
        self,
        request: servicemesh_20200111_models.DescribeAvailableNacosInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeAvailableNacosInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeAvailableNacosInstancesResponse(),
            self.do_rpcrequest('DescribeAvailableNacosInstances', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_available_nacos_instances_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeAvailableNacosInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeAvailableNacosInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeAvailableNacosInstancesResponse(),
            await self.do_rpcrequest_async('DescribeAvailableNacosInstances', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_available_nacos_instances(
        self,
        request: servicemesh_20200111_models.DescribeAvailableNacosInstancesRequest,
    ) -> servicemesh_20200111_models.DescribeAvailableNacosInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_available_nacos_instances_with_options(request, runtime)

    async def describe_available_nacos_instances_async(
        self,
        request: servicemesh_20200111_models.DescribeAvailableNacosInstancesRequest,
    ) -> servicemesh_20200111_models.DescribeAvailableNacosInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_nacos_instances_with_options_async(request, runtime)

    def describe_ingress_gateways_with_options(
        self,
        request: servicemesh_20200111_models.DescribeIngressGatewaysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeIngressGatewaysResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeIngressGatewaysResponse(),
            self.do_rpcrequest('DescribeIngressGateways', '2020-01-11', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_ingress_gateways_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeIngressGatewaysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeIngressGatewaysResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeIngressGatewaysResponse(),
            await self.do_rpcrequest_async('DescribeIngressGateways', '2020-01-11', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_ingress_gateways(
        self,
        request: servicemesh_20200111_models.DescribeIngressGatewaysRequest,
    ) -> servicemesh_20200111_models.DescribeIngressGatewaysResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ingress_gateways_with_options(request, runtime)

    async def describe_ingress_gateways_async(
        self,
        request: servicemesh_20200111_models.DescribeIngressGatewaysRequest,
    ) -> servicemesh_20200111_models.DescribeIngressGatewaysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ingress_gateways_with_options_async(request, runtime)

    def describe_service_mesh_detail_with_options(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshDetailResponse(),
            self.do_rpcrequest('DescribeServiceMeshDetail', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_service_mesh_detail_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshDetailResponse(),
            await self.do_rpcrequest_async('DescribeServiceMeshDetail', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_service_mesh_detail(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshDetailRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_service_mesh_detail_with_options(request, runtime)

    async def describe_service_mesh_detail_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshDetailRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_service_mesh_detail_with_options_async(request, runtime)

    def upgrade_mesh_version_with_options(
        self,
        request: servicemesh_20200111_models.UpgradeMeshVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpgradeMeshVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpgradeMeshVersionResponse(),
            self.do_rpcrequest('UpgradeMeshVersion', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upgrade_mesh_version_with_options_async(
        self,
        request: servicemesh_20200111_models.UpgradeMeshVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpgradeMeshVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpgradeMeshVersionResponse(),
            await self.do_rpcrequest_async('UpgradeMeshVersion', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upgrade_mesh_version(
        self,
        request: servicemesh_20200111_models.UpgradeMeshVersionRequest,
    ) -> servicemesh_20200111_models.UpgradeMeshVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_mesh_version_with_options(request, runtime)

    async def upgrade_mesh_version_async(
        self,
        request: servicemesh_20200111_models.UpgradeMeshVersionRequest,
    ) -> servicemesh_20200111_models.UpgradeMeshVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_mesh_version_with_options_async(request, runtime)

    def describe_service_mesh_kubeconfig_with_options(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshKubeconfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshKubeconfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshKubeconfigResponse(),
            self.do_rpcrequest('DescribeServiceMeshKubeconfig', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_service_mesh_kubeconfig_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshKubeconfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshKubeconfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshKubeconfigResponse(),
            await self.do_rpcrequest_async('DescribeServiceMeshKubeconfig', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_service_mesh_kubeconfig(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshKubeconfigRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshKubeconfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_service_mesh_kubeconfig_with_options(request, runtime)

    async def describe_service_mesh_kubeconfig_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshKubeconfigRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshKubeconfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_service_mesh_kubeconfig_with_options_async(request, runtime)

    def get_ca_cert_with_options(
        self,
        request: servicemesh_20200111_models.GetCaCertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetCaCertResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetCaCertResponse(),
            self.do_rpcrequest('GetCaCert', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_ca_cert_with_options_async(
        self,
        request: servicemesh_20200111_models.GetCaCertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetCaCertResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetCaCertResponse(),
            await self.do_rpcrequest_async('GetCaCert', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_ca_cert(
        self,
        request: servicemesh_20200111_models.GetCaCertRequest,
    ) -> servicemesh_20200111_models.GetCaCertResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ca_cert_with_options(request, runtime)

    async def get_ca_cert_async(
        self,
        request: servicemesh_20200111_models.GetCaCertRequest,
    ) -> servicemesh_20200111_models.GetCaCertResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ca_cert_with_options_async(request, runtime)

    def get_service_mesh_slb_with_options(
        self,
        request: servicemesh_20200111_models.GetServiceMeshSlbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetServiceMeshSlbResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetServiceMeshSlbResponse(),
            self.do_rpcrequest('GetServiceMeshSlb', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_service_mesh_slb_with_options_async(
        self,
        request: servicemesh_20200111_models.GetServiceMeshSlbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetServiceMeshSlbResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetServiceMeshSlbResponse(),
            await self.do_rpcrequest_async('GetServiceMeshSlb', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_service_mesh_slb(
        self,
        request: servicemesh_20200111_models.GetServiceMeshSlbRequest,
    ) -> servicemesh_20200111_models.GetServiceMeshSlbResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_service_mesh_slb_with_options(request, runtime)

    async def get_service_mesh_slb_async(
        self,
        request: servicemesh_20200111_models.GetServiceMeshSlbRequest,
    ) -> servicemesh_20200111_models.GetServiceMeshSlbResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_service_mesh_slb_with_options_async(request, runtime)

    def get_registered_service_endpoints_with_options(
        self,
        request: servicemesh_20200111_models.GetRegisteredServiceEndpointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetRegisteredServiceEndpointsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetRegisteredServiceEndpointsResponse(),
            self.do_rpcrequest('GetRegisteredServiceEndpoints', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_registered_service_endpoints_with_options_async(
        self,
        request: servicemesh_20200111_models.GetRegisteredServiceEndpointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetRegisteredServiceEndpointsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetRegisteredServiceEndpointsResponse(),
            await self.do_rpcrequest_async('GetRegisteredServiceEndpoints', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_registered_service_endpoints(
        self,
        request: servicemesh_20200111_models.GetRegisteredServiceEndpointsRequest,
    ) -> servicemesh_20200111_models.GetRegisteredServiceEndpointsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_registered_service_endpoints_with_options(request, runtime)

    async def get_registered_service_endpoints_async(
        self,
        request: servicemesh_20200111_models.GetRegisteredServiceEndpointsRequest,
    ) -> servicemesh_20200111_models.GetRegisteredServiceEndpointsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_registered_service_endpoints_with_options_async(request, runtime)

    def get_auto_injection_label_sync_status_with_options(
        self,
        request: servicemesh_20200111_models.GetAutoInjectionLabelSyncStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetAutoInjectionLabelSyncStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetAutoInjectionLabelSyncStatusResponse(),
            self.do_rpcrequest('GetAutoInjectionLabelSyncStatus', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_auto_injection_label_sync_status_with_options_async(
        self,
        request: servicemesh_20200111_models.GetAutoInjectionLabelSyncStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetAutoInjectionLabelSyncStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetAutoInjectionLabelSyncStatusResponse(),
            await self.do_rpcrequest_async('GetAutoInjectionLabelSyncStatus', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_auto_injection_label_sync_status(
        self,
        request: servicemesh_20200111_models.GetAutoInjectionLabelSyncStatusRequest,
    ) -> servicemesh_20200111_models.GetAutoInjectionLabelSyncStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_auto_injection_label_sync_status_with_options(request, runtime)

    async def get_auto_injection_label_sync_status_async(
        self,
        request: servicemesh_20200111_models.GetAutoInjectionLabelSyncStatusRequest,
    ) -> servicemesh_20200111_models.GetAutoInjectionLabelSyncStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_auto_injection_label_sync_status_with_options_async(request, runtime)

    def get_registered_service_namespaces_with_options(
        self,
        request: servicemesh_20200111_models.GetRegisteredServiceNamespacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetRegisteredServiceNamespacesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetRegisteredServiceNamespacesResponse(),
            self.do_rpcrequest('GetRegisteredServiceNamespaces', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_registered_service_namespaces_with_options_async(
        self,
        request: servicemesh_20200111_models.GetRegisteredServiceNamespacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetRegisteredServiceNamespacesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetRegisteredServiceNamespacesResponse(),
            await self.do_rpcrequest_async('GetRegisteredServiceNamespaces', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_registered_service_namespaces(
        self,
        request: servicemesh_20200111_models.GetRegisteredServiceNamespacesRequest,
    ) -> servicemesh_20200111_models.GetRegisteredServiceNamespacesResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_registered_service_namespaces_with_options(request, runtime)

    async def get_registered_service_namespaces_async(
        self,
        request: servicemesh_20200111_models.GetRegisteredServiceNamespacesRequest,
    ) -> servicemesh_20200111_models.GetRegisteredServiceNamespacesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_registered_service_namespaces_with_options_async(request, runtime)

    def describe_vswitches_with_options(
        self,
        request: servicemesh_20200111_models.DescribeVSwitchesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeVSwitchesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeVSwitchesResponse(),
            self.do_rpcrequest('DescribeVSwitches', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vswitches_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeVSwitchesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeVSwitchesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeVSwitchesResponse(),
            await self.do_rpcrequest_async('DescribeVSwitches', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vswitches(
        self,
        request: servicemesh_20200111_models.DescribeVSwitchesRequest,
    ) -> servicemesh_20200111_models.DescribeVSwitchesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vswitches_with_options(request, runtime)

    async def describe_vswitches_async(
        self,
        request: servicemesh_20200111_models.DescribeVSwitchesRequest,
    ) -> servicemesh_20200111_models.DescribeVSwitchesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vswitches_with_options_async(request, runtime)

    def describe_vpcs_with_options(
        self,
        request: servicemesh_20200111_models.DescribeVpcsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeVpcsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeVpcsResponse(),
            self.do_rpcrequest('DescribeVpcs', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vpcs_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeVpcsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeVpcsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeVpcsResponse(),
            await self.do_rpcrequest_async('DescribeVpcs', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vpcs(
        self,
        request: servicemesh_20200111_models.DescribeVpcsRequest,
    ) -> servicemesh_20200111_models.DescribeVpcsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vpcs_with_options(request, runtime)

    async def describe_vpcs_async(
        self,
        request: servicemesh_20200111_models.DescribeVpcsRequest,
    ) -> servicemesh_20200111_models.DescribeVpcsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpcs_with_options_async(request, runtime)

    def remove_vm_app_from_mesh_with_options(
        self,
        request: servicemesh_20200111_models.RemoveVmAppFromMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.RemoveVmAppFromMeshResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.RemoveVmAppFromMeshResponse(),
            self.do_rpcrequest('RemoveVmAppFromMesh', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_vm_app_from_mesh_with_options_async(
        self,
        request: servicemesh_20200111_models.RemoveVmAppFromMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.RemoveVmAppFromMeshResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.RemoveVmAppFromMeshResponse(),
            await self.do_rpcrequest_async('RemoveVmAppFromMesh', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_vm_app_from_mesh(
        self,
        request: servicemesh_20200111_models.RemoveVmAppFromMeshRequest,
    ) -> servicemesh_20200111_models.RemoveVmAppFromMeshResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_vm_app_from_mesh_with_options(request, runtime)

    async def remove_vm_app_from_mesh_async(
        self,
        request: servicemesh_20200111_models.RemoveVmAppFromMeshRequest,
    ) -> servicemesh_20200111_models.RemoveVmAppFromMeshResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_vm_app_from_mesh_with_options_async(request, runtime)

    def describe_cluster_prometheus_with_options(
        self,
        request: servicemesh_20200111_models.DescribeClusterPrometheusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeClusterPrometheusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeClusterPrometheusResponse(),
            self.do_rpcrequest('DescribeClusterPrometheus', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cluster_prometheus_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeClusterPrometheusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeClusterPrometheusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeClusterPrometheusResponse(),
            await self.do_rpcrequest_async('DescribeClusterPrometheus', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cluster_prometheus(
        self,
        request: servicemesh_20200111_models.DescribeClusterPrometheusRequest,
    ) -> servicemesh_20200111_models.DescribeClusterPrometheusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_prometheus_with_options(request, runtime)

    async def describe_cluster_prometheus_async(
        self,
        request: servicemesh_20200111_models.DescribeClusterPrometheusRequest,
    ) -> servicemesh_20200111_models.DescribeClusterPrometheusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_prometheus_with_options_async(request, runtime)

    def update_istio_injection_config_with_options(
        self,
        request: servicemesh_20200111_models.UpdateIstioInjectionConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateIstioInjectionConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateIstioInjectionConfigResponse(),
            self.do_rpcrequest('UpdateIstioInjectionConfig', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_istio_injection_config_with_options_async(
        self,
        request: servicemesh_20200111_models.UpdateIstioInjectionConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateIstioInjectionConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateIstioInjectionConfigResponse(),
            await self.do_rpcrequest_async('UpdateIstioInjectionConfig', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_istio_injection_config(
        self,
        request: servicemesh_20200111_models.UpdateIstioInjectionConfigRequest,
    ) -> servicemesh_20200111_models.UpdateIstioInjectionConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_istio_injection_config_with_options(request, runtime)

    async def update_istio_injection_config_async(
        self,
        request: servicemesh_20200111_models.UpdateIstioInjectionConfigRequest,
    ) -> servicemesh_20200111_models.UpdateIstioInjectionConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_istio_injection_config_with_options_async(request, runtime)

    def get_vm_meta_with_options(
        self,
        request: servicemesh_20200111_models.GetVmMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetVmMetaResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetVmMetaResponse(),
            self.do_rpcrequest('GetVmMeta', '2020-01-11', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_vm_meta_with_options_async(
        self,
        request: servicemesh_20200111_models.GetVmMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetVmMetaResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetVmMetaResponse(),
            await self.do_rpcrequest_async('GetVmMeta', '2020-01-11', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_vm_meta(
        self,
        request: servicemesh_20200111_models.GetVmMetaRequest,
    ) -> servicemesh_20200111_models.GetVmMetaResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_vm_meta_with_options(request, runtime)

    async def get_vm_meta_async(
        self,
        request: servicemesh_20200111_models.GetVmMetaRequest,
    ) -> servicemesh_20200111_models.GetVmMetaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_vm_meta_with_options_async(request, runtime)

    def describe_upgrade_version_with_options(
        self,
        request: servicemesh_20200111_models.DescribeUpgradeVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeUpgradeVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeUpgradeVersionResponse(),
            self.do_rpcrequest('DescribeUpgradeVersion', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_upgrade_version_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeUpgradeVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeUpgradeVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeUpgradeVersionResponse(),
            await self.do_rpcrequest_async('DescribeUpgradeVersion', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_upgrade_version(
        self,
        request: servicemesh_20200111_models.DescribeUpgradeVersionRequest,
    ) -> servicemesh_20200111_models.DescribeUpgradeVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_upgrade_version_with_options(request, runtime)

    async def describe_upgrade_version_async(
        self,
        request: servicemesh_20200111_models.DescribeUpgradeVersionRequest,
    ) -> servicemesh_20200111_models.DescribeUpgradeVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_upgrade_version_with_options_async(request, runtime)

    def describe_clusters_in_service_mesh_with_options(
        self,
        request: servicemesh_20200111_models.DescribeClustersInServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeClustersInServiceMeshResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeClustersInServiceMeshResponse(),
            self.do_rpcrequest('DescribeClustersInServiceMesh', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_clusters_in_service_mesh_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeClustersInServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeClustersInServiceMeshResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeClustersInServiceMeshResponse(),
            await self.do_rpcrequest_async('DescribeClustersInServiceMesh', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_clusters_in_service_mesh(
        self,
        request: servicemesh_20200111_models.DescribeClustersInServiceMeshRequest,
    ) -> servicemesh_20200111_models.DescribeClustersInServiceMeshResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_clusters_in_service_mesh_with_options(request, runtime)

    async def describe_clusters_in_service_mesh_async(
        self,
        request: servicemesh_20200111_models.DescribeClustersInServiceMeshRequest,
    ) -> servicemesh_20200111_models.DescribeClustersInServiceMeshResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_clusters_in_service_mesh_with_options_async(request, runtime)

    def get_builtin_envoy_filter_catalog_with_options(
        self,
        request: servicemesh_20200111_models.GetBuiltinEnvoyFilterCatalogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetBuiltinEnvoyFilterCatalogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetBuiltinEnvoyFilterCatalogResponse(),
            self.do_rpcrequest('GetBuiltinEnvoyFilterCatalog', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_builtin_envoy_filter_catalog_with_options_async(
        self,
        request: servicemesh_20200111_models.GetBuiltinEnvoyFilterCatalogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetBuiltinEnvoyFilterCatalogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetBuiltinEnvoyFilterCatalogResponse(),
            await self.do_rpcrequest_async('GetBuiltinEnvoyFilterCatalog', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_builtin_envoy_filter_catalog(
        self,
        request: servicemesh_20200111_models.GetBuiltinEnvoyFilterCatalogRequest,
    ) -> servicemesh_20200111_models.GetBuiltinEnvoyFilterCatalogResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_builtin_envoy_filter_catalog_with_options(request, runtime)

    async def get_builtin_envoy_filter_catalog_async(
        self,
        request: servicemesh_20200111_models.GetBuiltinEnvoyFilterCatalogRequest,
    ) -> servicemesh_20200111_models.GetBuiltinEnvoyFilterCatalogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_builtin_envoy_filter_catalog_with_options_async(request, runtime)

    def describe_cluster_grafana_with_options(
        self,
        request: servicemesh_20200111_models.DescribeClusterGrafanaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeClusterGrafanaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeClusterGrafanaResponse(),
            self.do_rpcrequest('DescribeClusterGrafana', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cluster_grafana_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeClusterGrafanaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeClusterGrafanaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeClusterGrafanaResponse(),
            await self.do_rpcrequest_async('DescribeClusterGrafana', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cluster_grafana(
        self,
        request: servicemesh_20200111_models.DescribeClusterGrafanaRequest,
    ) -> servicemesh_20200111_models.DescribeClusterGrafanaResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_grafana_with_options(request, runtime)

    async def describe_cluster_grafana_async(
        self,
        request: servicemesh_20200111_models.DescribeClusterGrafanaRequest,
    ) -> servicemesh_20200111_models.DescribeClusterGrafanaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_grafana_with_options_async(request, runtime)

    def get_diagnosis_with_options(
        self,
        request: servicemesh_20200111_models.GetDiagnosisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetDiagnosisResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetDiagnosisResponse(),
            self.do_rpcrequest('GetDiagnosis', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_diagnosis_with_options_async(
        self,
        request: servicemesh_20200111_models.GetDiagnosisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetDiagnosisResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetDiagnosisResponse(),
            await self.do_rpcrequest_async('GetDiagnosis', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_diagnosis(
        self,
        request: servicemesh_20200111_models.GetDiagnosisRequest,
    ) -> servicemesh_20200111_models.GetDiagnosisResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_diagnosis_with_options(request, runtime)

    async def get_diagnosis_async(
        self,
        request: servicemesh_20200111_models.GetDiagnosisRequest,
    ) -> servicemesh_20200111_models.GetDiagnosisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_diagnosis_with_options_async(request, runtime)

    def get_registered_services_with_options(
        self,
        request: servicemesh_20200111_models.GetRegisteredServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetRegisteredServicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetRegisteredServicesResponse(),
            self.do_rpcrequest('GetRegisteredServices', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_registered_services_with_options_async(
        self,
        request: servicemesh_20200111_models.GetRegisteredServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetRegisteredServicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetRegisteredServicesResponse(),
            await self.do_rpcrequest_async('GetRegisteredServices', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_registered_services(
        self,
        request: servicemesh_20200111_models.GetRegisteredServicesRequest,
    ) -> servicemesh_20200111_models.GetRegisteredServicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_registered_services_with_options(request, runtime)

    async def get_registered_services_async(
        self,
        request: servicemesh_20200111_models.GetRegisteredServicesRequest,
    ) -> servicemesh_20200111_models.GetRegisteredServicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_registered_services_with_options_async(request, runtime)

    def describe_cens_with_options(
        self,
        request: servicemesh_20200111_models.DescribeCensRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeCensResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeCensResponse(),
            self.do_rpcrequest('DescribeCens', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cens_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeCensRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeCensResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeCensResponse(),
            await self.do_rpcrequest_async('DescribeCens', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cens(
        self,
        request: servicemesh_20200111_models.DescribeCensRequest,
    ) -> servicemesh_20200111_models.DescribeCensResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cens_with_options(request, runtime)

    async def describe_cens_async(
        self,
        request: servicemesh_20200111_models.DescribeCensRequest,
    ) -> servicemesh_20200111_models.DescribeCensResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cens_with_options_async(request, runtime)

    def delete_service_mesh_with_options(
        self,
        request: servicemesh_20200111_models.DeleteServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DeleteServiceMeshResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DeleteServiceMeshResponse(),
            self.do_rpcrequest('DeleteServiceMesh', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_service_mesh_with_options_async(
        self,
        request: servicemesh_20200111_models.DeleteServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DeleteServiceMeshResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DeleteServiceMeshResponse(),
            await self.do_rpcrequest_async('DeleteServiceMesh', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_service_mesh(
        self,
        request: servicemesh_20200111_models.DeleteServiceMeshRequest,
    ) -> servicemesh_20200111_models.DeleteServiceMeshResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_service_mesh_with_options(request, runtime)

    async def delete_service_mesh_async(
        self,
        request: servicemesh_20200111_models.DeleteServiceMeshRequest,
    ) -> servicemesh_20200111_models.DeleteServiceMeshResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_service_mesh_with_options_async(request, runtime)

    def get_sa_token_with_options(
        self,
        request: servicemesh_20200111_models.GetSaTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetSaTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetSaTokenResponse(),
            self.do_rpcrequest('GetSaToken', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_sa_token_with_options_async(
        self,
        request: servicemesh_20200111_models.GetSaTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetSaTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetSaTokenResponse(),
            await self.do_rpcrequest_async('GetSaToken', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_sa_token(
        self,
        request: servicemesh_20200111_models.GetSaTokenRequest,
    ) -> servicemesh_20200111_models.GetSaTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_sa_token_with_options(request, runtime)

    async def get_sa_token_async(
        self,
        request: servicemesh_20200111_models.GetSaTokenRequest,
    ) -> servicemesh_20200111_models.GetSaTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_sa_token_with_options_async(request, runtime)

    def get_vm_app_mesh_info_with_options(
        self,
        request: servicemesh_20200111_models.GetVmAppMeshInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetVmAppMeshInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetVmAppMeshInfoResponse(),
            self.do_rpcrequest('GetVmAppMeshInfo', '2020-01-11', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_vm_app_mesh_info_with_options_async(
        self,
        request: servicemesh_20200111_models.GetVmAppMeshInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetVmAppMeshInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetVmAppMeshInfoResponse(),
            await self.do_rpcrequest_async('GetVmAppMeshInfo', '2020-01-11', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_vm_app_mesh_info(
        self,
        request: servicemesh_20200111_models.GetVmAppMeshInfoRequest,
    ) -> servicemesh_20200111_models.GetVmAppMeshInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_vm_app_mesh_info_with_options(request, runtime)

    async def get_vm_app_mesh_info_async(
        self,
        request: servicemesh_20200111_models.GetVmAppMeshInfoRequest,
    ) -> servicemesh_20200111_models.GetVmAppMeshInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_vm_app_mesh_info_with_options_async(request, runtime)

    def remove_cluster_from_service_mesh_with_options(
        self,
        request: servicemesh_20200111_models.RemoveClusterFromServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.RemoveClusterFromServiceMeshResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.RemoveClusterFromServiceMeshResponse(),
            self.do_rpcrequest('RemoveClusterFromServiceMesh', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_cluster_from_service_mesh_with_options_async(
        self,
        request: servicemesh_20200111_models.RemoveClusterFromServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.RemoveClusterFromServiceMeshResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.RemoveClusterFromServiceMeshResponse(),
            await self.do_rpcrequest_async('RemoveClusterFromServiceMesh', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_cluster_from_service_mesh(
        self,
        request: servicemesh_20200111_models.RemoveClusterFromServiceMeshRequest,
    ) -> servicemesh_20200111_models.RemoveClusterFromServiceMeshResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_cluster_from_service_mesh_with_options(request, runtime)

    async def remove_cluster_from_service_mesh_async(
        self,
        request: servicemesh_20200111_models.RemoveClusterFromServiceMeshRequest,
    ) -> servicemesh_20200111_models.RemoveClusterFromServiceMeshResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_cluster_from_service_mesh_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: servicemesh_20200111_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeRegionsResponse(),
            self.do_rpcrequest('DescribeRegions', '2020-01-11', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeRegionsResponse(),
            await self.do_rpcrequest_async('DescribeRegions', '2020-01-11', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_regions(
        self,
        request: servicemesh_20200111_models.DescribeRegionsRequest,
    ) -> servicemesh_20200111_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: servicemesh_20200111_models.DescribeRegionsRequest,
    ) -> servicemesh_20200111_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def set_service_registry_source_with_options(
        self,
        tmp_req: servicemesh_20200111_models.SetServiceRegistrySourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.SetServiceRegistrySourceResponse:
        UtilClient.validate_model(tmp_req)
        request = servicemesh_20200111_models.SetServiceRegistrySourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config):
            request.config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config, 'Config', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.SetServiceRegistrySourceResponse(),
            self.do_rpcrequest('SetServiceRegistrySource', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_service_registry_source_with_options_async(
        self,
        tmp_req: servicemesh_20200111_models.SetServiceRegistrySourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.SetServiceRegistrySourceResponse:
        UtilClient.validate_model(tmp_req)
        request = servicemesh_20200111_models.SetServiceRegistrySourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config):
            request.config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config, 'Config', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.SetServiceRegistrySourceResponse(),
            await self.do_rpcrequest_async('SetServiceRegistrySource', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_service_registry_source(
        self,
        request: servicemesh_20200111_models.SetServiceRegistrySourceRequest,
    ) -> servicemesh_20200111_models.SetServiceRegistrySourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_service_registry_source_with_options(request, runtime)

    async def set_service_registry_source_async(
        self,
        request: servicemesh_20200111_models.SetServiceRegistrySourceRequest,
    ) -> servicemesh_20200111_models.SetServiceRegistrySourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_service_registry_source_with_options_async(request, runtime)

    def add_cluster_into_service_mesh_with_options(
        self,
        request: servicemesh_20200111_models.AddClusterIntoServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.AddClusterIntoServiceMeshResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.AddClusterIntoServiceMeshResponse(),
            self.do_rpcrequest('AddClusterIntoServiceMesh', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_cluster_into_service_mesh_with_options_async(
        self,
        request: servicemesh_20200111_models.AddClusterIntoServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.AddClusterIntoServiceMeshResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.AddClusterIntoServiceMeshResponse(),
            await self.do_rpcrequest_async('AddClusterIntoServiceMesh', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_cluster_into_service_mesh(
        self,
        request: servicemesh_20200111_models.AddClusterIntoServiceMeshRequest,
    ) -> servicemesh_20200111_models.AddClusterIntoServiceMeshResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_cluster_into_service_mesh_with_options(request, runtime)

    async def add_cluster_into_service_mesh_async(
        self,
        request: servicemesh_20200111_models.AddClusterIntoServiceMeshRequest,
    ) -> servicemesh_20200111_models.AddClusterIntoServiceMeshResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_cluster_into_service_mesh_with_options_async(request, runtime)

    def add_builtin_envoy_filter_with_options(
        self,
        request: servicemesh_20200111_models.AddBuiltinEnvoyFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.AddBuiltinEnvoyFilterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.AddBuiltinEnvoyFilterResponse(),
            self.do_rpcrequest('AddBuiltinEnvoyFilter', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_builtin_envoy_filter_with_options_async(
        self,
        request: servicemesh_20200111_models.AddBuiltinEnvoyFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.AddBuiltinEnvoyFilterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.AddBuiltinEnvoyFilterResponse(),
            await self.do_rpcrequest_async('AddBuiltinEnvoyFilter', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_builtin_envoy_filter(
        self,
        request: servicemesh_20200111_models.AddBuiltinEnvoyFilterRequest,
    ) -> servicemesh_20200111_models.AddBuiltinEnvoyFilterResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_builtin_envoy_filter_with_options(request, runtime)

    async def add_builtin_envoy_filter_async(
        self,
        request: servicemesh_20200111_models.AddBuiltinEnvoyFilterRequest,
    ) -> servicemesh_20200111_models.AddBuiltinEnvoyFilterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_builtin_envoy_filter_with_options_async(request, runtime)

    def get_ecs_list_with_options(
        self,
        request: servicemesh_20200111_models.GetEcsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetEcsListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetEcsListResponse(),
            self.do_rpcrequest('GetEcsList', '2020-01-11', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_ecs_list_with_options_async(
        self,
        request: servicemesh_20200111_models.GetEcsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetEcsListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetEcsListResponse(),
            await self.do_rpcrequest_async('GetEcsList', '2020-01-11', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_ecs_list(
        self,
        request: servicemesh_20200111_models.GetEcsListRequest,
    ) -> servicemesh_20200111_models.GetEcsListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ecs_list_with_options(request, runtime)

    async def get_ecs_list_async(
        self,
        request: servicemesh_20200111_models.GetEcsListRequest,
    ) -> servicemesh_20200111_models.GetEcsListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ecs_list_with_options_async(request, runtime)

    def update_mesh_feature_with_options(
        self,
        request: servicemesh_20200111_models.UpdateMeshFeatureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateMeshFeatureResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateMeshFeatureResponse(),
            self.do_rpcrequest('UpdateMeshFeature', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_mesh_feature_with_options_async(
        self,
        request: servicemesh_20200111_models.UpdateMeshFeatureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateMeshFeatureResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateMeshFeatureResponse(),
            await self.do_rpcrequest_async('UpdateMeshFeature', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_mesh_feature(
        self,
        request: servicemesh_20200111_models.UpdateMeshFeatureRequest,
    ) -> servicemesh_20200111_models.UpdateMeshFeatureResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_mesh_feature_with_options(request, runtime)

    async def update_mesh_feature_async(
        self,
        request: servicemesh_20200111_models.UpdateMeshFeatureRequest,
    ) -> servicemesh_20200111_models.UpdateMeshFeatureResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_mesh_feature_with_options_async(request, runtime)

    def add_vm_app_to_mesh_with_options(
        self,
        request: servicemesh_20200111_models.AddVmAppToMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.AddVmAppToMeshResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.AddVmAppToMeshResponse(),
            self.do_rpcrequest('AddVmAppToMesh', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_vm_app_to_mesh_with_options_async(
        self,
        request: servicemesh_20200111_models.AddVmAppToMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.AddVmAppToMeshResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.AddVmAppToMeshResponse(),
            await self.do_rpcrequest_async('AddVmAppToMesh', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_vm_app_to_mesh(
        self,
        request: servicemesh_20200111_models.AddVmAppToMeshRequest,
    ) -> servicemesh_20200111_models.AddVmAppToMeshResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_vm_app_to_mesh_with_options(request, runtime)

    async def add_vm_app_to_mesh_async(
        self,
        request: servicemesh_20200111_models.AddVmAppToMeshRequest,
    ) -> servicemesh_20200111_models.AddVmAppToMeshResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_vm_app_to_mesh_with_options_async(request, runtime)

    def create_service_mesh_with_options(
        self,
        request: servicemesh_20200111_models.CreateServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.CreateServiceMeshResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.CreateServiceMeshResponse(),
            self.do_rpcrequest('CreateServiceMesh', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_service_mesh_with_options_async(
        self,
        request: servicemesh_20200111_models.CreateServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.CreateServiceMeshResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.CreateServiceMeshResponse(),
            await self.do_rpcrequest_async('CreateServiceMesh', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_service_mesh(
        self,
        request: servicemesh_20200111_models.CreateServiceMeshRequest,
    ) -> servicemesh_20200111_models.CreateServiceMeshResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_service_mesh_with_options(request, runtime)

    async def create_service_mesh_async(
        self,
        request: servicemesh_20200111_models.CreateServiceMeshRequest,
    ) -> servicemesh_20200111_models.CreateServiceMeshResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_service_mesh_with_options_async(request, runtime)

    def get_service_registry_source_with_options(
        self,
        request: servicemesh_20200111_models.GetServiceRegistrySourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetServiceRegistrySourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetServiceRegistrySourceResponse(),
            self.do_rpcrequest('GetServiceRegistrySource', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_service_registry_source_with_options_async(
        self,
        request: servicemesh_20200111_models.GetServiceRegistrySourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetServiceRegistrySourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetServiceRegistrySourceResponse(),
            await self.do_rpcrequest_async('GetServiceRegistrySource', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_service_registry_source(
        self,
        request: servicemesh_20200111_models.GetServiceRegistrySourceRequest,
    ) -> servicemesh_20200111_models.GetServiceRegistrySourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_service_registry_source_with_options(request, runtime)

    async def get_service_registry_source_async(
        self,
        request: servicemesh_20200111_models.GetServiceRegistrySourceRequest,
    ) -> servicemesh_20200111_models.GetServiceRegistrySourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_service_registry_source_with_options_async(request, runtime)

    def remove_builtin_envoy_filter_with_options(
        self,
        request: servicemesh_20200111_models.RemoveBuiltinEnvoyFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.RemoveBuiltinEnvoyFilterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.RemoveBuiltinEnvoyFilterResponse(),
            self.do_rpcrequest('RemoveBuiltinEnvoyFilter', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_builtin_envoy_filter_with_options_async(
        self,
        request: servicemesh_20200111_models.RemoveBuiltinEnvoyFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.RemoveBuiltinEnvoyFilterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.RemoveBuiltinEnvoyFilterResponse(),
            await self.do_rpcrequest_async('RemoveBuiltinEnvoyFilter', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_builtin_envoy_filter(
        self,
        request: servicemesh_20200111_models.RemoveBuiltinEnvoyFilterRequest,
    ) -> servicemesh_20200111_models.RemoveBuiltinEnvoyFilterResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_builtin_envoy_filter_with_options(request, runtime)

    async def remove_builtin_envoy_filter_async(
        self,
        request: servicemesh_20200111_models.RemoveBuiltinEnvoyFilterRequest,
    ) -> servicemesh_20200111_models.RemoveBuiltinEnvoyFilterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_builtin_envoy_filter_with_options_async(request, runtime)

    def get_builtin_envoy_filter_with_options(
        self,
        request: servicemesh_20200111_models.GetBuiltinEnvoyFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetBuiltinEnvoyFilterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetBuiltinEnvoyFilterResponse(),
            self.do_rpcrequest('GetBuiltinEnvoyFilter', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_builtin_envoy_filter_with_options_async(
        self,
        request: servicemesh_20200111_models.GetBuiltinEnvoyFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetBuiltinEnvoyFilterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetBuiltinEnvoyFilterResponse(),
            await self.do_rpcrequest_async('GetBuiltinEnvoyFilter', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_builtin_envoy_filter(
        self,
        request: servicemesh_20200111_models.GetBuiltinEnvoyFilterRequest,
    ) -> servicemesh_20200111_models.GetBuiltinEnvoyFilterResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_builtin_envoy_filter_with_options(request, runtime)

    async def get_builtin_envoy_filter_async(
        self,
        request: servicemesh_20200111_models.GetBuiltinEnvoyFilterRequest,
    ) -> servicemesh_20200111_models.GetBuiltinEnvoyFilterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_builtin_envoy_filter_with_options_async(request, runtime)

    def initialize_asmrole_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.InitializeASMRoleResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            servicemesh_20200111_models.InitializeASMRoleResponse(),
            self.do_rpcrequest('InitializeASMRole', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def initialize_asmrole_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.InitializeASMRoleResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            servicemesh_20200111_models.InitializeASMRoleResponse(),
            await self.do_rpcrequest_async('InitializeASMRole', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def initialize_asmrole(self) -> servicemesh_20200111_models.InitializeASMRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.initialize_asmrole_with_options(runtime)

    async def initialize_asmrole_async(self) -> servicemesh_20200111_models.InitializeASMRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.initialize_asmrole_with_options_async(runtime)

    def add_mesh_tag_to_ecs_with_options(
        self,
        request: servicemesh_20200111_models.AddMeshTagToEcsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.AddMeshTagToEcsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.AddMeshTagToEcsResponse(),
            self.do_rpcrequest('AddMeshTagToEcs', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_mesh_tag_to_ecs_with_options_async(
        self,
        request: servicemesh_20200111_models.AddMeshTagToEcsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.AddMeshTagToEcsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.AddMeshTagToEcsResponse(),
            await self.do_rpcrequest_async('AddMeshTagToEcs', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_mesh_tag_to_ecs(
        self,
        request: servicemesh_20200111_models.AddMeshTagToEcsRequest,
    ) -> servicemesh_20200111_models.AddMeshTagToEcsResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_mesh_tag_to_ecs_with_options(request, runtime)

    async def add_mesh_tag_to_ecs_async(
        self,
        request: servicemesh_20200111_models.AddMeshTagToEcsRequest,
    ) -> servicemesh_20200111_models.AddMeshTagToEcsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_mesh_tag_to_ecs_with_options_async(request, runtime)
