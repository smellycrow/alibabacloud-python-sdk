# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class DeleteAggregateConfigRulesRequest(TeaModel):
    def __init__(
        self,
        config_rule_ids: str = None,
        aggregator_id: str = None,
    ):
        self.config_rule_ids = config_rule_ids
        self.aggregator_id = aggregator_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_ids is not None:
            result['ConfigRuleIds'] = self.config_rule_ids
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleIds') is not None:
            self.config_rule_ids = m.get('ConfigRuleIds')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        return self


class DeleteAggregateConfigRulesResponseBodyOperateRuleResultOperateRuleItemList(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        success: bool = None,
        config_rule_id: str = None,
    ):
        self.error_code = error_code
        self.success = success
        self.config_rule_id = config_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        return self


class DeleteAggregateConfigRulesResponseBodyOperateRuleResult(TeaModel):
    def __init__(
        self,
        operate_rule_item_list: List[DeleteAggregateConfigRulesResponseBodyOperateRuleResultOperateRuleItemList] = None,
    ):
        self.operate_rule_item_list = operate_rule_item_list

    def validate(self):
        if self.operate_rule_item_list:
            for k in self.operate_rule_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OperateRuleItemList'] = []
        if self.operate_rule_item_list is not None:
            for k in self.operate_rule_item_list:
                result['OperateRuleItemList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operate_rule_item_list = []
        if m.get('OperateRuleItemList') is not None:
            for k in m.get('OperateRuleItemList'):
                temp_model = DeleteAggregateConfigRulesResponseBodyOperateRuleResultOperateRuleItemList()
                self.operate_rule_item_list.append(temp_model.from_map(k))
        return self


class DeleteAggregateConfigRulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        operate_rule_result: DeleteAggregateConfigRulesResponseBodyOperateRuleResult = None,
    ):
        self.request_id = request_id
        self.operate_rule_result = operate_rule_result

    def validate(self):
        if self.operate_rule_result:
            self.operate_rule_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.operate_rule_result is not None:
            result['OperateRuleResult'] = self.operate_rule_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OperateRuleResult') is not None:
            temp_model = DeleteAggregateConfigRulesResponseBodyOperateRuleResult()
            self.operate_rule_result = temp_model.from_map(m['OperateRuleResult'])
        return self


class DeleteAggregateConfigRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAggregateConfigRulesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteAggregateConfigRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeactiveAggregateConfigRulesRequest(TeaModel):
    def __init__(
        self,
        config_rule_ids: str = None,
        aggregator_id: str = None,
    ):
        self.config_rule_ids = config_rule_ids
        self.aggregator_id = aggregator_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_ids is not None:
            result['ConfigRuleIds'] = self.config_rule_ids
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleIds') is not None:
            self.config_rule_ids = m.get('ConfigRuleIds')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        return self


class DeactiveAggregateConfigRulesResponseBodyOperateRuleResultOperateRuleItemList(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        success: bool = None,
        config_rule_id: str = None,
    ):
        self.error_code = error_code
        self.success = success
        self.config_rule_id = config_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        return self


class DeactiveAggregateConfigRulesResponseBodyOperateRuleResult(TeaModel):
    def __init__(
        self,
        operate_rule_item_list: List[DeactiveAggregateConfigRulesResponseBodyOperateRuleResultOperateRuleItemList] = None,
    ):
        self.operate_rule_item_list = operate_rule_item_list

    def validate(self):
        if self.operate_rule_item_list:
            for k in self.operate_rule_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OperateRuleItemList'] = []
        if self.operate_rule_item_list is not None:
            for k in self.operate_rule_item_list:
                result['OperateRuleItemList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operate_rule_item_list = []
        if m.get('OperateRuleItemList') is not None:
            for k in m.get('OperateRuleItemList'):
                temp_model = DeactiveAggregateConfigRulesResponseBodyOperateRuleResultOperateRuleItemList()
                self.operate_rule_item_list.append(temp_model.from_map(k))
        return self


class DeactiveAggregateConfigRulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        operate_rule_result: DeactiveAggregateConfigRulesResponseBodyOperateRuleResult = None,
    ):
        self.request_id = request_id
        self.operate_rule_result = operate_rule_result

    def validate(self):
        if self.operate_rule_result:
            self.operate_rule_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.operate_rule_result is not None:
            result['OperateRuleResult'] = self.operate_rule_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OperateRuleResult') is not None:
            temp_model = DeactiveAggregateConfigRulesResponseBodyOperateRuleResult()
            self.operate_rule_result = temp_model.from_map(m['OperateRuleResult'])
        return self


class DeactiveAggregateConfigRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeactiveAggregateConfigRulesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeactiveAggregateConfigRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAggregateConfigRulesReportRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
    ):
        self.aggregator_id = aggregator_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        return self


class GetAggregateConfigRulesReportResponseBodyConfigRulesReport(TeaModel):
    def __init__(
        self,
        report_url: str = None,
        report_status: str = None,
        account_id: int = None,
        aggregator_id: str = None,
        report_create_timestamp: int = None,
    ):
        self.report_url = report_url
        self.report_status = report_status
        self.account_id = account_id
        self.aggregator_id = aggregator_id
        self.report_create_timestamp = report_create_timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.report_url is not None:
            result['ReportUrl'] = self.report_url
        if self.report_status is not None:
            result['ReportStatus'] = self.report_status
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.report_create_timestamp is not None:
            result['ReportCreateTimestamp'] = self.report_create_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReportUrl') is not None:
            self.report_url = m.get('ReportUrl')
        if m.get('ReportStatus') is not None:
            self.report_status = m.get('ReportStatus')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ReportCreateTimestamp') is not None:
            self.report_create_timestamp = m.get('ReportCreateTimestamp')
        return self


class GetAggregateConfigRulesReportResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        config_rules_report: GetAggregateConfigRulesReportResponseBodyConfigRulesReport = None,
    ):
        self.request_id = request_id
        self.config_rules_report = config_rules_report

    def validate(self):
        if self.config_rules_report:
            self.config_rules_report.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.config_rules_report is not None:
            result['ConfigRulesReport'] = self.config_rules_report.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ConfigRulesReport') is not None:
            temp_model = GetAggregateConfigRulesReportResponseBodyConfigRulesReport()
            self.config_rules_report = temp_model.from_map(m['ConfigRulesReport'])
        return self


class GetAggregateConfigRulesReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAggregateConfigRulesReportResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAggregateConfigRulesReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceInventoryResponseBodyResourceInventory(TeaModel):
    def __init__(
        self,
        download_url: str = None,
        status: str = None,
        account_id: int = None,
        resource_inventory_generate_time: int = None,
    ):
        self.download_url = download_url
        self.status = status
        self.account_id = account_id
        self.resource_inventory_generate_time = resource_inventory_generate_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.status is not None:
            result['Status'] = self.status
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.resource_inventory_generate_time is not None:
            result['ResourceInventoryGenerateTime'] = self.resource_inventory_generate_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ResourceInventoryGenerateTime') is not None:
            self.resource_inventory_generate_time = m.get('ResourceInventoryGenerateTime')
        return self


class GetResourceInventoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_inventory: GetResourceInventoryResponseBodyResourceInventory = None,
    ):
        self.request_id = request_id
        self.resource_inventory = resource_inventory

    def validate(self):
        if self.resource_inventory:
            self.resource_inventory.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_inventory is not None:
            result['ResourceInventory'] = self.resource_inventory.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceInventory') is not None:
            temp_model = GetResourceInventoryResponseBodyResourceInventory()
            self.resource_inventory = temp_model.from_map(m['ResourceInventory'])
        return self


class GetResourceInventoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetResourceInventoryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetResourceInventoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAggregateConfigRuleEvaluationResultsRequest(TeaModel):
    def __init__(
        self,
        compliance_type: str = None,
        next_token: str = None,
        max_results: int = None,
        config_rule_id: str = None,
        resource_owner_id: int = None,
        aggregator_id: str = None,
        compliance_pack_id: str = None,
    ):
        self.compliance_type = compliance_type
        self.next_token = next_token
        self.max_results = max_results
        self.config_rule_id = config_rule_id
        self.resource_owner_id = resource_owner_id
        self.aggregator_id = aggregator_id
        self.compliance_pack_id = compliance_pack_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        return self


class ListAggregateConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifierEvaluationResultQualifier(TeaModel):
    def __init__(
        self,
        resource_owner_id: int = None,
        config_rule_arn: str = None,
        resource_type: str = None,
        config_rule_name: str = None,
        resource_id: str = None,
        config_rule_id: str = None,
        resource_name: str = None,
        region_id: str = None,
        compliance_pack_id: str = None,
    ):
        self.resource_owner_id = resource_owner_id
        self.config_rule_arn = config_rule_arn
        self.resource_type = resource_type
        self.config_rule_name = config_rule_name
        self.resource_id = resource_id
        self.config_rule_id = config_rule_id
        self.resource_name = resource_name
        self.region_id = region_id
        self.compliance_pack_id = compliance_pack_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.config_rule_arn is not None:
            result['ConfigRuleArn'] = self.config_rule_arn
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ConfigRuleArn') is not None:
            self.config_rule_arn = m.get('ConfigRuleArn')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        return self


class ListAggregateConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifier(TeaModel):
    def __init__(
        self,
        ordering_timestamp: int = None,
        evaluation_result_qualifier: ListAggregateConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifierEvaluationResultQualifier = None,
    ):
        self.ordering_timestamp = ordering_timestamp
        self.evaluation_result_qualifier = evaluation_result_qualifier

    def validate(self):
        if self.evaluation_result_qualifier:
            self.evaluation_result_qualifier.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ordering_timestamp is not None:
            result['OrderingTimestamp'] = self.ordering_timestamp
        if self.evaluation_result_qualifier is not None:
            result['EvaluationResultQualifier'] = self.evaluation_result_qualifier.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderingTimestamp') is not None:
            self.ordering_timestamp = m.get('OrderingTimestamp')
        if m.get('EvaluationResultQualifier') is not None:
            temp_model = ListAggregateConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifierEvaluationResultQualifier()
            self.evaluation_result_qualifier = temp_model.from_map(m['EvaluationResultQualifier'])
        return self


class ListAggregateConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultList(TeaModel):
    def __init__(
        self,
        risk_level: int = None,
        compliance_type: str = None,
        result_recorded_timestamp: int = None,
        annotation: str = None,
        config_rule_invoked_timestamp: int = None,
        invoking_event_message_type: str = None,
        evaluation_result_identifier: ListAggregateConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifier = None,
        remediation_enabled: bool = None,
    ):
        self.risk_level = risk_level
        self.compliance_type = compliance_type
        self.result_recorded_timestamp = result_recorded_timestamp
        self.annotation = annotation
        self.config_rule_invoked_timestamp = config_rule_invoked_timestamp
        self.invoking_event_message_type = invoking_event_message_type
        self.evaluation_result_identifier = evaluation_result_identifier
        self.remediation_enabled = remediation_enabled

    def validate(self):
        if self.evaluation_result_identifier:
            self.evaluation_result_identifier.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.result_recorded_timestamp is not None:
            result['ResultRecordedTimestamp'] = self.result_recorded_timestamp
        if self.annotation is not None:
            result['Annotation'] = self.annotation
        if self.config_rule_invoked_timestamp is not None:
            result['ConfigRuleInvokedTimestamp'] = self.config_rule_invoked_timestamp
        if self.invoking_event_message_type is not None:
            result['InvokingEventMessageType'] = self.invoking_event_message_type
        if self.evaluation_result_identifier is not None:
            result['EvaluationResultIdentifier'] = self.evaluation_result_identifier.to_map()
        if self.remediation_enabled is not None:
            result['RemediationEnabled'] = self.remediation_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('ResultRecordedTimestamp') is not None:
            self.result_recorded_timestamp = m.get('ResultRecordedTimestamp')
        if m.get('Annotation') is not None:
            self.annotation = m.get('Annotation')
        if m.get('ConfigRuleInvokedTimestamp') is not None:
            self.config_rule_invoked_timestamp = m.get('ConfigRuleInvokedTimestamp')
        if m.get('InvokingEventMessageType') is not None:
            self.invoking_event_message_type = m.get('InvokingEventMessageType')
        if m.get('EvaluationResultIdentifier') is not None:
            temp_model = ListAggregateConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifier()
            self.evaluation_result_identifier = temp_model.from_map(m['EvaluationResultIdentifier'])
        if m.get('RemediationEnabled') is not None:
            self.remediation_enabled = m.get('RemediationEnabled')
        return self


class ListAggregateConfigRuleEvaluationResultsResponseBodyEvaluationResults(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        max_results: int = None,
        evaluation_result_list: List[ListAggregateConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultList] = None,
    ):
        self.next_token = next_token
        self.max_results = max_results
        self.evaluation_result_list = evaluation_result_list

    def validate(self):
        if self.evaluation_result_list:
            for k in self.evaluation_result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['EvaluationResultList'] = []
        if self.evaluation_result_list is not None:
            for k in self.evaluation_result_list:
                result['EvaluationResultList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.evaluation_result_list = []
        if m.get('EvaluationResultList') is not None:
            for k in m.get('EvaluationResultList'):
                temp_model = ListAggregateConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultList()
                self.evaluation_result_list.append(temp_model.from_map(k))
        return self


class ListAggregateConfigRuleEvaluationResultsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        evaluation_results: ListAggregateConfigRuleEvaluationResultsResponseBodyEvaluationResults = None,
    ):
        self.request_id = request_id
        self.evaluation_results = evaluation_results

    def validate(self):
        if self.evaluation_results:
            self.evaluation_results.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.evaluation_results is not None:
            result['EvaluationResults'] = self.evaluation_results.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('EvaluationResults') is not None:
            temp_model = ListAggregateConfigRuleEvaluationResultsResponseBodyEvaluationResults()
            self.evaluation_results = temp_model.from_map(m['EvaluationResults'])
        return self


class ListAggregateConfigRuleEvaluationResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAggregateConfigRuleEvaluationResultsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAggregateConfigRuleEvaluationResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAggregateRemediationsRequest(TeaModel):
    def __init__(
        self,
        config_rule_ids: str = None,
        aggregator_id: str = None,
    ):
        self.config_rule_ids = config_rule_ids
        self.aggregator_id = aggregator_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_ids is not None:
            result['ConfigRuleIds'] = self.config_rule_ids
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleIds') is not None:
            self.config_rule_ids = m.get('ConfigRuleIds')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        return self


class ListAggregateRemediationsResponseBodyRemediations(TeaModel):
    def __init__(
        self,
        remediation_template_id: str = None,
        remediation_dynamic_params: str = None,
        remediation_source_type: str = None,
        remediation_type: str = None,
        last_successful_invocation_id: str = None,
        account_id: int = None,
        aggregator_id: str = None,
        last_successful_invocation_type: str = None,
        remediation_id: str = None,
        invoke_type: str = None,
        config_rule_id: str = None,
        last_successful_invocation_time: int = None,
    ):
        self.remediation_template_id = remediation_template_id
        self.remediation_dynamic_params = remediation_dynamic_params
        self.remediation_source_type = remediation_source_type
        self.remediation_type = remediation_type
        self.last_successful_invocation_id = last_successful_invocation_id
        self.account_id = account_id
        self.aggregator_id = aggregator_id
        self.last_successful_invocation_type = last_successful_invocation_type
        self.remediation_id = remediation_id
        self.invoke_type = invoke_type
        self.config_rule_id = config_rule_id
        self.last_successful_invocation_time = last_successful_invocation_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.remediation_template_id is not None:
            result['RemediationTemplateId'] = self.remediation_template_id
        if self.remediation_dynamic_params is not None:
            result['RemediationDynamicParams'] = self.remediation_dynamic_params
        if self.remediation_source_type is not None:
            result['RemediationSourceType'] = self.remediation_source_type
        if self.remediation_type is not None:
            result['RemediationType'] = self.remediation_type
        if self.last_successful_invocation_id is not None:
            result['LastSuccessfulInvocationId'] = self.last_successful_invocation_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.last_successful_invocation_type is not None:
            result['LastSuccessfulInvocationType'] = self.last_successful_invocation_type
        if self.remediation_id is not None:
            result['RemediationId'] = self.remediation_id
        if self.invoke_type is not None:
            result['InvokeType'] = self.invoke_type
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.last_successful_invocation_time is not None:
            result['LastSuccessfulInvocationTime'] = self.last_successful_invocation_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RemediationTemplateId') is not None:
            self.remediation_template_id = m.get('RemediationTemplateId')
        if m.get('RemediationDynamicParams') is not None:
            self.remediation_dynamic_params = m.get('RemediationDynamicParams')
        if m.get('RemediationSourceType') is not None:
            self.remediation_source_type = m.get('RemediationSourceType')
        if m.get('RemediationType') is not None:
            self.remediation_type = m.get('RemediationType')
        if m.get('LastSuccessfulInvocationId') is not None:
            self.last_successful_invocation_id = m.get('LastSuccessfulInvocationId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('LastSuccessfulInvocationType') is not None:
            self.last_successful_invocation_type = m.get('LastSuccessfulInvocationType')
        if m.get('RemediationId') is not None:
            self.remediation_id = m.get('RemediationId')
        if m.get('InvokeType') is not None:
            self.invoke_type = m.get('InvokeType')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('LastSuccessfulInvocationTime') is not None:
            self.last_successful_invocation_time = m.get('LastSuccessfulInvocationTime')
        return self


class ListAggregateRemediationsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        remediations: List[ListAggregateRemediationsResponseBodyRemediations] = None,
    ):
        self.request_id = request_id
        self.remediations = remediations

    def validate(self):
        if self.remediations:
            for k in self.remediations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Remediations'] = []
        if self.remediations is not None:
            for k in self.remediations:
                result['Remediations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.remediations = []
        if m.get('Remediations') is not None:
            for k in m.get('Remediations'):
                temp_model = ListAggregateRemediationsResponseBodyRemediations()
                self.remediations.append(temp_model.from_map(k))
        return self


class ListAggregateRemediationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAggregateRemediationsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAggregateRemediationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAggregatorRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
    ):
        self.aggregator_id = aggregator_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        return self


class GetAggregatorResponseBodyAggregatorAggregatorAccounts(TeaModel):
    def __init__(
        self,
        recorder_status: str = None,
        account_id: int = None,
        account_type: str = None,
        account_name: str = None,
    ):
        self.recorder_status = recorder_status
        self.account_id = account_id
        self.account_type = account_type
        self.account_name = account_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.recorder_status is not None:
            result['RecorderStatus'] = self.recorder_status
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecorderStatus') is not None:
            self.recorder_status = m.get('RecorderStatus')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class GetAggregatorResponseBodyAggregator(TeaModel):
    def __init__(
        self,
        aggregator_create_timestamp: str = None,
        aggregator_accounts: List[GetAggregatorResponseBodyAggregatorAggregatorAccounts] = None,
        aggregator_account_count: int = None,
        description: str = None,
        aggregator_name: str = None,
        aggregator_status: int = None,
        aggregator_type: str = None,
        account_id: int = None,
        aggregator_id: str = None,
    ):
        self.aggregator_create_timestamp = aggregator_create_timestamp
        self.aggregator_accounts = aggregator_accounts
        self.aggregator_account_count = aggregator_account_count
        self.description = description
        self.aggregator_name = aggregator_name
        self.aggregator_status = aggregator_status
        self.aggregator_type = aggregator_type
        self.account_id = account_id
        self.aggregator_id = aggregator_id

    def validate(self):
        if self.aggregator_accounts:
            for k in self.aggregator_accounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_create_timestamp is not None:
            result['AggregatorCreateTimestamp'] = self.aggregator_create_timestamp
        result['AggregatorAccounts'] = []
        if self.aggregator_accounts is not None:
            for k in self.aggregator_accounts:
                result['AggregatorAccounts'].append(k.to_map() if k else None)
        if self.aggregator_account_count is not None:
            result['AggregatorAccountCount'] = self.aggregator_account_count
        if self.description is not None:
            result['Description'] = self.description
        if self.aggregator_name is not None:
            result['AggregatorName'] = self.aggregator_name
        if self.aggregator_status is not None:
            result['AggregatorStatus'] = self.aggregator_status
        if self.aggregator_type is not None:
            result['AggregatorType'] = self.aggregator_type
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorCreateTimestamp') is not None:
            self.aggregator_create_timestamp = m.get('AggregatorCreateTimestamp')
        self.aggregator_accounts = []
        if m.get('AggregatorAccounts') is not None:
            for k in m.get('AggregatorAccounts'):
                temp_model = GetAggregatorResponseBodyAggregatorAggregatorAccounts()
                self.aggregator_accounts.append(temp_model.from_map(k))
        if m.get('AggregatorAccountCount') is not None:
            self.aggregator_account_count = m.get('AggregatorAccountCount')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AggregatorName') is not None:
            self.aggregator_name = m.get('AggregatorName')
        if m.get('AggregatorStatus') is not None:
            self.aggregator_status = m.get('AggregatorStatus')
        if m.get('AggregatorType') is not None:
            self.aggregator_type = m.get('AggregatorType')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        return self


class GetAggregatorResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        aggregator: GetAggregatorResponseBodyAggregator = None,
    ):
        self.request_id = request_id
        self.aggregator = aggregator

    def validate(self):
        if self.aggregator:
            self.aggregator.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.aggregator is not None:
            result['Aggregator'] = self.aggregator.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Aggregator') is not None:
            temp_model = GetAggregatorResponseBodyAggregator()
            self.aggregator = temp_model.from_map(m['Aggregator'])
        return self


class GetAggregatorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAggregatorResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAggregatorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceComplianceTimelineRequest(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        resource_id: str = None,
        start_time: int = None,
        end_time: int = None,
        max_results: int = None,
        region: str = None,
        next_token: str = None,
    ):
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.start_time = start_time
        self.end_time = end_time
        self.max_results = max_results
        self.region = region
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.region is not None:
            result['Region'] = self.region
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class GetResourceComplianceTimelineResponseBodyResourceComplianceTimelineComplianceList(TeaModel):
    def __init__(
        self,
        tags: str = None,
        account_id: str = None,
        availability_zone: str = None,
        resource_type: str = None,
        resource_create_time: int = None,
        region: str = None,
        configuration: str = None,
        capture_time: int = None,
        configuration_diff: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_status: str = None,
    ):
        self.tags = tags
        self.account_id = account_id
        self.availability_zone = availability_zone
        self.resource_type = resource_type
        self.resource_create_time = resource_create_time
        self.region = region
        self.configuration = configuration
        self.capture_time = capture_time
        self.configuration_diff = configuration_diff
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_status = resource_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.availability_zone is not None:
            result['AvailabilityZone'] = self.availability_zone
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_create_time is not None:
            result['ResourceCreateTime'] = self.resource_create_time
        if self.region is not None:
            result['Region'] = self.region
        if self.configuration is not None:
            result['Configuration'] = self.configuration
        if self.capture_time is not None:
            result['CaptureTime'] = self.capture_time
        if self.configuration_diff is not None:
            result['ConfigurationDiff'] = self.configuration_diff
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_status is not None:
            result['ResourceStatus'] = self.resource_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AvailabilityZone') is not None:
            self.availability_zone = m.get('AvailabilityZone')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceCreateTime') is not None:
            self.resource_create_time = m.get('ResourceCreateTime')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Configuration') is not None:
            self.configuration = m.get('Configuration')
        if m.get('CaptureTime') is not None:
            self.capture_time = m.get('CaptureTime')
        if m.get('ConfigurationDiff') is not None:
            self.configuration_diff = m.get('ConfigurationDiff')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceStatus') is not None:
            self.resource_status = m.get('ResourceStatus')
        return self


class GetResourceComplianceTimelineResponseBodyResourceComplianceTimeline(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        max_results: int = None,
        compliance_list: List[GetResourceComplianceTimelineResponseBodyResourceComplianceTimelineComplianceList] = None,
    ):
        self.next_token = next_token
        self.max_results = max_results
        self.compliance_list = compliance_list

    def validate(self):
        if self.compliance_list:
            for k in self.compliance_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['ComplianceList'] = []
        if self.compliance_list is not None:
            for k in self.compliance_list:
                result['ComplianceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.compliance_list = []
        if m.get('ComplianceList') is not None:
            for k in m.get('ComplianceList'):
                temp_model = GetResourceComplianceTimelineResponseBodyResourceComplianceTimelineComplianceList()
                self.compliance_list.append(temp_model.from_map(k))
        return self


class GetResourceComplianceTimelineResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_compliance_timeline: GetResourceComplianceTimelineResponseBodyResourceComplianceTimeline = None,
    ):
        self.request_id = request_id
        self.resource_compliance_timeline = resource_compliance_timeline

    def validate(self):
        if self.resource_compliance_timeline:
            self.resource_compliance_timeline.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_compliance_timeline is not None:
            result['ResourceComplianceTimeline'] = self.resource_compliance_timeline.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceComplianceTimeline') is not None:
            temp_model = GetResourceComplianceTimelineResponseBodyResourceComplianceTimeline()
            self.resource_compliance_timeline = temp_model.from_map(m['ResourceComplianceTimeline'])
        return self


class GetResourceComplianceTimelineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetResourceComplianceTimelineResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetResourceComplianceTimelineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateAggregateConfigRulesReportRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        aggregator_id: str = None,
    ):
        self.client_token = client_token
        self.aggregator_id = aggregator_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        return self


class GenerateAggregateConfigRulesReportResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        aggregator_id: str = None,
    ):
        self.request_id = request_id
        self.aggregator_id = aggregator_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        return self


class GenerateAggregateConfigRulesReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GenerateAggregateConfigRulesReportResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GenerateAggregateConfigRulesReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAggregateCompliancePacksRequest(TeaModel):
    def __init__(
        self,
        status: str = None,
        aggregator_id: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.status = status
        self.aggregator_id = aggregator_id
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class ListAggregateCompliancePacksResponseBodyCompliancePacksResultCompliancePacks(TeaModel):
    def __init__(
        self,
        status: str = None,
        risk_level: int = None,
        compliance_pack_id: str = None,
        description: str = None,
        compliance_pack_name: str = None,
        account_id: int = None,
        aggregator_id: str = None,
        compliance_pack_template_id: str = None,
        create_timestamp: int = None,
    ):
        self.status = status
        self.risk_level = risk_level
        self.compliance_pack_id = compliance_pack_id
        self.description = description
        self.compliance_pack_name = compliance_pack_name
        self.account_id = account_id
        self.aggregator_id = aggregator_id
        self.compliance_pack_template_id = compliance_pack_template_id
        self.create_timestamp = create_timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.description is not None:
            result['Description'] = self.description
        if self.compliance_pack_name is not None:
            result['CompliancePackName'] = self.compliance_pack_name
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.compliance_pack_template_id is not None:
            result['CompliancePackTemplateId'] = self.compliance_pack_template_id
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CompliancePackName') is not None:
            self.compliance_pack_name = m.get('CompliancePackName')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('CompliancePackTemplateId') is not None:
            self.compliance_pack_template_id = m.get('CompliancePackTemplateId')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        return self


class ListAggregateCompliancePacksResponseBodyCompliancePacksResult(TeaModel):
    def __init__(
        self,
        compliance_packs: List[ListAggregateCompliancePacksResponseBodyCompliancePacksResultCompliancePacks] = None,
        page_size: int = None,
        page_number: int = None,
        total_count: int = None,
    ):
        self.compliance_packs = compliance_packs
        self.page_size = page_size
        self.page_number = page_number
        self.total_count = total_count

    def validate(self):
        if self.compliance_packs:
            for k in self.compliance_packs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CompliancePacks'] = []
        if self.compliance_packs is not None:
            for k in self.compliance_packs:
                result['CompliancePacks'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.compliance_packs = []
        if m.get('CompliancePacks') is not None:
            for k in m.get('CompliancePacks'):
                temp_model = ListAggregateCompliancePacksResponseBodyCompliancePacksResultCompliancePacks()
                self.compliance_packs.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAggregateCompliancePacksResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        compliance_packs_result: ListAggregateCompliancePacksResponseBodyCompliancePacksResult = None,
    ):
        self.request_id = request_id
        self.compliance_packs_result = compliance_packs_result

    def validate(self):
        if self.compliance_packs_result:
            self.compliance_packs_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.compliance_packs_result is not None:
            result['CompliancePacksResult'] = self.compliance_packs_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CompliancePacksResult') is not None:
            temp_model = ListAggregateCompliancePacksResponseBodyCompliancePacksResult()
            self.compliance_packs_result = temp_model.from_map(m['CompliancePacksResult'])
        return self


class ListAggregateCompliancePacksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAggregateCompliancePacksResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAggregateCompliancePacksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConfigRuleEvaluationResultsRequest(TeaModel):
    def __init__(
        self,
        compliance_type: str = None,
        next_token: str = None,
        max_results: int = None,
        config_rule_id: str = None,
        compliance_pack_id: str = None,
    ):
        self.compliance_type = compliance_type
        self.next_token = next_token
        self.max_results = max_results
        self.config_rule_id = config_rule_id
        self.compliance_pack_id = compliance_pack_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        return self


class ListConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifierEvaluationResultQualifier(TeaModel):
    def __init__(
        self,
        resource_owner_id: int = None,
        config_rule_arn: str = None,
        resource_type: str = None,
        config_rule_name: str = None,
        resource_id: str = None,
        config_rule_id: str = None,
        resource_name: str = None,
        region_id: str = None,
        compliance_pack_id: str = None,
    ):
        self.resource_owner_id = resource_owner_id
        self.config_rule_arn = config_rule_arn
        self.resource_type = resource_type
        self.config_rule_name = config_rule_name
        self.resource_id = resource_id
        self.config_rule_id = config_rule_id
        self.resource_name = resource_name
        self.region_id = region_id
        self.compliance_pack_id = compliance_pack_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.config_rule_arn is not None:
            result['ConfigRuleArn'] = self.config_rule_arn
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ConfigRuleArn') is not None:
            self.config_rule_arn = m.get('ConfigRuleArn')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        return self


class ListConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifier(TeaModel):
    def __init__(
        self,
        ordering_timestamp: int = None,
        evaluation_result_qualifier: ListConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifierEvaluationResultQualifier = None,
    ):
        self.ordering_timestamp = ordering_timestamp
        self.evaluation_result_qualifier = evaluation_result_qualifier

    def validate(self):
        if self.evaluation_result_qualifier:
            self.evaluation_result_qualifier.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ordering_timestamp is not None:
            result['OrderingTimestamp'] = self.ordering_timestamp
        if self.evaluation_result_qualifier is not None:
            result['EvaluationResultQualifier'] = self.evaluation_result_qualifier.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderingTimestamp') is not None:
            self.ordering_timestamp = m.get('OrderingTimestamp')
        if m.get('EvaluationResultQualifier') is not None:
            temp_model = ListConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifierEvaluationResultQualifier()
            self.evaluation_result_qualifier = temp_model.from_map(m['EvaluationResultQualifier'])
        return self


class ListConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultList(TeaModel):
    def __init__(
        self,
        risk_level: int = None,
        compliance_type: str = None,
        result_recorded_timestamp: int = None,
        annotation: str = None,
        config_rule_invoked_timestamp: int = None,
        invoking_event_message_type: str = None,
        evaluation_result_identifier: ListConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifier = None,
        remediation_enabled: bool = None,
    ):
        self.risk_level = risk_level
        self.compliance_type = compliance_type
        self.result_recorded_timestamp = result_recorded_timestamp
        self.annotation = annotation
        self.config_rule_invoked_timestamp = config_rule_invoked_timestamp
        self.invoking_event_message_type = invoking_event_message_type
        self.evaluation_result_identifier = evaluation_result_identifier
        self.remediation_enabled = remediation_enabled

    def validate(self):
        if self.evaluation_result_identifier:
            self.evaluation_result_identifier.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.result_recorded_timestamp is not None:
            result['ResultRecordedTimestamp'] = self.result_recorded_timestamp
        if self.annotation is not None:
            result['Annotation'] = self.annotation
        if self.config_rule_invoked_timestamp is not None:
            result['ConfigRuleInvokedTimestamp'] = self.config_rule_invoked_timestamp
        if self.invoking_event_message_type is not None:
            result['InvokingEventMessageType'] = self.invoking_event_message_type
        if self.evaluation_result_identifier is not None:
            result['EvaluationResultIdentifier'] = self.evaluation_result_identifier.to_map()
        if self.remediation_enabled is not None:
            result['RemediationEnabled'] = self.remediation_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('ResultRecordedTimestamp') is not None:
            self.result_recorded_timestamp = m.get('ResultRecordedTimestamp')
        if m.get('Annotation') is not None:
            self.annotation = m.get('Annotation')
        if m.get('ConfigRuleInvokedTimestamp') is not None:
            self.config_rule_invoked_timestamp = m.get('ConfigRuleInvokedTimestamp')
        if m.get('InvokingEventMessageType') is not None:
            self.invoking_event_message_type = m.get('InvokingEventMessageType')
        if m.get('EvaluationResultIdentifier') is not None:
            temp_model = ListConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifier()
            self.evaluation_result_identifier = temp_model.from_map(m['EvaluationResultIdentifier'])
        if m.get('RemediationEnabled') is not None:
            self.remediation_enabled = m.get('RemediationEnabled')
        return self


class ListConfigRuleEvaluationResultsResponseBodyEvaluationResults(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        max_results: int = None,
        evaluation_result_list: List[ListConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultList] = None,
    ):
        self.next_token = next_token
        self.max_results = max_results
        self.evaluation_result_list = evaluation_result_list

    def validate(self):
        if self.evaluation_result_list:
            for k in self.evaluation_result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['EvaluationResultList'] = []
        if self.evaluation_result_list is not None:
            for k in self.evaluation_result_list:
                result['EvaluationResultList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.evaluation_result_list = []
        if m.get('EvaluationResultList') is not None:
            for k in m.get('EvaluationResultList'):
                temp_model = ListConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultList()
                self.evaluation_result_list.append(temp_model.from_map(k))
        return self


class ListConfigRuleEvaluationResultsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        evaluation_results: ListConfigRuleEvaluationResultsResponseBodyEvaluationResults = None,
    ):
        self.request_id = request_id
        self.evaluation_results = evaluation_results

    def validate(self):
        if self.evaluation_results:
            self.evaluation_results.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.evaluation_results is not None:
            result['EvaluationResults'] = self.evaluation_results.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('EvaluationResults') is not None:
            temp_model = ListConfigRuleEvaluationResultsResponseBodyEvaluationResults()
            self.evaluation_results = temp_model.from_map(m['EvaluationResults'])
        return self


class ListConfigRuleEvaluationResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListConfigRuleEvaluationResultsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListConfigRuleEvaluationResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCompliancePacksRequest(TeaModel):
    def __init__(
        self,
        compliance_pack_ids: str = None,
        client_token: str = None,
    ):
        self.compliance_pack_ids = compliance_pack_ids
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_ids is not None:
            result['CompliancePackIds'] = self.compliance_pack_ids
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackIds') is not None:
            self.compliance_pack_ids = m.get('CompliancePackIds')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class DeleteCompliancePacksResponseBodyOperateCompliancePacksResultOperateCompliancePacks(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.error_code = error_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteCompliancePacksResponseBodyOperateCompliancePacksResult(TeaModel):
    def __init__(
        self,
        operate_compliance_packs: List[DeleteCompliancePacksResponseBodyOperateCompliancePacksResultOperateCompliancePacks] = None,
    ):
        self.operate_compliance_packs = operate_compliance_packs

    def validate(self):
        if self.operate_compliance_packs:
            for k in self.operate_compliance_packs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OperateCompliancePacks'] = []
        if self.operate_compliance_packs is not None:
            for k in self.operate_compliance_packs:
                result['OperateCompliancePacks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operate_compliance_packs = []
        if m.get('OperateCompliancePacks') is not None:
            for k in m.get('OperateCompliancePacks'):
                temp_model = DeleteCompliancePacksResponseBodyOperateCompliancePacksResultOperateCompliancePacks()
                self.operate_compliance_packs.append(temp_model.from_map(k))
        return self


class DeleteCompliancePacksResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        operate_compliance_packs_result: DeleteCompliancePacksResponseBodyOperateCompliancePacksResult = None,
    ):
        self.request_id = request_id
        self.operate_compliance_packs_result = operate_compliance_packs_result

    def validate(self):
        if self.operate_compliance_packs_result:
            self.operate_compliance_packs_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.operate_compliance_packs_result is not None:
            result['OperateCompliancePacksResult'] = self.operate_compliance_packs_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OperateCompliancePacksResult') is not None:
            temp_model = DeleteCompliancePacksResponseBodyOperateCompliancePacksResult()
            self.operate_compliance_packs_result = temp_model.from_map(m['OperateCompliancePacksResult'])
        return self


class DeleteCompliancePacksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteCompliancePacksResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteCompliancePacksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAggregateRemediationRequest(TeaModel):
    def __init__(
        self,
        remediation_id: str = None,
        remediation_type: str = None,
        remediation_template_id: str = None,
        invoke_type: str = None,
        source_type: str = None,
        params: str = None,
        aggregator_id: str = None,
    ):
        self.remediation_id = remediation_id
        self.remediation_type = remediation_type
        self.remediation_template_id = remediation_template_id
        self.invoke_type = invoke_type
        self.source_type = source_type
        self.params = params
        self.aggregator_id = aggregator_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.remediation_id is not None:
            result['RemediationId'] = self.remediation_id
        if self.remediation_type is not None:
            result['RemediationType'] = self.remediation_type
        if self.remediation_template_id is not None:
            result['RemediationTemplateId'] = self.remediation_template_id
        if self.invoke_type is not None:
            result['InvokeType'] = self.invoke_type
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.params is not None:
            result['Params'] = self.params
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RemediationId') is not None:
            self.remediation_id = m.get('RemediationId')
        if m.get('RemediationType') is not None:
            self.remediation_type = m.get('RemediationType')
        if m.get('RemediationTemplateId') is not None:
            self.remediation_template_id = m.get('RemediationTemplateId')
        if m.get('InvokeType') is not None:
            self.invoke_type = m.get('InvokeType')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        return self


class UpdateAggregateRemediationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        remediation_id: str = None,
    ):
        self.request_id = request_id
        self.remediation_id = remediation_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.remediation_id is not None:
            result['RemediationId'] = self.remediation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RemediationId') is not None:
            self.remediation_id = m.get('RemediationId')
        return self


class UpdateAggregateRemediationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAggregateRemediationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateAggregateRemediationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAggregateCompliancePacksRequest(TeaModel):
    def __init__(
        self,
        compliance_pack_ids: str = None,
        client_token: str = None,
        aggregator_id: str = None,
    ):
        self.compliance_pack_ids = compliance_pack_ids
        self.client_token = client_token
        self.aggregator_id = aggregator_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_ids is not None:
            result['CompliancePackIds'] = self.compliance_pack_ids
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackIds') is not None:
            self.compliance_pack_ids = m.get('CompliancePackIds')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        return self


class DeleteAggregateCompliancePacksResponseBodyOperateCompliancePacksResultOperateCompliancePacks(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.error_code = error_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAggregateCompliancePacksResponseBodyOperateCompliancePacksResult(TeaModel):
    def __init__(
        self,
        operate_compliance_packs: List[DeleteAggregateCompliancePacksResponseBodyOperateCompliancePacksResultOperateCompliancePacks] = None,
    ):
        self.operate_compliance_packs = operate_compliance_packs

    def validate(self):
        if self.operate_compliance_packs:
            for k in self.operate_compliance_packs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OperateCompliancePacks'] = []
        if self.operate_compliance_packs is not None:
            for k in self.operate_compliance_packs:
                result['OperateCompliancePacks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operate_compliance_packs = []
        if m.get('OperateCompliancePacks') is not None:
            for k in m.get('OperateCompliancePacks'):
                temp_model = DeleteAggregateCompliancePacksResponseBodyOperateCompliancePacksResultOperateCompliancePacks()
                self.operate_compliance_packs.append(temp_model.from_map(k))
        return self


class DeleteAggregateCompliancePacksResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        operate_compliance_packs_result: DeleteAggregateCompliancePacksResponseBodyOperateCompliancePacksResult = None,
    ):
        self.request_id = request_id
        self.operate_compliance_packs_result = operate_compliance_packs_result

    def validate(self):
        if self.operate_compliance_packs_result:
            self.operate_compliance_packs_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.operate_compliance_packs_result is not None:
            result['OperateCompliancePacksResult'] = self.operate_compliance_packs_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OperateCompliancePacksResult') is not None:
            temp_model = DeleteAggregateCompliancePacksResponseBodyOperateCompliancePacksResult()
            self.operate_compliance_packs_result = temp_model.from_map(m['OperateCompliancePacksResult'])
        return self


class DeleteAggregateCompliancePacksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAggregateCompliancePacksResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteAggregateCompliancePacksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAggregatorsRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        max_results: int = None,
    ):
        self.next_token = next_token
        self.max_results = max_results

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListAggregatorsResponseBodyAggregatorsResultAggregators(TeaModel):
    def __init__(
        self,
        aggregator_create_timestamp: int = None,
        aggregator_account_count: int = None,
        description: str = None,
        aggregator_name: str = None,
        aggregator_status: int = None,
        aggregator_type: str = None,
        account_id: int = None,
        aggregator_id: str = None,
    ):
        self.aggregator_create_timestamp = aggregator_create_timestamp
        self.aggregator_account_count = aggregator_account_count
        self.description = description
        self.aggregator_name = aggregator_name
        self.aggregator_status = aggregator_status
        self.aggregator_type = aggregator_type
        self.account_id = account_id
        self.aggregator_id = aggregator_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_create_timestamp is not None:
            result['AggregatorCreateTimestamp'] = self.aggregator_create_timestamp
        if self.aggregator_account_count is not None:
            result['AggregatorAccountCount'] = self.aggregator_account_count
        if self.description is not None:
            result['Description'] = self.description
        if self.aggregator_name is not None:
            result['AggregatorName'] = self.aggregator_name
        if self.aggregator_status is not None:
            result['AggregatorStatus'] = self.aggregator_status
        if self.aggregator_type is not None:
            result['AggregatorType'] = self.aggregator_type
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorCreateTimestamp') is not None:
            self.aggregator_create_timestamp = m.get('AggregatorCreateTimestamp')
        if m.get('AggregatorAccountCount') is not None:
            self.aggregator_account_count = m.get('AggregatorAccountCount')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AggregatorName') is not None:
            self.aggregator_name = m.get('AggregatorName')
        if m.get('AggregatorStatus') is not None:
            self.aggregator_status = m.get('AggregatorStatus')
        if m.get('AggregatorType') is not None:
            self.aggregator_type = m.get('AggregatorType')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        return self


class ListAggregatorsResponseBodyAggregatorsResult(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        aggregators: List[ListAggregatorsResponseBodyAggregatorsResultAggregators] = None,
    ):
        self.next_token = next_token
        self.aggregators = aggregators

    def validate(self):
        if self.aggregators:
            for k in self.aggregators:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Aggregators'] = []
        if self.aggregators is not None:
            for k in self.aggregators:
                result['Aggregators'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.aggregators = []
        if m.get('Aggregators') is not None:
            for k in m.get('Aggregators'):
                temp_model = ListAggregatorsResponseBodyAggregatorsResultAggregators()
                self.aggregators.append(temp_model.from_map(k))
        return self


class ListAggregatorsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        aggregators_result: ListAggregatorsResponseBodyAggregatorsResult = None,
    ):
        self.request_id = request_id
        self.aggregators_result = aggregators_result

    def validate(self):
        if self.aggregators_result:
            self.aggregators_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.aggregators_result is not None:
            result['AggregatorsResult'] = self.aggregators_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AggregatorsResult') is not None:
            temp_model = ListAggregatorsResponseBodyAggregatorsResult()
            self.aggregators_result = temp_model.from_map(m['AggregatorsResult'])
        return self


class ListAggregatorsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAggregatorsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAggregatorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAggregateCompliancePackRequestConfigRulesConfigRuleParameters(TeaModel):
    def __init__(
        self,
        parameter_name: str = None,
        parameter_value: str = None,
    ):
        self.parameter_name = parameter_name
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class UpdateAggregateCompliancePackRequestConfigRules(TeaModel):
    def __init__(
        self,
        managed_rule_identifier: str = None,
        config_rule_parameters: List[UpdateAggregateCompliancePackRequestConfigRulesConfigRuleParameters] = None,
        config_rule_id: str = None,
        config_rule_name: str = None,
        description: str = None,
        risk_level: int = None,
    ):
        self.managed_rule_identifier = managed_rule_identifier
        self.config_rule_parameters = config_rule_parameters
        self.config_rule_id = config_rule_id
        self.config_rule_name = config_rule_name
        self.description = description
        self.risk_level = risk_level

    def validate(self):
        if self.config_rule_parameters:
            for k in self.config_rule_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.managed_rule_identifier is not None:
            result['ManagedRuleIdentifier'] = self.managed_rule_identifier
        result['ConfigRuleParameters'] = []
        if self.config_rule_parameters is not None:
            for k in self.config_rule_parameters:
                result['ConfigRuleParameters'].append(k.to_map() if k else None)
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        if self.description is not None:
            result['Description'] = self.description
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ManagedRuleIdentifier') is not None:
            self.managed_rule_identifier = m.get('ManagedRuleIdentifier')
        self.config_rule_parameters = []
        if m.get('ConfigRuleParameters') is not None:
            for k in m.get('ConfigRuleParameters'):
                temp_model = UpdateAggregateCompliancePackRequestConfigRulesConfigRuleParameters()
                self.config_rule_parameters.append(temp_model.from_map(k))
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        return self


class UpdateAggregateCompliancePackRequest(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        description: str = None,
        risk_level: int = None,
        config_rules: List[UpdateAggregateCompliancePackRequestConfigRules] = None,
        client_token: str = None,
        aggregator_id: str = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.description = description
        self.risk_level = risk_level
        self.config_rules = config_rules
        self.client_token = client_token
        self.aggregator_id = aggregator_id

    def validate(self):
        if self.config_rules:
            for k in self.config_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.description is not None:
            result['Description'] = self.description
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        result['ConfigRules'] = []
        if self.config_rules is not None:
            for k in self.config_rules:
                result['ConfigRules'].append(k.to_map() if k else None)
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        self.config_rules = []
        if m.get('ConfigRules') is not None:
            for k in m.get('ConfigRules'):
                temp_model = UpdateAggregateCompliancePackRequestConfigRules()
                self.config_rules.append(temp_model.from_map(k))
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        return self


class UpdateAggregateCompliancePackShrinkRequest(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        description: str = None,
        risk_level: int = None,
        config_rules_shrink: str = None,
        client_token: str = None,
        aggregator_id: str = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.description = description
        self.risk_level = risk_level
        self.config_rules_shrink = config_rules_shrink
        self.client_token = client_token
        self.aggregator_id = aggregator_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.description is not None:
            result['Description'] = self.description
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.config_rules_shrink is not None:
            result['ConfigRules'] = self.config_rules_shrink
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('ConfigRules') is not None:
            self.config_rules_shrink = m.get('ConfigRules')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        return self


class UpdateAggregateCompliancePackResponseBody(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        request_id: str = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAggregateCompliancePackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAggregateCompliancePackResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateAggregateCompliancePackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAggregateCompliancePackRequest(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        aggregator_id: str = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.aggregator_id = aggregator_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        return self


class GetAggregateCompliancePackResponseBodyCompliancePackConfigRulesConfigRuleParameters(TeaModel):
    def __init__(
        self,
        required: bool = None,
        parameter_name: str = None,
        parameter_value: str = None,
    ):
        self.required = required
        self.parameter_name = parameter_name
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.required is not None:
            result['Required'] = self.required
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class GetAggregateCompliancePackResponseBodyCompliancePackConfigRules(TeaModel):
    def __init__(
        self,
        managed_rule_identifier: str = None,
        config_rule_name: str = None,
        config_rule_id: str = None,
        config_rule_parameters: List[GetAggregateCompliancePackResponseBodyCompliancePackConfigRulesConfigRuleParameters] = None,
        description: str = None,
        risk_level: int = None,
    ):
        self.managed_rule_identifier = managed_rule_identifier
        self.config_rule_name = config_rule_name
        self.config_rule_id = config_rule_id
        self.config_rule_parameters = config_rule_parameters
        self.description = description
        self.risk_level = risk_level

    def validate(self):
        if self.config_rule_parameters:
            for k in self.config_rule_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.managed_rule_identifier is not None:
            result['ManagedRuleIdentifier'] = self.managed_rule_identifier
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        result['ConfigRuleParameters'] = []
        if self.config_rule_parameters is not None:
            for k in self.config_rule_parameters:
                result['ConfigRuleParameters'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ManagedRuleIdentifier') is not None:
            self.managed_rule_identifier = m.get('ManagedRuleIdentifier')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        self.config_rule_parameters = []
        if m.get('ConfigRuleParameters') is not None:
            for k in m.get('ConfigRuleParameters'):
                temp_model = GetAggregateCompliancePackResponseBodyCompliancePackConfigRulesConfigRuleParameters()
                self.config_rule_parameters.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        return self


class GetAggregateCompliancePackResponseBodyCompliancePack(TeaModel):
    def __init__(
        self,
        status: str = None,
        risk_level: int = None,
        compliance_pack_id: str = None,
        description: str = None,
        config_rules: List[GetAggregateCompliancePackResponseBodyCompliancePackConfigRules] = None,
        compliance_pack_name: str = None,
        account_id: int = None,
        aggregator_id: str = None,
        compliance_pack_template_id: str = None,
        create_timestamp: int = None,
    ):
        self.status = status
        self.risk_level = risk_level
        self.compliance_pack_id = compliance_pack_id
        self.description = description
        self.config_rules = config_rules
        self.compliance_pack_name = compliance_pack_name
        self.account_id = account_id
        self.aggregator_id = aggregator_id
        self.compliance_pack_template_id = compliance_pack_template_id
        self.create_timestamp = create_timestamp

    def validate(self):
        if self.config_rules:
            for k in self.config_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.description is not None:
            result['Description'] = self.description
        result['ConfigRules'] = []
        if self.config_rules is not None:
            for k in self.config_rules:
                result['ConfigRules'].append(k.to_map() if k else None)
        if self.compliance_pack_name is not None:
            result['CompliancePackName'] = self.compliance_pack_name
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.compliance_pack_template_id is not None:
            result['CompliancePackTemplateId'] = self.compliance_pack_template_id
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.config_rules = []
        if m.get('ConfigRules') is not None:
            for k in m.get('ConfigRules'):
                temp_model = GetAggregateCompliancePackResponseBodyCompliancePackConfigRules()
                self.config_rules.append(temp_model.from_map(k))
        if m.get('CompliancePackName') is not None:
            self.compliance_pack_name = m.get('CompliancePackName')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('CompliancePackTemplateId') is not None:
            self.compliance_pack_template_id = m.get('CompliancePackTemplateId')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        return self


class GetAggregateCompliancePackResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        compliance_pack: GetAggregateCompliancePackResponseBodyCompliancePack = None,
    ):
        self.request_id = request_id
        self.compliance_pack = compliance_pack

    def validate(self):
        if self.compliance_pack:
            self.compliance_pack.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.compliance_pack is not None:
            result['CompliancePack'] = self.compliance_pack.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CompliancePack') is not None:
            temp_model = GetAggregateCompliancePackResponseBodyCompliancePack()
            self.compliance_pack = temp_model.from_map(m['CompliancePack'])
        return self


class GetAggregateCompliancePackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAggregateCompliancePackResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAggregateCompliancePackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAggregateRemediationsRequest(TeaModel):
    def __init__(
        self,
        remediation_ids: str = None,
        aggregator_id: str = None,
    ):
        self.remediation_ids = remediation_ids
        self.aggregator_id = aggregator_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.remediation_ids is not None:
            result['RemediationIds'] = self.remediation_ids
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RemediationIds') is not None:
            self.remediation_ids = m.get('RemediationIds')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        return self


class DeleteAggregateRemediationsResponseBodyRemediationDeleteResults(TeaModel):
    def __init__(
        self,
        remediation_id: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.remediation_id = remediation_id
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.remediation_id is not None:
            result['RemediationId'] = self.remediation_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RemediationId') is not None:
            self.remediation_id = m.get('RemediationId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAggregateRemediationsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        remediation_delete_results: List[DeleteAggregateRemediationsResponseBodyRemediationDeleteResults] = None,
    ):
        self.request_id = request_id
        self.remediation_delete_results = remediation_delete_results

    def validate(self):
        if self.remediation_delete_results:
            for k in self.remediation_delete_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RemediationDeleteResults'] = []
        if self.remediation_delete_results is not None:
            for k in self.remediation_delete_results:
                result['RemediationDeleteResults'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.remediation_delete_results = []
        if m.get('RemediationDeleteResults') is not None:
            for k in m.get('RemediationDeleteResults'):
                temp_model = DeleteAggregateRemediationsResponseBodyRemediationDeleteResults()
                self.remediation_delete_results.append(temp_model.from_map(k))
        return self


class DeleteAggregateRemediationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAggregateRemediationsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteAggregateRemediationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateConfigRulesReportRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class GenerateConfigRulesReportResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateConfigRulesReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GenerateConfigRulesReportResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GenerateConfigRulesReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAggregateResourceComplianceByPackRequest(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        aggregator_id: str = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.aggregator_id = aggregator_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        return self


class GetAggregateResourceComplianceByPackResponseBodyResourceComplianceResult(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        non_compliant_count: int = None,
        total_count: int = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.non_compliant_count = non_compliant_count
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.non_compliant_count is not None:
            result['NonCompliantCount'] = self.non_compliant_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('NonCompliantCount') is not None:
            self.non_compliant_count = m.get('NonCompliantCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetAggregateResourceComplianceByPackResponseBody(TeaModel):
    def __init__(
        self,
        resource_compliance_result: GetAggregateResourceComplianceByPackResponseBodyResourceComplianceResult = None,
        request_id: str = None,
    ):
        self.resource_compliance_result = resource_compliance_result
        self.request_id = request_id

    def validate(self):
        if self.resource_compliance_result:
            self.resource_compliance_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_compliance_result is not None:
            result['ResourceComplianceResult'] = self.resource_compliance_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceComplianceResult') is not None:
            temp_model = GetAggregateResourceComplianceByPackResponseBodyResourceComplianceResult()
            self.resource_compliance_result = temp_model.from_map(m['ResourceComplianceResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAggregateResourceComplianceByPackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAggregateResourceComplianceByPackResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAggregateResourceComplianceByPackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRemediationsRequest(TeaModel):
    def __init__(
        self,
        remediation_ids: str = None,
    ):
        self.remediation_ids = remediation_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.remediation_ids is not None:
            result['RemediationIds'] = self.remediation_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RemediationIds') is not None:
            self.remediation_ids = m.get('RemediationIds')
        return self


class DeleteRemediationsResponseBodyRemediationDeleteResults(TeaModel):
    def __init__(
        self,
        remediation_id: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.remediation_id = remediation_id
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.remediation_id is not None:
            result['RemediationId'] = self.remediation_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RemediationId') is not None:
            self.remediation_id = m.get('RemediationId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteRemediationsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        remediation_delete_results: List[DeleteRemediationsResponseBodyRemediationDeleteResults] = None,
    ):
        self.request_id = request_id
        self.remediation_delete_results = remediation_delete_results

    def validate(self):
        if self.remediation_delete_results:
            for k in self.remediation_delete_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RemediationDeleteResults'] = []
        if self.remediation_delete_results is not None:
            for k in self.remediation_delete_results:
                result['RemediationDeleteResults'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.remediation_delete_results = []
        if m.get('RemediationDeleteResults') is not None:
            for k in m.get('RemediationDeleteResults'):
                temp_model = DeleteRemediationsResponseBodyRemediationDeleteResults()
                self.remediation_delete_results.append(temp_model.from_map(k))
        return self


class DeleteRemediationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteRemediationsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteRemediationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCompliancePacksRequest(TeaModel):
    def __init__(
        self,
        status: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.status = status
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class ListCompliancePacksResponseBodyCompliancePacksResultCompliancePacks(TeaModel):
    def __init__(
        self,
        status: str = None,
        compliance_pack_id: str = None,
        risk_level: int = None,
        description: str = None,
        compliance_pack_name: str = None,
        account_id: int = None,
        compliance_pack_template_id: str = None,
        create_timestamp: int = None,
    ):
        self.status = status
        self.compliance_pack_id = compliance_pack_id
        self.risk_level = risk_level
        self.description = description
        self.compliance_pack_name = compliance_pack_name
        self.account_id = account_id
        self.compliance_pack_template_id = compliance_pack_template_id
        self.create_timestamp = create_timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.description is not None:
            result['Description'] = self.description
        if self.compliance_pack_name is not None:
            result['CompliancePackName'] = self.compliance_pack_name
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.compliance_pack_template_id is not None:
            result['CompliancePackTemplateId'] = self.compliance_pack_template_id
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CompliancePackName') is not None:
            self.compliance_pack_name = m.get('CompliancePackName')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CompliancePackTemplateId') is not None:
            self.compliance_pack_template_id = m.get('CompliancePackTemplateId')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        return self


class ListCompliancePacksResponseBodyCompliancePacksResult(TeaModel):
    def __init__(
        self,
        compliance_packs: List[ListCompliancePacksResponseBodyCompliancePacksResultCompliancePacks] = None,
        page_size: int = None,
        page_number: int = None,
        total_count: int = None,
    ):
        self.compliance_packs = compliance_packs
        self.page_size = page_size
        self.page_number = page_number
        self.total_count = total_count

    def validate(self):
        if self.compliance_packs:
            for k in self.compliance_packs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CompliancePacks'] = []
        if self.compliance_packs is not None:
            for k in self.compliance_packs:
                result['CompliancePacks'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.compliance_packs = []
        if m.get('CompliancePacks') is not None:
            for k in m.get('CompliancePacks'):
                temp_model = ListCompliancePacksResponseBodyCompliancePacksResultCompliancePacks()
                self.compliance_packs.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCompliancePacksResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        compliance_packs_result: ListCompliancePacksResponseBodyCompliancePacksResult = None,
    ):
        self.request_id = request_id
        self.compliance_packs_result = compliance_packs_result

    def validate(self):
        if self.compliance_packs_result:
            self.compliance_packs_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.compliance_packs_result is not None:
            result['CompliancePacksResult'] = self.compliance_packs_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CompliancePacksResult') is not None:
            temp_model = ListCompliancePacksResponseBodyCompliancePacksResult()
            self.compliance_packs_result = temp_model.from_map(m['CompliancePacksResult'])
        return self


class ListCompliancePacksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListCompliancePacksResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListCompliancePacksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ActiveAggregateConfigRulesRequest(TeaModel):
    def __init__(
        self,
        config_rule_ids: str = None,
        aggregator_id: str = None,
    ):
        self.config_rule_ids = config_rule_ids
        self.aggregator_id = aggregator_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_ids is not None:
            result['ConfigRuleIds'] = self.config_rule_ids
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleIds') is not None:
            self.config_rule_ids = m.get('ConfigRuleIds')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        return self


class ActiveAggregateConfigRulesResponseBodyOperateRuleResultOperateRuleItemList(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        success: bool = None,
        config_rule_id: str = None,
    ):
        self.error_code = error_code
        self.success = success
        self.config_rule_id = config_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        return self


class ActiveAggregateConfigRulesResponseBodyOperateRuleResult(TeaModel):
    def __init__(
        self,
        operate_rule_item_list: List[ActiveAggregateConfigRulesResponseBodyOperateRuleResultOperateRuleItemList] = None,
    ):
        self.operate_rule_item_list = operate_rule_item_list

    def validate(self):
        if self.operate_rule_item_list:
            for k in self.operate_rule_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OperateRuleItemList'] = []
        if self.operate_rule_item_list is not None:
            for k in self.operate_rule_item_list:
                result['OperateRuleItemList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operate_rule_item_list = []
        if m.get('OperateRuleItemList') is not None:
            for k in m.get('OperateRuleItemList'):
                temp_model = ActiveAggregateConfigRulesResponseBodyOperateRuleResultOperateRuleItemList()
                self.operate_rule_item_list.append(temp_model.from_map(k))
        return self


class ActiveAggregateConfigRulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        operate_rule_result: ActiveAggregateConfigRulesResponseBodyOperateRuleResult = None,
    ):
        self.request_id = request_id
        self.operate_rule_result = operate_rule_result

    def validate(self):
        if self.operate_rule_result:
            self.operate_rule_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.operate_rule_result is not None:
            result['OperateRuleResult'] = self.operate_rule_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OperateRuleResult') is not None:
            temp_model = ActiveAggregateConfigRulesResponseBodyOperateRuleResult()
            self.operate_rule_result = temp_model.from_map(m['OperateRuleResult'])
        return self


class ActiveAggregateConfigRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ActiveAggregateConfigRulesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ActiveAggregateConfigRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceComplianceByPackRequest(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
    ):
        self.compliance_pack_id = compliance_pack_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        return self


class GetResourceComplianceByPackResponseBodyResourceComplianceResult(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        non_compliant_count: int = None,
        total_count: int = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.non_compliant_count = non_compliant_count
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.non_compliant_count is not None:
            result['NonCompliantCount'] = self.non_compliant_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('NonCompliantCount') is not None:
            self.non_compliant_count = m.get('NonCompliantCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetResourceComplianceByPackResponseBody(TeaModel):
    def __init__(
        self,
        resource_compliance_result: GetResourceComplianceByPackResponseBodyResourceComplianceResult = None,
        request_id: str = None,
    ):
        self.resource_compliance_result = resource_compliance_result
        self.request_id = request_id

    def validate(self):
        if self.resource_compliance_result:
            self.resource_compliance_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_compliance_result is not None:
            result['ResourceComplianceResult'] = self.resource_compliance_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceComplianceResult') is not None:
            temp_model = GetResourceComplianceByPackResponseBodyResourceComplianceResult()
            self.resource_compliance_result = temp_model.from_map(m['ResourceComplianceResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetResourceComplianceByPackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetResourceComplianceByPackResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetResourceComplianceByPackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceOwnerInAllAggregatorResponseBodyAccountInAggregator(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        account_name: str = None,
    ):
        self.account_id = account_id
        self.account_name = account_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class ListResourceOwnerInAllAggregatorResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        account_in_aggregator: List[ListResourceOwnerInAllAggregatorResponseBodyAccountInAggregator] = None,
    ):
        self.request_id = request_id
        self.account_in_aggregator = account_in_aggregator

    def validate(self):
        if self.account_in_aggregator:
            for k in self.account_in_aggregator:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['AccountInAggregator'] = []
        if self.account_in_aggregator is not None:
            for k in self.account_in_aggregator:
                result['AccountInAggregator'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.account_in_aggregator = []
        if m.get('AccountInAggregator') is not None:
            for k in m.get('AccountInAggregator'):
                temp_model = ListResourceOwnerInAllAggregatorResponseBodyAccountInAggregator()
                self.account_in_aggregator.append(temp_model.from_map(k))
        return self


class ListResourceOwnerInAllAggregatorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListResourceOwnerInAllAggregatorResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListResourceOwnerInAllAggregatorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCompliancePackTemplatesRequest(TeaModel):
    def __init__(
        self,
        compliance_pack_template_id: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.compliance_pack_template_id = compliance_pack_template_id
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_template_id is not None:
            result['CompliancePackTemplateId'] = self.compliance_pack_template_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackTemplateId') is not None:
            self.compliance_pack_template_id = m.get('CompliancePackTemplateId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class ListCompliancePackTemplatesResponseBodyCompliancePackTemplatesResultCompliancePackTemplatesConfigRulesConfigRuleParameters(TeaModel):
    def __init__(
        self,
        required: bool = None,
        parameter_name: str = None,
        parameter_value: str = None,
    ):
        self.required = required
        self.parameter_name = parameter_name
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.required is not None:
            result['Required'] = self.required
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class ListCompliancePackTemplatesResponseBodyCompliancePackTemplatesResultCompliancePackTemplatesConfigRules(TeaModel):
    def __init__(
        self,
        description: str = None,
        managed_rule_identifier: str = None,
        managed_rule_name: str = None,
        config_rule_parameters: List[ListCompliancePackTemplatesResponseBodyCompliancePackTemplatesResultCompliancePackTemplatesConfigRulesConfigRuleParameters] = None,
        risk_level: int = None,
    ):
        self.description = description
        self.managed_rule_identifier = managed_rule_identifier
        self.managed_rule_name = managed_rule_name
        self.config_rule_parameters = config_rule_parameters
        self.risk_level = risk_level

    def validate(self):
        if self.config_rule_parameters:
            for k in self.config_rule_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.managed_rule_identifier is not None:
            result['ManagedRuleIdentifier'] = self.managed_rule_identifier
        if self.managed_rule_name is not None:
            result['ManagedRuleName'] = self.managed_rule_name
        result['ConfigRuleParameters'] = []
        if self.config_rule_parameters is not None:
            for k in self.config_rule_parameters:
                result['ConfigRuleParameters'].append(k.to_map() if k else None)
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ManagedRuleIdentifier') is not None:
            self.managed_rule_identifier = m.get('ManagedRuleIdentifier')
        if m.get('ManagedRuleName') is not None:
            self.managed_rule_name = m.get('ManagedRuleName')
        self.config_rule_parameters = []
        if m.get('ConfigRuleParameters') is not None:
            for k in m.get('ConfigRuleParameters'):
                temp_model = ListCompliancePackTemplatesResponseBodyCompliancePackTemplatesResultCompliancePackTemplatesConfigRulesConfigRuleParameters()
                self.config_rule_parameters.append(temp_model.from_map(k))
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        return self


class ListCompliancePackTemplatesResponseBodyCompliancePackTemplatesResultCompliancePackTemplates(TeaModel):
    def __init__(
        self,
        risk_level: int = None,
        description: str = None,
        config_rules: List[ListCompliancePackTemplatesResponseBodyCompliancePackTemplatesResultCompliancePackTemplatesConfigRules] = None,
        compliance_pack_template_name: str = None,
        compliance_pack_template_id: str = None,
    ):
        self.risk_level = risk_level
        self.description = description
        self.config_rules = config_rules
        self.compliance_pack_template_name = compliance_pack_template_name
        self.compliance_pack_template_id = compliance_pack_template_id

    def validate(self):
        if self.config_rules:
            for k in self.config_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.description is not None:
            result['Description'] = self.description
        result['ConfigRules'] = []
        if self.config_rules is not None:
            for k in self.config_rules:
                result['ConfigRules'].append(k.to_map() if k else None)
        if self.compliance_pack_template_name is not None:
            result['CompliancePackTemplateName'] = self.compliance_pack_template_name
        if self.compliance_pack_template_id is not None:
            result['CompliancePackTemplateId'] = self.compliance_pack_template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.config_rules = []
        if m.get('ConfigRules') is not None:
            for k in m.get('ConfigRules'):
                temp_model = ListCompliancePackTemplatesResponseBodyCompliancePackTemplatesResultCompliancePackTemplatesConfigRules()
                self.config_rules.append(temp_model.from_map(k))
        if m.get('CompliancePackTemplateName') is not None:
            self.compliance_pack_template_name = m.get('CompliancePackTemplateName')
        if m.get('CompliancePackTemplateId') is not None:
            self.compliance_pack_template_id = m.get('CompliancePackTemplateId')
        return self


class ListCompliancePackTemplatesResponseBodyCompliancePackTemplatesResult(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        page_number: int = None,
        total_count: int = None,
        compliance_pack_templates: List[ListCompliancePackTemplatesResponseBodyCompliancePackTemplatesResultCompliancePackTemplates] = None,
    ):
        self.page_size = page_size
        self.page_number = page_number
        self.total_count = total_count
        self.compliance_pack_templates = compliance_pack_templates

    def validate(self):
        if self.compliance_pack_templates:
            for k in self.compliance_pack_templates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['CompliancePackTemplates'] = []
        if self.compliance_pack_templates is not None:
            for k in self.compliance_pack_templates:
                result['CompliancePackTemplates'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.compliance_pack_templates = []
        if m.get('CompliancePackTemplates') is not None:
            for k in m.get('CompliancePackTemplates'):
                temp_model = ListCompliancePackTemplatesResponseBodyCompliancePackTemplatesResultCompliancePackTemplates()
                self.compliance_pack_templates.append(temp_model.from_map(k))
        return self


class ListCompliancePackTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        compliance_pack_templates_result: ListCompliancePackTemplatesResponseBodyCompliancePackTemplatesResult = None,
        request_id: str = None,
    ):
        self.compliance_pack_templates_result = compliance_pack_templates_result
        self.request_id = request_id

    def validate(self):
        if self.compliance_pack_templates_result:
            self.compliance_pack_templates_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_templates_result is not None:
            result['CompliancePackTemplatesResult'] = self.compliance_pack_templates_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackTemplatesResult') is not None:
            temp_model = ListCompliancePackTemplatesResponseBodyCompliancePackTemplatesResult()
            self.compliance_pack_templates_result = temp_model.from_map(m['CompliancePackTemplatesResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListCompliancePackTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListCompliancePackTemplatesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListCompliancePackTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRemediationRequest(TeaModel):
    def __init__(
        self,
        remediation_id: str = None,
        remediation_type: str = None,
        remediation_template_id: str = None,
        invoke_type: str = None,
        source_type: str = None,
        params: str = None,
    ):
        self.remediation_id = remediation_id
        self.remediation_type = remediation_type
        self.remediation_template_id = remediation_template_id
        self.invoke_type = invoke_type
        self.source_type = source_type
        self.params = params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.remediation_id is not None:
            result['RemediationId'] = self.remediation_id
        if self.remediation_type is not None:
            result['RemediationType'] = self.remediation_type
        if self.remediation_template_id is not None:
            result['RemediationTemplateId'] = self.remediation_template_id
        if self.invoke_type is not None:
            result['InvokeType'] = self.invoke_type
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.params is not None:
            result['Params'] = self.params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RemediationId') is not None:
            self.remediation_id = m.get('RemediationId')
        if m.get('RemediationType') is not None:
            self.remediation_type = m.get('RemediationType')
        if m.get('RemediationTemplateId') is not None:
            self.remediation_template_id = m.get('RemediationTemplateId')
        if m.get('InvokeType') is not None:
            self.invoke_type = m.get('InvokeType')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        return self


class UpdateRemediationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        remediation_id: str = None,
    ):
        self.request_id = request_id
        self.remediation_id = remediation_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.remediation_id is not None:
            result['RemediationId'] = self.remediation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RemediationId') is not None:
            self.remediation_id = m.get('RemediationId')
        return self


class UpdateRemediationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateRemediationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateRemediationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAggregateAccountComplianceByPackRequest(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        aggregator_id: str = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.aggregator_id = aggregator_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        return self


class GetAggregateAccountComplianceByPackResponseBodyAccountComplianceResultAccountCompliances(TeaModel):
    def __init__(
        self,
        compliance_type: str = None,
        account_id: int = None,
        account_name: str = None,
    ):
        self.compliance_type = compliance_type
        self.account_id = account_id
        self.account_name = account_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class GetAggregateAccountComplianceByPackResponseBodyAccountComplianceResult(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        non_compliant_count: int = None,
        total_count: int = None,
        account_compliances: List[GetAggregateAccountComplianceByPackResponseBodyAccountComplianceResultAccountCompliances] = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.non_compliant_count = non_compliant_count
        self.total_count = total_count
        self.account_compliances = account_compliances

    def validate(self):
        if self.account_compliances:
            for k in self.account_compliances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.non_compliant_count is not None:
            result['NonCompliantCount'] = self.non_compliant_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['AccountCompliances'] = []
        if self.account_compliances is not None:
            for k in self.account_compliances:
                result['AccountCompliances'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('NonCompliantCount') is not None:
            self.non_compliant_count = m.get('NonCompliantCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.account_compliances = []
        if m.get('AccountCompliances') is not None:
            for k in m.get('AccountCompliances'):
                temp_model = GetAggregateAccountComplianceByPackResponseBodyAccountComplianceResultAccountCompliances()
                self.account_compliances.append(temp_model.from_map(k))
        return self


class GetAggregateAccountComplianceByPackResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        account_compliance_result: GetAggregateAccountComplianceByPackResponseBodyAccountComplianceResult = None,
    ):
        self.request_id = request_id
        self.account_compliance_result = account_compliance_result

    def validate(self):
        if self.account_compliance_result:
            self.account_compliance_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.account_compliance_result is not None:
            result['AccountComplianceResult'] = self.account_compliance_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AccountComplianceResult') is not None:
            temp_model = GetAggregateAccountComplianceByPackResponseBodyAccountComplianceResult()
            self.account_compliance_result = temp_model.from_map(m['AccountComplianceResult'])
        return self


class GetAggregateAccountComplianceByPackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAggregateAccountComplianceByPackResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAggregateAccountComplianceByPackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateConfigRuleRequest(TeaModel):
    def __init__(
        self,
        config_rule_name: str = None,
        description: str = None,
        input_parameters: Dict[str, Any] = None,
        config_rule_trigger_types: str = None,
        maximum_execution_frequency: str = None,
        resource_types_scope: List[str] = None,
        risk_level: int = None,
        client_token: str = None,
        region_ids_scope: str = None,
        exclude_resource_ids_scope: str = None,
        resource_group_ids_scope: str = None,
        tag_key_scope: str = None,
        tag_value_scope: str = None,
        source_owner: str = None,
        source_identifier: str = None,
    ):
        self.config_rule_name = config_rule_name
        self.description = description
        self.input_parameters = input_parameters
        self.config_rule_trigger_types = config_rule_trigger_types
        self.maximum_execution_frequency = maximum_execution_frequency
        self.resource_types_scope = resource_types_scope
        self.risk_level = risk_level
        self.client_token = client_token
        self.region_ids_scope = region_ids_scope
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        self.resource_group_ids_scope = resource_group_ids_scope
        self.tag_key_scope = tag_key_scope
        self.tag_value_scope = tag_value_scope
        self.source_owner = source_owner
        self.source_identifier = source_identifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        if self.description is not None:
            result['Description'] = self.description
        if self.input_parameters is not None:
            result['InputParameters'] = self.input_parameters
        if self.config_rule_trigger_types is not None:
            result['ConfigRuleTriggerTypes'] = self.config_rule_trigger_types
        if self.maximum_execution_frequency is not None:
            result['MaximumExecutionFrequency'] = self.maximum_execution_frequency
        if self.resource_types_scope is not None:
            result['ResourceTypesScope'] = self.resource_types_scope
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_ids_scope is not None:
            result['RegionIdsScope'] = self.region_ids_scope
        if self.exclude_resource_ids_scope is not None:
            result['ExcludeResourceIdsScope'] = self.exclude_resource_ids_scope
        if self.resource_group_ids_scope is not None:
            result['ResourceGroupIdsScope'] = self.resource_group_ids_scope
        if self.tag_key_scope is not None:
            result['TagKeyScope'] = self.tag_key_scope
        if self.tag_value_scope is not None:
            result['TagValueScope'] = self.tag_value_scope
        if self.source_owner is not None:
            result['SourceOwner'] = self.source_owner
        if self.source_identifier is not None:
            result['SourceIdentifier'] = self.source_identifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InputParameters') is not None:
            self.input_parameters = m.get('InputParameters')
        if m.get('ConfigRuleTriggerTypes') is not None:
            self.config_rule_trigger_types = m.get('ConfigRuleTriggerTypes')
        if m.get('MaximumExecutionFrequency') is not None:
            self.maximum_execution_frequency = m.get('MaximumExecutionFrequency')
        if m.get('ResourceTypesScope') is not None:
            self.resource_types_scope = m.get('ResourceTypesScope')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionIdsScope') is not None:
            self.region_ids_scope = m.get('RegionIdsScope')
        if m.get('ExcludeResourceIdsScope') is not None:
            self.exclude_resource_ids_scope = m.get('ExcludeResourceIdsScope')
        if m.get('ResourceGroupIdsScope') is not None:
            self.resource_group_ids_scope = m.get('ResourceGroupIdsScope')
        if m.get('TagKeyScope') is not None:
            self.tag_key_scope = m.get('TagKeyScope')
        if m.get('TagValueScope') is not None:
            self.tag_value_scope = m.get('TagValueScope')
        if m.get('SourceOwner') is not None:
            self.source_owner = m.get('SourceOwner')
        if m.get('SourceIdentifier') is not None:
            self.source_identifier = m.get('SourceIdentifier')
        return self


class CreateConfigRuleShrinkRequest(TeaModel):
    def __init__(
        self,
        config_rule_name: str = None,
        description: str = None,
        input_parameters_shrink: str = None,
        config_rule_trigger_types: str = None,
        maximum_execution_frequency: str = None,
        resource_types_scope_shrink: str = None,
        risk_level: int = None,
        client_token: str = None,
        region_ids_scope: str = None,
        exclude_resource_ids_scope: str = None,
        resource_group_ids_scope: str = None,
        tag_key_scope: str = None,
        tag_value_scope: str = None,
        source_owner: str = None,
        source_identifier: str = None,
    ):
        self.config_rule_name = config_rule_name
        self.description = description
        self.input_parameters_shrink = input_parameters_shrink
        self.config_rule_trigger_types = config_rule_trigger_types
        self.maximum_execution_frequency = maximum_execution_frequency
        self.resource_types_scope_shrink = resource_types_scope_shrink
        self.risk_level = risk_level
        self.client_token = client_token
        self.region_ids_scope = region_ids_scope
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        self.resource_group_ids_scope = resource_group_ids_scope
        self.tag_key_scope = tag_key_scope
        self.tag_value_scope = tag_value_scope
        self.source_owner = source_owner
        self.source_identifier = source_identifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        if self.description is not None:
            result['Description'] = self.description
        if self.input_parameters_shrink is not None:
            result['InputParameters'] = self.input_parameters_shrink
        if self.config_rule_trigger_types is not None:
            result['ConfigRuleTriggerTypes'] = self.config_rule_trigger_types
        if self.maximum_execution_frequency is not None:
            result['MaximumExecutionFrequency'] = self.maximum_execution_frequency
        if self.resource_types_scope_shrink is not None:
            result['ResourceTypesScope'] = self.resource_types_scope_shrink
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_ids_scope is not None:
            result['RegionIdsScope'] = self.region_ids_scope
        if self.exclude_resource_ids_scope is not None:
            result['ExcludeResourceIdsScope'] = self.exclude_resource_ids_scope
        if self.resource_group_ids_scope is not None:
            result['ResourceGroupIdsScope'] = self.resource_group_ids_scope
        if self.tag_key_scope is not None:
            result['TagKeyScope'] = self.tag_key_scope
        if self.tag_value_scope is not None:
            result['TagValueScope'] = self.tag_value_scope
        if self.source_owner is not None:
            result['SourceOwner'] = self.source_owner
        if self.source_identifier is not None:
            result['SourceIdentifier'] = self.source_identifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InputParameters') is not None:
            self.input_parameters_shrink = m.get('InputParameters')
        if m.get('ConfigRuleTriggerTypes') is not None:
            self.config_rule_trigger_types = m.get('ConfigRuleTriggerTypes')
        if m.get('MaximumExecutionFrequency') is not None:
            self.maximum_execution_frequency = m.get('MaximumExecutionFrequency')
        if m.get('ResourceTypesScope') is not None:
            self.resource_types_scope_shrink = m.get('ResourceTypesScope')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionIdsScope') is not None:
            self.region_ids_scope = m.get('RegionIdsScope')
        if m.get('ExcludeResourceIdsScope') is not None:
            self.exclude_resource_ids_scope = m.get('ExcludeResourceIdsScope')
        if m.get('ResourceGroupIdsScope') is not None:
            self.resource_group_ids_scope = m.get('ResourceGroupIdsScope')
        if m.get('TagKeyScope') is not None:
            self.tag_key_scope = m.get('TagKeyScope')
        if m.get('TagValueScope') is not None:
            self.tag_value_scope = m.get('TagValueScope')
        if m.get('SourceOwner') is not None:
            self.source_owner = m.get('SourceOwner')
        if m.get('SourceIdentifier') is not None:
            self.source_identifier = m.get('SourceIdentifier')
        return self


class CreateConfigRuleResponseBody(TeaModel):
    def __init__(
        self,
        config_rule_id: str = None,
        request_id: str = None,
    ):
        self.config_rule_id = config_rule_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateConfigRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateConfigRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateConfigRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAggregateResourceConfigurationTimelineRequest(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        start_time: int = None,
        end_time: int = None,
        max_results: int = None,
        resource_type: str = None,
        region: str = None,
        aggregator_id: str = None,
        resource_owner_id: int = None,
        next_token: str = None,
    ):
        self.resource_id = resource_id
        self.start_time = start_time
        self.end_time = end_time
        self.max_results = max_results
        self.resource_type = resource_type
        self.region = region
        self.aggregator_id = aggregator_id
        self.resource_owner_id = resource_owner_id
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.region is not None:
            result['Region'] = self.region
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class GetAggregateResourceConfigurationTimelineResponseBodyResourceConfigurationTimelineConfigurationList(TeaModel):
    def __init__(
        self,
        tags: str = None,
        account_id: int = None,
        resource_event_type: str = None,
        availability_zone: str = None,
        resource_type: str = None,
        resource_create_time: str = None,
        region: str = None,
        capture_time: str = None,
        configuration_diff: str = None,
        resource_id: str = None,
        resource_name: str = None,
    ):
        self.tags = tags
        self.account_id = account_id
        self.resource_event_type = resource_event_type
        self.availability_zone = availability_zone
        self.resource_type = resource_type
        self.resource_create_time = resource_create_time
        self.region = region
        self.capture_time = capture_time
        self.configuration_diff = configuration_diff
        self.resource_id = resource_id
        self.resource_name = resource_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.resource_event_type is not None:
            result['ResourceEventType'] = self.resource_event_type
        if self.availability_zone is not None:
            result['AvailabilityZone'] = self.availability_zone
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_create_time is not None:
            result['ResourceCreateTime'] = self.resource_create_time
        if self.region is not None:
            result['Region'] = self.region
        if self.capture_time is not None:
            result['CaptureTime'] = self.capture_time
        if self.configuration_diff is not None:
            result['ConfigurationDiff'] = self.configuration_diff
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ResourceEventType') is not None:
            self.resource_event_type = m.get('ResourceEventType')
        if m.get('AvailabilityZone') is not None:
            self.availability_zone = m.get('AvailabilityZone')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceCreateTime') is not None:
            self.resource_create_time = m.get('ResourceCreateTime')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('CaptureTime') is not None:
            self.capture_time = m.get('CaptureTime')
        if m.get('ConfigurationDiff') is not None:
            self.configuration_diff = m.get('ConfigurationDiff')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        return self


class GetAggregateResourceConfigurationTimelineResponseBodyResourceConfigurationTimeline(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        max_results: int = None,
        configuration_list: List[GetAggregateResourceConfigurationTimelineResponseBodyResourceConfigurationTimelineConfigurationList] = None,
    ):
        self.next_token = next_token
        self.max_results = max_results
        self.configuration_list = configuration_list

    def validate(self):
        if self.configuration_list:
            for k in self.configuration_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['ConfigurationList'] = []
        if self.configuration_list is not None:
            for k in self.configuration_list:
                result['ConfigurationList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.configuration_list = []
        if m.get('ConfigurationList') is not None:
            for k in m.get('ConfigurationList'):
                temp_model = GetAggregateResourceConfigurationTimelineResponseBodyResourceConfigurationTimelineConfigurationList()
                self.configuration_list.append(temp_model.from_map(k))
        return self


class GetAggregateResourceConfigurationTimelineResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_configuration_timeline: GetAggregateResourceConfigurationTimelineResponseBodyResourceConfigurationTimeline = None,
    ):
        self.request_id = request_id
        self.resource_configuration_timeline = resource_configuration_timeline

    def validate(self):
        if self.resource_configuration_timeline:
            self.resource_configuration_timeline.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_configuration_timeline is not None:
            result['ResourceConfigurationTimeline'] = self.resource_configuration_timeline.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceConfigurationTimeline') is not None:
            temp_model = GetAggregateResourceConfigurationTimelineResponseBodyResourceConfigurationTimeline()
            self.resource_configuration_timeline = temp_model.from_map(m['ResourceConfigurationTimeline'])
        return self


class GetAggregateResourceConfigurationTimelineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAggregateResourceConfigurationTimelineResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAggregateResourceConfigurationTimelineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAggregatorsRequest(TeaModel):
    def __init__(
        self,
        aggregator_ids: str = None,
        client_token: str = None,
    ):
        self.aggregator_ids = aggregator_ids
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_ids is not None:
            result['AggregatorIds'] = self.aggregator_ids
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorIds') is not None:
            self.aggregator_ids = m.get('AggregatorIds')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class DeleteAggregatorsResponseBodyOperateAggregatorsResultOperateAggregators(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        success: bool = None,
        aggregator_id: str = None,
    ):
        self.error_code = error_code
        self.success = success
        self.aggregator_id = aggregator_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        return self


class DeleteAggregatorsResponseBodyOperateAggregatorsResult(TeaModel):
    def __init__(
        self,
        operate_aggregators: List[DeleteAggregatorsResponseBodyOperateAggregatorsResultOperateAggregators] = None,
    ):
        self.operate_aggregators = operate_aggregators

    def validate(self):
        if self.operate_aggregators:
            for k in self.operate_aggregators:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OperateAggregators'] = []
        if self.operate_aggregators is not None:
            for k in self.operate_aggregators:
                result['OperateAggregators'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operate_aggregators = []
        if m.get('OperateAggregators') is not None:
            for k in m.get('OperateAggregators'):
                temp_model = DeleteAggregatorsResponseBodyOperateAggregatorsResultOperateAggregators()
                self.operate_aggregators.append(temp_model.from_map(k))
        return self


class DeleteAggregatorsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        operate_aggregators_result: DeleteAggregatorsResponseBodyOperateAggregatorsResult = None,
    ):
        self.request_id = request_id
        self.operate_aggregators_result = operate_aggregators_result

    def validate(self):
        if self.operate_aggregators_result:
            self.operate_aggregators_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.operate_aggregators_result is not None:
            result['OperateAggregatorsResult'] = self.operate_aggregators_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OperateAggregatorsResult') is not None:
            temp_model = DeleteAggregatorsResponseBodyOperateAggregatorsResult()
            self.operate_aggregators_result = temp_model.from_map(m['OperateAggregatorsResult'])
        return self


class DeleteAggregatorsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAggregatorsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteAggregatorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateResourceInventoryRequest(TeaModel):
    def __init__(
        self,
        regions: str = None,
        resource_types: str = None,
    ):
        self.regions = regions
        self.resource_types = resource_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.regions is not None:
            result['Regions'] = self.regions
        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Regions') is not None:
            self.regions = m.get('Regions')
        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')
        return self


class GenerateResourceInventoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateResourceInventoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GenerateResourceInventoryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GenerateResourceInventoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRemediationRequest(TeaModel):
    def __init__(
        self,
        config_rule_id: str = None,
        remediation_type: str = None,
        remediation_template_id: str = None,
        invoke_type: str = None,
        source_type: str = None,
        params: str = None,
        client_token: str = None,
    ):
        self.config_rule_id = config_rule_id
        self.remediation_type = remediation_type
        self.remediation_template_id = remediation_template_id
        self.invoke_type = invoke_type
        self.source_type = source_type
        self.params = params
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.remediation_type is not None:
            result['RemediationType'] = self.remediation_type
        if self.remediation_template_id is not None:
            result['RemediationTemplateId'] = self.remediation_template_id
        if self.invoke_type is not None:
            result['InvokeType'] = self.invoke_type
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.params is not None:
            result['Params'] = self.params
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('RemediationType') is not None:
            self.remediation_type = m.get('RemediationType')
        if m.get('RemediationTemplateId') is not None:
            self.remediation_template_id = m.get('RemediationTemplateId')
        if m.get('InvokeType') is not None:
            self.invoke_type = m.get('InvokeType')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateRemediationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        remediation_id: str = None,
    ):
        self.request_id = request_id
        self.remediation_id = remediation_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.remediation_id is not None:
            result['RemediationId'] = self.remediation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RemediationId') is not None:
            self.remediation_id = m.get('RemediationId')
        return self


class CreateRemediationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRemediationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateRemediationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCompliancePackRequest(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
    ):
        self.compliance_pack_id = compliance_pack_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        return self


class GetCompliancePackResponseBodyCompliancePackConfigRulesConfigRuleParameters(TeaModel):
    def __init__(
        self,
        required: bool = None,
        parameter_name: str = None,
        parameter_value: str = None,
    ):
        self.required = required
        self.parameter_name = parameter_name
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.required is not None:
            result['Required'] = self.required
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class GetCompliancePackResponseBodyCompliancePackConfigRules(TeaModel):
    def __init__(
        self,
        managed_rule_identifier: str = None,
        config_rule_name: str = None,
        config_rule_id: str = None,
        config_rule_parameters: List[GetCompliancePackResponseBodyCompliancePackConfigRulesConfigRuleParameters] = None,
        description: str = None,
        risk_level: int = None,
    ):
        self.managed_rule_identifier = managed_rule_identifier
        self.config_rule_name = config_rule_name
        self.config_rule_id = config_rule_id
        self.config_rule_parameters = config_rule_parameters
        self.description = description
        self.risk_level = risk_level

    def validate(self):
        if self.config_rule_parameters:
            for k in self.config_rule_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.managed_rule_identifier is not None:
            result['ManagedRuleIdentifier'] = self.managed_rule_identifier
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        result['ConfigRuleParameters'] = []
        if self.config_rule_parameters is not None:
            for k in self.config_rule_parameters:
                result['ConfigRuleParameters'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ManagedRuleIdentifier') is not None:
            self.managed_rule_identifier = m.get('ManagedRuleIdentifier')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        self.config_rule_parameters = []
        if m.get('ConfigRuleParameters') is not None:
            for k in m.get('ConfigRuleParameters'):
                temp_model = GetCompliancePackResponseBodyCompliancePackConfigRulesConfigRuleParameters()
                self.config_rule_parameters.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        return self


class GetCompliancePackResponseBodyCompliancePack(TeaModel):
    def __init__(
        self,
        status: str = None,
        compliance_pack_id: str = None,
        risk_level: int = None,
        description: str = None,
        config_rules: List[GetCompliancePackResponseBodyCompliancePackConfigRules] = None,
        compliance_pack_name: str = None,
        account_id: int = None,
        compliance_pack_template_id: str = None,
        create_timestamp: int = None,
    ):
        self.status = status
        self.compliance_pack_id = compliance_pack_id
        self.risk_level = risk_level
        self.description = description
        self.config_rules = config_rules
        self.compliance_pack_name = compliance_pack_name
        self.account_id = account_id
        self.compliance_pack_template_id = compliance_pack_template_id
        self.create_timestamp = create_timestamp

    def validate(self):
        if self.config_rules:
            for k in self.config_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.description is not None:
            result['Description'] = self.description
        result['ConfigRules'] = []
        if self.config_rules is not None:
            for k in self.config_rules:
                result['ConfigRules'].append(k.to_map() if k else None)
        if self.compliance_pack_name is not None:
            result['CompliancePackName'] = self.compliance_pack_name
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.compliance_pack_template_id is not None:
            result['CompliancePackTemplateId'] = self.compliance_pack_template_id
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.config_rules = []
        if m.get('ConfigRules') is not None:
            for k in m.get('ConfigRules'):
                temp_model = GetCompliancePackResponseBodyCompliancePackConfigRules()
                self.config_rules.append(temp_model.from_map(k))
        if m.get('CompliancePackName') is not None:
            self.compliance_pack_name = m.get('CompliancePackName')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CompliancePackTemplateId') is not None:
            self.compliance_pack_template_id = m.get('CompliancePackTemplateId')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        return self


class GetCompliancePackResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        compliance_pack: GetCompliancePackResponseBodyCompliancePack = None,
    ):
        self.request_id = request_id
        self.compliance_pack = compliance_pack

    def validate(self):
        if self.compliance_pack:
            self.compliance_pack.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.compliance_pack is not None:
            result['CompliancePack'] = self.compliance_pack.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CompliancePack') is not None:
            temp_model = GetCompliancePackResponseBodyCompliancePack()
            self.compliance_pack = temp_model.from_map(m['CompliancePack'])
        return self


class GetCompliancePackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetCompliancePackResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetCompliancePackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConfigRulesReportResponseBodyConfigRulesReport(TeaModel):
    def __init__(
        self,
        report_status: str = None,
        report_url: str = None,
        account_id: int = None,
        report_create_timestamp: int = None,
    ):
        self.report_status = report_status
        self.report_url = report_url
        self.account_id = account_id
        self.report_create_timestamp = report_create_timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.report_status is not None:
            result['ReportStatus'] = self.report_status
        if self.report_url is not None:
            result['ReportUrl'] = self.report_url
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.report_create_timestamp is not None:
            result['ReportCreateTimestamp'] = self.report_create_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReportStatus') is not None:
            self.report_status = m.get('ReportStatus')
        if m.get('ReportUrl') is not None:
            self.report_url = m.get('ReportUrl')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ReportCreateTimestamp') is not None:
            self.report_create_timestamp = m.get('ReportCreateTimestamp')
        return self


class GetConfigRulesReportResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        config_rules_report: GetConfigRulesReportResponseBodyConfigRulesReport = None,
    ):
        self.request_id = request_id
        self.config_rules_report = config_rules_report

    def validate(self):
        if self.config_rules_report:
            self.config_rules_report.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.config_rules_report is not None:
            result['ConfigRulesReport'] = self.config_rules_report.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ConfigRulesReport') is not None:
            temp_model = GetConfigRulesReportResponseBodyConfigRulesReport()
            self.config_rules_report = temp_model.from_map(m['ConfigRulesReport'])
        return self


class GetConfigRulesReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetConfigRulesReportResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetConfigRulesReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceConfigurationTimelineRequest(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        start_time: int = None,
        end_time: int = None,
        max_results: int = None,
        resource_type: str = None,
        region: str = None,
        next_token: str = None,
    ):
        self.resource_id = resource_id
        self.start_time = start_time
        self.end_time = end_time
        self.max_results = max_results
        self.resource_type = resource_type
        self.region = region
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.region is not None:
            result['Region'] = self.region
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class GetResourceConfigurationTimelineResponseBodyResourceConfigurationTimelineConfigurationList(TeaModel):
    def __init__(
        self,
        tags: str = None,
        account_id: int = None,
        resource_event_type: str = None,
        availability_zone: str = None,
        resource_type: str = None,
        resource_create_time: str = None,
        region: str = None,
        capture_time: str = None,
        configuration_diff: str = None,
        resource_id: str = None,
        resource_name: str = None,
        relationship: str = None,
        relationship_diff: str = None,
    ):
        self.tags = tags
        self.account_id = account_id
        self.resource_event_type = resource_event_type
        self.availability_zone = availability_zone
        self.resource_type = resource_type
        self.resource_create_time = resource_create_time
        self.region = region
        self.capture_time = capture_time
        self.configuration_diff = configuration_diff
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.relationship = relationship
        self.relationship_diff = relationship_diff

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.resource_event_type is not None:
            result['ResourceEventType'] = self.resource_event_type
        if self.availability_zone is not None:
            result['AvailabilityZone'] = self.availability_zone
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_create_time is not None:
            result['ResourceCreateTime'] = self.resource_create_time
        if self.region is not None:
            result['Region'] = self.region
        if self.capture_time is not None:
            result['CaptureTime'] = self.capture_time
        if self.configuration_diff is not None:
            result['ConfigurationDiff'] = self.configuration_diff
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.relationship is not None:
            result['Relationship'] = self.relationship
        if self.relationship_diff is not None:
            result['RelationshipDiff'] = self.relationship_diff
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ResourceEventType') is not None:
            self.resource_event_type = m.get('ResourceEventType')
        if m.get('AvailabilityZone') is not None:
            self.availability_zone = m.get('AvailabilityZone')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceCreateTime') is not None:
            self.resource_create_time = m.get('ResourceCreateTime')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('CaptureTime') is not None:
            self.capture_time = m.get('CaptureTime')
        if m.get('ConfigurationDiff') is not None:
            self.configuration_diff = m.get('ConfigurationDiff')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('Relationship') is not None:
            self.relationship = m.get('Relationship')
        if m.get('RelationshipDiff') is not None:
            self.relationship_diff = m.get('RelationshipDiff')
        return self


class GetResourceConfigurationTimelineResponseBodyResourceConfigurationTimeline(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        max_results: int = None,
        configuration_list: List[GetResourceConfigurationTimelineResponseBodyResourceConfigurationTimelineConfigurationList] = None,
    ):
        self.next_token = next_token
        self.max_results = max_results
        self.configuration_list = configuration_list

    def validate(self):
        if self.configuration_list:
            for k in self.configuration_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['ConfigurationList'] = []
        if self.configuration_list is not None:
            for k in self.configuration_list:
                result['ConfigurationList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.configuration_list = []
        if m.get('ConfigurationList') is not None:
            for k in m.get('ConfigurationList'):
                temp_model = GetResourceConfigurationTimelineResponseBodyResourceConfigurationTimelineConfigurationList()
                self.configuration_list.append(temp_model.from_map(k))
        return self


class GetResourceConfigurationTimelineResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_configuration_timeline: GetResourceConfigurationTimelineResponseBodyResourceConfigurationTimeline = None,
    ):
        self.request_id = request_id
        self.resource_configuration_timeline = resource_configuration_timeline

    def validate(self):
        if self.resource_configuration_timeline:
            self.resource_configuration_timeline.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_configuration_timeline is not None:
            result['ResourceConfigurationTimeline'] = self.resource_configuration_timeline.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceConfigurationTimeline') is not None:
            temp_model = GetResourceConfigurationTimelineResponseBodyResourceConfigurationTimeline()
            self.resource_configuration_timeline = temp_model.from_map(m['ResourceConfigurationTimeline'])
        return self


class GetResourceConfigurationTimelineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetResourceConfigurationTimelineResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetResourceConfigurationTimelineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDiscoveredResourceCountsGroupByResourceTypeRequest(TeaModel):
    def __init__(
        self,
        region: str = None,
    ):
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class GetDiscoveredResourceCountsGroupByResourceTypeResponseBodyDiscoveredResourceCountsSummary(TeaModel):
    def __init__(
        self,
        resource_count: int = None,
        resource_type: str = None,
    ):
        self.resource_count = resource_count
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_count is not None:
            result['ResourceCount'] = self.resource_count
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceCount') is not None:
            self.resource_count = m.get('ResourceCount')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetDiscoveredResourceCountsGroupByResourceTypeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        discovered_resource_counts_summary: List[GetDiscoveredResourceCountsGroupByResourceTypeResponseBodyDiscoveredResourceCountsSummary] = None,
    ):
        self.request_id = request_id
        self.discovered_resource_counts_summary = discovered_resource_counts_summary

    def validate(self):
        if self.discovered_resource_counts_summary:
            for k in self.discovered_resource_counts_summary:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['DiscoveredResourceCountsSummary'] = []
        if self.discovered_resource_counts_summary is not None:
            for k in self.discovered_resource_counts_summary:
                result['DiscoveredResourceCountsSummary'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.discovered_resource_counts_summary = []
        if m.get('DiscoveredResourceCountsSummary') is not None:
            for k in m.get('DiscoveredResourceCountsSummary'):
                temp_model = GetDiscoveredResourceCountsGroupByResourceTypeResponseBodyDiscoveredResourceCountsSummary()
                self.discovered_resource_counts_summary.append(temp_model.from_map(k))
        return self


class GetDiscoveredResourceCountsGroupByResourceTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDiscoveredResourceCountsGroupByResourceTypeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDiscoveredResourceCountsGroupByResourceTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAggregatorRequestAggregatorAccounts(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        account_name: str = None,
        account_type: str = None,
    ):
        self.account_id = account_id
        self.account_name = account_name
        self.account_type = account_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        return self


class CreateAggregatorRequest(TeaModel):
    def __init__(
        self,
        aggregator_name: str = None,
        description: str = None,
        aggregator_accounts: List[CreateAggregatorRequestAggregatorAccounts] = None,
        client_token: str = None,
        aggregator_type: str = None,
    ):
        self.aggregator_name = aggregator_name
        self.description = description
        self.aggregator_accounts = aggregator_accounts
        self.client_token = client_token
        self.aggregator_type = aggregator_type

    def validate(self):
        if self.aggregator_accounts:
            for k in self.aggregator_accounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_name is not None:
            result['AggregatorName'] = self.aggregator_name
        if self.description is not None:
            result['Description'] = self.description
        result['AggregatorAccounts'] = []
        if self.aggregator_accounts is not None:
            for k in self.aggregator_accounts:
                result['AggregatorAccounts'].append(k.to_map() if k else None)
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.aggregator_type is not None:
            result['AggregatorType'] = self.aggregator_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorName') is not None:
            self.aggregator_name = m.get('AggregatorName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.aggregator_accounts = []
        if m.get('AggregatorAccounts') is not None:
            for k in m.get('AggregatorAccounts'):
                temp_model = CreateAggregatorRequestAggregatorAccounts()
                self.aggregator_accounts.append(temp_model.from_map(k))
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('AggregatorType') is not None:
            self.aggregator_type = m.get('AggregatorType')
        return self


class CreateAggregatorShrinkRequest(TeaModel):
    def __init__(
        self,
        aggregator_name: str = None,
        description: str = None,
        aggregator_accounts_shrink: str = None,
        client_token: str = None,
        aggregator_type: str = None,
    ):
        self.aggregator_name = aggregator_name
        self.description = description
        self.aggregator_accounts_shrink = aggregator_accounts_shrink
        self.client_token = client_token
        self.aggregator_type = aggregator_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_name is not None:
            result['AggregatorName'] = self.aggregator_name
        if self.description is not None:
            result['Description'] = self.description
        if self.aggregator_accounts_shrink is not None:
            result['AggregatorAccounts'] = self.aggregator_accounts_shrink
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.aggregator_type is not None:
            result['AggregatorType'] = self.aggregator_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorName') is not None:
            self.aggregator_name = m.get('AggregatorName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AggregatorAccounts') is not None:
            self.aggregator_accounts_shrink = m.get('AggregatorAccounts')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('AggregatorType') is not None:
            self.aggregator_type = m.get('AggregatorType')
        return self


class CreateAggregatorResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        aggregator_id: str = None,
    ):
        self.request_id = request_id
        self.aggregator_id = aggregator_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        return self


class CreateAggregatorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAggregatorResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAggregatorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAggregateConfigRulesRequest(TeaModel):
    def __init__(
        self,
        config_rule_state: str = None,
        compliance_type: str = None,
        risk_level: int = None,
        config_rule_name: str = None,
        aggregator_id: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.config_rule_state = config_rule_state
        self.compliance_type = compliance_type
        self.risk_level = risk_level
        self.config_rule_name = config_rule_name
        self.aggregator_id = aggregator_id
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_state is not None:
            result['ConfigRuleState'] = self.config_rule_state
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleState') is not None:
            self.config_rule_state = m.get('ConfigRuleState')
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class ListAggregateConfigRulesResponseBodyConfigRulesConfigRuleListCompliance(TeaModel):
    def __init__(
        self,
        compliance_type: str = None,
        count: int = None,
    ):
        self.compliance_type = compliance_type
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class ListAggregateConfigRulesResponseBodyConfigRulesConfigRuleListCreateBy(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        aggregator_name: str = None,
        compliance_pack_name: str = None,
        creator_name: str = None,
        creator_type: str = None,
        creator_id: str = None,
        aggregator_id: str = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.aggregator_name = aggregator_name
        self.compliance_pack_name = compliance_pack_name
        self.creator_name = creator_name
        self.creator_type = creator_type
        self.creator_id = creator_id
        self.aggregator_id = aggregator_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.aggregator_name is not None:
            result['AggregatorName'] = self.aggregator_name
        if self.compliance_pack_name is not None:
            result['CompliancePackName'] = self.compliance_pack_name
        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name
        if self.creator_type is not None:
            result['CreatorType'] = self.creator_type
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('AggregatorName') is not None:
            self.aggregator_name = m.get('AggregatorName')
        if m.get('CompliancePackName') is not None:
            self.compliance_pack_name = m.get('CompliancePackName')
        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')
        if m.get('CreatorType') is not None:
            self.creator_type = m.get('CreatorType')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        return self


class ListAggregateConfigRulesResponseBodyConfigRulesConfigRuleList(TeaModel):
    def __init__(
        self,
        risk_level: int = None,
        source_owner: str = None,
        account_id: int = None,
        config_rule_state: str = None,
        compliance: ListAggregateConfigRulesResponseBodyConfigRulesConfigRuleListCompliance = None,
        source_identifier: str = None,
        config_rule_arn: str = None,
        description: str = None,
        create_by: ListAggregateConfigRulesResponseBodyConfigRulesConfigRuleListCreateBy = None,
        automation_type: str = None,
        config_rule_name: str = None,
        config_rule_id: str = None,
    ):
        self.risk_level = risk_level
        self.source_owner = source_owner
        self.account_id = account_id
        self.config_rule_state = config_rule_state
        self.compliance = compliance
        self.source_identifier = source_identifier
        self.config_rule_arn = config_rule_arn
        self.description = description
        self.create_by = create_by
        self.automation_type = automation_type
        self.config_rule_name = config_rule_name
        self.config_rule_id = config_rule_id

    def validate(self):
        if self.compliance:
            self.compliance.validate()
        if self.create_by:
            self.create_by.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.source_owner is not None:
            result['SourceOwner'] = self.source_owner
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.config_rule_state is not None:
            result['ConfigRuleState'] = self.config_rule_state
        if self.compliance is not None:
            result['Compliance'] = self.compliance.to_map()
        if self.source_identifier is not None:
            result['SourceIdentifier'] = self.source_identifier
        if self.config_rule_arn is not None:
            result['ConfigRuleArn'] = self.config_rule_arn
        if self.description is not None:
            result['Description'] = self.description
        if self.create_by is not None:
            result['CreateBy'] = self.create_by.to_map()
        if self.automation_type is not None:
            result['AutomationType'] = self.automation_type
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('SourceOwner') is not None:
            self.source_owner = m.get('SourceOwner')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ConfigRuleState') is not None:
            self.config_rule_state = m.get('ConfigRuleState')
        if m.get('Compliance') is not None:
            temp_model = ListAggregateConfigRulesResponseBodyConfigRulesConfigRuleListCompliance()
            self.compliance = temp_model.from_map(m['Compliance'])
        if m.get('SourceIdentifier') is not None:
            self.source_identifier = m.get('SourceIdentifier')
        if m.get('ConfigRuleArn') is not None:
            self.config_rule_arn = m.get('ConfigRuleArn')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CreateBy') is not None:
            temp_model = ListAggregateConfigRulesResponseBodyConfigRulesConfigRuleListCreateBy()
            self.create_by = temp_model.from_map(m['CreateBy'])
        if m.get('AutomationType') is not None:
            self.automation_type = m.get('AutomationType')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        return self


class ListAggregateConfigRulesResponseBodyConfigRules(TeaModel):
    def __init__(
        self,
        config_rule_list: List[ListAggregateConfigRulesResponseBodyConfigRulesConfigRuleList] = None,
        page_size: int = None,
        page_number: int = None,
        total_count: int = None,
    ):
        self.config_rule_list = config_rule_list
        self.page_size = page_size
        self.page_number = page_number
        self.total_count = total_count

    def validate(self):
        if self.config_rule_list:
            for k in self.config_rule_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConfigRuleList'] = []
        if self.config_rule_list is not None:
            for k in self.config_rule_list:
                result['ConfigRuleList'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_rule_list = []
        if m.get('ConfigRuleList') is not None:
            for k in m.get('ConfigRuleList'):
                temp_model = ListAggregateConfigRulesResponseBodyConfigRulesConfigRuleList()
                self.config_rule_list.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAggregateConfigRulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        config_rules: ListAggregateConfigRulesResponseBodyConfigRules = None,
    ):
        self.request_id = request_id
        self.config_rules = config_rules

    def validate(self):
        if self.config_rules:
            self.config_rules.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.config_rules is not None:
            result['ConfigRules'] = self.config_rules.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ConfigRules') is not None:
            temp_model = ListAggregateConfigRulesResponseBodyConfigRules()
            self.config_rules = temp_model.from_map(m['ConfigRules'])
        return self


class ListAggregateConfigRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAggregateConfigRulesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAggregateConfigRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateAggregateResourceInventoryRequest(TeaModel):
    def __init__(
        self,
        regions: str = None,
        resource_types: str = None,
        account_ids: str = None,
        aggregator_id: str = None,
    ):
        self.regions = regions
        self.resource_types = resource_types
        self.account_ids = account_ids
        self.aggregator_id = aggregator_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.regions is not None:
            result['Regions'] = self.regions
        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Regions') is not None:
            self.regions = m.get('Regions')
        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        return self


class GenerateAggregateResourceInventoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateAggregateResourceInventoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GenerateAggregateResourceInventoryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GenerateAggregateResourceInventoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAggregateConfigRuleRequest(TeaModel):
    def __init__(
        self,
        config_rule_name: str = None,
        description: str = None,
        input_parameters: Dict[str, Any] = None,
        config_rule_trigger_types: str = None,
        maximum_execution_frequency: str = None,
        resource_types_scope: List[str] = None,
        risk_level: int = None,
        client_token: str = None,
        region_ids_scope: str = None,
        exclude_resource_ids_scope: str = None,
        aggregator_id: str = None,
        resource_group_ids_scope: str = None,
        tag_key_scope: str = None,
        tag_value_scope: str = None,
        source_owner: str = None,
        source_identifier: str = None,
    ):
        self.config_rule_name = config_rule_name
        self.description = description
        self.input_parameters = input_parameters
        self.config_rule_trigger_types = config_rule_trigger_types
        self.maximum_execution_frequency = maximum_execution_frequency
        self.resource_types_scope = resource_types_scope
        self.risk_level = risk_level
        self.client_token = client_token
        self.region_ids_scope = region_ids_scope
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        self.aggregator_id = aggregator_id
        self.resource_group_ids_scope = resource_group_ids_scope
        self.tag_key_scope = tag_key_scope
        self.tag_value_scope = tag_value_scope
        self.source_owner = source_owner
        self.source_identifier = source_identifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        if self.description is not None:
            result['Description'] = self.description
        if self.input_parameters is not None:
            result['InputParameters'] = self.input_parameters
        if self.config_rule_trigger_types is not None:
            result['ConfigRuleTriggerTypes'] = self.config_rule_trigger_types
        if self.maximum_execution_frequency is not None:
            result['MaximumExecutionFrequency'] = self.maximum_execution_frequency
        if self.resource_types_scope is not None:
            result['ResourceTypesScope'] = self.resource_types_scope
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_ids_scope is not None:
            result['RegionIdsScope'] = self.region_ids_scope
        if self.exclude_resource_ids_scope is not None:
            result['ExcludeResourceIdsScope'] = self.exclude_resource_ids_scope
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.resource_group_ids_scope is not None:
            result['ResourceGroupIdsScope'] = self.resource_group_ids_scope
        if self.tag_key_scope is not None:
            result['TagKeyScope'] = self.tag_key_scope
        if self.tag_value_scope is not None:
            result['TagValueScope'] = self.tag_value_scope
        if self.source_owner is not None:
            result['SourceOwner'] = self.source_owner
        if self.source_identifier is not None:
            result['SourceIdentifier'] = self.source_identifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InputParameters') is not None:
            self.input_parameters = m.get('InputParameters')
        if m.get('ConfigRuleTriggerTypes') is not None:
            self.config_rule_trigger_types = m.get('ConfigRuleTriggerTypes')
        if m.get('MaximumExecutionFrequency') is not None:
            self.maximum_execution_frequency = m.get('MaximumExecutionFrequency')
        if m.get('ResourceTypesScope') is not None:
            self.resource_types_scope = m.get('ResourceTypesScope')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionIdsScope') is not None:
            self.region_ids_scope = m.get('RegionIdsScope')
        if m.get('ExcludeResourceIdsScope') is not None:
            self.exclude_resource_ids_scope = m.get('ExcludeResourceIdsScope')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ResourceGroupIdsScope') is not None:
            self.resource_group_ids_scope = m.get('ResourceGroupIdsScope')
        if m.get('TagKeyScope') is not None:
            self.tag_key_scope = m.get('TagKeyScope')
        if m.get('TagValueScope') is not None:
            self.tag_value_scope = m.get('TagValueScope')
        if m.get('SourceOwner') is not None:
            self.source_owner = m.get('SourceOwner')
        if m.get('SourceIdentifier') is not None:
            self.source_identifier = m.get('SourceIdentifier')
        return self


class CreateAggregateConfigRuleShrinkRequest(TeaModel):
    def __init__(
        self,
        config_rule_name: str = None,
        description: str = None,
        input_parameters_shrink: str = None,
        config_rule_trigger_types: str = None,
        maximum_execution_frequency: str = None,
        resource_types_scope_shrink: str = None,
        risk_level: int = None,
        client_token: str = None,
        region_ids_scope: str = None,
        exclude_resource_ids_scope: str = None,
        aggregator_id: str = None,
        resource_group_ids_scope: str = None,
        tag_key_scope: str = None,
        tag_value_scope: str = None,
        source_owner: str = None,
        source_identifier: str = None,
    ):
        self.config_rule_name = config_rule_name
        self.description = description
        self.input_parameters_shrink = input_parameters_shrink
        self.config_rule_trigger_types = config_rule_trigger_types
        self.maximum_execution_frequency = maximum_execution_frequency
        self.resource_types_scope_shrink = resource_types_scope_shrink
        self.risk_level = risk_level
        self.client_token = client_token
        self.region_ids_scope = region_ids_scope
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        self.aggregator_id = aggregator_id
        self.resource_group_ids_scope = resource_group_ids_scope
        self.tag_key_scope = tag_key_scope
        self.tag_value_scope = tag_value_scope
        self.source_owner = source_owner
        self.source_identifier = source_identifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        if self.description is not None:
            result['Description'] = self.description
        if self.input_parameters_shrink is not None:
            result['InputParameters'] = self.input_parameters_shrink
        if self.config_rule_trigger_types is not None:
            result['ConfigRuleTriggerTypes'] = self.config_rule_trigger_types
        if self.maximum_execution_frequency is not None:
            result['MaximumExecutionFrequency'] = self.maximum_execution_frequency
        if self.resource_types_scope_shrink is not None:
            result['ResourceTypesScope'] = self.resource_types_scope_shrink
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_ids_scope is not None:
            result['RegionIdsScope'] = self.region_ids_scope
        if self.exclude_resource_ids_scope is not None:
            result['ExcludeResourceIdsScope'] = self.exclude_resource_ids_scope
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.resource_group_ids_scope is not None:
            result['ResourceGroupIdsScope'] = self.resource_group_ids_scope
        if self.tag_key_scope is not None:
            result['TagKeyScope'] = self.tag_key_scope
        if self.tag_value_scope is not None:
            result['TagValueScope'] = self.tag_value_scope
        if self.source_owner is not None:
            result['SourceOwner'] = self.source_owner
        if self.source_identifier is not None:
            result['SourceIdentifier'] = self.source_identifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InputParameters') is not None:
            self.input_parameters_shrink = m.get('InputParameters')
        if m.get('ConfigRuleTriggerTypes') is not None:
            self.config_rule_trigger_types = m.get('ConfigRuleTriggerTypes')
        if m.get('MaximumExecutionFrequency') is not None:
            self.maximum_execution_frequency = m.get('MaximumExecutionFrequency')
        if m.get('ResourceTypesScope') is not None:
            self.resource_types_scope_shrink = m.get('ResourceTypesScope')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionIdsScope') is not None:
            self.region_ids_scope = m.get('RegionIdsScope')
        if m.get('ExcludeResourceIdsScope') is not None:
            self.exclude_resource_ids_scope = m.get('ExcludeResourceIdsScope')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ResourceGroupIdsScope') is not None:
            self.resource_group_ids_scope = m.get('ResourceGroupIdsScope')
        if m.get('TagKeyScope') is not None:
            self.tag_key_scope = m.get('TagKeyScope')
        if m.get('TagValueScope') is not None:
            self.tag_value_scope = m.get('TagValueScope')
        if m.get('SourceOwner') is not None:
            self.source_owner = m.get('SourceOwner')
        if m.get('SourceIdentifier') is not None:
            self.source_identifier = m.get('SourceIdentifier')
        return self


class CreateAggregateConfigRuleResponseBody(TeaModel):
    def __init__(
        self,
        config_rule_id: str = None,
        request_id: str = None,
    ):
        self.config_rule_id = config_rule_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAggregateConfigRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAggregateConfigRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAggregateConfigRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAggregateRemediationRequest(TeaModel):
    def __init__(
        self,
        config_rule_id: str = None,
        remediation_type: str = None,
        remediation_template_id: str = None,
        invoke_type: str = None,
        source_type: str = None,
        params: str = None,
        aggregator_id: str = None,
        client_token: str = None,
    ):
        self.config_rule_id = config_rule_id
        self.remediation_type = remediation_type
        self.remediation_template_id = remediation_template_id
        self.invoke_type = invoke_type
        self.source_type = source_type
        self.params = params
        self.aggregator_id = aggregator_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.remediation_type is not None:
            result['RemediationType'] = self.remediation_type
        if self.remediation_template_id is not None:
            result['RemediationTemplateId'] = self.remediation_template_id
        if self.invoke_type is not None:
            result['InvokeType'] = self.invoke_type
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.params is not None:
            result['Params'] = self.params
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('RemediationType') is not None:
            self.remediation_type = m.get('RemediationType')
        if m.get('RemediationTemplateId') is not None:
            self.remediation_template_id = m.get('RemediationTemplateId')
        if m.get('InvokeType') is not None:
            self.invoke_type = m.get('InvokeType')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateAggregateRemediationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        remediation_id: str = None,
    ):
        self.request_id = request_id
        self.remediation_id = remediation_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.remediation_id is not None:
            result['RemediationId'] = self.remediation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RemediationId') is not None:
            self.remediation_id = m.get('RemediationId')
        return self


class CreateAggregateRemediationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAggregateRemediationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAggregateRemediationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartAggregateConfigRuleEvaluationRequest(TeaModel):
    def __init__(
        self,
        config_rule_id: str = None,
        aggregator_id: str = None,
    ):
        self.config_rule_id = config_rule_id
        self.aggregator_id = aggregator_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        return self


class StartAggregateConfigRuleEvaluationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class StartAggregateConfigRuleEvaluationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartAggregateConfigRuleEvaluationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartAggregateConfigRuleEvaluationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateAggregateCompliancePackReportRequest(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        client_token: str = None,
        aggregator_id: str = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.client_token = client_token
        self.aggregator_id = aggregator_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        return self


class GenerateAggregateCompliancePackReportResponseBody(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        request_id: str = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateAggregateCompliancePackReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GenerateAggregateCompliancePackReportResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GenerateAggregateCompliancePackReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCompliancePackReportRequest(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
    ):
        self.compliance_pack_id = compliance_pack_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        return self


class GetCompliancePackReportResponseBodyCompliancePackReport(TeaModel):
    def __init__(
        self,
        report_url: str = None,
        report_status: str = None,
        compliance_pack_id: str = None,
        account_id: int = None,
        report_create_timestamp: int = None,
    ):
        self.report_url = report_url
        self.report_status = report_status
        self.compliance_pack_id = compliance_pack_id
        self.account_id = account_id
        self.report_create_timestamp = report_create_timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.report_url is not None:
            result['ReportUrl'] = self.report_url
        if self.report_status is not None:
            result['ReportStatus'] = self.report_status
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.report_create_timestamp is not None:
            result['ReportCreateTimestamp'] = self.report_create_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReportUrl') is not None:
            self.report_url = m.get('ReportUrl')
        if m.get('ReportStatus') is not None:
            self.report_status = m.get('ReportStatus')
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ReportCreateTimestamp') is not None:
            self.report_create_timestamp = m.get('ReportCreateTimestamp')
        return self


class GetCompliancePackReportResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        compliance_pack_report: GetCompliancePackReportResponseBodyCompliancePackReport = None,
    ):
        self.request_id = request_id
        self.compliance_pack_report = compliance_pack_report

    def validate(self):
        if self.compliance_pack_report:
            self.compliance_pack_report.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.compliance_pack_report is not None:
            result['CompliancePackReport'] = self.compliance_pack_report.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CompliancePackReport') is not None:
            temp_model = GetCompliancePackReportResponseBodyCompliancePackReport()
            self.compliance_pack_report = temp_model.from_map(m['CompliancePackReport'])
        return self


class GetCompliancePackReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetCompliancePackReportResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetCompliancePackReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceComplianceByConfigRuleRequest(TeaModel):
    def __init__(
        self,
        compliance_type: str = None,
        config_rule_id: str = None,
    ):
        self.compliance_type = compliance_type
        self.config_rule_id = config_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        return self


class GetResourceComplianceByConfigRuleResponseBodyComplianceResultCompliances(TeaModel):
    def __init__(
        self,
        compliance_type: str = None,
        count: int = None,
    ):
        self.compliance_type = compliance_type
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class GetResourceComplianceByConfigRuleResponseBodyComplianceResult(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        compliances: List[GetResourceComplianceByConfigRuleResponseBodyComplianceResultCompliances] = None,
    ):
        self.total_count = total_count
        self.compliances = compliances

    def validate(self):
        if self.compliances:
            for k in self.compliances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Compliances'] = []
        if self.compliances is not None:
            for k in self.compliances:
                result['Compliances'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.compliances = []
        if m.get('Compliances') is not None:
            for k in m.get('Compliances'):
                temp_model = GetResourceComplianceByConfigRuleResponseBodyComplianceResultCompliances()
                self.compliances.append(temp_model.from_map(k))
        return self


class GetResourceComplianceByConfigRuleResponseBody(TeaModel):
    def __init__(
        self,
        compliance_result: GetResourceComplianceByConfigRuleResponseBodyComplianceResult = None,
        request_id: str = None,
    ):
        self.compliance_result = compliance_result
        self.request_id = request_id

    def validate(self):
        if self.compliance_result:
            self.compliance_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_result is not None:
            result['ComplianceResult'] = self.compliance_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceResult') is not None:
            temp_model = GetResourceComplianceByConfigRuleResponseBodyComplianceResult()
            self.compliance_result = temp_model.from_map(m['ComplianceResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetResourceComplianceByConfigRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetResourceComplianceByConfigRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetResourceComplianceByConfigRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceEvaluationResultsRequest(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        resource_id: str = None,
        compliance_type: str = None,
        next_token: str = None,
        max_results: int = None,
        region: str = None,
    ):
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.compliance_type = compliance_type
        self.next_token = next_token
        self.max_results = max_results
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class ListResourceEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifierEvaluationResultQualifier(TeaModel):
    def __init__(
        self,
        config_rule_arn: str = None,
        resource_type: str = None,
        config_rule_name: str = None,
        resource_id: str = None,
        config_rule_id: str = None,
        resource_name: str = None,
        region_id: str = None,
    ):
        self.config_rule_arn = config_rule_arn
        self.resource_type = resource_type
        self.config_rule_name = config_rule_name
        self.resource_id = resource_id
        self.config_rule_id = config_rule_id
        self.resource_name = resource_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_arn is not None:
            result['ConfigRuleArn'] = self.config_rule_arn
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleArn') is not None:
            self.config_rule_arn = m.get('ConfigRuleArn')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListResourceEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifier(TeaModel):
    def __init__(
        self,
        ordering_timestamp: int = None,
        evaluation_result_qualifier: ListResourceEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifierEvaluationResultQualifier = None,
    ):
        self.ordering_timestamp = ordering_timestamp
        self.evaluation_result_qualifier = evaluation_result_qualifier

    def validate(self):
        if self.evaluation_result_qualifier:
            self.evaluation_result_qualifier.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ordering_timestamp is not None:
            result['OrderingTimestamp'] = self.ordering_timestamp
        if self.evaluation_result_qualifier is not None:
            result['EvaluationResultQualifier'] = self.evaluation_result_qualifier.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderingTimestamp') is not None:
            self.ordering_timestamp = m.get('OrderingTimestamp')
        if m.get('EvaluationResultQualifier') is not None:
            temp_model = ListResourceEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifierEvaluationResultQualifier()
            self.evaluation_result_qualifier = temp_model.from_map(m['EvaluationResultQualifier'])
        return self


class ListResourceEvaluationResultsResponseBodyEvaluationResultsEvaluationResultList(TeaModel):
    def __init__(
        self,
        risk_level: int = None,
        compliance_type: str = None,
        result_recorded_timestamp: int = None,
        annotation: str = None,
        config_rule_invoked_timestamp: int = None,
        invoking_event_message_type: str = None,
        evaluation_result_identifier: ListResourceEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifier = None,
        remediation_enabled: bool = None,
    ):
        self.risk_level = risk_level
        self.compliance_type = compliance_type
        self.result_recorded_timestamp = result_recorded_timestamp
        self.annotation = annotation
        self.config_rule_invoked_timestamp = config_rule_invoked_timestamp
        self.invoking_event_message_type = invoking_event_message_type
        self.evaluation_result_identifier = evaluation_result_identifier
        self.remediation_enabled = remediation_enabled

    def validate(self):
        if self.evaluation_result_identifier:
            self.evaluation_result_identifier.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.result_recorded_timestamp is not None:
            result['ResultRecordedTimestamp'] = self.result_recorded_timestamp
        if self.annotation is not None:
            result['Annotation'] = self.annotation
        if self.config_rule_invoked_timestamp is not None:
            result['ConfigRuleInvokedTimestamp'] = self.config_rule_invoked_timestamp
        if self.invoking_event_message_type is not None:
            result['InvokingEventMessageType'] = self.invoking_event_message_type
        if self.evaluation_result_identifier is not None:
            result['EvaluationResultIdentifier'] = self.evaluation_result_identifier.to_map()
        if self.remediation_enabled is not None:
            result['RemediationEnabled'] = self.remediation_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('ResultRecordedTimestamp') is not None:
            self.result_recorded_timestamp = m.get('ResultRecordedTimestamp')
        if m.get('Annotation') is not None:
            self.annotation = m.get('Annotation')
        if m.get('ConfigRuleInvokedTimestamp') is not None:
            self.config_rule_invoked_timestamp = m.get('ConfigRuleInvokedTimestamp')
        if m.get('InvokingEventMessageType') is not None:
            self.invoking_event_message_type = m.get('InvokingEventMessageType')
        if m.get('EvaluationResultIdentifier') is not None:
            temp_model = ListResourceEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifier()
            self.evaluation_result_identifier = temp_model.from_map(m['EvaluationResultIdentifier'])
        if m.get('RemediationEnabled') is not None:
            self.remediation_enabled = m.get('RemediationEnabled')
        return self


class ListResourceEvaluationResultsResponseBodyEvaluationResults(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        max_results: int = None,
        evaluation_result_list: List[ListResourceEvaluationResultsResponseBodyEvaluationResultsEvaluationResultList] = None,
    ):
        self.next_token = next_token
        self.max_results = max_results
        self.evaluation_result_list = evaluation_result_list

    def validate(self):
        if self.evaluation_result_list:
            for k in self.evaluation_result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['EvaluationResultList'] = []
        if self.evaluation_result_list is not None:
            for k in self.evaluation_result_list:
                result['EvaluationResultList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.evaluation_result_list = []
        if m.get('EvaluationResultList') is not None:
            for k in m.get('EvaluationResultList'):
                temp_model = ListResourceEvaluationResultsResponseBodyEvaluationResultsEvaluationResultList()
                self.evaluation_result_list.append(temp_model.from_map(k))
        return self


class ListResourceEvaluationResultsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        evaluation_results: ListResourceEvaluationResultsResponseBodyEvaluationResults = None,
    ):
        self.request_id = request_id
        self.evaluation_results = evaluation_results

    def validate(self):
        if self.evaluation_results:
            self.evaluation_results.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.evaluation_results is not None:
            result['EvaluationResults'] = self.evaluation_results.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('EvaluationResults') is not None:
            temp_model = ListResourceEvaluationResultsResponseBodyEvaluationResults()
            self.evaluation_results = temp_model.from_map(m['EvaluationResults'])
        return self


class ListResourceEvaluationResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListResourceEvaluationResultsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListResourceEvaluationResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCompliancePackRequestConfigRulesConfigRuleParameters(TeaModel):
    def __init__(
        self,
        parameter_name: str = None,
        parameter_value: str = None,
    ):
        self.parameter_name = parameter_name
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class UpdateCompliancePackRequestConfigRules(TeaModel):
    def __init__(
        self,
        managed_rule_identifier: str = None,
        config_rule_parameters: List[UpdateCompliancePackRequestConfigRulesConfigRuleParameters] = None,
        config_rule_id: str = None,
        config_rule_name: str = None,
        description: str = None,
        risk_level: int = None,
    ):
        self.managed_rule_identifier = managed_rule_identifier
        self.config_rule_parameters = config_rule_parameters
        self.config_rule_id = config_rule_id
        self.config_rule_name = config_rule_name
        self.description = description
        self.risk_level = risk_level

    def validate(self):
        if self.config_rule_parameters:
            for k in self.config_rule_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.managed_rule_identifier is not None:
            result['ManagedRuleIdentifier'] = self.managed_rule_identifier
        result['ConfigRuleParameters'] = []
        if self.config_rule_parameters is not None:
            for k in self.config_rule_parameters:
                result['ConfigRuleParameters'].append(k.to_map() if k else None)
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        if self.description is not None:
            result['Description'] = self.description
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ManagedRuleIdentifier') is not None:
            self.managed_rule_identifier = m.get('ManagedRuleIdentifier')
        self.config_rule_parameters = []
        if m.get('ConfigRuleParameters') is not None:
            for k in m.get('ConfigRuleParameters'):
                temp_model = UpdateCompliancePackRequestConfigRulesConfigRuleParameters()
                self.config_rule_parameters.append(temp_model.from_map(k))
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        return self


class UpdateCompliancePackRequest(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        description: str = None,
        risk_level: int = None,
        config_rules: List[UpdateCompliancePackRequestConfigRules] = None,
        client_token: str = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.description = description
        self.risk_level = risk_level
        self.config_rules = config_rules
        self.client_token = client_token

    def validate(self):
        if self.config_rules:
            for k in self.config_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.description is not None:
            result['Description'] = self.description
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        result['ConfigRules'] = []
        if self.config_rules is not None:
            for k in self.config_rules:
                result['ConfigRules'].append(k.to_map() if k else None)
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        self.config_rules = []
        if m.get('ConfigRules') is not None:
            for k in m.get('ConfigRules'):
                temp_model = UpdateCompliancePackRequestConfigRules()
                self.config_rules.append(temp_model.from_map(k))
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class UpdateCompliancePackShrinkRequest(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        description: str = None,
        risk_level: int = None,
        config_rules_shrink: str = None,
        client_token: str = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.description = description
        self.risk_level = risk_level
        self.config_rules_shrink = config_rules_shrink
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.description is not None:
            result['Description'] = self.description
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.config_rules_shrink is not None:
            result['ConfigRules'] = self.config_rules_shrink
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('ConfigRules') is not None:
            self.config_rules_shrink = m.get('ConfigRules')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class UpdateCompliancePackResponseBody(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        request_id: str = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateCompliancePackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateCompliancePackResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateCompliancePackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAggregateResourceEvaluationResultsRequest(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        resource_id: str = None,
        compliance_type: str = None,
        next_token: str = None,
        max_results: int = None,
        region: str = None,
        aggregator_id: str = None,
    ):
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.compliance_type = compliance_type
        self.next_token = next_token
        self.max_results = max_results
        self.region = region
        self.aggregator_id = aggregator_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.region is not None:
            result['Region'] = self.region
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        return self


class ListAggregateResourceEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifierEvaluationResultQualifier(TeaModel):
    def __init__(
        self,
        config_rule_arn: str = None,
        resource_type: str = None,
        config_rule_name: str = None,
        resource_id: str = None,
        config_rule_id: str = None,
        resource_name: str = None,
        region_id: str = None,
    ):
        self.config_rule_arn = config_rule_arn
        self.resource_type = resource_type
        self.config_rule_name = config_rule_name
        self.resource_id = resource_id
        self.config_rule_id = config_rule_id
        self.resource_name = resource_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_arn is not None:
            result['ConfigRuleArn'] = self.config_rule_arn
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleArn') is not None:
            self.config_rule_arn = m.get('ConfigRuleArn')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListAggregateResourceEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifier(TeaModel):
    def __init__(
        self,
        ordering_timestamp: int = None,
        evaluation_result_qualifier: ListAggregateResourceEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifierEvaluationResultQualifier = None,
    ):
        self.ordering_timestamp = ordering_timestamp
        self.evaluation_result_qualifier = evaluation_result_qualifier

    def validate(self):
        if self.evaluation_result_qualifier:
            self.evaluation_result_qualifier.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ordering_timestamp is not None:
            result['OrderingTimestamp'] = self.ordering_timestamp
        if self.evaluation_result_qualifier is not None:
            result['EvaluationResultQualifier'] = self.evaluation_result_qualifier.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderingTimestamp') is not None:
            self.ordering_timestamp = m.get('OrderingTimestamp')
        if m.get('EvaluationResultQualifier') is not None:
            temp_model = ListAggregateResourceEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifierEvaluationResultQualifier()
            self.evaluation_result_qualifier = temp_model.from_map(m['EvaluationResultQualifier'])
        return self


class ListAggregateResourceEvaluationResultsResponseBodyEvaluationResultsEvaluationResultList(TeaModel):
    def __init__(
        self,
        risk_level: int = None,
        compliance_type: str = None,
        result_recorded_timestamp: int = None,
        annotation: str = None,
        config_rule_invoked_timestamp: int = None,
        invoking_event_message_type: str = None,
        evaluation_result_identifier: ListAggregateResourceEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifier = None,
        remediation_enabled: bool = None,
    ):
        self.risk_level = risk_level
        self.compliance_type = compliance_type
        self.result_recorded_timestamp = result_recorded_timestamp
        self.annotation = annotation
        self.config_rule_invoked_timestamp = config_rule_invoked_timestamp
        self.invoking_event_message_type = invoking_event_message_type
        self.evaluation_result_identifier = evaluation_result_identifier
        self.remediation_enabled = remediation_enabled

    def validate(self):
        if self.evaluation_result_identifier:
            self.evaluation_result_identifier.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.result_recorded_timestamp is not None:
            result['ResultRecordedTimestamp'] = self.result_recorded_timestamp
        if self.annotation is not None:
            result['Annotation'] = self.annotation
        if self.config_rule_invoked_timestamp is not None:
            result['ConfigRuleInvokedTimestamp'] = self.config_rule_invoked_timestamp
        if self.invoking_event_message_type is not None:
            result['InvokingEventMessageType'] = self.invoking_event_message_type
        if self.evaluation_result_identifier is not None:
            result['EvaluationResultIdentifier'] = self.evaluation_result_identifier.to_map()
        if self.remediation_enabled is not None:
            result['RemediationEnabled'] = self.remediation_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('ResultRecordedTimestamp') is not None:
            self.result_recorded_timestamp = m.get('ResultRecordedTimestamp')
        if m.get('Annotation') is not None:
            self.annotation = m.get('Annotation')
        if m.get('ConfigRuleInvokedTimestamp') is not None:
            self.config_rule_invoked_timestamp = m.get('ConfigRuleInvokedTimestamp')
        if m.get('InvokingEventMessageType') is not None:
            self.invoking_event_message_type = m.get('InvokingEventMessageType')
        if m.get('EvaluationResultIdentifier') is not None:
            temp_model = ListAggregateResourceEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifier()
            self.evaluation_result_identifier = temp_model.from_map(m['EvaluationResultIdentifier'])
        if m.get('RemediationEnabled') is not None:
            self.remediation_enabled = m.get('RemediationEnabled')
        return self


class ListAggregateResourceEvaluationResultsResponseBodyEvaluationResults(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        max_results: int = None,
        evaluation_result_list: List[ListAggregateResourceEvaluationResultsResponseBodyEvaluationResultsEvaluationResultList] = None,
    ):
        self.next_token = next_token
        self.max_results = max_results
        self.evaluation_result_list = evaluation_result_list

    def validate(self):
        if self.evaluation_result_list:
            for k in self.evaluation_result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['EvaluationResultList'] = []
        if self.evaluation_result_list is not None:
            for k in self.evaluation_result_list:
                result['EvaluationResultList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.evaluation_result_list = []
        if m.get('EvaluationResultList') is not None:
            for k in m.get('EvaluationResultList'):
                temp_model = ListAggregateResourceEvaluationResultsResponseBodyEvaluationResultsEvaluationResultList()
                self.evaluation_result_list.append(temp_model.from_map(k))
        return self


class ListAggregateResourceEvaluationResultsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        evaluation_results: ListAggregateResourceEvaluationResultsResponseBodyEvaluationResults = None,
    ):
        self.request_id = request_id
        self.evaluation_results = evaluation_results

    def validate(self):
        if self.evaluation_results:
            self.evaluation_results.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.evaluation_results is not None:
            result['EvaluationResults'] = self.evaluation_results.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('EvaluationResults') is not None:
            temp_model = ListAggregateResourceEvaluationResultsResponseBodyEvaluationResults()
            self.evaluation_results = temp_model.from_map(m['EvaluationResults'])
        return self


class ListAggregateResourceEvaluationResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAggregateResourceEvaluationResultsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAggregateResourceEvaluationResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConfigRuleRequest(TeaModel):
    def __init__(
        self,
        config_rule_id: str = None,
    ):
        self.config_rule_id = config_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        return self


class GetConfigRuleResponseBodyConfigRuleSourceSourceDetails(TeaModel):
    def __init__(
        self,
        message_type: str = None,
        event_source: str = None,
        maximum_execution_frequency: str = None,
    ):
        self.message_type = message_type
        self.event_source = event_source
        self.maximum_execution_frequency = maximum_execution_frequency

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        if self.event_source is not None:
            result['EventSource'] = self.event_source
        if self.maximum_execution_frequency is not None:
            result['MaximumExecutionFrequency'] = self.maximum_execution_frequency
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        if m.get('EventSource') is not None:
            self.event_source = m.get('EventSource')
        if m.get('MaximumExecutionFrequency') is not None:
            self.maximum_execution_frequency = m.get('MaximumExecutionFrequency')
        return self


class GetConfigRuleResponseBodyConfigRuleSource(TeaModel):
    def __init__(
        self,
        source_details: List[GetConfigRuleResponseBodyConfigRuleSourceSourceDetails] = None,
        owner: str = None,
        identifier: str = None,
    ):
        self.source_details = source_details
        self.owner = owner
        self.identifier = identifier

    def validate(self):
        if self.source_details:
            for k in self.source_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SourceDetails'] = []
        if self.source_details is not None:
            for k in self.source_details:
                result['SourceDetails'].append(k.to_map() if k else None)
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.source_details = []
        if m.get('SourceDetails') is not None:
            for k in m.get('SourceDetails'):
                temp_model = GetConfigRuleResponseBodyConfigRuleSourceSourceDetails()
                self.source_details.append(temp_model.from_map(k))
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        return self


class GetConfigRuleResponseBodyConfigRuleManagedRuleSourceDetails(TeaModel):
    def __init__(
        self,
        message_type: str = None,
        event_source: str = None,
        maximum_execution_frequency: str = None,
    ):
        self.message_type = message_type
        self.event_source = event_source
        self.maximum_execution_frequency = maximum_execution_frequency

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        if self.event_source is not None:
            result['EventSource'] = self.event_source
        if self.maximum_execution_frequency is not None:
            result['MaximumExecutionFrequency'] = self.maximum_execution_frequency
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        if m.get('EventSource') is not None:
            self.event_source = m.get('EventSource')
        if m.get('MaximumExecutionFrequency') is not None:
            self.maximum_execution_frequency = m.get('MaximumExecutionFrequency')
        return self


class GetConfigRuleResponseBodyConfigRuleManagedRule(TeaModel):
    def __init__(
        self,
        source_details: List[GetConfigRuleResponseBodyConfigRuleManagedRuleSourceDetails] = None,
        description: str = None,
        labels: List[str] = None,
        identifier: str = None,
        optional_input_parameter_details: Dict[str, Any] = None,
        managed_rule_name: str = None,
        compulsory_input_parameter_details: Dict[str, Any] = None,
    ):
        self.source_details = source_details
        self.description = description
        self.labels = labels
        self.identifier = identifier
        self.optional_input_parameter_details = optional_input_parameter_details
        self.managed_rule_name = managed_rule_name
        self.compulsory_input_parameter_details = compulsory_input_parameter_details

    def validate(self):
        if self.source_details:
            for k in self.source_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SourceDetails'] = []
        if self.source_details is not None:
            for k in self.source_details:
                result['SourceDetails'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.optional_input_parameter_details is not None:
            result['OptionalInputParameterDetails'] = self.optional_input_parameter_details
        if self.managed_rule_name is not None:
            result['ManagedRuleName'] = self.managed_rule_name
        if self.compulsory_input_parameter_details is not None:
            result['CompulsoryInputParameterDetails'] = self.compulsory_input_parameter_details
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.source_details = []
        if m.get('SourceDetails') is not None:
            for k in m.get('SourceDetails'):
                temp_model = GetConfigRuleResponseBodyConfigRuleManagedRuleSourceDetails()
                self.source_details.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('OptionalInputParameterDetails') is not None:
            self.optional_input_parameter_details = m.get('OptionalInputParameterDetails')
        if m.get('ManagedRuleName') is not None:
            self.managed_rule_name = m.get('ManagedRuleName')
        if m.get('CompulsoryInputParameterDetails') is not None:
            self.compulsory_input_parameter_details = m.get('CompulsoryInputParameterDetails')
        return self


class GetConfigRuleResponseBodyConfigRuleCreateBy(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        compliance_pack_name: str = None,
        creator_name: str = None,
        creator_id: str = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.compliance_pack_name = compliance_pack_name
        self.creator_name = creator_name
        self.creator_id = creator_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.compliance_pack_name is not None:
            result['CompliancePackName'] = self.compliance_pack_name
        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('CompliancePackName') is not None:
            self.compliance_pack_name = m.get('CompliancePackName')
        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        return self


class GetConfigRuleResponseBodyConfigRuleConfigRuleEvaluationStatus(TeaModel):
    def __init__(
        self,
        last_error_code: str = None,
        last_successful_evaluation_timestamp: int = None,
        first_activated_timestamp: int = None,
        first_evaluation_started: bool = None,
        last_successful_invocation_timestamp: int = None,
        last_error_message: str = None,
        last_failed_evaluation_timestamp: int = None,
        last_failed_invocation_timestamp: int = None,
    ):
        self.last_error_code = last_error_code
        self.last_successful_evaluation_timestamp = last_successful_evaluation_timestamp
        self.first_activated_timestamp = first_activated_timestamp
        self.first_evaluation_started = first_evaluation_started
        self.last_successful_invocation_timestamp = last_successful_invocation_timestamp
        self.last_error_message = last_error_message
        self.last_failed_evaluation_timestamp = last_failed_evaluation_timestamp
        self.last_failed_invocation_timestamp = last_failed_invocation_timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_error_code is not None:
            result['LastErrorCode'] = self.last_error_code
        if self.last_successful_evaluation_timestamp is not None:
            result['LastSuccessfulEvaluationTimestamp'] = self.last_successful_evaluation_timestamp
        if self.first_activated_timestamp is not None:
            result['FirstActivatedTimestamp'] = self.first_activated_timestamp
        if self.first_evaluation_started is not None:
            result['FirstEvaluationStarted'] = self.first_evaluation_started
        if self.last_successful_invocation_timestamp is not None:
            result['LastSuccessfulInvocationTimestamp'] = self.last_successful_invocation_timestamp
        if self.last_error_message is not None:
            result['LastErrorMessage'] = self.last_error_message
        if self.last_failed_evaluation_timestamp is not None:
            result['LastFailedEvaluationTimestamp'] = self.last_failed_evaluation_timestamp
        if self.last_failed_invocation_timestamp is not None:
            result['LastFailedInvocationTimestamp'] = self.last_failed_invocation_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastErrorCode') is not None:
            self.last_error_code = m.get('LastErrorCode')
        if m.get('LastSuccessfulEvaluationTimestamp') is not None:
            self.last_successful_evaluation_timestamp = m.get('LastSuccessfulEvaluationTimestamp')
        if m.get('FirstActivatedTimestamp') is not None:
            self.first_activated_timestamp = m.get('FirstActivatedTimestamp')
        if m.get('FirstEvaluationStarted') is not None:
            self.first_evaluation_started = m.get('FirstEvaluationStarted')
        if m.get('LastSuccessfulInvocationTimestamp') is not None:
            self.last_successful_invocation_timestamp = m.get('LastSuccessfulInvocationTimestamp')
        if m.get('LastErrorMessage') is not None:
            self.last_error_message = m.get('LastErrorMessage')
        if m.get('LastFailedEvaluationTimestamp') is not None:
            self.last_failed_evaluation_timestamp = m.get('LastFailedEvaluationTimestamp')
        if m.get('LastFailedInvocationTimestamp') is not None:
            self.last_failed_invocation_timestamp = m.get('LastFailedInvocationTimestamp')
        return self


class GetConfigRuleResponseBodyConfigRule(TeaModel):
    def __init__(
        self,
        risk_level: int = None,
        input_parameters: Dict[str, Any] = None,
        source: GetConfigRuleResponseBodyConfigRuleSource = None,
        config_rule_state: str = None,
        maximum_execution_frequency: str = None,
        managed_rule: GetConfigRuleResponseBodyConfigRuleManagedRule = None,
        config_rule_arn: str = None,
        description: str = None,
        create_by: GetConfigRuleResponseBodyConfigRuleCreateBy = None,
        config_rule_name: str = None,
        config_rule_evaluation_status: GetConfigRuleResponseBodyConfigRuleConfigRuleEvaluationStatus = None,
        config_rule_id: str = None,
        modified_timestamp: int = None,
        create_timestamp: int = None,
        resource_types_scope: str = None,
        region_ids_scope: str = None,
        exclude_resource_ids_scope: str = None,
        resource_group_ids_scope: str = None,
        tag_key_scope: str = None,
        tag_value_scope: str = None,
        config_rule_trigger_types: str = None,
    ):
        self.risk_level = risk_level
        self.input_parameters = input_parameters
        self.source = source
        self.config_rule_state = config_rule_state
        self.maximum_execution_frequency = maximum_execution_frequency
        self.managed_rule = managed_rule
        self.config_rule_arn = config_rule_arn
        self.description = description
        self.create_by = create_by
        self.config_rule_name = config_rule_name
        self.config_rule_evaluation_status = config_rule_evaluation_status
        self.config_rule_id = config_rule_id
        self.modified_timestamp = modified_timestamp
        self.create_timestamp = create_timestamp
        self.resource_types_scope = resource_types_scope
        self.region_ids_scope = region_ids_scope
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        self.resource_group_ids_scope = resource_group_ids_scope
        self.tag_key_scope = tag_key_scope
        self.tag_value_scope = tag_value_scope
        self.config_rule_trigger_types = config_rule_trigger_types

    def validate(self):
        if self.source:
            self.source.validate()
        if self.managed_rule:
            self.managed_rule.validate()
        if self.create_by:
            self.create_by.validate()
        if self.config_rule_evaluation_status:
            self.config_rule_evaluation_status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.input_parameters is not None:
            result['InputParameters'] = self.input_parameters
        if self.source is not None:
            result['Source'] = self.source.to_map()
        if self.config_rule_state is not None:
            result['ConfigRuleState'] = self.config_rule_state
        if self.maximum_execution_frequency is not None:
            result['MaximumExecutionFrequency'] = self.maximum_execution_frequency
        if self.managed_rule is not None:
            result['ManagedRule'] = self.managed_rule.to_map()
        if self.config_rule_arn is not None:
            result['ConfigRuleArn'] = self.config_rule_arn
        if self.description is not None:
            result['Description'] = self.description
        if self.create_by is not None:
            result['CreateBy'] = self.create_by.to_map()
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        if self.config_rule_evaluation_status is not None:
            result['ConfigRuleEvaluationStatus'] = self.config_rule_evaluation_status.to_map()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.modified_timestamp is not None:
            result['ModifiedTimestamp'] = self.modified_timestamp
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.resource_types_scope is not None:
            result['ResourceTypesScope'] = self.resource_types_scope
        if self.region_ids_scope is not None:
            result['RegionIdsScope'] = self.region_ids_scope
        if self.exclude_resource_ids_scope is not None:
            result['ExcludeResourceIdsScope'] = self.exclude_resource_ids_scope
        if self.resource_group_ids_scope is not None:
            result['ResourceGroupIdsScope'] = self.resource_group_ids_scope
        if self.tag_key_scope is not None:
            result['TagKeyScope'] = self.tag_key_scope
        if self.tag_value_scope is not None:
            result['TagValueScope'] = self.tag_value_scope
        if self.config_rule_trigger_types is not None:
            result['ConfigRuleTriggerTypes'] = self.config_rule_trigger_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('InputParameters') is not None:
            self.input_parameters = m.get('InputParameters')
        if m.get('Source') is not None:
            temp_model = GetConfigRuleResponseBodyConfigRuleSource()
            self.source = temp_model.from_map(m['Source'])
        if m.get('ConfigRuleState') is not None:
            self.config_rule_state = m.get('ConfigRuleState')
        if m.get('MaximumExecutionFrequency') is not None:
            self.maximum_execution_frequency = m.get('MaximumExecutionFrequency')
        if m.get('ManagedRule') is not None:
            temp_model = GetConfigRuleResponseBodyConfigRuleManagedRule()
            self.managed_rule = temp_model.from_map(m['ManagedRule'])
        if m.get('ConfigRuleArn') is not None:
            self.config_rule_arn = m.get('ConfigRuleArn')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CreateBy') is not None:
            temp_model = GetConfigRuleResponseBodyConfigRuleCreateBy()
            self.create_by = temp_model.from_map(m['CreateBy'])
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        if m.get('ConfigRuleEvaluationStatus') is not None:
            temp_model = GetConfigRuleResponseBodyConfigRuleConfigRuleEvaluationStatus()
            self.config_rule_evaluation_status = temp_model.from_map(m['ConfigRuleEvaluationStatus'])
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('ModifiedTimestamp') is not None:
            self.modified_timestamp = m.get('ModifiedTimestamp')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('ResourceTypesScope') is not None:
            self.resource_types_scope = m.get('ResourceTypesScope')
        if m.get('RegionIdsScope') is not None:
            self.region_ids_scope = m.get('RegionIdsScope')
        if m.get('ExcludeResourceIdsScope') is not None:
            self.exclude_resource_ids_scope = m.get('ExcludeResourceIdsScope')
        if m.get('ResourceGroupIdsScope') is not None:
            self.resource_group_ids_scope = m.get('ResourceGroupIdsScope')
        if m.get('TagKeyScope') is not None:
            self.tag_key_scope = m.get('TagKeyScope')
        if m.get('TagValueScope') is not None:
            self.tag_value_scope = m.get('TagValueScope')
        if m.get('ConfigRuleTriggerTypes') is not None:
            self.config_rule_trigger_types = m.get('ConfigRuleTriggerTypes')
        return self


class GetConfigRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        config_rule: GetConfigRuleResponseBodyConfigRule = None,
    ):
        self.request_id = request_id
        self.config_rule = config_rule

    def validate(self):
        if self.config_rule:
            self.config_rule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.config_rule is not None:
            result['ConfigRule'] = self.config_rule.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ConfigRule') is not None:
            temp_model = GetConfigRuleResponseBodyConfigRule()
            self.config_rule = temp_model.from_map(m['ConfigRule'])
        return self


class GetConfigRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetConfigRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetConfigRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeactiveConfigRulesRequest(TeaModel):
    def __init__(
        self,
        config_rule_ids: str = None,
    ):
        self.config_rule_ids = config_rule_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_ids is not None:
            result['ConfigRuleIds'] = self.config_rule_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleIds') is not None:
            self.config_rule_ids = m.get('ConfigRuleIds')
        return self


class DeactiveConfigRulesResponseBodyOperateRuleResultOperateRuleItemList(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        success: bool = None,
        config_rule_id: str = None,
    ):
        self.error_code = error_code
        self.success = success
        self.config_rule_id = config_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        return self


class DeactiveConfigRulesResponseBodyOperateRuleResult(TeaModel):
    def __init__(
        self,
        operate_rule_item_list: List[DeactiveConfigRulesResponseBodyOperateRuleResultOperateRuleItemList] = None,
    ):
        self.operate_rule_item_list = operate_rule_item_list

    def validate(self):
        if self.operate_rule_item_list:
            for k in self.operate_rule_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OperateRuleItemList'] = []
        if self.operate_rule_item_list is not None:
            for k in self.operate_rule_item_list:
                result['OperateRuleItemList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operate_rule_item_list = []
        if m.get('OperateRuleItemList') is not None:
            for k in m.get('OperateRuleItemList'):
                temp_model = DeactiveConfigRulesResponseBodyOperateRuleResultOperateRuleItemList()
                self.operate_rule_item_list.append(temp_model.from_map(k))
        return self


class DeactiveConfigRulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        operate_rule_result: DeactiveConfigRulesResponseBodyOperateRuleResult = None,
    ):
        self.request_id = request_id
        self.operate_rule_result = operate_rule_result

    def validate(self):
        if self.operate_rule_result:
            self.operate_rule_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.operate_rule_result is not None:
            result['OperateRuleResult'] = self.operate_rule_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OperateRuleResult') is not None:
            temp_model = DeactiveConfigRulesResponseBodyOperateRuleResult()
            self.operate_rule_result = temp_model.from_map(m['OperateRuleResult'])
        return self


class DeactiveConfigRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeactiveConfigRulesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeactiveConfigRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCompliancePackRequestConfigRulesConfigRuleParameters(TeaModel):
    def __init__(
        self,
        parameter_name: str = None,
        parameter_value: str = None,
    ):
        self.parameter_name = parameter_name
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class CreateCompliancePackRequestConfigRules(TeaModel):
    def __init__(
        self,
        managed_rule_identifier: str = None,
        config_rule_name: str = None,
        config_rule_parameters: List[CreateCompliancePackRequestConfigRulesConfigRuleParameters] = None,
        config_rule_id: str = None,
        description: str = None,
        risk_level: int = None,
    ):
        self.managed_rule_identifier = managed_rule_identifier
        self.config_rule_name = config_rule_name
        self.config_rule_parameters = config_rule_parameters
        self.config_rule_id = config_rule_id
        self.description = description
        self.risk_level = risk_level

    def validate(self):
        if self.config_rule_parameters:
            for k in self.config_rule_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.managed_rule_identifier is not None:
            result['ManagedRuleIdentifier'] = self.managed_rule_identifier
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        result['ConfigRuleParameters'] = []
        if self.config_rule_parameters is not None:
            for k in self.config_rule_parameters:
                result['ConfigRuleParameters'].append(k.to_map() if k else None)
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.description is not None:
            result['Description'] = self.description
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ManagedRuleIdentifier') is not None:
            self.managed_rule_identifier = m.get('ManagedRuleIdentifier')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        self.config_rule_parameters = []
        if m.get('ConfigRuleParameters') is not None:
            for k in m.get('ConfigRuleParameters'):
                temp_model = CreateCompliancePackRequestConfigRulesConfigRuleParameters()
                self.config_rule_parameters.append(temp_model.from_map(k))
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        return self


class CreateCompliancePackRequest(TeaModel):
    def __init__(
        self,
        compliance_pack_template_id: str = None,
        compliance_pack_name: str = None,
        description: str = None,
        risk_level: int = None,
        config_rules: List[CreateCompliancePackRequestConfigRules] = None,
        client_token: str = None,
    ):
        self.compliance_pack_template_id = compliance_pack_template_id
        self.compliance_pack_name = compliance_pack_name
        self.description = description
        self.risk_level = risk_level
        self.config_rules = config_rules
        self.client_token = client_token

    def validate(self):
        if self.config_rules:
            for k in self.config_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_template_id is not None:
            result['CompliancePackTemplateId'] = self.compliance_pack_template_id
        if self.compliance_pack_name is not None:
            result['CompliancePackName'] = self.compliance_pack_name
        if self.description is not None:
            result['Description'] = self.description
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        result['ConfigRules'] = []
        if self.config_rules is not None:
            for k in self.config_rules:
                result['ConfigRules'].append(k.to_map() if k else None)
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackTemplateId') is not None:
            self.compliance_pack_template_id = m.get('CompliancePackTemplateId')
        if m.get('CompliancePackName') is not None:
            self.compliance_pack_name = m.get('CompliancePackName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        self.config_rules = []
        if m.get('ConfigRules') is not None:
            for k in m.get('ConfigRules'):
                temp_model = CreateCompliancePackRequestConfigRules()
                self.config_rules.append(temp_model.from_map(k))
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateCompliancePackShrinkRequest(TeaModel):
    def __init__(
        self,
        compliance_pack_template_id: str = None,
        compliance_pack_name: str = None,
        description: str = None,
        risk_level: int = None,
        config_rules_shrink: str = None,
        client_token: str = None,
    ):
        self.compliance_pack_template_id = compliance_pack_template_id
        self.compliance_pack_name = compliance_pack_name
        self.description = description
        self.risk_level = risk_level
        self.config_rules_shrink = config_rules_shrink
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_template_id is not None:
            result['CompliancePackTemplateId'] = self.compliance_pack_template_id
        if self.compliance_pack_name is not None:
            result['CompliancePackName'] = self.compliance_pack_name
        if self.description is not None:
            result['Description'] = self.description
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.config_rules_shrink is not None:
            result['ConfigRules'] = self.config_rules_shrink
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackTemplateId') is not None:
            self.compliance_pack_template_id = m.get('CompliancePackTemplateId')
        if m.get('CompliancePackName') is not None:
            self.compliance_pack_name = m.get('CompliancePackName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('ConfigRules') is not None:
            self.config_rules_shrink = m.get('ConfigRules')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateCompliancePackResponseBody(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        request_id: str = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCompliancePackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateCompliancePackResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateCompliancePackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDiscoveredResourceCountsGroupByRegionRequest(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
    ):
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetDiscoveredResourceCountsGroupByRegionResponseBodyDiscoveredResourceCountsSummary(TeaModel):
    def __init__(
        self,
        resource_count: int = None,
        region: str = None,
    ):
        self.resource_count = resource_count
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_count is not None:
            result['ResourceCount'] = self.resource_count
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceCount') is not None:
            self.resource_count = m.get('ResourceCount')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class GetDiscoveredResourceCountsGroupByRegionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        discovered_resource_counts_summary: List[GetDiscoveredResourceCountsGroupByRegionResponseBodyDiscoveredResourceCountsSummary] = None,
    ):
        self.request_id = request_id
        self.discovered_resource_counts_summary = discovered_resource_counts_summary

    def validate(self):
        if self.discovered_resource_counts_summary:
            for k in self.discovered_resource_counts_summary:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['DiscoveredResourceCountsSummary'] = []
        if self.discovered_resource_counts_summary is not None:
            for k in self.discovered_resource_counts_summary:
                result['DiscoveredResourceCountsSummary'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.discovered_resource_counts_summary = []
        if m.get('DiscoveredResourceCountsSummary') is not None:
            for k in m.get('DiscoveredResourceCountsSummary'):
                temp_model = GetDiscoveredResourceCountsGroupByRegionResponseBodyDiscoveredResourceCountsSummary()
                self.discovered_resource_counts_summary.append(temp_model.from_map(k))
        return self


class GetDiscoveredResourceCountsGroupByRegionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDiscoveredResourceCountsGroupByRegionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDiscoveredResourceCountsGroupByRegionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAggregateConfigRuleComplianceByPackRequest(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        aggregator_id: str = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.aggregator_id = aggregator_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        return self


class GetAggregateConfigRuleComplianceByPackResponseBodyConfigRuleComplianceResultConfigRuleCompliances(TeaModel):
    def __init__(
        self,
        compliance_type: str = None,
        config_rule_name: str = None,
        config_rule_id: str = None,
    ):
        self.compliance_type = compliance_type
        self.config_rule_name = config_rule_name
        self.config_rule_id = config_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        return self


class GetAggregateConfigRuleComplianceByPackResponseBodyConfigRuleComplianceResult(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        non_compliant_count: int = None,
        config_rule_compliances: List[GetAggregateConfigRuleComplianceByPackResponseBodyConfigRuleComplianceResultConfigRuleCompliances] = None,
        total_count: int = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.non_compliant_count = non_compliant_count
        self.config_rule_compliances = config_rule_compliances
        self.total_count = total_count

    def validate(self):
        if self.config_rule_compliances:
            for k in self.config_rule_compliances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.non_compliant_count is not None:
            result['NonCompliantCount'] = self.non_compliant_count
        result['ConfigRuleCompliances'] = []
        if self.config_rule_compliances is not None:
            for k in self.config_rule_compliances:
                result['ConfigRuleCompliances'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('NonCompliantCount') is not None:
            self.non_compliant_count = m.get('NonCompliantCount')
        self.config_rule_compliances = []
        if m.get('ConfigRuleCompliances') is not None:
            for k in m.get('ConfigRuleCompliances'):
                temp_model = GetAggregateConfigRuleComplianceByPackResponseBodyConfigRuleComplianceResultConfigRuleCompliances()
                self.config_rule_compliances.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetAggregateConfigRuleComplianceByPackResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        config_rule_compliance_result: GetAggregateConfigRuleComplianceByPackResponseBodyConfigRuleComplianceResult = None,
    ):
        self.request_id = request_id
        self.config_rule_compliance_result = config_rule_compliance_result

    def validate(self):
        if self.config_rule_compliance_result:
            self.config_rule_compliance_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.config_rule_compliance_result is not None:
            result['ConfigRuleComplianceResult'] = self.config_rule_compliance_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ConfigRuleComplianceResult') is not None:
            temp_model = GetAggregateConfigRuleComplianceByPackResponseBodyConfigRuleComplianceResult()
            self.config_rule_compliance_result = temp_model.from_map(m['ConfigRuleComplianceResult'])
        return self


class GetAggregateConfigRuleComplianceByPackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAggregateConfigRuleComplianceByPackResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAggregateConfigRuleComplianceByPackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAggregateResourceComplianceByConfigRuleRequest(TeaModel):
    def __init__(
        self,
        compliance_type: str = None,
        config_rule_id: str = None,
        aggregator_id: str = None,
    ):
        self.compliance_type = compliance_type
        self.config_rule_id = config_rule_id
        self.aggregator_id = aggregator_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        return self


class GetAggregateResourceComplianceByConfigRuleResponseBodyComplianceResultCompliances(TeaModel):
    def __init__(
        self,
        compliance_type: str = None,
        count: int = None,
    ):
        self.compliance_type = compliance_type
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class GetAggregateResourceComplianceByConfigRuleResponseBodyComplianceResult(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        compliances: List[GetAggregateResourceComplianceByConfigRuleResponseBodyComplianceResultCompliances] = None,
    ):
        self.total_count = total_count
        self.compliances = compliances

    def validate(self):
        if self.compliances:
            for k in self.compliances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Compliances'] = []
        if self.compliances is not None:
            for k in self.compliances:
                result['Compliances'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.compliances = []
        if m.get('Compliances') is not None:
            for k in m.get('Compliances'):
                temp_model = GetAggregateResourceComplianceByConfigRuleResponseBodyComplianceResultCompliances()
                self.compliances.append(temp_model.from_map(k))
        return self


class GetAggregateResourceComplianceByConfigRuleResponseBody(TeaModel):
    def __init__(
        self,
        compliance_result: GetAggregateResourceComplianceByConfigRuleResponseBodyComplianceResult = None,
        request_id: str = None,
    ):
        self.compliance_result = compliance_result
        self.request_id = request_id

    def validate(self):
        if self.compliance_result:
            self.compliance_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_result is not None:
            result['ComplianceResult'] = self.compliance_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceResult') is not None:
            temp_model = GetAggregateResourceComplianceByConfigRuleResponseBodyComplianceResult()
            self.compliance_result = temp_model.from_map(m['ComplianceResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAggregateResourceComplianceByConfigRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAggregateResourceComplianceByConfigRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAggregateResourceComplianceByConfigRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAggregateConfigRuleSummaryByRiskLevelRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
    ):
        self.aggregator_id = aggregator_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        return self


class GetAggregateConfigRuleSummaryByRiskLevelResponseBodyConfigRuleSummaries(TeaModel):
    def __init__(
        self,
        risk_level: int = None,
        compliant_count: int = None,
        non_compliant_count: int = None,
    ):
        self.risk_level = risk_level
        self.compliant_count = compliant_count
        self.non_compliant_count = non_compliant_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.compliant_count is not None:
            result['CompliantCount'] = self.compliant_count
        if self.non_compliant_count is not None:
            result['NonCompliantCount'] = self.non_compliant_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('CompliantCount') is not None:
            self.compliant_count = m.get('CompliantCount')
        if m.get('NonCompliantCount') is not None:
            self.non_compliant_count = m.get('NonCompliantCount')
        return self


class GetAggregateConfigRuleSummaryByRiskLevelResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        config_rule_summaries: List[GetAggregateConfigRuleSummaryByRiskLevelResponseBodyConfigRuleSummaries] = None,
    ):
        self.request_id = request_id
        self.config_rule_summaries = config_rule_summaries

    def validate(self):
        if self.config_rule_summaries:
            for k in self.config_rule_summaries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ConfigRuleSummaries'] = []
        if self.config_rule_summaries is not None:
            for k in self.config_rule_summaries:
                result['ConfigRuleSummaries'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.config_rule_summaries = []
        if m.get('ConfigRuleSummaries') is not None:
            for k in m.get('ConfigRuleSummaries'):
                temp_model = GetAggregateConfigRuleSummaryByRiskLevelResponseBodyConfigRuleSummaries()
                self.config_rule_summaries.append(temp_model.from_map(k))
        return self


class GetAggregateConfigRuleSummaryByRiskLevelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAggregateConfigRuleSummaryByRiskLevelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAggregateConfigRuleSummaryByRiskLevelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateConfigRuleRequest(TeaModel):
    def __init__(
        self,
        config_rule_id: str = None,
        description: str = None,
        input_parameters: Dict[str, Any] = None,
        maximum_execution_frequency: str = None,
        resource_types_scope: List[str] = None,
        risk_level: int = None,
        client_token: str = None,
        region_ids_scope: str = None,
        exclude_resource_ids_scope: str = None,
        config_rule_trigger_types: str = None,
        resource_group_ids_scope: str = None,
        tag_key_scope: str = None,
        tag_value_scope: str = None,
    ):
        self.config_rule_id = config_rule_id
        self.description = description
        self.input_parameters = input_parameters
        self.maximum_execution_frequency = maximum_execution_frequency
        self.resource_types_scope = resource_types_scope
        self.risk_level = risk_level
        self.client_token = client_token
        self.region_ids_scope = region_ids_scope
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        self.config_rule_trigger_types = config_rule_trigger_types
        self.resource_group_ids_scope = resource_group_ids_scope
        self.tag_key_scope = tag_key_scope
        self.tag_value_scope = tag_value_scope

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.description is not None:
            result['Description'] = self.description
        if self.input_parameters is not None:
            result['InputParameters'] = self.input_parameters
        if self.maximum_execution_frequency is not None:
            result['MaximumExecutionFrequency'] = self.maximum_execution_frequency
        if self.resource_types_scope is not None:
            result['ResourceTypesScope'] = self.resource_types_scope
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_ids_scope is not None:
            result['RegionIdsScope'] = self.region_ids_scope
        if self.exclude_resource_ids_scope is not None:
            result['ExcludeResourceIdsScope'] = self.exclude_resource_ids_scope
        if self.config_rule_trigger_types is not None:
            result['ConfigRuleTriggerTypes'] = self.config_rule_trigger_types
        if self.resource_group_ids_scope is not None:
            result['ResourceGroupIdsScope'] = self.resource_group_ids_scope
        if self.tag_key_scope is not None:
            result['TagKeyScope'] = self.tag_key_scope
        if self.tag_value_scope is not None:
            result['TagValueScope'] = self.tag_value_scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InputParameters') is not None:
            self.input_parameters = m.get('InputParameters')
        if m.get('MaximumExecutionFrequency') is not None:
            self.maximum_execution_frequency = m.get('MaximumExecutionFrequency')
        if m.get('ResourceTypesScope') is not None:
            self.resource_types_scope = m.get('ResourceTypesScope')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionIdsScope') is not None:
            self.region_ids_scope = m.get('RegionIdsScope')
        if m.get('ExcludeResourceIdsScope') is not None:
            self.exclude_resource_ids_scope = m.get('ExcludeResourceIdsScope')
        if m.get('ConfigRuleTriggerTypes') is not None:
            self.config_rule_trigger_types = m.get('ConfigRuleTriggerTypes')
        if m.get('ResourceGroupIdsScope') is not None:
            self.resource_group_ids_scope = m.get('ResourceGroupIdsScope')
        if m.get('TagKeyScope') is not None:
            self.tag_key_scope = m.get('TagKeyScope')
        if m.get('TagValueScope') is not None:
            self.tag_value_scope = m.get('TagValueScope')
        return self


class UpdateConfigRuleShrinkRequest(TeaModel):
    def __init__(
        self,
        config_rule_id: str = None,
        description: str = None,
        input_parameters_shrink: str = None,
        maximum_execution_frequency: str = None,
        resource_types_scope_shrink: str = None,
        risk_level: int = None,
        client_token: str = None,
        region_ids_scope: str = None,
        exclude_resource_ids_scope: str = None,
        config_rule_trigger_types: str = None,
        resource_group_ids_scope: str = None,
        tag_key_scope: str = None,
        tag_value_scope: str = None,
    ):
        self.config_rule_id = config_rule_id
        self.description = description
        self.input_parameters_shrink = input_parameters_shrink
        self.maximum_execution_frequency = maximum_execution_frequency
        self.resource_types_scope_shrink = resource_types_scope_shrink
        self.risk_level = risk_level
        self.client_token = client_token
        self.region_ids_scope = region_ids_scope
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        self.config_rule_trigger_types = config_rule_trigger_types
        self.resource_group_ids_scope = resource_group_ids_scope
        self.tag_key_scope = tag_key_scope
        self.tag_value_scope = tag_value_scope

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.description is not None:
            result['Description'] = self.description
        if self.input_parameters_shrink is not None:
            result['InputParameters'] = self.input_parameters_shrink
        if self.maximum_execution_frequency is not None:
            result['MaximumExecutionFrequency'] = self.maximum_execution_frequency
        if self.resource_types_scope_shrink is not None:
            result['ResourceTypesScope'] = self.resource_types_scope_shrink
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_ids_scope is not None:
            result['RegionIdsScope'] = self.region_ids_scope
        if self.exclude_resource_ids_scope is not None:
            result['ExcludeResourceIdsScope'] = self.exclude_resource_ids_scope
        if self.config_rule_trigger_types is not None:
            result['ConfigRuleTriggerTypes'] = self.config_rule_trigger_types
        if self.resource_group_ids_scope is not None:
            result['ResourceGroupIdsScope'] = self.resource_group_ids_scope
        if self.tag_key_scope is not None:
            result['TagKeyScope'] = self.tag_key_scope
        if self.tag_value_scope is not None:
            result['TagValueScope'] = self.tag_value_scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InputParameters') is not None:
            self.input_parameters_shrink = m.get('InputParameters')
        if m.get('MaximumExecutionFrequency') is not None:
            self.maximum_execution_frequency = m.get('MaximumExecutionFrequency')
        if m.get('ResourceTypesScope') is not None:
            self.resource_types_scope_shrink = m.get('ResourceTypesScope')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionIdsScope') is not None:
            self.region_ids_scope = m.get('RegionIdsScope')
        if m.get('ExcludeResourceIdsScope') is not None:
            self.exclude_resource_ids_scope = m.get('ExcludeResourceIdsScope')
        if m.get('ConfigRuleTriggerTypes') is not None:
            self.config_rule_trigger_types = m.get('ConfigRuleTriggerTypes')
        if m.get('ResourceGroupIdsScope') is not None:
            self.resource_group_ids_scope = m.get('ResourceGroupIdsScope')
        if m.get('TagKeyScope') is not None:
            self.tag_key_scope = m.get('TagKeyScope')
        if m.get('TagValueScope') is not None:
            self.tag_value_scope = m.get('TagValueScope')
        return self


class UpdateConfigRuleResponseBody(TeaModel):
    def __init__(
        self,
        config_rule_id: str = None,
        request_id: str = None,
    ):
        self.config_rule_id = config_rule_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateConfigRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateConfigRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateConfigRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAggregateResourceInventoryRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
    ):
        self.aggregator_id = aggregator_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        return self


class GetAggregateResourceInventoryResponseBodyResourceInventory(TeaModel):
    def __init__(
        self,
        download_url: str = None,
        status: str = None,
        account_id: int = None,
        resource_inventory_generate_time: int = None,
    ):
        self.download_url = download_url
        self.status = status
        self.account_id = account_id
        self.resource_inventory_generate_time = resource_inventory_generate_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.status is not None:
            result['Status'] = self.status
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.resource_inventory_generate_time is not None:
            result['ResourceInventoryGenerateTime'] = self.resource_inventory_generate_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ResourceInventoryGenerateTime') is not None:
            self.resource_inventory_generate_time = m.get('ResourceInventoryGenerateTime')
        return self


class GetAggregateResourceInventoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_inventory: GetAggregateResourceInventoryResponseBodyResourceInventory = None,
    ):
        self.request_id = request_id
        self.resource_inventory = resource_inventory

    def validate(self):
        if self.resource_inventory:
            self.resource_inventory.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_inventory is not None:
            result['ResourceInventory'] = self.resource_inventory.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceInventory') is not None:
            temp_model = GetAggregateResourceInventoryResponseBodyResourceInventory()
            self.resource_inventory = temp_model.from_map(m['ResourceInventory'])
        return self


class GetAggregateResourceInventoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAggregateResourceInventoryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAggregateResourceInventoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAggregateResourceComplianceTimelineRequest(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        resource_id: str = None,
        start_time: int = None,
        end_time: int = None,
        max_results: int = None,
        aggregator_id: str = None,
        resource_owner_id: int = None,
        region: str = None,
        next_token: str = None,
    ):
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.start_time = start_time
        self.end_time = end_time
        self.max_results = max_results
        self.aggregator_id = aggregator_id
        self.resource_owner_id = resource_owner_id
        self.region = region
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region is not None:
            result['Region'] = self.region
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class GetAggregateResourceComplianceTimelineResponseBodyResourceComplianceTimelineComplianceList(TeaModel):
    def __init__(
        self,
        tags: str = None,
        account_id: str = None,
        availability_zone: str = None,
        resource_type: str = None,
        resource_create_time: int = None,
        region: str = None,
        configuration: str = None,
        capture_time: int = None,
        configuration_diff: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_status: str = None,
    ):
        self.tags = tags
        self.account_id = account_id
        self.availability_zone = availability_zone
        self.resource_type = resource_type
        self.resource_create_time = resource_create_time
        self.region = region
        self.configuration = configuration
        self.capture_time = capture_time
        self.configuration_diff = configuration_diff
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_status = resource_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.availability_zone is not None:
            result['AvailabilityZone'] = self.availability_zone
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_create_time is not None:
            result['ResourceCreateTime'] = self.resource_create_time
        if self.region is not None:
            result['Region'] = self.region
        if self.configuration is not None:
            result['Configuration'] = self.configuration
        if self.capture_time is not None:
            result['CaptureTime'] = self.capture_time
        if self.configuration_diff is not None:
            result['ConfigurationDiff'] = self.configuration_diff
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_status is not None:
            result['ResourceStatus'] = self.resource_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AvailabilityZone') is not None:
            self.availability_zone = m.get('AvailabilityZone')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceCreateTime') is not None:
            self.resource_create_time = m.get('ResourceCreateTime')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Configuration') is not None:
            self.configuration = m.get('Configuration')
        if m.get('CaptureTime') is not None:
            self.capture_time = m.get('CaptureTime')
        if m.get('ConfigurationDiff') is not None:
            self.configuration_diff = m.get('ConfigurationDiff')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceStatus') is not None:
            self.resource_status = m.get('ResourceStatus')
        return self


class GetAggregateResourceComplianceTimelineResponseBodyResourceComplianceTimeline(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        max_results: int = None,
        compliance_list: List[GetAggregateResourceComplianceTimelineResponseBodyResourceComplianceTimelineComplianceList] = None,
    ):
        self.next_token = next_token
        self.max_results = max_results
        self.compliance_list = compliance_list

    def validate(self):
        if self.compliance_list:
            for k in self.compliance_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['ComplianceList'] = []
        if self.compliance_list is not None:
            for k in self.compliance_list:
                result['ComplianceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.compliance_list = []
        if m.get('ComplianceList') is not None:
            for k in m.get('ComplianceList'):
                temp_model = GetAggregateResourceComplianceTimelineResponseBodyResourceComplianceTimelineComplianceList()
                self.compliance_list.append(temp_model.from_map(k))
        return self


class GetAggregateResourceComplianceTimelineResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_compliance_timeline: GetAggregateResourceComplianceTimelineResponseBodyResourceComplianceTimeline = None,
    ):
        self.request_id = request_id
        self.resource_compliance_timeline = resource_compliance_timeline

    def validate(self):
        if self.resource_compliance_timeline:
            self.resource_compliance_timeline.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_compliance_timeline is not None:
            result['ResourceComplianceTimeline'] = self.resource_compliance_timeline.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceComplianceTimeline') is not None:
            temp_model = GetAggregateResourceComplianceTimelineResponseBodyResourceComplianceTimeline()
            self.resource_compliance_timeline = temp_model.from_map(m['ResourceComplianceTimeline'])
        return self


class GetAggregateResourceComplianceTimelineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAggregateResourceComplianceTimelineResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAggregateResourceComplianceTimelineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAggregateConfigRuleRequest(TeaModel):
    def __init__(
        self,
        config_rule_id: str = None,
        description: str = None,
        input_parameters: Dict[str, Any] = None,
        maximum_execution_frequency: str = None,
        resource_types_scope: List[str] = None,
        risk_level: int = None,
        client_token: str = None,
        region_ids_scope: str = None,
        exclude_resource_ids_scope: str = None,
        config_rule_trigger_types: str = None,
        aggregator_id: str = None,
        resource_group_ids_scope: str = None,
        tag_key_scope: str = None,
        tag_value_scope: str = None,
    ):
        self.config_rule_id = config_rule_id
        self.description = description
        self.input_parameters = input_parameters
        self.maximum_execution_frequency = maximum_execution_frequency
        self.resource_types_scope = resource_types_scope
        self.risk_level = risk_level
        self.client_token = client_token
        self.region_ids_scope = region_ids_scope
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        self.config_rule_trigger_types = config_rule_trigger_types
        self.aggregator_id = aggregator_id
        self.resource_group_ids_scope = resource_group_ids_scope
        self.tag_key_scope = tag_key_scope
        self.tag_value_scope = tag_value_scope

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.description is not None:
            result['Description'] = self.description
        if self.input_parameters is not None:
            result['InputParameters'] = self.input_parameters
        if self.maximum_execution_frequency is not None:
            result['MaximumExecutionFrequency'] = self.maximum_execution_frequency
        if self.resource_types_scope is not None:
            result['ResourceTypesScope'] = self.resource_types_scope
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_ids_scope is not None:
            result['RegionIdsScope'] = self.region_ids_scope
        if self.exclude_resource_ids_scope is not None:
            result['ExcludeResourceIdsScope'] = self.exclude_resource_ids_scope
        if self.config_rule_trigger_types is not None:
            result['ConfigRuleTriggerTypes'] = self.config_rule_trigger_types
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.resource_group_ids_scope is not None:
            result['ResourceGroupIdsScope'] = self.resource_group_ids_scope
        if self.tag_key_scope is not None:
            result['TagKeyScope'] = self.tag_key_scope
        if self.tag_value_scope is not None:
            result['TagValueScope'] = self.tag_value_scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InputParameters') is not None:
            self.input_parameters = m.get('InputParameters')
        if m.get('MaximumExecutionFrequency') is not None:
            self.maximum_execution_frequency = m.get('MaximumExecutionFrequency')
        if m.get('ResourceTypesScope') is not None:
            self.resource_types_scope = m.get('ResourceTypesScope')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionIdsScope') is not None:
            self.region_ids_scope = m.get('RegionIdsScope')
        if m.get('ExcludeResourceIdsScope') is not None:
            self.exclude_resource_ids_scope = m.get('ExcludeResourceIdsScope')
        if m.get('ConfigRuleTriggerTypes') is not None:
            self.config_rule_trigger_types = m.get('ConfigRuleTriggerTypes')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ResourceGroupIdsScope') is not None:
            self.resource_group_ids_scope = m.get('ResourceGroupIdsScope')
        if m.get('TagKeyScope') is not None:
            self.tag_key_scope = m.get('TagKeyScope')
        if m.get('TagValueScope') is not None:
            self.tag_value_scope = m.get('TagValueScope')
        return self


class UpdateAggregateConfigRuleShrinkRequest(TeaModel):
    def __init__(
        self,
        config_rule_id: str = None,
        description: str = None,
        input_parameters_shrink: str = None,
        maximum_execution_frequency: str = None,
        resource_types_scope_shrink: str = None,
        risk_level: int = None,
        client_token: str = None,
        region_ids_scope: str = None,
        exclude_resource_ids_scope: str = None,
        config_rule_trigger_types: str = None,
        aggregator_id: str = None,
        resource_group_ids_scope: str = None,
        tag_key_scope: str = None,
        tag_value_scope: str = None,
    ):
        self.config_rule_id = config_rule_id
        self.description = description
        self.input_parameters_shrink = input_parameters_shrink
        self.maximum_execution_frequency = maximum_execution_frequency
        self.resource_types_scope_shrink = resource_types_scope_shrink
        self.risk_level = risk_level
        self.client_token = client_token
        self.region_ids_scope = region_ids_scope
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        self.config_rule_trigger_types = config_rule_trigger_types
        self.aggregator_id = aggregator_id
        self.resource_group_ids_scope = resource_group_ids_scope
        self.tag_key_scope = tag_key_scope
        self.tag_value_scope = tag_value_scope

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.description is not None:
            result['Description'] = self.description
        if self.input_parameters_shrink is not None:
            result['InputParameters'] = self.input_parameters_shrink
        if self.maximum_execution_frequency is not None:
            result['MaximumExecutionFrequency'] = self.maximum_execution_frequency
        if self.resource_types_scope_shrink is not None:
            result['ResourceTypesScope'] = self.resource_types_scope_shrink
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_ids_scope is not None:
            result['RegionIdsScope'] = self.region_ids_scope
        if self.exclude_resource_ids_scope is not None:
            result['ExcludeResourceIdsScope'] = self.exclude_resource_ids_scope
        if self.config_rule_trigger_types is not None:
            result['ConfigRuleTriggerTypes'] = self.config_rule_trigger_types
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.resource_group_ids_scope is not None:
            result['ResourceGroupIdsScope'] = self.resource_group_ids_scope
        if self.tag_key_scope is not None:
            result['TagKeyScope'] = self.tag_key_scope
        if self.tag_value_scope is not None:
            result['TagValueScope'] = self.tag_value_scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InputParameters') is not None:
            self.input_parameters_shrink = m.get('InputParameters')
        if m.get('MaximumExecutionFrequency') is not None:
            self.maximum_execution_frequency = m.get('MaximumExecutionFrequency')
        if m.get('ResourceTypesScope') is not None:
            self.resource_types_scope_shrink = m.get('ResourceTypesScope')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionIdsScope') is not None:
            self.region_ids_scope = m.get('RegionIdsScope')
        if m.get('ExcludeResourceIdsScope') is not None:
            self.exclude_resource_ids_scope = m.get('ExcludeResourceIdsScope')
        if m.get('ConfigRuleTriggerTypes') is not None:
            self.config_rule_trigger_types = m.get('ConfigRuleTriggerTypes')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ResourceGroupIdsScope') is not None:
            self.resource_group_ids_scope = m.get('ResourceGroupIdsScope')
        if m.get('TagKeyScope') is not None:
            self.tag_key_scope = m.get('TagKeyScope')
        if m.get('TagValueScope') is not None:
            self.tag_value_scope = m.get('TagValueScope')
        return self


class UpdateAggregateConfigRuleResponseBody(TeaModel):
    def __init__(
        self,
        config_rule_id: str = None,
        request_id: str = None,
    ):
        self.config_rule_id = config_rule_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAggregateConfigRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAggregateConfigRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateAggregateConfigRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAggregateCompliancePackReportRequest(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        aggregator_id: str = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.aggregator_id = aggregator_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        return self


class GetAggregateCompliancePackReportResponseBodyCompliancePackReport(TeaModel):
    def __init__(
        self,
        report_url: str = None,
        report_status: str = None,
        compliance_pack_id: str = None,
        account_id: int = None,
        report_create_timestamp: int = None,
    ):
        self.report_url = report_url
        self.report_status = report_status
        self.compliance_pack_id = compliance_pack_id
        self.account_id = account_id
        self.report_create_timestamp = report_create_timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.report_url is not None:
            result['ReportUrl'] = self.report_url
        if self.report_status is not None:
            result['ReportStatus'] = self.report_status
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.report_create_timestamp is not None:
            result['ReportCreateTimestamp'] = self.report_create_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReportUrl') is not None:
            self.report_url = m.get('ReportUrl')
        if m.get('ReportStatus') is not None:
            self.report_status = m.get('ReportStatus')
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ReportCreateTimestamp') is not None:
            self.report_create_timestamp = m.get('ReportCreateTimestamp')
        return self


class GetAggregateCompliancePackReportResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        compliance_pack_report: GetAggregateCompliancePackReportResponseBodyCompliancePackReport = None,
    ):
        self.request_id = request_id
        self.compliance_pack_report = compliance_pack_report

    def validate(self):
        if self.compliance_pack_report:
            self.compliance_pack_report.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.compliance_pack_report is not None:
            result['CompliancePackReport'] = self.compliance_pack_report.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CompliancePackReport') is not None:
            temp_model = GetAggregateCompliancePackReportResponseBodyCompliancePackReport()
            self.compliance_pack_report = temp_model.from_map(m['CompliancePackReport'])
        return self


class GetAggregateCompliancePackReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAggregateCompliancePackReportResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAggregateCompliancePackReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAggregateCompliancePackRequestConfigRulesConfigRuleParameters(TeaModel):
    def __init__(
        self,
        parameter_name: str = None,
        parameter_value: str = None,
    ):
        self.parameter_name = parameter_name
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class CreateAggregateCompliancePackRequestConfigRules(TeaModel):
    def __init__(
        self,
        managed_rule_identifier: str = None,
        config_rule_name: str = None,
        config_rule_parameters: List[CreateAggregateCompliancePackRequestConfigRulesConfigRuleParameters] = None,
        config_rule_id: str = None,
        description: str = None,
        risk_level: int = None,
    ):
        self.managed_rule_identifier = managed_rule_identifier
        self.config_rule_name = config_rule_name
        self.config_rule_parameters = config_rule_parameters
        self.config_rule_id = config_rule_id
        self.description = description
        self.risk_level = risk_level

    def validate(self):
        if self.config_rule_parameters:
            for k in self.config_rule_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.managed_rule_identifier is not None:
            result['ManagedRuleIdentifier'] = self.managed_rule_identifier
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        result['ConfigRuleParameters'] = []
        if self.config_rule_parameters is not None:
            for k in self.config_rule_parameters:
                result['ConfigRuleParameters'].append(k.to_map() if k else None)
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.description is not None:
            result['Description'] = self.description
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ManagedRuleIdentifier') is not None:
            self.managed_rule_identifier = m.get('ManagedRuleIdentifier')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        self.config_rule_parameters = []
        if m.get('ConfigRuleParameters') is not None:
            for k in m.get('ConfigRuleParameters'):
                temp_model = CreateAggregateCompliancePackRequestConfigRulesConfigRuleParameters()
                self.config_rule_parameters.append(temp_model.from_map(k))
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        return self


class CreateAggregateCompliancePackRequest(TeaModel):
    def __init__(
        self,
        compliance_pack_template_id: str = None,
        compliance_pack_name: str = None,
        description: str = None,
        risk_level: int = None,
        aggregator_id: str = None,
        config_rules: List[CreateAggregateCompliancePackRequestConfigRules] = None,
        client_token: str = None,
    ):
        self.compliance_pack_template_id = compliance_pack_template_id
        self.compliance_pack_name = compliance_pack_name
        self.description = description
        self.risk_level = risk_level
        self.aggregator_id = aggregator_id
        self.config_rules = config_rules
        self.client_token = client_token

    def validate(self):
        if self.config_rules:
            for k in self.config_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_template_id is not None:
            result['CompliancePackTemplateId'] = self.compliance_pack_template_id
        if self.compliance_pack_name is not None:
            result['CompliancePackName'] = self.compliance_pack_name
        if self.description is not None:
            result['Description'] = self.description
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        result['ConfigRules'] = []
        if self.config_rules is not None:
            for k in self.config_rules:
                result['ConfigRules'].append(k.to_map() if k else None)
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackTemplateId') is not None:
            self.compliance_pack_template_id = m.get('CompliancePackTemplateId')
        if m.get('CompliancePackName') is not None:
            self.compliance_pack_name = m.get('CompliancePackName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        self.config_rules = []
        if m.get('ConfigRules') is not None:
            for k in m.get('ConfigRules'):
                temp_model = CreateAggregateCompliancePackRequestConfigRules()
                self.config_rules.append(temp_model.from_map(k))
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateAggregateCompliancePackShrinkRequest(TeaModel):
    def __init__(
        self,
        compliance_pack_template_id: str = None,
        compliance_pack_name: str = None,
        description: str = None,
        risk_level: int = None,
        aggregator_id: str = None,
        config_rules_shrink: str = None,
        client_token: str = None,
    ):
        self.compliance_pack_template_id = compliance_pack_template_id
        self.compliance_pack_name = compliance_pack_name
        self.description = description
        self.risk_level = risk_level
        self.aggregator_id = aggregator_id
        self.config_rules_shrink = config_rules_shrink
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_template_id is not None:
            result['CompliancePackTemplateId'] = self.compliance_pack_template_id
        if self.compliance_pack_name is not None:
            result['CompliancePackName'] = self.compliance_pack_name
        if self.description is not None:
            result['Description'] = self.description
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.config_rules_shrink is not None:
            result['ConfigRules'] = self.config_rules_shrink
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackTemplateId') is not None:
            self.compliance_pack_template_id = m.get('CompliancePackTemplateId')
        if m.get('CompliancePackName') is not None:
            self.compliance_pack_name = m.get('CompliancePackName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ConfigRules') is not None:
            self.config_rules_shrink = m.get('ConfigRules')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateAggregateCompliancePackResponseBody(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        request_id: str = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAggregateCompliancePackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAggregateCompliancePackResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAggregateCompliancePackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAggregateResourceCountsGroupByResourceTypeRequest(TeaModel):
    def __init__(
        self,
        region: str = None,
        aggregator_id: str = None,
    ):
        self.region = region
        self.aggregator_id = aggregator_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        return self


class GetAggregateResourceCountsGroupByResourceTypeResponseBodyDiscoveredResourceCountsSummary(TeaModel):
    def __init__(
        self,
        resource_count: int = None,
        resource_type: str = None,
    ):
        self.resource_count = resource_count
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_count is not None:
            result['ResourceCount'] = self.resource_count
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceCount') is not None:
            self.resource_count = m.get('ResourceCount')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetAggregateResourceCountsGroupByResourceTypeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        discovered_resource_counts_summary: List[GetAggregateResourceCountsGroupByResourceTypeResponseBodyDiscoveredResourceCountsSummary] = None,
    ):
        self.request_id = request_id
        self.discovered_resource_counts_summary = discovered_resource_counts_summary

    def validate(self):
        if self.discovered_resource_counts_summary:
            for k in self.discovered_resource_counts_summary:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['DiscoveredResourceCountsSummary'] = []
        if self.discovered_resource_counts_summary is not None:
            for k in self.discovered_resource_counts_summary:
                result['DiscoveredResourceCountsSummary'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.discovered_resource_counts_summary = []
        if m.get('DiscoveredResourceCountsSummary') is not None:
            for k in m.get('DiscoveredResourceCountsSummary'):
                temp_model = GetAggregateResourceCountsGroupByResourceTypeResponseBodyDiscoveredResourceCountsSummary()
                self.discovered_resource_counts_summary.append(temp_model.from_map(k))
        return self


class GetAggregateResourceCountsGroupByResourceTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAggregateResourceCountsGroupByResourceTypeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAggregateResourceCountsGroupByResourceTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAggregateConfigRuleRequest(TeaModel):
    def __init__(
        self,
        config_rule_id: str = None,
        aggregator_id: str = None,
    ):
        self.config_rule_id = config_rule_id
        self.aggregator_id = aggregator_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        return self


class GetAggregateConfigRuleResponseBodyConfigRuleSourceSourceDetails(TeaModel):
    def __init__(
        self,
        message_type: str = None,
        event_source: str = None,
        maximum_execution_frequency: str = None,
    ):
        self.message_type = message_type
        self.event_source = event_source
        self.maximum_execution_frequency = maximum_execution_frequency

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        if self.event_source is not None:
            result['EventSource'] = self.event_source
        if self.maximum_execution_frequency is not None:
            result['MaximumExecutionFrequency'] = self.maximum_execution_frequency
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        if m.get('EventSource') is not None:
            self.event_source = m.get('EventSource')
        if m.get('MaximumExecutionFrequency') is not None:
            self.maximum_execution_frequency = m.get('MaximumExecutionFrequency')
        return self


class GetAggregateConfigRuleResponseBodyConfigRuleSource(TeaModel):
    def __init__(
        self,
        source_details: List[GetAggregateConfigRuleResponseBodyConfigRuleSourceSourceDetails] = None,
        owner: str = None,
        identifier: str = None,
    ):
        self.source_details = source_details
        self.owner = owner
        self.identifier = identifier

    def validate(self):
        if self.source_details:
            for k in self.source_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SourceDetails'] = []
        if self.source_details is not None:
            for k in self.source_details:
                result['SourceDetails'].append(k.to_map() if k else None)
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.source_details = []
        if m.get('SourceDetails') is not None:
            for k in m.get('SourceDetails'):
                temp_model = GetAggregateConfigRuleResponseBodyConfigRuleSourceSourceDetails()
                self.source_details.append(temp_model.from_map(k))
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        return self


class GetAggregateConfigRuleResponseBodyConfigRuleManagedRuleSourceDetails(TeaModel):
    def __init__(
        self,
        message_type: str = None,
        event_source: str = None,
        maximum_execution_frequency: str = None,
    ):
        self.message_type = message_type
        self.event_source = event_source
        self.maximum_execution_frequency = maximum_execution_frequency

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        if self.event_source is not None:
            result['EventSource'] = self.event_source
        if self.maximum_execution_frequency is not None:
            result['MaximumExecutionFrequency'] = self.maximum_execution_frequency
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        if m.get('EventSource') is not None:
            self.event_source = m.get('EventSource')
        if m.get('MaximumExecutionFrequency') is not None:
            self.maximum_execution_frequency = m.get('MaximumExecutionFrequency')
        return self


class GetAggregateConfigRuleResponseBodyConfigRuleManagedRule(TeaModel):
    def __init__(
        self,
        source_details: List[GetAggregateConfigRuleResponseBodyConfigRuleManagedRuleSourceDetails] = None,
        description: str = None,
        labels: List[str] = None,
        identifier: str = None,
        optional_input_parameter_details: Dict[str, Any] = None,
        managed_rule_name: str = None,
        compulsory_input_parameter_details: Dict[str, Any] = None,
    ):
        self.source_details = source_details
        self.description = description
        self.labels = labels
        self.identifier = identifier
        self.optional_input_parameter_details = optional_input_parameter_details
        self.managed_rule_name = managed_rule_name
        self.compulsory_input_parameter_details = compulsory_input_parameter_details

    def validate(self):
        if self.source_details:
            for k in self.source_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SourceDetails'] = []
        if self.source_details is not None:
            for k in self.source_details:
                result['SourceDetails'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.optional_input_parameter_details is not None:
            result['OptionalInputParameterDetails'] = self.optional_input_parameter_details
        if self.managed_rule_name is not None:
            result['ManagedRuleName'] = self.managed_rule_name
        if self.compulsory_input_parameter_details is not None:
            result['CompulsoryInputParameterDetails'] = self.compulsory_input_parameter_details
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.source_details = []
        if m.get('SourceDetails') is not None:
            for k in m.get('SourceDetails'):
                temp_model = GetAggregateConfigRuleResponseBodyConfigRuleManagedRuleSourceDetails()
                self.source_details.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('OptionalInputParameterDetails') is not None:
            self.optional_input_parameter_details = m.get('OptionalInputParameterDetails')
        if m.get('ManagedRuleName') is not None:
            self.managed_rule_name = m.get('ManagedRuleName')
        if m.get('CompulsoryInputParameterDetails') is not None:
            self.compulsory_input_parameter_details = m.get('CompulsoryInputParameterDetails')
        return self


class GetAggregateConfigRuleResponseBodyConfigRuleCreateBy(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        aggregator_name: str = None,
        compliance_pack_name: str = None,
        creator_name: str = None,
        creator_type: str = None,
        creator_id: str = None,
        aggregator_id: str = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.aggregator_name = aggregator_name
        self.compliance_pack_name = compliance_pack_name
        self.creator_name = creator_name
        self.creator_type = creator_type
        self.creator_id = creator_id
        self.aggregator_id = aggregator_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.aggregator_name is not None:
            result['AggregatorName'] = self.aggregator_name
        if self.compliance_pack_name is not None:
            result['CompliancePackName'] = self.compliance_pack_name
        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name
        if self.creator_type is not None:
            result['CreatorType'] = self.creator_type
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('AggregatorName') is not None:
            self.aggregator_name = m.get('AggregatorName')
        if m.get('CompliancePackName') is not None:
            self.compliance_pack_name = m.get('CompliancePackName')
        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')
        if m.get('CreatorType') is not None:
            self.creator_type = m.get('CreatorType')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        return self


class GetAggregateConfigRuleResponseBodyConfigRuleConfigRuleEvaluationStatus(TeaModel):
    def __init__(
        self,
        last_error_code: str = None,
        last_successful_evaluation_timestamp: int = None,
        first_activated_timestamp: int = None,
        first_evaluation_started: bool = None,
        last_successful_invocation_timestamp: int = None,
        last_error_message: str = None,
        last_failed_evaluation_timestamp: int = None,
        last_failed_invocation_timestamp: int = None,
    ):
        self.last_error_code = last_error_code
        self.last_successful_evaluation_timestamp = last_successful_evaluation_timestamp
        self.first_activated_timestamp = first_activated_timestamp
        self.first_evaluation_started = first_evaluation_started
        self.last_successful_invocation_timestamp = last_successful_invocation_timestamp
        self.last_error_message = last_error_message
        self.last_failed_evaluation_timestamp = last_failed_evaluation_timestamp
        self.last_failed_invocation_timestamp = last_failed_invocation_timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_error_code is not None:
            result['LastErrorCode'] = self.last_error_code
        if self.last_successful_evaluation_timestamp is not None:
            result['LastSuccessfulEvaluationTimestamp'] = self.last_successful_evaluation_timestamp
        if self.first_activated_timestamp is not None:
            result['FirstActivatedTimestamp'] = self.first_activated_timestamp
        if self.first_evaluation_started is not None:
            result['FirstEvaluationStarted'] = self.first_evaluation_started
        if self.last_successful_invocation_timestamp is not None:
            result['LastSuccessfulInvocationTimestamp'] = self.last_successful_invocation_timestamp
        if self.last_error_message is not None:
            result['LastErrorMessage'] = self.last_error_message
        if self.last_failed_evaluation_timestamp is not None:
            result['LastFailedEvaluationTimestamp'] = self.last_failed_evaluation_timestamp
        if self.last_failed_invocation_timestamp is not None:
            result['LastFailedInvocationTimestamp'] = self.last_failed_invocation_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastErrorCode') is not None:
            self.last_error_code = m.get('LastErrorCode')
        if m.get('LastSuccessfulEvaluationTimestamp') is not None:
            self.last_successful_evaluation_timestamp = m.get('LastSuccessfulEvaluationTimestamp')
        if m.get('FirstActivatedTimestamp') is not None:
            self.first_activated_timestamp = m.get('FirstActivatedTimestamp')
        if m.get('FirstEvaluationStarted') is not None:
            self.first_evaluation_started = m.get('FirstEvaluationStarted')
        if m.get('LastSuccessfulInvocationTimestamp') is not None:
            self.last_successful_invocation_timestamp = m.get('LastSuccessfulInvocationTimestamp')
        if m.get('LastErrorMessage') is not None:
            self.last_error_message = m.get('LastErrorMessage')
        if m.get('LastFailedEvaluationTimestamp') is not None:
            self.last_failed_evaluation_timestamp = m.get('LastFailedEvaluationTimestamp')
        if m.get('LastFailedInvocationTimestamp') is not None:
            self.last_failed_invocation_timestamp = m.get('LastFailedInvocationTimestamp')
        return self


class GetAggregateConfigRuleResponseBodyConfigRule(TeaModel):
    def __init__(
        self,
        risk_level: int = None,
        input_parameters: Dict[str, Any] = None,
        source: GetAggregateConfigRuleResponseBodyConfigRuleSource = None,
        config_rule_state: str = None,
        maximum_execution_frequency: str = None,
        managed_rule: GetAggregateConfigRuleResponseBodyConfigRuleManagedRule = None,
        config_rule_arn: str = None,
        description: str = None,
        create_by: GetAggregateConfigRuleResponseBodyConfigRuleCreateBy = None,
        config_rule_name: str = None,
        config_rule_evaluation_status: GetAggregateConfigRuleResponseBodyConfigRuleConfigRuleEvaluationStatus = None,
        config_rule_id: str = None,
        modified_timestamp: int = None,
        create_timestamp: int = None,
        resource_types_scope: str = None,
        region_ids_scope: str = None,
        exclude_resource_ids_scope: str = None,
        resource_group_ids_scope: str = None,
        tag_key_scope: str = None,
        tag_value_scope: str = None,
        config_rule_trigger_types: str = None,
    ):
        self.risk_level = risk_level
        self.input_parameters = input_parameters
        self.source = source
        self.config_rule_state = config_rule_state
        self.maximum_execution_frequency = maximum_execution_frequency
        self.managed_rule = managed_rule
        self.config_rule_arn = config_rule_arn
        self.description = description
        self.create_by = create_by
        self.config_rule_name = config_rule_name
        self.config_rule_evaluation_status = config_rule_evaluation_status
        self.config_rule_id = config_rule_id
        self.modified_timestamp = modified_timestamp
        self.create_timestamp = create_timestamp
        self.resource_types_scope = resource_types_scope
        self.region_ids_scope = region_ids_scope
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        self.resource_group_ids_scope = resource_group_ids_scope
        self.tag_key_scope = tag_key_scope
        self.tag_value_scope = tag_value_scope
        self.config_rule_trigger_types = config_rule_trigger_types

    def validate(self):
        if self.source:
            self.source.validate()
        if self.managed_rule:
            self.managed_rule.validate()
        if self.create_by:
            self.create_by.validate()
        if self.config_rule_evaluation_status:
            self.config_rule_evaluation_status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.input_parameters is not None:
            result['InputParameters'] = self.input_parameters
        if self.source is not None:
            result['Source'] = self.source.to_map()
        if self.config_rule_state is not None:
            result['ConfigRuleState'] = self.config_rule_state
        if self.maximum_execution_frequency is not None:
            result['MaximumExecutionFrequency'] = self.maximum_execution_frequency
        if self.managed_rule is not None:
            result['ManagedRule'] = self.managed_rule.to_map()
        if self.config_rule_arn is not None:
            result['ConfigRuleArn'] = self.config_rule_arn
        if self.description is not None:
            result['Description'] = self.description
        if self.create_by is not None:
            result['CreateBy'] = self.create_by.to_map()
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        if self.config_rule_evaluation_status is not None:
            result['ConfigRuleEvaluationStatus'] = self.config_rule_evaluation_status.to_map()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.modified_timestamp is not None:
            result['ModifiedTimestamp'] = self.modified_timestamp
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.resource_types_scope is not None:
            result['ResourceTypesScope'] = self.resource_types_scope
        if self.region_ids_scope is not None:
            result['RegionIdsScope'] = self.region_ids_scope
        if self.exclude_resource_ids_scope is not None:
            result['ExcludeResourceIdsScope'] = self.exclude_resource_ids_scope
        if self.resource_group_ids_scope is not None:
            result['ResourceGroupIdsScope'] = self.resource_group_ids_scope
        if self.tag_key_scope is not None:
            result['TagKeyScope'] = self.tag_key_scope
        if self.tag_value_scope is not None:
            result['TagValueScope'] = self.tag_value_scope
        if self.config_rule_trigger_types is not None:
            result['ConfigRuleTriggerTypes'] = self.config_rule_trigger_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('InputParameters') is not None:
            self.input_parameters = m.get('InputParameters')
        if m.get('Source') is not None:
            temp_model = GetAggregateConfigRuleResponseBodyConfigRuleSource()
            self.source = temp_model.from_map(m['Source'])
        if m.get('ConfigRuleState') is not None:
            self.config_rule_state = m.get('ConfigRuleState')
        if m.get('MaximumExecutionFrequency') is not None:
            self.maximum_execution_frequency = m.get('MaximumExecutionFrequency')
        if m.get('ManagedRule') is not None:
            temp_model = GetAggregateConfigRuleResponseBodyConfigRuleManagedRule()
            self.managed_rule = temp_model.from_map(m['ManagedRule'])
        if m.get('ConfigRuleArn') is not None:
            self.config_rule_arn = m.get('ConfigRuleArn')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CreateBy') is not None:
            temp_model = GetAggregateConfigRuleResponseBodyConfigRuleCreateBy()
            self.create_by = temp_model.from_map(m['CreateBy'])
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        if m.get('ConfigRuleEvaluationStatus') is not None:
            temp_model = GetAggregateConfigRuleResponseBodyConfigRuleConfigRuleEvaluationStatus()
            self.config_rule_evaluation_status = temp_model.from_map(m['ConfigRuleEvaluationStatus'])
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('ModifiedTimestamp') is not None:
            self.modified_timestamp = m.get('ModifiedTimestamp')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('ResourceTypesScope') is not None:
            self.resource_types_scope = m.get('ResourceTypesScope')
        if m.get('RegionIdsScope') is not None:
            self.region_ids_scope = m.get('RegionIdsScope')
        if m.get('ExcludeResourceIdsScope') is not None:
            self.exclude_resource_ids_scope = m.get('ExcludeResourceIdsScope')
        if m.get('ResourceGroupIdsScope') is not None:
            self.resource_group_ids_scope = m.get('ResourceGroupIdsScope')
        if m.get('TagKeyScope') is not None:
            self.tag_key_scope = m.get('TagKeyScope')
        if m.get('TagValueScope') is not None:
            self.tag_value_scope = m.get('TagValueScope')
        if m.get('ConfigRuleTriggerTypes') is not None:
            self.config_rule_trigger_types = m.get('ConfigRuleTriggerTypes')
        return self


class GetAggregateConfigRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        config_rule: GetAggregateConfigRuleResponseBodyConfigRule = None,
    ):
        self.request_id = request_id
        self.config_rule = config_rule

    def validate(self):
        if self.config_rule:
            self.config_rule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.config_rule is not None:
            result['ConfigRule'] = self.config_rule.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ConfigRule') is not None:
            temp_model = GetAggregateConfigRuleResponseBodyConfigRule()
            self.config_rule = temp_model.from_map(m['ConfigRule'])
        return self


class GetAggregateConfigRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAggregateConfigRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAggregateConfigRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAggregateResourceCountsGroupByRegionRequest(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        aggregator_id: str = None,
    ):
        self.resource_type = resource_type
        self.aggregator_id = aggregator_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        return self


class GetAggregateResourceCountsGroupByRegionResponseBodyDiscoveredResourceCountsSummary(TeaModel):
    def __init__(
        self,
        resource_count: int = None,
        region: str = None,
    ):
        self.resource_count = resource_count
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_count is not None:
            result['ResourceCount'] = self.resource_count
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceCount') is not None:
            self.resource_count = m.get('ResourceCount')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class GetAggregateResourceCountsGroupByRegionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        discovered_resource_counts_summary: List[GetAggregateResourceCountsGroupByRegionResponseBodyDiscoveredResourceCountsSummary] = None,
    ):
        self.request_id = request_id
        self.discovered_resource_counts_summary = discovered_resource_counts_summary

    def validate(self):
        if self.discovered_resource_counts_summary:
            for k in self.discovered_resource_counts_summary:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['DiscoveredResourceCountsSummary'] = []
        if self.discovered_resource_counts_summary is not None:
            for k in self.discovered_resource_counts_summary:
                result['DiscoveredResourceCountsSummary'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.discovered_resource_counts_summary = []
        if m.get('DiscoveredResourceCountsSummary') is not None:
            for k in m.get('DiscoveredResourceCountsSummary'):
                temp_model = GetAggregateResourceCountsGroupByRegionResponseBodyDiscoveredResourceCountsSummary()
                self.discovered_resource_counts_summary.append(temp_model.from_map(k))
        return self


class GetAggregateResourceCountsGroupByRegionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAggregateResourceCountsGroupByRegionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAggregateResourceCountsGroupByRegionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConfigRuleComplianceByPackRequest(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
    ):
        self.compliance_pack_id = compliance_pack_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        return self


class GetConfigRuleComplianceByPackResponseBodyConfigRuleComplianceResultConfigRuleCompliances(TeaModel):
    def __init__(
        self,
        compliance_type: str = None,
        config_rule_name: str = None,
        config_rule_id: str = None,
    ):
        self.compliance_type = compliance_type
        self.config_rule_name = config_rule_name
        self.config_rule_id = config_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        return self


class GetConfigRuleComplianceByPackResponseBodyConfigRuleComplianceResult(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        non_compliant_count: int = None,
        config_rule_compliances: List[GetConfigRuleComplianceByPackResponseBodyConfigRuleComplianceResultConfigRuleCompliances] = None,
        total_count: int = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.non_compliant_count = non_compliant_count
        self.config_rule_compliances = config_rule_compliances
        self.total_count = total_count

    def validate(self):
        if self.config_rule_compliances:
            for k in self.config_rule_compliances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.non_compliant_count is not None:
            result['NonCompliantCount'] = self.non_compliant_count
        result['ConfigRuleCompliances'] = []
        if self.config_rule_compliances is not None:
            for k in self.config_rule_compliances:
                result['ConfigRuleCompliances'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('NonCompliantCount') is not None:
            self.non_compliant_count = m.get('NonCompliantCount')
        self.config_rule_compliances = []
        if m.get('ConfigRuleCompliances') is not None:
            for k in m.get('ConfigRuleCompliances'):
                temp_model = GetConfigRuleComplianceByPackResponseBodyConfigRuleComplianceResultConfigRuleCompliances()
                self.config_rule_compliances.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetConfigRuleComplianceByPackResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        config_rule_compliance_result: GetConfigRuleComplianceByPackResponseBodyConfigRuleComplianceResult = None,
    ):
        self.request_id = request_id
        self.config_rule_compliance_result = config_rule_compliance_result

    def validate(self):
        if self.config_rule_compliance_result:
            self.config_rule_compliance_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.config_rule_compliance_result is not None:
            result['ConfigRuleComplianceResult'] = self.config_rule_compliance_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ConfigRuleComplianceResult') is not None:
            temp_model = GetConfigRuleComplianceByPackResponseBodyConfigRuleComplianceResult()
            self.config_rule_compliance_result = temp_model.from_map(m['ConfigRuleComplianceResult'])
        return self


class GetConfigRuleComplianceByPackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetConfigRuleComplianceByPackResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetConfigRuleComplianceByPackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConfigRuleSummaryByRiskLevelResponseBodyConfigRuleSummaries(TeaModel):
    def __init__(
        self,
        risk_level: int = None,
        compliant_count: int = None,
        non_compliant_count: int = None,
    ):
        self.risk_level = risk_level
        self.compliant_count = compliant_count
        self.non_compliant_count = non_compliant_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.compliant_count is not None:
            result['CompliantCount'] = self.compliant_count
        if self.non_compliant_count is not None:
            result['NonCompliantCount'] = self.non_compliant_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('CompliantCount') is not None:
            self.compliant_count = m.get('CompliantCount')
        if m.get('NonCompliantCount') is not None:
            self.non_compliant_count = m.get('NonCompliantCount')
        return self


class GetConfigRuleSummaryByRiskLevelResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        config_rule_summaries: List[GetConfigRuleSummaryByRiskLevelResponseBodyConfigRuleSummaries] = None,
    ):
        self.request_id = request_id
        self.config_rule_summaries = config_rule_summaries

    def validate(self):
        if self.config_rule_summaries:
            for k in self.config_rule_summaries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ConfigRuleSummaries'] = []
        if self.config_rule_summaries is not None:
            for k in self.config_rule_summaries:
                result['ConfigRuleSummaries'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.config_rule_summaries = []
        if m.get('ConfigRuleSummaries') is not None:
            for k in m.get('ConfigRuleSummaries'):
                temp_model = GetConfigRuleSummaryByRiskLevelResponseBodyConfigRuleSummaries()
                self.config_rule_summaries.append(temp_model.from_map(k))
        return self


class GetConfigRuleSummaryByRiskLevelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetConfigRuleSummaryByRiskLevelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetConfigRuleSummaryByRiskLevelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartRemediationRequest(TeaModel):
    def __init__(
        self,
        config_rule_id: str = None,
    ):
        self.config_rule_id = config_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        return self


class StartRemediationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: bool = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class StartRemediationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartRemediationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartRemediationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateCompliancePackReportRequest(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        client_token: str = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class GenerateCompliancePackReportResponseBody(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        request_id: str = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateCompliancePackReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GenerateCompliancePackReportResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GenerateCompliancePackReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartAggregateRemediationRequest(TeaModel):
    def __init__(
        self,
        config_rule_id: str = None,
        aggregator_id: str = None,
    ):
        self.config_rule_id = config_rule_id
        self.aggregator_id = aggregator_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        return self


class StartAggregateRemediationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: bool = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class StartAggregateRemediationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartAggregateRemediationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartAggregateRemediationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRemediationsRequest(TeaModel):
    def __init__(
        self,
        config_rule_ids: str = None,
    ):
        self.config_rule_ids = config_rule_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_ids is not None:
            result['ConfigRuleIds'] = self.config_rule_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleIds') is not None:
            self.config_rule_ids = m.get('ConfigRuleIds')
        return self


class ListRemediationsResponseBodyRemediations(TeaModel):
    def __init__(
        self,
        last_successful_invocation_type: str = None,
        remediation_template_id: str = None,
        remediation_dynamic_params: str = None,
        remediation_id: str = None,
        remediation_source_type: str = None,
        remediation_type: str = None,
        last_successful_invocation_id: str = None,
        account_id: int = None,
        invoke_type: str = None,
        config_rule_id: str = None,
        last_successful_invocation_time: int = None,
    ):
        self.last_successful_invocation_type = last_successful_invocation_type
        self.remediation_template_id = remediation_template_id
        self.remediation_dynamic_params = remediation_dynamic_params
        self.remediation_id = remediation_id
        self.remediation_source_type = remediation_source_type
        self.remediation_type = remediation_type
        self.last_successful_invocation_id = last_successful_invocation_id
        self.account_id = account_id
        self.invoke_type = invoke_type
        self.config_rule_id = config_rule_id
        self.last_successful_invocation_time = last_successful_invocation_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_successful_invocation_type is not None:
            result['LastSuccessfulInvocationType'] = self.last_successful_invocation_type
        if self.remediation_template_id is not None:
            result['RemediationTemplateId'] = self.remediation_template_id
        if self.remediation_dynamic_params is not None:
            result['RemediationDynamicParams'] = self.remediation_dynamic_params
        if self.remediation_id is not None:
            result['RemediationId'] = self.remediation_id
        if self.remediation_source_type is not None:
            result['RemediationSourceType'] = self.remediation_source_type
        if self.remediation_type is not None:
            result['RemediationType'] = self.remediation_type
        if self.last_successful_invocation_id is not None:
            result['LastSuccessfulInvocationId'] = self.last_successful_invocation_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.invoke_type is not None:
            result['InvokeType'] = self.invoke_type
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.last_successful_invocation_time is not None:
            result['LastSuccessfulInvocationTime'] = self.last_successful_invocation_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastSuccessfulInvocationType') is not None:
            self.last_successful_invocation_type = m.get('LastSuccessfulInvocationType')
        if m.get('RemediationTemplateId') is not None:
            self.remediation_template_id = m.get('RemediationTemplateId')
        if m.get('RemediationDynamicParams') is not None:
            self.remediation_dynamic_params = m.get('RemediationDynamicParams')
        if m.get('RemediationId') is not None:
            self.remediation_id = m.get('RemediationId')
        if m.get('RemediationSourceType') is not None:
            self.remediation_source_type = m.get('RemediationSourceType')
        if m.get('RemediationType') is not None:
            self.remediation_type = m.get('RemediationType')
        if m.get('LastSuccessfulInvocationId') is not None:
            self.last_successful_invocation_id = m.get('LastSuccessfulInvocationId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('InvokeType') is not None:
            self.invoke_type = m.get('InvokeType')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('LastSuccessfulInvocationTime') is not None:
            self.last_successful_invocation_time = m.get('LastSuccessfulInvocationTime')
        return self


class ListRemediationsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        remediations: List[ListRemediationsResponseBodyRemediations] = None,
    ):
        self.request_id = request_id
        self.remediations = remediations

    def validate(self):
        if self.remediations:
            for k in self.remediations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Remediations'] = []
        if self.remediations is not None:
            for k in self.remediations:
                result['Remediations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.remediations = []
        if m.get('Remediations') is not None:
            for k in m.get('Remediations'):
                temp_model = ListRemediationsResponseBodyRemediations()
                self.remediations.append(temp_model.from_map(k))
        return self


class ListRemediationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRemediationsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListRemediationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAggregatorRequestAggregatorAccounts(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        account_name: str = None,
        account_type: str = None,
    ):
        self.account_id = account_id
        self.account_name = account_name
        self.account_type = account_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        return self


class UpdateAggregatorRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        aggregator_name: str = None,
        description: str = None,
        aggregator_accounts: List[UpdateAggregatorRequestAggregatorAccounts] = None,
        client_token: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.aggregator_name = aggregator_name
        self.description = description
        self.aggregator_accounts = aggregator_accounts
        self.client_token = client_token

    def validate(self):
        if self.aggregator_accounts:
            for k in self.aggregator_accounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.aggregator_name is not None:
            result['AggregatorName'] = self.aggregator_name
        if self.description is not None:
            result['Description'] = self.description
        result['AggregatorAccounts'] = []
        if self.aggregator_accounts is not None:
            for k in self.aggregator_accounts:
                result['AggregatorAccounts'].append(k.to_map() if k else None)
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('AggregatorName') is not None:
            self.aggregator_name = m.get('AggregatorName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.aggregator_accounts = []
        if m.get('AggregatorAccounts') is not None:
            for k in m.get('AggregatorAccounts'):
                temp_model = UpdateAggregatorRequestAggregatorAccounts()
                self.aggregator_accounts.append(temp_model.from_map(k))
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class UpdateAggregatorShrinkRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        aggregator_name: str = None,
        description: str = None,
        aggregator_accounts_shrink: str = None,
        client_token: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.aggregator_name = aggregator_name
        self.description = description
        self.aggregator_accounts_shrink = aggregator_accounts_shrink
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.aggregator_name is not None:
            result['AggregatorName'] = self.aggregator_name
        if self.description is not None:
            result['Description'] = self.description
        if self.aggregator_accounts_shrink is not None:
            result['AggregatorAccounts'] = self.aggregator_accounts_shrink
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('AggregatorName') is not None:
            self.aggregator_name = m.get('AggregatorName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AggregatorAccounts') is not None:
            self.aggregator_accounts_shrink = m.get('AggregatorAccounts')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class UpdateAggregatorResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        aggregator_id: str = None,
    ):
        self.request_id = request_id
        self.aggregator_id = aggregator_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        return self


class UpdateAggregatorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAggregatorResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateAggregatorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


