# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore
from typing import Dict

from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_tea_rpc import models as rpc_models
from alibabacloud_pcdn20170411 import models as pcdn_20170411_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(
        self, 
        config: rpc_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('pcdn', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def stop_domain_with_options(
        self,
        request: pcdn_20170411_models.StopDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.StopDomainResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.StopDomainResponse().from_map(
            self.do_request('StopDomain', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    async def stop_domain_with_options_async(
        self,
        request: pcdn_20170411_models.StopDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.StopDomainResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.StopDomainResponse().from_map(
            await self.do_request_async('StopDomain', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    def stop_domain(
        self,
        request: pcdn_20170411_models.StopDomainRequest,
    ) -> pcdn_20170411_models.StopDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_domain_with_options(request, runtime)

    async def stop_domain_async(
        self,
        request: pcdn_20170411_models.StopDomainRequest,
    ) -> pcdn_20170411_models.StopDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_domain_with_options_async(request, runtime)

    def start_domain_with_options(
        self,
        request: pcdn_20170411_models.StartDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.StartDomainResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.StartDomainResponse().from_map(
            self.do_request('StartDomain', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    async def start_domain_with_options_async(
        self,
        request: pcdn_20170411_models.StartDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.StartDomainResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.StartDomainResponse().from_map(
            await self.do_request_async('StartDomain', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    def start_domain(
        self,
        request: pcdn_20170411_models.StartDomainRequest,
    ) -> pcdn_20170411_models.StartDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_domain_with_options(request, runtime)

    async def start_domain_async(
        self,
        request: pcdn_20170411_models.StartDomainRequest,
    ) -> pcdn_20170411_models.StartDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_domain_with_options_async(request, runtime)

    def delete_domain_with_options(
        self,
        request: pcdn_20170411_models.DeleteDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.DeleteDomainResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.DeleteDomainResponse().from_map(
            self.do_request('DeleteDomain', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    async def delete_domain_with_options_async(
        self,
        request: pcdn_20170411_models.DeleteDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.DeleteDomainResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.DeleteDomainResponse().from_map(
            await self.do_request_async('DeleteDomain', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    def delete_domain(
        self,
        request: pcdn_20170411_models.DeleteDomainRequest,
    ) -> pcdn_20170411_models.DeleteDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_with_options(request, runtime)

    async def delete_domain_async(
        self,
        request: pcdn_20170411_models.DeleteDomainRequest,
    ) -> pcdn_20170411_models.DeleteDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_domain_with_options_async(request, runtime)

    def add_domain_with_options(
        self,
        request: pcdn_20170411_models.AddDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.AddDomainResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.AddDomainResponse().from_map(
            self.do_request('AddDomain', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    async def add_domain_with_options_async(
        self,
        request: pcdn_20170411_models.AddDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.AddDomainResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.AddDomainResponse().from_map(
            await self.do_request_async('AddDomain', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    def add_domain(
        self,
        request: pcdn_20170411_models.AddDomainRequest,
    ) -> pcdn_20170411_models.AddDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_domain_with_options(request, runtime)

    async def add_domain_async(
        self,
        request: pcdn_20170411_models.AddDomainRequest,
    ) -> pcdn_20170411_models.AddDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_domain_with_options_async(request, runtime)

    def get_balance_traffic_data_with_options(
        self,
        request: pcdn_20170411_models.GetBalanceTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetBalanceTrafficDataResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetBalanceTrafficDataResponse().from_map(
            self.do_request('GetBalanceTrafficData', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    async def get_balance_traffic_data_with_options_async(
        self,
        request: pcdn_20170411_models.GetBalanceTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetBalanceTrafficDataResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetBalanceTrafficDataResponse().from_map(
            await self.do_request_async('GetBalanceTrafficData', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    def get_balance_traffic_data(
        self,
        request: pcdn_20170411_models.GetBalanceTrafficDataRequest,
    ) -> pcdn_20170411_models.GetBalanceTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_balance_traffic_data_with_options(request, runtime)

    async def get_balance_traffic_data_async(
        self,
        request: pcdn_20170411_models.GetBalanceTrafficDataRequest,
    ) -> pcdn_20170411_models.GetBalanceTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_balance_traffic_data_with_options_async(request, runtime)

    def add_pcdn_control_rule_with_options(
        self,
        request: pcdn_20170411_models.AddPcdnControlRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.AddPcdnControlRuleResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.AddPcdnControlRuleResponse().from_map(
            self.do_request('AddPcdnControlRule', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    async def add_pcdn_control_rule_with_options_async(
        self,
        request: pcdn_20170411_models.AddPcdnControlRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.AddPcdnControlRuleResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.AddPcdnControlRuleResponse().from_map(
            await self.do_request_async('AddPcdnControlRule', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    def add_pcdn_control_rule(
        self,
        request: pcdn_20170411_models.AddPcdnControlRuleRequest,
    ) -> pcdn_20170411_models.AddPcdnControlRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_pcdn_control_rule_with_options(request, runtime)

    async def add_pcdn_control_rule_async(
        self,
        request: pcdn_20170411_models.AddPcdnControlRuleRequest,
    ) -> pcdn_20170411_models.AddPcdnControlRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_pcdn_control_rule_with_options_async(request, runtime)

    def add_consumer_with_options(
        self,
        request: pcdn_20170411_models.AddConsumerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.AddConsumerResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.AddConsumerResponse().from_map(
            self.do_request('AddConsumer', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    async def add_consumer_with_options_async(
        self,
        request: pcdn_20170411_models.AddConsumerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.AddConsumerResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.AddConsumerResponse().from_map(
            await self.do_request_async('AddConsumer', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    def add_consumer(
        self,
        request: pcdn_20170411_models.AddConsumerRequest,
    ) -> pcdn_20170411_models.AddConsumerResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_consumer_with_options(request, runtime)

    async def add_consumer_async(
        self,
        request: pcdn_20170411_models.AddConsumerRequest,
    ) -> pcdn_20170411_models.AddConsumerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_consumer_with_options_async(request, runtime)

    def get_access_data_with_options(
        self,
        request: pcdn_20170411_models.GetAccessDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetAccessDataResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetAccessDataResponse().from_map(
            self.do_request('GetAccessData', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    async def get_access_data_with_options_async(
        self,
        request: pcdn_20170411_models.GetAccessDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetAccessDataResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetAccessDataResponse().from_map(
            await self.do_request_async('GetAccessData', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    def get_access_data(
        self,
        request: pcdn_20170411_models.GetAccessDataRequest,
    ) -> pcdn_20170411_models.GetAccessDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_access_data_with_options(request, runtime)

    async def get_access_data_async(
        self,
        request: pcdn_20170411_models.GetAccessDataRequest,
    ) -> pcdn_20170411_models.GetAccessDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_access_data_with_options_async(request, runtime)

    def enable_pcdn_control_rule_with_options(
        self,
        request: pcdn_20170411_models.EnablePcdnControlRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.EnablePcdnControlRuleResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.EnablePcdnControlRuleResponse().from_map(
            self.do_request('EnablePcdnControlRule', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    async def enable_pcdn_control_rule_with_options_async(
        self,
        request: pcdn_20170411_models.EnablePcdnControlRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.EnablePcdnControlRuleResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.EnablePcdnControlRuleResponse().from_map(
            await self.do_request_async('EnablePcdnControlRule', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    def enable_pcdn_control_rule(
        self,
        request: pcdn_20170411_models.EnablePcdnControlRuleRequest,
    ) -> pcdn_20170411_models.EnablePcdnControlRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_pcdn_control_rule_with_options(request, runtime)

    async def enable_pcdn_control_rule_async(
        self,
        request: pcdn_20170411_models.EnablePcdnControlRuleRequest,
    ) -> pcdn_20170411_models.EnablePcdnControlRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_pcdn_control_rule_with_options_async(request, runtime)

    def edit_pcdn_control_rule_with_options(
        self,
        request: pcdn_20170411_models.EditPcdnControlRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.EditPcdnControlRuleResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.EditPcdnControlRuleResponse().from_map(
            self.do_request('EditPcdnControlRule', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    async def edit_pcdn_control_rule_with_options_async(
        self,
        request: pcdn_20170411_models.EditPcdnControlRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.EditPcdnControlRuleResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.EditPcdnControlRuleResponse().from_map(
            await self.do_request_async('EditPcdnControlRule', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    def edit_pcdn_control_rule(
        self,
        request: pcdn_20170411_models.EditPcdnControlRuleRequest,
    ) -> pcdn_20170411_models.EditPcdnControlRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.edit_pcdn_control_rule_with_options(request, runtime)

    async def edit_pcdn_control_rule_async(
        self,
        request: pcdn_20170411_models.EditPcdnControlRuleRequest,
    ) -> pcdn_20170411_models.EditPcdnControlRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.edit_pcdn_control_rule_with_options_async(request, runtime)

    def disable_pcdn_control_rule_with_options(
        self,
        request: pcdn_20170411_models.DisablePcdnControlRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.DisablePcdnControlRuleResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.DisablePcdnControlRuleResponse().from_map(
            self.do_request('DisablePcdnControlRule', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    async def disable_pcdn_control_rule_with_options_async(
        self,
        request: pcdn_20170411_models.DisablePcdnControlRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.DisablePcdnControlRuleResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.DisablePcdnControlRuleResponse().from_map(
            await self.do_request_async('DisablePcdnControlRule', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    def disable_pcdn_control_rule(
        self,
        request: pcdn_20170411_models.DisablePcdnControlRuleRequest,
    ) -> pcdn_20170411_models.DisablePcdnControlRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_pcdn_control_rule_with_options(request, runtime)

    async def disable_pcdn_control_rule_async(
        self,
        request: pcdn_20170411_models.DisablePcdnControlRuleRequest,
    ) -> pcdn_20170411_models.DisablePcdnControlRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_pcdn_control_rule_with_options_async(request, runtime)

    def delete_pcdn_control_rule_with_options(
        self,
        request: pcdn_20170411_models.DeletePcdnControlRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.DeletePcdnControlRuleResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.DeletePcdnControlRuleResponse().from_map(
            self.do_request('DeletePcdnControlRule', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    async def delete_pcdn_control_rule_with_options_async(
        self,
        request: pcdn_20170411_models.DeletePcdnControlRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.DeletePcdnControlRuleResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.DeletePcdnControlRuleResponse().from_map(
            await self.do_request_async('DeletePcdnControlRule', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    def delete_pcdn_control_rule(
        self,
        request: pcdn_20170411_models.DeletePcdnControlRuleRequest,
    ) -> pcdn_20170411_models.DeletePcdnControlRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_pcdn_control_rule_with_options(request, runtime)

    async def delete_pcdn_control_rule_async(
        self,
        request: pcdn_20170411_models.DeletePcdnControlRuleRequest,
    ) -> pcdn_20170411_models.DeletePcdnControlRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_pcdn_control_rule_with_options_async(request, runtime)

    def get_all_platform_types_with_options(
        self,
        request: pcdn_20170411_models.GetAllPlatformTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetAllPlatformTypesResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetAllPlatformTypesResponse().from_map(
            self.do_request('GetAllPlatformTypes', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    async def get_all_platform_types_with_options_async(
        self,
        request: pcdn_20170411_models.GetAllPlatformTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetAllPlatformTypesResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetAllPlatformTypesResponse().from_map(
            await self.do_request_async('GetAllPlatformTypes', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    def get_all_platform_types(
        self,
        request: pcdn_20170411_models.GetAllPlatformTypesRequest,
    ) -> pcdn_20170411_models.GetAllPlatformTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_all_platform_types_with_options(request, runtime)

    async def get_all_platform_types_async(
        self,
        request: pcdn_20170411_models.GetAllPlatformTypesRequest,
    ) -> pcdn_20170411_models.GetAllPlatformTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_all_platform_types_with_options_async(request, runtime)

    def get_all_markets_with_options(
        self,
        request: pcdn_20170411_models.GetAllMarketsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetAllMarketsResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetAllMarketsResponse().from_map(
            self.do_request('GetAllMarkets', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    async def get_all_markets_with_options_async(
        self,
        request: pcdn_20170411_models.GetAllMarketsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetAllMarketsResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetAllMarketsResponse().from_map(
            await self.do_request_async('GetAllMarkets', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    def get_all_markets(
        self,
        request: pcdn_20170411_models.GetAllMarketsRequest,
    ) -> pcdn_20170411_models.GetAllMarketsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_all_markets_with_options(request, runtime)

    async def get_all_markets_async(
        self,
        request: pcdn_20170411_models.GetAllMarketsRequest,
    ) -> pcdn_20170411_models.GetAllMarketsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_all_markets_with_options_async(request, runtime)

    def get_all_isp_with_options(
        self,
        request: pcdn_20170411_models.GetAllIspRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetAllIspResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetAllIspResponse().from_map(
            self.do_request('GetAllIsp', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    async def get_all_isp_with_options_async(
        self,
        request: pcdn_20170411_models.GetAllIspRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetAllIspResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetAllIspResponse().from_map(
            await self.do_request_async('GetAllIsp', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    def get_all_isp(
        self,
        request: pcdn_20170411_models.GetAllIspRequest,
    ) -> pcdn_20170411_models.GetAllIspResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_all_isp_with_options(request, runtime)

    async def get_all_isp_async(
        self,
        request: pcdn_20170411_models.GetAllIspRequest,
    ) -> pcdn_20170411_models.GetAllIspResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_all_isp_with_options_async(request, runtime)

    def get_all_app_versions_with_options(
        self,
        request: pcdn_20170411_models.GetAllAppVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetAllAppVersionsResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetAllAppVersionsResponse().from_map(
            self.do_request('GetAllAppVersions', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    async def get_all_app_versions_with_options_async(
        self,
        request: pcdn_20170411_models.GetAllAppVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetAllAppVersionsResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetAllAppVersionsResponse().from_map(
            await self.do_request_async('GetAllAppVersions', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    def get_all_app_versions(
        self,
        request: pcdn_20170411_models.GetAllAppVersionsRequest,
    ) -> pcdn_20170411_models.GetAllAppVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_all_app_versions_with_options(request, runtime)

    async def get_all_app_versions_async(
        self,
        request: pcdn_20170411_models.GetAllAppVersionsRequest,
    ) -> pcdn_20170411_models.GetAllAppVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_all_app_versions_with_options_async(request, runtime)

    def get_consumer_status_with_options(
        self,
        request: pcdn_20170411_models.GetConsumerStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetConsumerStatusResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetConsumerStatusResponse().from_map(
            self.do_request('GetConsumerStatus', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    async def get_consumer_status_with_options_async(
        self,
        request: pcdn_20170411_models.GetConsumerStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetConsumerStatusResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetConsumerStatusResponse().from_map(
            await self.do_request_async('GetConsumerStatus', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    def get_consumer_status(
        self,
        request: pcdn_20170411_models.GetConsumerStatusRequest,
    ) -> pcdn_20170411_models.GetConsumerStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_consumer_status_with_options(request, runtime)

    async def get_consumer_status_async(
        self,
        request: pcdn_20170411_models.GetConsumerStatusRequest,
    ) -> pcdn_20170411_models.GetConsumerStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_consumer_status_with_options_async(request, runtime)

    def get_clients_ratio_with_options(
        self,
        request: pcdn_20170411_models.GetClientsRatioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetClientsRatioResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetClientsRatioResponse().from_map(
            self.do_request('GetClientsRatio', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    async def get_clients_ratio_with_options_async(
        self,
        request: pcdn_20170411_models.GetClientsRatioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetClientsRatioResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetClientsRatioResponse().from_map(
            await self.do_request_async('GetClientsRatio', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    def get_clients_ratio(
        self,
        request: pcdn_20170411_models.GetClientsRatioRequest,
    ) -> pcdn_20170411_models.GetClientsRatioResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_clients_ratio_with_options(request, runtime)

    async def get_clients_ratio_async(
        self,
        request: pcdn_20170411_models.GetClientsRatioRequest,
    ) -> pcdn_20170411_models.GetClientsRatioResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_clients_ratio_with_options_async(request, runtime)

    def get_bandwidth_data_with_options(
        self,
        request: pcdn_20170411_models.GetBandwidthDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetBandwidthDataResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetBandwidthDataResponse().from_map(
            self.do_request('GetBandwidthData', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    async def get_bandwidth_data_with_options_async(
        self,
        request: pcdn_20170411_models.GetBandwidthDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetBandwidthDataResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetBandwidthDataResponse().from_map(
            await self.do_request_async('GetBandwidthData', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    def get_bandwidth_data(
        self,
        request: pcdn_20170411_models.GetBandwidthDataRequest,
    ) -> pcdn_20170411_models.GetBandwidthDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_bandwidth_data_with_options(request, runtime)

    async def get_bandwidth_data_async(
        self,
        request: pcdn_20170411_models.GetBandwidthDataRequest,
    ) -> pcdn_20170411_models.GetBandwidthDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_bandwidth_data_with_options_async(request, runtime)

    def get_balance_bandwidth_data_with_options(
        self,
        request: pcdn_20170411_models.GetBalanceBandwidthDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetBalanceBandwidthDataResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetBalanceBandwidthDataResponse().from_map(
            self.do_request('GetBalanceBandwidthData', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    async def get_balance_bandwidth_data_with_options_async(
        self,
        request: pcdn_20170411_models.GetBalanceBandwidthDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetBalanceBandwidthDataResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetBalanceBandwidthDataResponse().from_map(
            await self.do_request_async('GetBalanceBandwidthData', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    def get_balance_bandwidth_data(
        self,
        request: pcdn_20170411_models.GetBalanceBandwidthDataRequest,
    ) -> pcdn_20170411_models.GetBalanceBandwidthDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_balance_bandwidth_data_with_options(request, runtime)

    async def get_balance_bandwidth_data_async(
        self,
        request: pcdn_20170411_models.GetBalanceBandwidthDataRequest,
    ) -> pcdn_20170411_models.GetBalanceBandwidthDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_balance_bandwidth_data_with_options_async(request, runtime)

    def get_control_rules_with_options(
        self,
        request: pcdn_20170411_models.GetControlRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetControlRulesResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetControlRulesResponse().from_map(
            self.do_request('GetControlRules', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    async def get_control_rules_with_options_async(
        self,
        request: pcdn_20170411_models.GetControlRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetControlRulesResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetControlRulesResponse().from_map(
            await self.do_request_async('GetControlRules', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    def get_control_rules(
        self,
        request: pcdn_20170411_models.GetControlRulesRequest,
    ) -> pcdn_20170411_models.GetControlRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_control_rules_with_options(request, runtime)

    async def get_control_rules_async(
        self,
        request: pcdn_20170411_models.GetControlRulesRequest,
    ) -> pcdn_20170411_models.GetControlRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_control_rules_with_options_async(request, runtime)

    def get_domain_count_with_options(
        self,
        request: pcdn_20170411_models.GetDomainCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetDomainCountResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetDomainCountResponse().from_map(
            self.do_request('GetDomainCount', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    async def get_domain_count_with_options_async(
        self,
        request: pcdn_20170411_models.GetDomainCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetDomainCountResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetDomainCountResponse().from_map(
            await self.do_request_async('GetDomainCount', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    def get_domain_count(
        self,
        request: pcdn_20170411_models.GetDomainCountRequest,
    ) -> pcdn_20170411_models.GetDomainCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_domain_count_with_options(request, runtime)

    async def get_domain_count_async(
        self,
        request: pcdn_20170411_models.GetDomainCountRequest,
    ) -> pcdn_20170411_models.GetDomainCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_domain_count_with_options_async(request, runtime)

    def get_current_mode_with_options(
        self,
        request: pcdn_20170411_models.GetCurrentModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetCurrentModeResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetCurrentModeResponse().from_map(
            self.do_request('GetCurrentMode', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    async def get_current_mode_with_options_async(
        self,
        request: pcdn_20170411_models.GetCurrentModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetCurrentModeResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetCurrentModeResponse().from_map(
            await self.do_request_async('GetCurrentMode', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    def get_current_mode(
        self,
        request: pcdn_20170411_models.GetCurrentModeRequest,
    ) -> pcdn_20170411_models.GetCurrentModeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_current_mode_with_options(request, runtime)

    async def get_current_mode_async(
        self,
        request: pcdn_20170411_models.GetCurrentModeRequest,
    ) -> pcdn_20170411_models.GetCurrentModeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_current_mode_with_options_async(request, runtime)

    def get_cover_rate_data_with_options(
        self,
        request: pcdn_20170411_models.GetCoverRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetCoverRateDataResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetCoverRateDataResponse().from_map(
            self.do_request('GetCoverRateData', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    async def get_cover_rate_data_with_options_async(
        self,
        request: pcdn_20170411_models.GetCoverRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetCoverRateDataResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetCoverRateDataResponse().from_map(
            await self.do_request_async('GetCoverRateData', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    def get_cover_rate_data(
        self,
        request: pcdn_20170411_models.GetCoverRateDataRequest,
    ) -> pcdn_20170411_models.GetCoverRateDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_cover_rate_data_with_options(request, runtime)

    async def get_cover_rate_data_async(
        self,
        request: pcdn_20170411_models.GetCoverRateDataRequest,
    ) -> pcdn_20170411_models.GetCoverRateDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_cover_rate_data_with_options_async(request, runtime)

    def get_fee_history_with_options(
        self,
        request: pcdn_20170411_models.GetFeeHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetFeeHistoryResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetFeeHistoryResponse().from_map(
            self.do_request('GetFeeHistory', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    async def get_fee_history_with_options_async(
        self,
        request: pcdn_20170411_models.GetFeeHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetFeeHistoryResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetFeeHistoryResponse().from_map(
            await self.do_request_async('GetFeeHistory', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    def get_fee_history(
        self,
        request: pcdn_20170411_models.GetFeeHistoryRequest,
    ) -> pcdn_20170411_models.GetFeeHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_fee_history_with_options(request, runtime)

    async def get_fee_history_async(
        self,
        request: pcdn_20170411_models.GetFeeHistoryRequest,
    ) -> pcdn_20170411_models.GetFeeHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_fee_history_with_options_async(request, runtime)

    def get_expense_summary_with_options(
        self,
        request: pcdn_20170411_models.GetExpenseSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetExpenseSummaryResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetExpenseSummaryResponse().from_map(
            self.do_request('GetExpenseSummary', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    async def get_expense_summary_with_options_async(
        self,
        request: pcdn_20170411_models.GetExpenseSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetExpenseSummaryResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetExpenseSummaryResponse().from_map(
            await self.do_request_async('GetExpenseSummary', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    def get_expense_summary(
        self,
        request: pcdn_20170411_models.GetExpenseSummaryRequest,
    ) -> pcdn_20170411_models.GetExpenseSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_expense_summary_with_options(request, runtime)

    async def get_expense_summary_async(
        self,
        request: pcdn_20170411_models.GetExpenseSummaryRequest,
    ) -> pcdn_20170411_models.GetExpenseSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_expense_summary_with_options_async(request, runtime)

    def get_domains_with_options(
        self,
        request: pcdn_20170411_models.GetDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetDomainsResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetDomainsResponse().from_map(
            self.do_request('GetDomains', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    async def get_domains_with_options_async(
        self,
        request: pcdn_20170411_models.GetDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetDomainsResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetDomainsResponse().from_map(
            await self.do_request_async('GetDomains', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    def get_domains(
        self,
        request: pcdn_20170411_models.GetDomainsRequest,
    ) -> pcdn_20170411_models.GetDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_domains_with_options(request, runtime)

    async def get_domains_async(
        self,
        request: pcdn_20170411_models.GetDomainsRequest,
    ) -> pcdn_20170411_models.GetDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_domains_with_options_async(request, runtime)

    def get_logs_list_with_options(
        self,
        request: pcdn_20170411_models.GetLogsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetLogsListResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetLogsListResponse().from_map(
            self.do_request('GetLogsList', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    async def get_logs_list_with_options_async(
        self,
        request: pcdn_20170411_models.GetLogsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetLogsListResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetLogsListResponse().from_map(
            await self.do_request_async('GetLogsList', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    def get_logs_list(
        self,
        request: pcdn_20170411_models.GetLogsListRequest,
    ) -> pcdn_20170411_models.GetLogsListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_logs_list_with_options(request, runtime)

    async def get_logs_list_async(
        self,
        request: pcdn_20170411_models.GetLogsListRequest,
    ) -> pcdn_20170411_models.GetLogsListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_logs_list_with_options_async(request, runtime)

    def get_fluency_data_with_options(
        self,
        request: pcdn_20170411_models.GetFluencyDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetFluencyDataResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetFluencyDataResponse().from_map(
            self.do_request('GetFluencyData', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    async def get_fluency_data_with_options_async(
        self,
        request: pcdn_20170411_models.GetFluencyDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetFluencyDataResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetFluencyDataResponse().from_map(
            await self.do_request_async('GetFluencyData', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    def get_fluency_data(
        self,
        request: pcdn_20170411_models.GetFluencyDataRequest,
    ) -> pcdn_20170411_models.GetFluencyDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_fluency_data_with_options(request, runtime)

    async def get_fluency_data_async(
        self,
        request: pcdn_20170411_models.GetFluencyDataRequest,
    ) -> pcdn_20170411_models.GetFluencyDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_fluency_data_with_options_async(request, runtime)

    def get_first_frame_delay_data_with_options(
        self,
        request: pcdn_20170411_models.GetFirstFrameDelayDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetFirstFrameDelayDataResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetFirstFrameDelayDataResponse().from_map(
            self.do_request('GetFirstFrameDelayData', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    async def get_first_frame_delay_data_with_options_async(
        self,
        request: pcdn_20170411_models.GetFirstFrameDelayDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetFirstFrameDelayDataResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetFirstFrameDelayDataResponse().from_map(
            await self.do_request_async('GetFirstFrameDelayData', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    def get_first_frame_delay_data(
        self,
        request: pcdn_20170411_models.GetFirstFrameDelayDataRequest,
    ) -> pcdn_20170411_models.GetFirstFrameDelayDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_first_frame_delay_data_with_options(request, runtime)

    async def get_first_frame_delay_data_async(
        self,
        request: pcdn_20170411_models.GetFirstFrameDelayDataRequest,
    ) -> pcdn_20170411_models.GetFirstFrameDelayDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_first_frame_delay_data_with_options_async(request, runtime)

    def get_token_list_with_options(
        self,
        request: pcdn_20170411_models.GetTokenListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetTokenListResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetTokenListResponse().from_map(
            self.do_request('GetTokenList', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    async def get_token_list_with_options_async(
        self,
        request: pcdn_20170411_models.GetTokenListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetTokenListResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetTokenListResponse().from_map(
            await self.do_request_async('GetTokenList', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    def get_token_list(
        self,
        request: pcdn_20170411_models.GetTokenListRequest,
    ) -> pcdn_20170411_models.GetTokenListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_token_list_with_options(request, runtime)

    async def get_token_list_async(
        self,
        request: pcdn_20170411_models.GetTokenListRequest,
    ) -> pcdn_20170411_models.GetTokenListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_token_list_with_options_async(request, runtime)

    def get_share_rate_data_with_options(
        self,
        request: pcdn_20170411_models.GetShareRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetShareRateDataResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetShareRateDataResponse().from_map(
            self.do_request('GetShareRateData', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    async def get_share_rate_data_with_options_async(
        self,
        request: pcdn_20170411_models.GetShareRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetShareRateDataResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetShareRateDataResponse().from_map(
            await self.do_request_async('GetShareRateData', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    def get_share_rate_data(
        self,
        request: pcdn_20170411_models.GetShareRateDataRequest,
    ) -> pcdn_20170411_models.GetShareRateDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_share_rate_data_with_options(request, runtime)

    async def get_share_rate_data_async(
        self,
        request: pcdn_20170411_models.GetShareRateDataRequest,
    ) -> pcdn_20170411_models.GetShareRateDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_share_rate_data_with_options_async(request, runtime)

    def get_traffic_data_with_options(
        self,
        request: pcdn_20170411_models.GetTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetTrafficDataResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetTrafficDataResponse().from_map(
            self.do_request('GetTrafficData', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    async def get_traffic_data_with_options_async(
        self,
        request: pcdn_20170411_models.GetTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetTrafficDataResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetTrafficDataResponse().from_map(
            await self.do_request_async('GetTrafficData', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    def get_traffic_data(
        self,
        request: pcdn_20170411_models.GetTrafficDataRequest,
    ) -> pcdn_20170411_models.GetTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_traffic_data_with_options(request, runtime)

    async def get_traffic_data_async(
        self,
        request: pcdn_20170411_models.GetTrafficDataRequest,
    ) -> pcdn_20170411_models.GetTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_traffic_data_with_options_async(request, runtime)

    def get_traffic_by_region_with_options(
        self,
        request: pcdn_20170411_models.GetTrafficByRegionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetTrafficByRegionResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetTrafficByRegionResponse().from_map(
            self.do_request('GetTrafficByRegion', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    async def get_traffic_by_region_with_options_async(
        self,
        request: pcdn_20170411_models.GetTrafficByRegionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetTrafficByRegionResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetTrafficByRegionResponse().from_map(
            await self.do_request_async('GetTrafficByRegion', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    def get_traffic_by_region(
        self,
        request: pcdn_20170411_models.GetTrafficByRegionRequest,
    ) -> pcdn_20170411_models.GetTrafficByRegionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_traffic_by_region_with_options(request, runtime)

    async def get_traffic_by_region_async(
        self,
        request: pcdn_20170411_models.GetTrafficByRegionRequest,
    ) -> pcdn_20170411_models.GetTrafficByRegionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_traffic_by_region_with_options_async(request, runtime)

    def get_all_regions_with_options(
        self,
        request: pcdn_20170411_models.GetAllRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetAllRegionsResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetAllRegionsResponse().from_map(
            self.do_request('GetAllRegions', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    async def get_all_regions_with_options_async(
        self,
        request: pcdn_20170411_models.GetAllRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pcdn_20170411_models.GetAllRegionsResponse:
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetAllRegionsResponse().from_map(
            await self.do_request_async('GetAllRegions', 'HTTPS', 'GET', '2017-04-11', 'AK', TeaCore.to_map(request), None, runtime)
        )

    def get_all_regions(
        self,
        request: pcdn_20170411_models.GetAllRegionsRequest,
    ) -> pcdn_20170411_models.GetAllRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_all_regions_with_options(request, runtime)

    async def get_all_regions_async(
        self,
        request: pcdn_20170411_models.GetAllRegionsRequest,
    ) -> pcdn_20170411_models.GetAllRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_all_regions_with_options_async(request, runtime)

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
