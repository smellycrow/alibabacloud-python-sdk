# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddDomainRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        domain_name: str = None,
    ):
        self.account_id = account_id
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class AddDomainResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        domain_name: str = None,
    ):
        self.request_id = request_id
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class AddDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddDomainResponseBody = None,
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
            temp_model = AddDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDomainRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        domain_name: str = None,
    ):
        self.account_id = account_id
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DeleteDomainResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        domain_name: str = None,
    ):
        self.request_id = request_id
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DeleteDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDomainResponseBody = None,
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
            temp_model = DeleteDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainsRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.account_id = account_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeDomainsResponseBodyDomainsDomain(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
    ):
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeDomainsResponseBodyDomains(TeaModel):
    def __init__(
        self,
        domain: List[DescribeDomainsResponseBodyDomainsDomain] = None,
    ):
        self.domain = domain

    def validate(self):
        if self.domain:
            for k in self.domain:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Domain'] = []
        if self.domain is not None:
            for k in self.domain:
                result['Domain'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain = []
        if m.get('Domain') is not None:
            for k in m.get('Domain'):
                temp_model = DescribeDomainsResponseBodyDomainsDomain()
                self.domain.append(temp_model.from_map(k))
        return self


class DescribeDomainsResponseBody(TeaModel):
    def __init__(
        self,
        domains: DescribeDomainsResponseBodyDomains = None,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
    ):
        self.domains = domains
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number

    def validate(self):
        if self.domains:
            self.domains.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domains is not None:
            result['Domains'] = self.domains.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domains') is not None:
            temp_model = DescribeDomainsResponseBodyDomains()
            self.domains = temp_model.from_map(m['Domains'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeDomainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainsResponseBody = None,
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
            temp_model = DescribeDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccountInfoResponseBodyAccountInfo(TeaModel):
    def __init__(
        self,
        sign_secret: str = None,
        signed_count: int = None,
        month_resolve_count: int = None,
        account_id: str = None,
        unsigned_enabled: bool = None,
        unsigned_count: int = None,
        month_https_resolve_count: int = None,
        month_free_count: int = None,
    ):
        self.sign_secret = sign_secret
        self.signed_count = signed_count
        self.month_resolve_count = month_resolve_count
        self.account_id = account_id
        self.unsigned_enabled = unsigned_enabled
        self.unsigned_count = unsigned_count
        self.month_https_resolve_count = month_https_resolve_count
        self.month_free_count = month_free_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sign_secret is not None:
            result['SignSecret'] = self.sign_secret
        if self.signed_count is not None:
            result['SignedCount'] = self.signed_count
        if self.month_resolve_count is not None:
            result['MonthResolveCount'] = self.month_resolve_count
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.unsigned_enabled is not None:
            result['UnsignedEnabled'] = self.unsigned_enabled
        if self.unsigned_count is not None:
            result['UnsignedCount'] = self.unsigned_count
        if self.month_https_resolve_count is not None:
            result['MonthHttpsResolveCount'] = self.month_https_resolve_count
        if self.month_free_count is not None:
            result['MonthFreeCount'] = self.month_free_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SignSecret') is not None:
            self.sign_secret = m.get('SignSecret')
        if m.get('SignedCount') is not None:
            self.signed_count = m.get('SignedCount')
        if m.get('MonthResolveCount') is not None:
            self.month_resolve_count = m.get('MonthResolveCount')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('UnsignedEnabled') is not None:
            self.unsigned_enabled = m.get('UnsignedEnabled')
        if m.get('UnsignedCount') is not None:
            self.unsigned_count = m.get('UnsignedCount')
        if m.get('MonthHttpsResolveCount') is not None:
            self.month_https_resolve_count = m.get('MonthHttpsResolveCount')
        if m.get('MonthFreeCount') is not None:
            self.month_free_count = m.get('MonthFreeCount')
        return self


class GetAccountInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        account_info: GetAccountInfoResponseBodyAccountInfo = None,
    ):
        self.request_id = request_id
        self.account_info = account_info

    def validate(self):
        if self.account_info:
            self.account_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.account_info is not None:
            result['AccountInfo'] = self.account_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AccountInfo') is not None:
            temp_model = GetAccountInfoResponseBodyAccountInfo()
            self.account_info = temp_model.from_map(m['AccountInfo'])
        return self


class GetAccountInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAccountInfoResponseBody = None,
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
            temp_model = GetAccountInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResolveCountSummaryRequest(TeaModel):
    def __init__(
        self,
        granularity: str = None,
        time_span: int = None,
    ):
        self.granularity = granularity
        self.time_span = time_span

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.granularity is not None:
            result['Granularity'] = self.granularity
        if self.time_span is not None:
            result['TimeSpan'] = self.time_span
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')
        if m.get('TimeSpan') is not None:
            self.time_span = m.get('TimeSpan')
        return self


class GetResolveCountSummaryResponseBodyResolveSummary(TeaModel):
    def __init__(
        self,
        https: int = None,
        https_6: int = None,
        http_6: int = None,
        http: int = None,
    ):
        self.https = https
        self.https_6 = https_6
        self.http_6 = http_6
        self.http = http

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.https is not None:
            result['Https'] = self.https
        if self.https_6 is not None:
            result['Https6'] = self.https_6
        if self.http_6 is not None:
            result['Http6'] = self.http_6
        if self.http is not None:
            result['Http'] = self.http
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Https') is not None:
            self.https = m.get('Https')
        if m.get('Https6') is not None:
            self.https_6 = m.get('Https6')
        if m.get('Http6') is not None:
            self.http_6 = m.get('Http6')
        if m.get('Http') is not None:
            self.http = m.get('Http')
        return self


class GetResolveCountSummaryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resolve_summary: GetResolveCountSummaryResponseBodyResolveSummary = None,
    ):
        self.request_id = request_id
        self.resolve_summary = resolve_summary

    def validate(self):
        if self.resolve_summary:
            self.resolve_summary.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resolve_summary is not None:
            result['ResolveSummary'] = self.resolve_summary.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResolveSummary') is not None:
            temp_model = GetResolveCountSummaryResponseBodyResolveSummary()
            self.resolve_summary = temp_model.from_map(m['ResolveSummary'])
        return self


class GetResolveCountSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetResolveCountSummaryResponseBody = None,
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
            temp_model = GetResolveCountSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResolveStatisticsRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        granularity: str = None,
        time_span: int = None,
        protocol_name: str = None,
    ):
        self.domain_name = domain_name
        self.granularity = granularity
        self.time_span = time_span
        self.protocol_name = protocol_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.granularity is not None:
            result['Granularity'] = self.granularity
        if self.time_span is not None:
            result['TimeSpan'] = self.time_span
        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')
        if m.get('TimeSpan') is not None:
            self.time_span = m.get('TimeSpan')
        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')
        return self


