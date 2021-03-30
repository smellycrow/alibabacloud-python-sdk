# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_actiontrail20171204 import models as actiontrail_20171204_models
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
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'ap-northeast-2-pop': 'actiontrail.ap-northeast-1.aliyuncs.com',
            'cn-beijing-finance-1': 'actiontrail.aliyuncs.com',
            'cn-beijing-finance-pop': 'actiontrail.aliyuncs.com',
            'cn-beijing-gov-1': 'actiontrail.aliyuncs.com',
            'cn-beijing-nu16-b01': 'actiontrail.aliyuncs.com',
            'cn-edge-1': 'actiontrail.aliyuncs.com',
            'cn-fujian': 'actiontrail.aliyuncs.com',
            'cn-haidian-cm12-c01': 'actiontrail.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'actiontrail.aliyuncs.com',
            'cn-hangzhou-finance': 'actiontrail.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'actiontrail.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'actiontrail.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'actiontrail.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'actiontrail.aliyuncs.com',
            'cn-hangzhou-test-306': 'actiontrail.aliyuncs.com',
            'cn-hongkong-finance-pop': 'actiontrail.aliyuncs.com',
            'cn-qingdao-nebula': 'actiontrail.aliyuncs.com',
            'cn-shanghai-et15-b01': 'actiontrail.aliyuncs.com',
            'cn-shanghai-et2-b01': 'actiontrail.aliyuncs.com',
            'cn-shanghai-inner': 'actiontrail.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'actiontrail.aliyuncs.com',
            'cn-shenzhen-finance-1': 'actiontrail.aliyuncs.com',
            'cn-shenzhen-inner': 'actiontrail.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'actiontrail.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'actiontrail.aliyuncs.com',
            'cn-wuhan': 'actiontrail.aliyuncs.com',
            'cn-yushanfang': 'actiontrail.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'actiontrail.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'actiontrail.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'actiontrail.aliyuncs.com',
            'eu-west-1-oxs': 'actiontrail.ap-northeast-1.aliyuncs.com',
            'rus-west-1-pop': 'actiontrail.ap-northeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('actiontrail', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_trail_with_options(
        self,
        request: actiontrail_20171204_models.CreateTrailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20171204_models.CreateTrailResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Name'] = request.name
        query['OssBucketName'] = request.oss_bucket_name
        query['OssKeyPrefix'] = request.oss_key_prefix
        query['RoleName'] = request.role_name
        query['SlsProjectArn'] = request.sls_project_arn
        query['SlsWriteRoleArn'] = request.sls_write_role_arn
        query['EventRW'] = request.event_rw
        query['TrailRegion'] = request.trail_region
        query['MnsTopicArn'] = request.mns_topic_arn
        query['IsOrganizationTrail'] = request.is_organization_trail
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateTrail',
            version='2017-12-04',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20171204_models.CreateTrailResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_trail_with_options_async(
        self,
        request: actiontrail_20171204_models.CreateTrailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20171204_models.CreateTrailResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Name'] = request.name
        query['OssBucketName'] = request.oss_bucket_name
        query['OssKeyPrefix'] = request.oss_key_prefix
        query['RoleName'] = request.role_name
        query['SlsProjectArn'] = request.sls_project_arn
        query['SlsWriteRoleArn'] = request.sls_write_role_arn
        query['EventRW'] = request.event_rw
        query['TrailRegion'] = request.trail_region
        query['MnsTopicArn'] = request.mns_topic_arn
        query['IsOrganizationTrail'] = request.is_organization_trail
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateTrail',
            version='2017-12-04',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20171204_models.CreateTrailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_trail(
        self,
        request: actiontrail_20171204_models.CreateTrailRequest,
    ) -> actiontrail_20171204_models.CreateTrailResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_trail_with_options(request, runtime)

    async def create_trail_async(
        self,
        request: actiontrail_20171204_models.CreateTrailRequest,
    ) -> actiontrail_20171204_models.CreateTrailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_trail_with_options_async(request, runtime)

    def delete_trail_with_options(
        self,
        request: actiontrail_20171204_models.DeleteTrailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20171204_models.DeleteTrailResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteTrail',
            version='2017-12-04',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20171204_models.DeleteTrailResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_trail_with_options_async(
        self,
        request: actiontrail_20171204_models.DeleteTrailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20171204_models.DeleteTrailResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteTrail',
            version='2017-12-04',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20171204_models.DeleteTrailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_trail(
        self,
        request: actiontrail_20171204_models.DeleteTrailRequest,
    ) -> actiontrail_20171204_models.DeleteTrailResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_trail_with_options(request, runtime)

    async def delete_trail_async(
        self,
        request: actiontrail_20171204_models.DeleteTrailRequest,
    ) -> actiontrail_20171204_models.DeleteTrailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_trail_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20171204_models.DescribeRegionsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2017-12-04',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20171204_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20171204_models.DescribeRegionsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2017-12-04',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20171204_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(self) -> actiontrail_20171204_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(runtime)

    async def describe_regions_async(self) -> actiontrail_20171204_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(runtime)

    def describe_trails_with_options(
        self,
        request: actiontrail_20171204_models.DescribeTrailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20171204_models.DescribeTrailsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['IncludeShadowTrails'] = request.include_shadow_trails
        query['NameList'] = request.name_list
        query['IncludeOrganizationTrail'] = request.include_organization_trail
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeTrails',
            version='2017-12-04',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20171204_models.DescribeTrailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_trails_with_options_async(
        self,
        request: actiontrail_20171204_models.DescribeTrailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20171204_models.DescribeTrailsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['IncludeShadowTrails'] = request.include_shadow_trails
        query['NameList'] = request.name_list
        query['IncludeOrganizationTrail'] = request.include_organization_trail
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeTrails',
            version='2017-12-04',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20171204_models.DescribeTrailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_trails(
        self,
        request: actiontrail_20171204_models.DescribeTrailsRequest,
    ) -> actiontrail_20171204_models.DescribeTrailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_trails_with_options(request, runtime)

    async def describe_trails_async(
        self,
        request: actiontrail_20171204_models.DescribeTrailsRequest,
    ) -> actiontrail_20171204_models.DescribeTrailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_trails_with_options_async(request, runtime)

    def get_trail_status_with_options(
        self,
        request: actiontrail_20171204_models.GetTrailStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20171204_models.GetTrailStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Name'] = request.name
        query['IsOrganizationTrail'] = request.is_organization_trail
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetTrailStatus',
            version='2017-12-04',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20171204_models.GetTrailStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_trail_status_with_options_async(
        self,
        request: actiontrail_20171204_models.GetTrailStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20171204_models.GetTrailStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Name'] = request.name
        query['IsOrganizationTrail'] = request.is_organization_trail
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetTrailStatus',
            version='2017-12-04',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20171204_models.GetTrailStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_trail_status(
        self,
        request: actiontrail_20171204_models.GetTrailStatusRequest,
    ) -> actiontrail_20171204_models.GetTrailStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_trail_status_with_options(request, runtime)

    async def get_trail_status_async(
        self,
        request: actiontrail_20171204_models.GetTrailStatusRequest,
    ) -> actiontrail_20171204_models.GetTrailStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_trail_status_with_options_async(request, runtime)

    def lookup_events_with_options(
        self,
        request: actiontrail_20171204_models.LookupEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20171204_models.LookupEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Event'] = request.event
        query['Request'] = request.request
        query['EventType'] = request.event_type
        query['ServiceName'] = request.service_name
        query['EventName'] = request.event_name
        query['User'] = request.user
        query['ResourceType'] = request.resource_type
        query['ResourceName'] = request.resource_name
        query['EventRW'] = request.event_rw
        query['EventAccessKeyId'] = request.event_access_key_id
        query['NextToken'] = request.next_token
        query['MaxResults'] = request.max_results
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='LookupEvents',
            version='2017-12-04',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20171204_models.LookupEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def lookup_events_with_options_async(
        self,
        request: actiontrail_20171204_models.LookupEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20171204_models.LookupEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Event'] = request.event
        query['Request'] = request.request
        query['EventType'] = request.event_type
        query['ServiceName'] = request.service_name
        query['EventName'] = request.event_name
        query['User'] = request.user
        query['ResourceType'] = request.resource_type
        query['ResourceName'] = request.resource_name
        query['EventRW'] = request.event_rw
        query['EventAccessKeyId'] = request.event_access_key_id
        query['NextToken'] = request.next_token
        query['MaxResults'] = request.max_results
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='LookupEvents',
            version='2017-12-04',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20171204_models.LookupEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def lookup_events(
        self,
        request: actiontrail_20171204_models.LookupEventsRequest,
    ) -> actiontrail_20171204_models.LookupEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.lookup_events_with_options(request, runtime)

    async def lookup_events_async(
        self,
        request: actiontrail_20171204_models.LookupEventsRequest,
    ) -> actiontrail_20171204_models.LookupEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.lookup_events_with_options_async(request, runtime)

    def start_logging_with_options(
        self,
        request: actiontrail_20171204_models.StartLoggingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20171204_models.StartLoggingResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartLogging',
            version='2017-12-04',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20171204_models.StartLoggingResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_logging_with_options_async(
        self,
        request: actiontrail_20171204_models.StartLoggingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20171204_models.StartLoggingResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartLogging',
            version='2017-12-04',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20171204_models.StartLoggingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_logging(
        self,
        request: actiontrail_20171204_models.StartLoggingRequest,
    ) -> actiontrail_20171204_models.StartLoggingResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_logging_with_options(request, runtime)

    async def start_logging_async(
        self,
        request: actiontrail_20171204_models.StartLoggingRequest,
    ) -> actiontrail_20171204_models.StartLoggingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_logging_with_options_async(request, runtime)

    def stop_logging_with_options(
        self,
        request: actiontrail_20171204_models.StopLoggingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20171204_models.StopLoggingResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopLogging',
            version='2017-12-04',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20171204_models.StopLoggingResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_logging_with_options_async(
        self,
        request: actiontrail_20171204_models.StopLoggingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20171204_models.StopLoggingResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopLogging',
            version='2017-12-04',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20171204_models.StopLoggingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_logging(
        self,
        request: actiontrail_20171204_models.StopLoggingRequest,
    ) -> actiontrail_20171204_models.StopLoggingResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_logging_with_options(request, runtime)

    async def stop_logging_async(
        self,
        request: actiontrail_20171204_models.StopLoggingRequest,
    ) -> actiontrail_20171204_models.StopLoggingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_logging_with_options_async(request, runtime)

    def update_trail_with_options(
        self,
        request: actiontrail_20171204_models.UpdateTrailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20171204_models.UpdateTrailResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Name'] = request.name
        query['OssBucketName'] = request.oss_bucket_name
        query['OssKeyPrefix'] = request.oss_key_prefix
        query['RoleName'] = request.role_name
        query['SlsProjectArn'] = request.sls_project_arn
        query['SlsWriteRoleArn'] = request.sls_write_role_arn
        query['EventRW'] = request.event_rw
        query['TrailRegion'] = request.trail_region
        query['MnsTopicArn'] = request.mns_topic_arn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateTrail',
            version='2017-12-04',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20171204_models.UpdateTrailResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_trail_with_options_async(
        self,
        request: actiontrail_20171204_models.UpdateTrailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20171204_models.UpdateTrailResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Name'] = request.name
        query['OssBucketName'] = request.oss_bucket_name
        query['OssKeyPrefix'] = request.oss_key_prefix
        query['RoleName'] = request.role_name
        query['SlsProjectArn'] = request.sls_project_arn
        query['SlsWriteRoleArn'] = request.sls_write_role_arn
        query['EventRW'] = request.event_rw
        query['TrailRegion'] = request.trail_region
        query['MnsTopicArn'] = request.mns_topic_arn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateTrail',
            version='2017-12-04',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20171204_models.UpdateTrailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_trail(
        self,
        request: actiontrail_20171204_models.UpdateTrailRequest,
    ) -> actiontrail_20171204_models.UpdateTrailResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_trail_with_options(request, runtime)

    async def update_trail_async(
        self,
        request: actiontrail_20171204_models.UpdateTrailRequest,
    ) -> actiontrail_20171204_models.UpdateTrailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_trail_with_options_async(request, runtime)
