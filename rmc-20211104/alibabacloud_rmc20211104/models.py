# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class SearchResourcesRequestFilter(TeaModel):
    def __init__(
        self,
        key: str = None,
        match_type: str = None,
        value: List[str] = None,
    ):
        self.key = key
        self.match_type = match_type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SearchResourcesRequest(TeaModel):
    def __init__(
        self,
        filter: List[SearchResourcesRequestFilter] = None,
        max_results: int = None,
        next_token: str = None,
        resource_group_id: str = None,
    ):
        self.filter = filter
        self.max_results = max_results
        self.next_token = next_token
        self.resource_group_id = resource_group_id

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = SearchResourcesRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class SearchResourcesResponseBodyFilters(TeaModel):
    def __init__(
        self,
        key: str = None,
        match_type: str = None,
        values: List[str] = None,
    ):
        self.key = key
        self.match_type = match_type
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class SearchResourcesResponseBodyResourcesTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SearchResourcesResponseBodyResources(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        create_time: str = None,
        ip_addresses: List[str] = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        tags: List[SearchResourcesResponseBodyResourcesTags] = None,
        zone_id: str = None,
    ):
        self.account_id = account_id
        self.create_time = create_time
        self.ip_addresses = ip_addresses
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_type = resource_type
        self.tags = tags
        self.zone_id = zone_id

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.ip_addresses is not None:
            result['IpAddresses'] = self.ip_addresses
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('IpAddresses') is not None:
            self.ip_addresses = m.get('IpAddresses')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = SearchResourcesResponseBodyResourcesTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class SearchResourcesResponseBody(TeaModel):
    def __init__(
        self,
        filters: List[SearchResourcesResponseBodyFilters] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        resources: List[SearchResourcesResponseBodyResources] = None,
    ):
        self.filters = filters
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.resources = resources

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = SearchResourcesResponseBodyFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = SearchResourcesResponseBodyResources()
                self.resources.append(temp_model.from_map(k))
        return self


class SearchResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchResourcesResponseBody = None,
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
            temp_model = SearchResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