class GetResolveStatisticsResponseBodyDataPointsDataPoint(TeaModel):
    def __init__(
        self,
        time: int = None,
        count: int = None,
    ):
        self.time = time
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class GetResolveStatisticsResponseBodyDataPoints(TeaModel):
    def __init__(
        self,
        data_point: List[GetResolveStatisticsResponseBodyDataPointsDataPoint] = None,
    ):
        self.data_point = data_point

    def validate(self):
        if self.data_point:
            for k in self.data_point:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataPoint'] = []
        if self.data_point is not None:
            for k in self.data_point:
                result['DataPoint'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_point = []
        if m.get('DataPoint') is not None:
            for k in m.get('DataPoint'):
                temp_model = GetResolveStatisticsResponseBodyDataPointsDataPoint()
                self.data_point.append(temp_model.from_map(k))
        return self


class GetResolveStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data_points: GetResolveStatisticsResponseBodyDataPoints = None,
    ):
        self.request_id = request_id
        self.data_points = data_points

    def validate(self):
        if self.data_points:
            self.data_points.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data_points is not None:
            result['DataPoints'] = self.data_points.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DataPoints') is not None:
            temp_model = GetResolveStatisticsResponseBodyDataPoints()
            self.data_points = temp_model.from_map(m['DataPoints'])
        return self


class GetResolveStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetResolveStatisticsResponseBody = None,
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
            temp_model = GetResolveStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDomainsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListDomainsResponseBodyDomainInfosDomainInfo(TeaModel):
    def __init__(
        self,
        resolved_https_6: int = None,
        resolved: int = None,
        resolved_6: int = None,
        domain_name: str = None,
        resolved_https: int = None,
    ):
        self.resolved_https_6 = resolved_https_6
        self.resolved = resolved
        self.resolved_6 = resolved_6
        self.domain_name = domain_name
        self.resolved_https = resolved_https

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resolved_https_6 is not None:
            result['ResolvedHttps6'] = self.resolved_https_6
        if self.resolved is not None:
            result['Resolved'] = self.resolved
        if self.resolved_6 is not None:
            result['Resolved6'] = self.resolved_6
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.resolved_https is not None:
            result['ResolvedHttps'] = self.resolved_https
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResolvedHttps6') is not None:
            self.resolved_https_6 = m.get('ResolvedHttps6')
        if m.get('Resolved') is not None:
            self.resolved = m.get('Resolved')
        if m.get('Resolved6') is not None:
            self.resolved_6 = m.get('Resolved6')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ResolvedHttps') is not None:
            self.resolved_https = m.get('ResolvedHttps')
        return self


class ListDomainsResponseBodyDomainInfos(TeaModel):
    def __init__(
        self,
        domain_info: List[ListDomainsResponseBodyDomainInfosDomainInfo] = None,
    ):
        self.domain_info = domain_info

    def validate(self):
        if self.domain_info:
            for k in self.domain_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DomainInfo'] = []
        if self.domain_info is not None:
            for k in self.domain_info:
                result['DomainInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_info = []
        if m.get('DomainInfo') is not None:
            for k in m.get('DomainInfo'):
                temp_model = ListDomainsResponseBodyDomainInfosDomainInfo()
                self.domain_info.append(temp_model.from_map(k))
        return self


class ListDomainsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        domain_infos: ListDomainsResponseBodyDomainInfos = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.domain_infos = domain_infos

    def validate(self):
        if self.domain_infos:
            self.domain_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.domain_infos is not None:
            result['DomainInfos'] = self.domain_infos.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('DomainInfos') is not None:
            temp_model = ListDomainsResponseBodyDomainInfos()
            self.domain_infos = temp_model.from_map(m['DomainInfos'])
        return self


class ListDomainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDomainsResponseBody = None,
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
            temp_model = ListDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


