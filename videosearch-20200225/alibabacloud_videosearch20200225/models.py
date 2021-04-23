# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, BinaryIO


class AddDeletionAudioTaskRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        audio_id: str = None,
        instance_id: str = None,
    ):
        self.client_token = client_token
        self.audio_id = audio_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.audio_id is not None:
            result['AudioId'] = self.audio_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('AudioId') is not None:
            self.audio_id = m.get('AudioId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class AddDeletionAudioTaskResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: bool = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')

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


class GetAudioTaskStatusRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        task_id: str = None,
        instance_id: str = None,
    ):
        self.client_token = client_token
        self.task_id = task_id
        self.instance_id = instance_id

    def validate(self):
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetAudioTaskStatusResponseTaskInfo(TeaModel):
    def __init__(
        self,
        analysis_use_time: int = None,
        duration: float = None,
        process_result_oss: str = None,
        status: int = None,
        submit_time: int = None,
        finish_time: int = None,
        task_id: int = None,
        error_info: str = None,
        storage_info: int = None,
        description: str = None,
        audio_id: str = None,
        audio_tags: str = None,
        audio_url: str = None,
        query_tags: str = None,
        resource_type: str = None,
        replace_storage_threshold: str = None,
    ):
        self.analysis_use_time = analysis_use_time
        self.duration = duration
        self.process_result_oss = process_result_oss
        self.status = status
        self.submit_time = submit_time
        self.finish_time = finish_time
        self.task_id = task_id
        self.error_info = error_info
        self.storage_info = storage_info
        self.description = description
        self.audio_id = audio_id
        self.audio_tags = audio_tags
        self.audio_url = audio_url
        self.query_tags = query_tags
        self.resource_type = resource_type
        self.replace_storage_threshold = replace_storage_threshold

    def validate(self):
        self.validate_required(self.analysis_use_time, 'analysis_use_time')
        self.validate_required(self.duration, 'duration')
        self.validate_required(self.process_result_oss, 'process_result_oss')
        self.validate_required(self.status, 'status')
        self.validate_required(self.submit_time, 'submit_time')
        self.validate_required(self.finish_time, 'finish_time')
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.error_info, 'error_info')
        self.validate_required(self.storage_info, 'storage_info')
        self.validate_required(self.description, 'description')
        self.validate_required(self.audio_id, 'audio_id')
        self.validate_required(self.audio_tags, 'audio_tags')
        self.validate_required(self.audio_url, 'audio_url')
        self.validate_required(self.query_tags, 'query_tags')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.replace_storage_threshold, 'replace_storage_threshold')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analysis_use_time is not None:
            result['AnalysisUseTime'] = self.analysis_use_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.process_result_oss is not None:
            result['ProcessResultOss'] = self.process_result_oss
        if self.status is not None:
            result['Status'] = self.status
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.error_info is not None:
            result['ErrorInfo'] = self.error_info
        if self.storage_info is not None:
            result['StorageInfo'] = self.storage_info
        if self.description is not None:
            result['Description'] = self.description
        if self.audio_id is not None:
            result['AudioId'] = self.audio_id
        if self.audio_tags is not None:
            result['AudioTags'] = self.audio_tags
        if self.audio_url is not None:
            result['AudioUrl'] = self.audio_url
        if self.query_tags is not None:
            result['QueryTags'] = self.query_tags
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.replace_storage_threshold is not None:
            result['ReplaceStorageThreshold'] = self.replace_storage_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnalysisUseTime') is not None:
            self.analysis_use_time = m.get('AnalysisUseTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('ProcessResultOss') is not None:
            self.process_result_oss = m.get('ProcessResultOss')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('ErrorInfo') is not None:
            self.error_info = m.get('ErrorInfo')
        if m.get('StorageInfo') is not None:
            self.storage_info = m.get('StorageInfo')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AudioId') is not None:
            self.audio_id = m.get('AudioId')
        if m.get('AudioTags') is not None:
            self.audio_tags = m.get('AudioTags')
        if m.get('AudioUrl') is not None:
            self.audio_url = m.get('AudioUrl')
        if m.get('QueryTags') is not None:
            self.query_tags = m.get('QueryTags')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ReplaceStorageThreshold') is not None:
            self.replace_storage_threshold = m.get('ReplaceStorageThreshold')
        return self


class GetAudioTaskStatusResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: int = None,
        task_info: GetAudioTaskStatusResponseTaskInfo = None,
    ):
        self.request_id = request_id
        self.data = data
        self.task_info = task_info

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        self.validate_required(self.task_info, 'task_info')
        if self.task_info:
            self.task_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.task_info is not None:
            result['TaskInfo'] = self.task_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('TaskInfo') is not None:
            temp_model = GetAudioTaskStatusResponseTaskInfo()
            self.task_info = temp_model.from_map(m['TaskInfo'])
        return self


class CancelBatchTaskRequest(TeaModel):
    def __init__(
        self,
        batch_task_id: int = None,
    ):
        self.batch_task_id = batch_task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_task_id is not None:
            result['BatchTaskId'] = self.batch_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchTaskId') is not None:
            self.batch_task_id = m.get('BatchTaskId')
        return self


class CancelBatchTaskResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: bool = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')

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


class GetAudioStorageHistoryRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        audio_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.audio_id = audio_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.audio_id, 'audio_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.audio_id is not None:
            result['AudioId'] = self.audio_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AudioId') is not None:
            self.audio_id = m.get('AudioId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetAudioStorageHistoryResponseDataList(TeaModel):
    def __init__(
        self,
        audio_id: str = None,
        description: str = None,
        storage_type: int = None,
        storage_info: int = None,
        modified_time: int = None,
        audio_url: str = None,
    ):
        self.audio_id = audio_id
        self.description = description
        self.storage_type = storage_type
        self.storage_info = storage_info
        self.modified_time = modified_time
        self.audio_url = audio_url

    def validate(self):
        self.validate_required(self.audio_id, 'audio_id')
        self.validate_required(self.description, 'description')
        self.validate_required(self.storage_type, 'storage_type')
        self.validate_required(self.storage_info, 'storage_info')
        self.validate_required(self.modified_time, 'modified_time')
        self.validate_required(self.audio_url, 'audio_url')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_id is not None:
            result['AudioId'] = self.audio_id
        if self.description is not None:
            result['Description'] = self.description
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.storage_info is not None:
            result['StorageInfo'] = self.storage_info
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.audio_url is not None:
            result['AudioUrl'] = self.audio_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioId') is not None:
            self.audio_id = m.get('AudioId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('StorageInfo') is not None:
            self.storage_info = m.get('StorageInfo')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('AudioUrl') is not None:
            self.audio_url = m.get('AudioUrl')
        return self


class GetAudioStorageHistoryResponseData(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        count: int = None,
        list: List[GetAudioStorageHistoryResponseDataList] = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.count = count
        self.list = list

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.count, 'count')
        self.validate_required(self.list, 'list')
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.count is not None:
            result['Count'] = self.count
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = GetAudioStorageHistoryResponseDataList()
                self.list.append(temp_model.from_map(k))
        return self


class GetAudioStorageHistoryResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GetAudioStorageHistoryResponseData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetAudioStorageHistoryResponseData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ModifyPriorityRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        task_id: str = None,
        sort: int = None,
    ):
        self.client_token = client_token
        self.task_id = task_id
        self.sort = sort

    def validate(self):
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.sort, 'sort')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.sort is not None:
            result['Sort'] = self.sort
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        return self


class ModifyPriorityResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: bool = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')

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


class GetAudioInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetAudioInstanceResponseData(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_name: str = None,
        create_time: int = None,
        region_id: str = None,
        instance_status: int = None,
        audio_number: int = None,
        expire_time: int = None,
        concurrency_number: int = None,
        max_audio_capacity: str = None,
        current_audio_capacity: str = None,
        audio_info_update_time: int = None,
        bundling_type: str = None,
    ):
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.create_time = create_time
        self.region_id = region_id
        self.instance_status = instance_status
        self.audio_number = audio_number
        self.expire_time = expire_time
        self.concurrency_number = concurrency_number
        self.max_audio_capacity = max_audio_capacity
        self.current_audio_capacity = current_audio_capacity
        self.audio_info_update_time = audio_info_update_time
        self.bundling_type = bundling_type

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.instance_name, 'instance_name')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.instance_status, 'instance_status')
        self.validate_required(self.audio_number, 'audio_number')
        self.validate_required(self.expire_time, 'expire_time')
        self.validate_required(self.concurrency_number, 'concurrency_number')
        self.validate_required(self.max_audio_capacity, 'max_audio_capacity')
        self.validate_required(self.current_audio_capacity, 'current_audio_capacity')
        self.validate_required(self.audio_info_update_time, 'audio_info_update_time')
        self.validate_required(self.bundling_type, 'bundling_type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.audio_number is not None:
            result['AudioNumber'] = self.audio_number
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.concurrency_number is not None:
            result['ConcurrencyNumber'] = self.concurrency_number
        if self.max_audio_capacity is not None:
            result['MaxAudioCapacity'] = self.max_audio_capacity
        if self.current_audio_capacity is not None:
            result['CurrentAudioCapacity'] = self.current_audio_capacity
        if self.audio_info_update_time is not None:
            result['AudioInfoUpdateTime'] = self.audio_info_update_time
        if self.bundling_type is not None:
            result['BundlingType'] = self.bundling_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('AudioNumber') is not None:
            self.audio_number = m.get('AudioNumber')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('ConcurrencyNumber') is not None:
            self.concurrency_number = m.get('ConcurrencyNumber')
        if m.get('MaxAudioCapacity') is not None:
            self.max_audio_capacity = m.get('MaxAudioCapacity')
        if m.get('CurrentAudioCapacity') is not None:
            self.current_audio_capacity = m.get('CurrentAudioCapacity')
        if m.get('AudioInfoUpdateTime') is not None:
            self.audio_info_update_time = m.get('AudioInfoUpdateTime')
        if m.get('BundlingType') is not None:
            self.bundling_type = m.get('BundlingType')
        return self


class GetAudioInstanceResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GetAudioInstanceResponseData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetAudioInstanceResponseData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetBatchTaskRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        batch_task_id: int = None,
        instance_id: str = None,
    ):
        self.client_token = client_token
        self.batch_task_id = batch_task_id
        self.instance_id = instance_id

    def validate(self):
        self.validate_required(self.batch_task_id, 'batch_task_id')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.batch_task_id is not None:
            result['BatchTaskId'] = self.batch_task_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('BatchTaskId') is not None:
            self.batch_task_id = m.get('BatchTaskId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetBatchTaskResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        batch_task_id: int = None,
        status: int = None,
        modified_time: int = None,
        process_message: str = None,
        sub_task_detail: str = None,
    ):
        self.request_id = request_id
        self.batch_task_id = batch_task_id
        self.status = status
        self.modified_time = modified_time
        self.process_message = process_message
        self.sub_task_detail = sub_task_detail

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.batch_task_id, 'batch_task_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.modified_time, 'modified_time')
        self.validate_required(self.process_message, 'process_message')
        self.validate_required(self.sub_task_detail, 'sub_task_detail')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.batch_task_id is not None:
            result['BatchTaskId'] = self.batch_task_id
        if self.status is not None:
            result['Status'] = self.status
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.process_message is not None:
            result['ProcessMessage'] = self.process_message
        if self.sub_task_detail is not None:
            result['SubTaskDetail'] = self.sub_task_detail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BatchTaskId') is not None:
            self.batch_task_id = m.get('BatchTaskId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ProcessMessage') is not None:
            self.process_message = m.get('ProcessMessage')
        if m.get('SubTaskDetail') is not None:
            self.sub_task_detail = m.get('SubTaskDetail')
        return self


class AddSearchAudioTaskRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        audio_url: str = None,
        return_audio_number: int = None,
        query_tags: str = None,
        callback_url: str = None,
        instance_id: str = None,
        description: str = None,
        content_source: int = None,
        audio_file: str = None,
        sort: int = None,
        need_feature_file: int = None,
        resource_type: int = None,
    ):
        self.client_token = client_token
        self.audio_url = audio_url
        self.return_audio_number = return_audio_number
        self.query_tags = query_tags
        self.callback_url = callback_url
        self.instance_id = instance_id
        self.description = description
        self.content_source = content_source
        self.audio_file = audio_file
        self.sort = sort
        self.need_feature_file = need_feature_file
        self.resource_type = resource_type

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.audio_url is not None:
            result['AudioUrl'] = self.audio_url
        if self.return_audio_number is not None:
            result['ReturnAudioNumber'] = self.return_audio_number
        if self.query_tags is not None:
            result['QueryTags'] = self.query_tags
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.description is not None:
            result['Description'] = self.description
        if self.content_source is not None:
            result['ContentSource'] = self.content_source
        if self.audio_file is not None:
            result['AudioFile'] = self.audio_file
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.need_feature_file is not None:
            result['NeedFeatureFile'] = self.need_feature_file
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('AudioUrl') is not None:
            self.audio_url = m.get('AudioUrl')
        if m.get('ReturnAudioNumber') is not None:
            self.return_audio_number = m.get('ReturnAudioNumber')
        if m.get('QueryTags') is not None:
            self.query_tags = m.get('QueryTags')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ContentSource') is not None:
            self.content_source = m.get('ContentSource')
        if m.get('AudioFile') is not None:
            self.audio_file = m.get('AudioFile')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('NeedFeatureFile') is not None:
            self.need_feature_file = m.get('NeedFeatureFile')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class AddSearchAudioTaskResponseData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class AddSearchAudioTaskResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: AddSearchAudioTaskResponseData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = AddSearchAudioTaskResponseData()
            self.data = temp_model.from_map(m['Data'])
        return self


class AddSearchAudioTaskAdvanceRequest(TeaModel):
    def __init__(
        self,
        audio_file_object: BinaryIO = None,
        client_token: str = None,
        audio_url: str = None,
        return_audio_number: int = None,
        query_tags: str = None,
        callback_url: str = None,
        instance_id: str = None,
        description: str = None,
        content_source: int = None,
        sort: int = None,
        need_feature_file: int = None,
        resource_type: int = None,
    ):
        self.audio_file_object = audio_file_object
        self.client_token = client_token
        self.audio_url = audio_url
        self.return_audio_number = return_audio_number
        self.query_tags = query_tags
        self.callback_url = callback_url
        self.instance_id = instance_id
        self.description = description
        self.content_source = content_source
        self.sort = sort
        self.need_feature_file = need_feature_file
        self.resource_type = resource_type

    def validate(self):
        self.validate_required(self.audio_file_object, 'audio_file_object')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_file_object is not None:
            result['AudioFileObject'] = self.audio_file_object
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.audio_url is not None:
            result['AudioUrl'] = self.audio_url
        if self.return_audio_number is not None:
            result['ReturnAudioNumber'] = self.return_audio_number
        if self.query_tags is not None:
            result['QueryTags'] = self.query_tags
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.description is not None:
            result['Description'] = self.description
        if self.content_source is not None:
            result['ContentSource'] = self.content_source
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.need_feature_file is not None:
            result['NeedFeatureFile'] = self.need_feature_file
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioFileObject') is not None:
            self.audio_file_object = m.get('AudioFileObject')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('AudioUrl') is not None:
            self.audio_url = m.get('AudioUrl')
        if m.get('ReturnAudioNumber') is not None:
            self.return_audio_number = m.get('ReturnAudioNumber')
        if m.get('QueryTags') is not None:
            self.query_tags = m.get('QueryTags')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ContentSource') is not None:
            self.content_source = m.get('ContentSource')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('NeedFeatureFile') is not None:
            self.need_feature_file = m.get('NeedFeatureFile')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class AddStorageAudioTaskRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        audio_url: str = None,
        audio_id: str = None,
        audio_tags: str = None,
        callback_url: str = None,
        description: str = None,
        client_token: str = None,
        content_source: int = None,
        audio_file: str = None,
        sort: int = None,
    ):
        self.instance_id = instance_id
        self.audio_url = audio_url
        self.audio_id = audio_id
        self.audio_tags = audio_tags
        self.callback_url = callback_url
        self.description = description
        self.client_token = client_token
        self.content_source = content_source
        self.audio_file = audio_file
        self.sort = sort

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.audio_id, 'audio_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.audio_url is not None:
            result['AudioUrl'] = self.audio_url
        if self.audio_id is not None:
            result['AudioId'] = self.audio_id
        if self.audio_tags is not None:
            result['AudioTags'] = self.audio_tags
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.description is not None:
            result['Description'] = self.description
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.content_source is not None:
            result['ContentSource'] = self.content_source
        if self.audio_file is not None:
            result['AudioFile'] = self.audio_file
        if self.sort is not None:
            result['Sort'] = self.sort
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AudioUrl') is not None:
            self.audio_url = m.get('AudioUrl')
        if m.get('AudioId') is not None:
            self.audio_id = m.get('AudioId')
        if m.get('AudioTags') is not None:
            self.audio_tags = m.get('AudioTags')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ContentSource') is not None:
            self.content_source = m.get('ContentSource')
        if m.get('AudioFile') is not None:
            self.audio_file = m.get('AudioFile')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        return self


class AddStorageAudioTaskResponseData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class AddStorageAudioTaskResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: AddStorageAudioTaskResponseData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = AddStorageAudioTaskResponseData()
            self.data = temp_model.from_map(m['Data'])
        return self


class AddStorageAudioTaskAdvanceRequest(TeaModel):
    def __init__(
        self,
        audio_file_object: BinaryIO = None,
        instance_id: str = None,
        audio_url: str = None,
        audio_id: str = None,
        audio_tags: str = None,
        callback_url: str = None,
        description: str = None,
        client_token: str = None,
        content_source: int = None,
        sort: int = None,
    ):
        self.audio_file_object = audio_file_object
        self.instance_id = instance_id
        self.audio_url = audio_url
        self.audio_id = audio_id
        self.audio_tags = audio_tags
        self.callback_url = callback_url
        self.description = description
        self.client_token = client_token
        self.content_source = content_source
        self.sort = sort

    def validate(self):
        self.validate_required(self.audio_file_object, 'audio_file_object')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.audio_id, 'audio_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_file_object is not None:
            result['AudioFileObject'] = self.audio_file_object
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.audio_url is not None:
            result['AudioUrl'] = self.audio_url
        if self.audio_id is not None:
            result['AudioId'] = self.audio_id
        if self.audio_tags is not None:
            result['AudioTags'] = self.audio_tags
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.description is not None:
            result['Description'] = self.description
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.content_source is not None:
            result['ContentSource'] = self.content_source
        if self.sort is not None:
            result['Sort'] = self.sort
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioFileObject') is not None:
            self.audio_file_object = m.get('AudioFileObject')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AudioUrl') is not None:
            self.audio_url = m.get('AudioUrl')
        if m.get('AudioId') is not None:
            self.audio_id = m.get('AudioId')
        if m.get('AudioTags') is not None:
            self.audio_tags = m.get('AudioTags')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ContentSource') is not None:
            self.content_source = m.get('ContentSource')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        return self


class ListStorageAudioTasksRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        task_id: str = None,
        audio_id: str = None,
        page_number: int = None,
        page_size: int = None,
        instance_id: str = None,
        status_list: str = None,
        description: str = None,
        storage_info_list: str = None,
        sort_list: str = None,
    ):
        self.client_token = client_token
        self.task_id = task_id
        self.audio_id = audio_id
        self.page_number = page_number
        self.page_size = page_size
        self.instance_id = instance_id
        self.status_list = status_list
        self.description = description
        self.storage_info_list = storage_info_list
        self.sort_list = sort_list

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.audio_id is not None:
            result['AudioId'] = self.audio_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        if self.description is not None:
            result['Description'] = self.description
        if self.storage_info_list is not None:
            result['StorageInfoList'] = self.storage_info_list
        if self.sort_list is not None:
            result['SortList'] = self.sort_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('AudioId') is not None:
            self.audio_id = m.get('AudioId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('StorageInfoList') is not None:
            self.storage_info_list = m.get('StorageInfoList')
        if m.get('SortList') is not None:
            self.sort_list = m.get('SortList')
        return self


class ListStorageAudioTasksResponseDataTaskList(TeaModel):
    def __init__(
        self,
        task_id: int = None,
        audio_id: str = None,
        process_time: int = None,
        storage_info: int = None,
        update_time: int = None,
        status: str = None,
        error_detail: str = None,
        remote_task_id: str = None,
        description: str = None,
        audio_url: str = None,
        sort: int = None,
    ):
        self.task_id = task_id
        self.audio_id = audio_id
        self.process_time = process_time
        self.storage_info = storage_info
        self.update_time = update_time
        self.status = status
        self.error_detail = error_detail
        self.remote_task_id = remote_task_id
        self.description = description
        self.audio_url = audio_url
        self.sort = sort

    def validate(self):
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.audio_id, 'audio_id')
        self.validate_required(self.process_time, 'process_time')
        self.validate_required(self.storage_info, 'storage_info')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.status, 'status')
        self.validate_required(self.error_detail, 'error_detail')
        self.validate_required(self.remote_task_id, 'remote_task_id')
        self.validate_required(self.description, 'description')
        self.validate_required(self.audio_url, 'audio_url')
        self.validate_required(self.sort, 'sort')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.audio_id is not None:
            result['AudioId'] = self.audio_id
        if self.process_time is not None:
            result['ProcessTime'] = self.process_time
        if self.storage_info is not None:
            result['StorageInfo'] = self.storage_info
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.status is not None:
            result['Status'] = self.status
        if self.error_detail is not None:
            result['ErrorDetail'] = self.error_detail
        if self.remote_task_id is not None:
            result['RemoteTaskId'] = self.remote_task_id
        if self.description is not None:
            result['Description'] = self.description
        if self.audio_url is not None:
            result['AudioUrl'] = self.audio_url
        if self.sort is not None:
            result['Sort'] = self.sort
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('AudioId') is not None:
            self.audio_id = m.get('AudioId')
        if m.get('ProcessTime') is not None:
            self.process_time = m.get('ProcessTime')
        if m.get('StorageInfo') is not None:
            self.storage_info = m.get('StorageInfo')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ErrorDetail') is not None:
            self.error_detail = m.get('ErrorDetail')
        if m.get('RemoteTaskId') is not None:
            self.remote_task_id = m.get('RemoteTaskId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AudioUrl') is not None:
            self.audio_url = m.get('AudioUrl')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        return self


class ListStorageAudioTasksResponseData(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        count: int = None,
        task_list: List[ListStorageAudioTasksResponseDataTaskList] = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.count = count
        self.task_list = task_list

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.count, 'count')
        self.validate_required(self.task_list, 'task_list')
        if self.task_list:
            for k in self.task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.count is not None:
            result['Count'] = self.count
        result['TaskList'] = []
        if self.task_list is not None:
            for k in self.task_list:
                result['TaskList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.task_list = []
        if m.get('TaskList') is not None:
            for k in m.get('TaskList'):
                temp_model = ListStorageAudioTasksResponseDataTaskList()
                self.task_list.append(temp_model.from_map(k))
        return self


class ListStorageAudioTasksResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ListStorageAudioTasksResponseData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListStorageAudioTasksResponseData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ListSearchAudioTasksRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        task_id: str = None,
        page_number: int = None,
        page_size: int = None,
        instance_id: str = None,
        status_list: str = None,
        description: str = None,
        sort_list: str = None,
    ):
        self.client_token = client_token
        self.task_id = task_id
        self.page_number = page_number
        self.page_size = page_size
        self.instance_id = instance_id
        self.status_list = status_list
        self.description = description
        self.sort_list = sort_list

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        if self.description is not None:
            result['Description'] = self.description
        if self.sort_list is not None:
            result['SortList'] = self.sort_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SortList') is not None:
            self.sort_list = m.get('SortList')
        return self


class ListSearchAudioTasksResponseDataTaskList(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        audio_id: str = None,
        process_time: int = None,
        status: int = None,
        modified_time: int = None,
        process_result_url: str = None,
        storage_info: int = None,
        audio_url: str = None,
        error_detail: str = None,
        remote_task_id: str = None,
        audio_tags: str = None,
        description: str = None,
        sort: int = None,
    ):
        self.task_id = task_id
        self.audio_id = audio_id
        self.process_time = process_time
        self.status = status
        self.modified_time = modified_time
        self.process_result_url = process_result_url
        self.storage_info = storage_info
        self.audio_url = audio_url
        self.error_detail = error_detail
        self.remote_task_id = remote_task_id
        self.audio_tags = audio_tags
        self.description = description
        self.sort = sort

    def validate(self):
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.audio_id, 'audio_id')
        self.validate_required(self.process_time, 'process_time')
        self.validate_required(self.status, 'status')
        self.validate_required(self.modified_time, 'modified_time')
        self.validate_required(self.process_result_url, 'process_result_url')
        self.validate_required(self.storage_info, 'storage_info')
        self.validate_required(self.audio_url, 'audio_url')
        self.validate_required(self.error_detail, 'error_detail')
        self.validate_required(self.remote_task_id, 'remote_task_id')
        self.validate_required(self.audio_tags, 'audio_tags')
        self.validate_required(self.description, 'description')
        self.validate_required(self.sort, 'sort')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.audio_id is not None:
            result['AudioId'] = self.audio_id
        if self.process_time is not None:
            result['ProcessTime'] = self.process_time
        if self.status is not None:
            result['Status'] = self.status
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.process_result_url is not None:
            result['ProcessResultUrl'] = self.process_result_url
        if self.storage_info is not None:
            result['StorageInfo'] = self.storage_info
        if self.audio_url is not None:
            result['AudioUrl'] = self.audio_url
        if self.error_detail is not None:
            result['ErrorDetail'] = self.error_detail
        if self.remote_task_id is not None:
            result['RemoteTaskId'] = self.remote_task_id
        if self.audio_tags is not None:
            result['AudioTags'] = self.audio_tags
        if self.description is not None:
            result['Description'] = self.description
        if self.sort is not None:
            result['Sort'] = self.sort
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('AudioId') is not None:
            self.audio_id = m.get('AudioId')
        if m.get('ProcessTime') is not None:
            self.process_time = m.get('ProcessTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ProcessResultUrl') is not None:
            self.process_result_url = m.get('ProcessResultUrl')
        if m.get('StorageInfo') is not None:
            self.storage_info = m.get('StorageInfo')
        if m.get('AudioUrl') is not None:
            self.audio_url = m.get('AudioUrl')
        if m.get('ErrorDetail') is not None:
            self.error_detail = m.get('ErrorDetail')
        if m.get('RemoteTaskId') is not None:
            self.remote_task_id = m.get('RemoteTaskId')
        if m.get('AudioTags') is not None:
            self.audio_tags = m.get('AudioTags')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        return self


class ListSearchAudioTasksResponseData(TeaModel):
    def __init__(
        self,
        count: int = None,
        page_number: int = None,
        page_size: int = None,
        task_list: List[ListSearchAudioTasksResponseDataTaskList] = None,
    ):
        self.count = count
        self.page_number = page_number
        self.page_size = page_size
        self.task_list = task_list

    def validate(self):
        self.validate_required(self.count, 'count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.task_list, 'task_list')
        if self.task_list:
            for k in self.task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['TaskList'] = []
        if self.task_list is not None:
            for k in self.task_list:
                result['TaskList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.task_list = []
        if m.get('TaskList') is not None:
            for k in m.get('TaskList'):
                temp_model = ListSearchAudioTasksResponseDataTaskList()
                self.task_list.append(temp_model.from_map(k))
        return self


class ListSearchAudioTasksResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ListSearchAudioTasksResponseData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListSearchAudioTasksResponseData()
            self.data = temp_model.from_map(m['Data'])
        return self


class CreateBatchTaskRequest(TeaModel):
    def __init__(
        self,
        batch_task_type: int = None,
        oss_bucket_name: str = None,
        oss_data_path: str = None,
        oss_meta_file: str = None,
        file_url: str = None,
        role_arn: str = None,
        instance_id: str = None,
        client_token: str = None,
        callback_url: str = None,
    ):
        self.batch_task_type = batch_task_type
        self.oss_bucket_name = oss_bucket_name
        self.oss_data_path = oss_data_path
        self.oss_meta_file = oss_meta_file
        self.file_url = file_url
        self.role_arn = role_arn
        self.instance_id = instance_id
        self.client_token = client_token
        self.callback_url = callback_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_task_type is not None:
            result['BatchTaskType'] = self.batch_task_type
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_data_path is not None:
            result['OssDataPath'] = self.oss_data_path
        if self.oss_meta_file is not None:
            result['OssMetaFile'] = self.oss_meta_file
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchTaskType') is not None:
            self.batch_task_type = m.get('BatchTaskType')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssDataPath') is not None:
            self.oss_data_path = m.get('OssDataPath')
        if m.get('OssMetaFile') is not None:
            self.oss_meta_file = m.get('OssMetaFile')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        return self


class CreateBatchTaskResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: int = None,
    ):
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateBatchTaskAdvanceRequest(TeaModel):
    def __init__(
        self,
        file_url_object: BinaryIO = None,
        batch_task_type: int = None,
        oss_bucket_name: str = None,
        oss_data_path: str = None,
        oss_meta_file: str = None,
        role_arn: str = None,
        instance_id: str = None,
        client_token: str = None,
        callback_url: str = None,
    ):
        self.file_url_object = file_url_object
        self.batch_task_type = batch_task_type
        self.oss_bucket_name = oss_bucket_name
        self.oss_data_path = oss_data_path
        self.oss_meta_file = oss_meta_file
        self.role_arn = role_arn
        self.instance_id = instance_id
        self.client_token = client_token
        self.callback_url = callback_url

    def validate(self):
        self.validate_required(self.file_url_object, 'file_url_object')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_url_object is not None:
            result['FileUrlObject'] = self.file_url_object
        if self.batch_task_type is not None:
            result['BatchTaskType'] = self.batch_task_type
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_data_path is not None:
            result['OssDataPath'] = self.oss_data_path
        if self.oss_meta_file is not None:
            result['OssMetaFile'] = self.oss_meta_file
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileUrlObject') is not None:
            self.file_url_object = m.get('FileUrlObject')
        if m.get('BatchTaskType') is not None:
            self.batch_task_type = m.get('BatchTaskType')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssDataPath') is not None:
            self.oss_data_path = m.get('OssDataPath')
        if m.get('OssMetaFile') is not None:
            self.oss_meta_file = m.get('OssMetaFile')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        return self


class GetStorageHistoryRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        video_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.video_id = video_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.video_id, 'video_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetStorageHistoryResponseDataList(TeaModel):
    def __init__(
        self,
        video_id: str = None,
        description: str = None,
        storage_type: int = None,
        storage_info: int = None,
        modified_time: int = None,
        video_url: str = None,
    ):
        self.video_id = video_id
        self.description = description
        self.storage_type = storage_type
        self.storage_info = storage_info
        self.modified_time = modified_time
        self.video_url = video_url

    def validate(self):
        self.validate_required(self.video_id, 'video_id')
        self.validate_required(self.description, 'description')
        self.validate_required(self.storage_type, 'storage_type')
        self.validate_required(self.storage_info, 'storage_info')
        self.validate_required(self.modified_time, 'modified_time')
        self.validate_required(self.video_url, 'video_url')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.description is not None:
            result['Description'] = self.description
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.storage_info is not None:
            result['StorageInfo'] = self.storage_info
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('StorageInfo') is not None:
            self.storage_info = m.get('StorageInfo')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class GetStorageHistoryResponseData(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        count: int = None,
        list: List[GetStorageHistoryResponseDataList] = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.count = count
        self.list = list

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.count, 'count')
        self.validate_required(self.list, 'list')
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.count is not None:
            result['Count'] = self.count
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = GetStorageHistoryResponseDataList()
                self.list.append(temp_model.from_map(k))
        return self


class GetStorageHistoryResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GetStorageHistoryResponseData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetStorageHistoryResponseData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ListBatchTaskRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        client_token: str = None,
        batch_task_type: str = None,
        status: str = None,
        instance_id: str = None,
        bucket_name: str = None,
        data_path: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.client_token = client_token
        self.batch_task_type = batch_task_type
        self.status = status
        self.instance_id = instance_id
        self.bucket_name = bucket_name
        self.data_path = data_path

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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.batch_task_type is not None:
            result['BatchTaskType'] = self.batch_task_type
        if self.status is not None:
            result['Status'] = self.status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.data_path is not None:
            result['DataPath'] = self.data_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('BatchTaskType') is not None:
            self.batch_task_type = m.get('BatchTaskType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('DataPath') is not None:
            self.data_path = m.get('DataPath')
        return self


class ListBatchTaskResponseDataList(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        status: int = None,
        task_type: int = None,
        region_id: str = None,
        bucket_name: str = None,
        data_path: str = None,
        meta_file: str = None,
        modified_time: int = None,
        process_message: str = None,
        sub_task_detail: str = None,
        arn: str = None,
    ):
        self.task_id = task_id
        self.status = status
        self.task_type = task_type
        self.region_id = region_id
        self.bucket_name = bucket_name
        self.data_path = data_path
        self.meta_file = meta_file
        self.modified_time = modified_time
        self.process_message = process_message
        self.sub_task_detail = sub_task_detail
        self.arn = arn

    def validate(self):
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.task_type, 'task_type')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.bucket_name, 'bucket_name')
        self.validate_required(self.data_path, 'data_path')
        self.validate_required(self.meta_file, 'meta_file')
        self.validate_required(self.modified_time, 'modified_time')
        self.validate_required(self.process_message, 'process_message')
        self.validate_required(self.sub_task_detail, 'sub_task_detail')
        self.validate_required(self.arn, 'arn')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.status is not None:
            result['Status'] = self.status
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.data_path is not None:
            result['DataPath'] = self.data_path
        if self.meta_file is not None:
            result['MetaFile'] = self.meta_file
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.process_message is not None:
            result['ProcessMessage'] = self.process_message
        if self.sub_task_detail is not None:
            result['SubTaskDetail'] = self.sub_task_detail
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('DataPath') is not None:
            self.data_path = m.get('DataPath')
        if m.get('MetaFile') is not None:
            self.meta_file = m.get('MetaFile')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ProcessMessage') is not None:
            self.process_message = m.get('ProcessMessage')
        if m.get('SubTaskDetail') is not None:
            self.sub_task_detail = m.get('SubTaskDetail')
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class ListBatchTaskResponseData(TeaModel):
    def __init__(
        self,
        count: int = None,
        page_number: int = None,
        page_size: int = None,
        list: List[ListBatchTaskResponseDataList] = None,
    ):
        self.count = count
        self.page_number = page_number
        self.page_size = page_size
        self.list = list

    def validate(self):
        self.validate_required(self.count, 'count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.list, 'list')
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListBatchTaskResponseDataList()
                self.list.append(temp_model.from_map(k))
        return self


class ListBatchTaskResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ListBatchTaskResponseData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListBatchTaskResponseData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ListInstancesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_name: str = None,
        page_number: int = None,
        page_size: int = None,
        tags: str = None,
        status: int = None,
        instance_type: int = None,
    ):
        self.client_token = client_token
        self.instance_name = instance_name
        self.page_number = page_number
        self.page_size = page_size
        self.tags = tags
        self.status = status
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.status is not None:
            result['Status'] = self.status
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class ListInstancesResponseDataListTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        self.validate_required(self.key, 'key')
        self.validate_required(self.value, 'value')

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


class ListInstancesResponseDataList(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_name: str = None,
        instance_status: int = None,
        create_time: str = None,
        expired_time: str = None,
        tags: List[ListInstancesResponseDataListTags] = None,
    ):
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.instance_status = instance_status
        self.create_time = create_time
        self.expired_time = expired_time
        self.tags = tags

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.instance_name, 'instance_name')
        self.validate_required(self.instance_status, 'instance_status')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.expired_time, 'expired_time')
        self.validate_required(self.tags, 'tags')
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListInstancesResponseDataListTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListInstancesResponseData(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        count: int = None,
        list: List[ListInstancesResponseDataList] = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.count = count
        self.list = list

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.count, 'count')
        self.validate_required(self.list, 'list')
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.count is not None:
            result['Count'] = self.count
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListInstancesResponseDataList()
                self.list.append(temp_model.from_map(k))
        return self


class ListInstancesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ListInstancesResponseData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListInstancesResponseData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ListStorageVideoTasksRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        task_id: str = None,
        video_name: str = None,
        video_id: str = None,
        page_number: int = None,
        page_size: int = None,
        instance_id: str = None,
        status_list: str = None,
        description: str = None,
        storage_info_list: str = None,
        sort_list: str = None,
    ):
        self.client_token = client_token
        self.task_id = task_id
        self.video_name = video_name
        self.video_id = video_id
        self.page_number = page_number
        self.page_size = page_size
        self.instance_id = instance_id
        self.status_list = status_list
        self.description = description
        self.storage_info_list = storage_info_list
        self.sort_list = sort_list

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.video_name is not None:
            result['VideoName'] = self.video_name
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        if self.description is not None:
            result['Description'] = self.description
        if self.storage_info_list is not None:
            result['StorageInfoList'] = self.storage_info_list
        if self.sort_list is not None:
            result['SortList'] = self.sort_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('VideoName') is not None:
            self.video_name = m.get('VideoName')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('StorageInfoList') is not None:
            self.storage_info_list = m.get('StorageInfoList')
        if m.get('SortList') is not None:
            self.sort_list = m.get('SortList')
        return self


class ListStorageVideoTasksResponseDataTaskList(TeaModel):
    def __init__(
        self,
        task_id: int = None,
        video_id: str = None,
        video_name: str = None,
        process_time: int = None,
        storage_info: int = None,
        modified_time: int = None,
        status: str = None,
        error_detail: str = None,
        remote_task_id: str = None,
        description: str = None,
        video_url: str = None,
        sort: int = None,
    ):
        self.task_id = task_id
        self.video_id = video_id
        self.video_name = video_name
        self.process_time = process_time
        self.storage_info = storage_info
        self.modified_time = modified_time
        self.status = status
        self.error_detail = error_detail
        self.remote_task_id = remote_task_id
        self.description = description
        self.video_url = video_url
        self.sort = sort

    def validate(self):
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.video_id, 'video_id')
        self.validate_required(self.video_name, 'video_name')
        self.validate_required(self.process_time, 'process_time')
        self.validate_required(self.storage_info, 'storage_info')
        self.validate_required(self.modified_time, 'modified_time')
        self.validate_required(self.status, 'status')
        self.validate_required(self.error_detail, 'error_detail')
        self.validate_required(self.remote_task_id, 'remote_task_id')
        self.validate_required(self.description, 'description')
        self.validate_required(self.video_url, 'video_url')
        self.validate_required(self.sort, 'sort')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.video_name is not None:
            result['VideoName'] = self.video_name
        if self.process_time is not None:
            result['ProcessTime'] = self.process_time
        if self.storage_info is not None:
            result['StorageInfo'] = self.storage_info
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.status is not None:
            result['Status'] = self.status
        if self.error_detail is not None:
            result['ErrorDetail'] = self.error_detail
        if self.remote_task_id is not None:
            result['RemoteTaskId'] = self.remote_task_id
        if self.description is not None:
            result['Description'] = self.description
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.sort is not None:
            result['Sort'] = self.sort
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('VideoName') is not None:
            self.video_name = m.get('VideoName')
        if m.get('ProcessTime') is not None:
            self.process_time = m.get('ProcessTime')
        if m.get('StorageInfo') is not None:
            self.storage_info = m.get('StorageInfo')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ErrorDetail') is not None:
            self.error_detail = m.get('ErrorDetail')
        if m.get('RemoteTaskId') is not None:
            self.remote_task_id = m.get('RemoteTaskId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        return self


class ListStorageVideoTasksResponseData(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        count: int = None,
        task_list: List[ListStorageVideoTasksResponseDataTaskList] = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.count = count
        self.task_list = task_list

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.count, 'count')
        self.validate_required(self.task_list, 'task_list')
        if self.task_list:
            for k in self.task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.count is not None:
            result['Count'] = self.count
        result['TaskList'] = []
        if self.task_list is not None:
            for k in self.task_list:
                result['TaskList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.task_list = []
        if m.get('TaskList') is not None:
            for k in m.get('TaskList'):
                temp_model = ListStorageVideoTasksResponseDataTaskList()
                self.task_list.append(temp_model.from_map(k))
        return self


class ListStorageVideoTasksResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ListStorageVideoTasksResponseData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListStorageVideoTasksResponseData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ListSearchVideoTasksRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        task_id: str = None,
        video_name: str = None,
        page_number: int = None,
        page_size: int = None,
        instance_id: str = None,
        status_list: str = None,
        search_type_list: str = None,
        description: str = None,
        sort_list: str = None,
        video_id: str = None,
    ):
        self.client_token = client_token
        self.task_id = task_id
        self.video_name = video_name
        self.page_number = page_number
        self.page_size = page_size
        self.instance_id = instance_id
        self.status_list = status_list
        self.search_type_list = search_type_list
        self.description = description
        self.sort_list = sort_list
        self.video_id = video_id

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.video_name is not None:
            result['VideoName'] = self.video_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        if self.search_type_list is not None:
            result['SearchTypeList'] = self.search_type_list
        if self.description is not None:
            result['Description'] = self.description
        if self.sort_list is not None:
            result['SortList'] = self.sort_list
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('VideoName') is not None:
            self.video_name = m.get('VideoName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        if m.get('SearchTypeList') is not None:
            self.search_type_list = m.get('SearchTypeList')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SortList') is not None:
            self.sort_list = m.get('SortList')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        return self


class ListSearchVideoTasksResponseDataTaskList(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        video_id: str = None,
        video_name: str = None,
        process_time: int = None,
        status: int = None,
        modified_time: int = None,
        process_result_url: str = None,
        storage_type: int = None,
        storage_info: int = None,
        video_url: str = None,
        error_detail: str = None,
        replace_storage_threshold: str = None,
        query_tags: str = None,
        remote_task_id: str = None,
        video_tags: str = None,
        search_type: int = None,
        description: str = None,
        sort: int = None,
    ):
        self.task_id = task_id
        self.video_id = video_id
        self.video_name = video_name
        self.process_time = process_time
        self.status = status
        self.modified_time = modified_time
        self.process_result_url = process_result_url
        self.storage_type = storage_type
        self.storage_info = storage_info
        self.video_url = video_url
        self.error_detail = error_detail
        self.replace_storage_threshold = replace_storage_threshold
        self.query_tags = query_tags
        self.remote_task_id = remote_task_id
        self.video_tags = video_tags
        self.search_type = search_type
        self.description = description
        self.sort = sort

    def validate(self):
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.video_id, 'video_id')
        self.validate_required(self.video_name, 'video_name')
        self.validate_required(self.process_time, 'process_time')
        self.validate_required(self.status, 'status')
        self.validate_required(self.modified_time, 'modified_time')
        self.validate_required(self.process_result_url, 'process_result_url')
        self.validate_required(self.storage_type, 'storage_type')
        self.validate_required(self.storage_info, 'storage_info')
        self.validate_required(self.video_url, 'video_url')
        self.validate_required(self.error_detail, 'error_detail')
        self.validate_required(self.replace_storage_threshold, 'replace_storage_threshold')
        self.validate_required(self.query_tags, 'query_tags')
        self.validate_required(self.remote_task_id, 'remote_task_id')
        self.validate_required(self.video_tags, 'video_tags')
        self.validate_required(self.search_type, 'search_type')
        self.validate_required(self.description, 'description')
        self.validate_required(self.sort, 'sort')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.video_name is not None:
            result['VideoName'] = self.video_name
        if self.process_time is not None:
            result['ProcessTime'] = self.process_time
        if self.status is not None:
            result['Status'] = self.status
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.process_result_url is not None:
            result['ProcessResultUrl'] = self.process_result_url
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.storage_info is not None:
            result['StorageInfo'] = self.storage_info
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.error_detail is not None:
            result['ErrorDetail'] = self.error_detail
        if self.replace_storage_threshold is not None:
            result['ReplaceStorageThreshold'] = self.replace_storage_threshold
        if self.query_tags is not None:
            result['QueryTags'] = self.query_tags
        if self.remote_task_id is not None:
            result['RemoteTaskId'] = self.remote_task_id
        if self.video_tags is not None:
            result['VideoTags'] = self.video_tags
        if self.search_type is not None:
            result['SearchType'] = self.search_type
        if self.description is not None:
            result['Description'] = self.description
        if self.sort is not None:
            result['Sort'] = self.sort
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('VideoName') is not None:
            self.video_name = m.get('VideoName')
        if m.get('ProcessTime') is not None:
            self.process_time = m.get('ProcessTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ProcessResultUrl') is not None:
            self.process_result_url = m.get('ProcessResultUrl')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('StorageInfo') is not None:
            self.storage_info = m.get('StorageInfo')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        if m.get('ErrorDetail') is not None:
            self.error_detail = m.get('ErrorDetail')
        if m.get('ReplaceStorageThreshold') is not None:
            self.replace_storage_threshold = m.get('ReplaceStorageThreshold')
        if m.get('QueryTags') is not None:
            self.query_tags = m.get('QueryTags')
        if m.get('RemoteTaskId') is not None:
            self.remote_task_id = m.get('RemoteTaskId')
        if m.get('VideoTags') is not None:
            self.video_tags = m.get('VideoTags')
        if m.get('SearchType') is not None:
            self.search_type = m.get('SearchType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        return self


class ListSearchVideoTasksResponseData(TeaModel):
    def __init__(
        self,
        count: int = None,
        page_number: int = None,
        page_size: int = None,
        task_list: List[ListSearchVideoTasksResponseDataTaskList] = None,
    ):
        self.count = count
        self.page_number = page_number
        self.page_size = page_size
        self.task_list = task_list

    def validate(self):
        self.validate_required(self.count, 'count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.task_list, 'task_list')
        if self.task_list:
            for k in self.task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['TaskList'] = []
        if self.task_list is not None:
            for k in self.task_list:
                result['TaskList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.task_list = []
        if m.get('TaskList') is not None:
            for k in m.get('TaskList'):
                temp_model = ListSearchVideoTasksResponseDataTaskList()
                self.task_list.append(temp_model.from_map(k))
        return self


class ListSearchVideoTasksResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ListSearchVideoTasksResponseData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListSearchVideoTasksResponseData()
            self.data = temp_model.from_map(m['Data'])
        return self


class AddStorageVideoTaskRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        video_url: str = None,
        video_id: str = None,
        video_tags: str = None,
        callback_url: str = None,
        description: str = None,
        storage_info: int = None,
        client_token: str = None,
        sort: int = None,
        video_file: str = None,
    ):
        self.instance_id = instance_id
        self.video_url = video_url
        self.video_id = video_id
        self.video_tags = video_tags
        self.callback_url = callback_url
        self.description = description
        self.storage_info = storage_info
        self.client_token = client_token
        self.sort = sort
        self.video_file = video_file

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.video_id, 'video_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.video_tags is not None:
            result['VideoTags'] = self.video_tags
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.description is not None:
            result['Description'] = self.description
        if self.storage_info is not None:
            result['StorageInfo'] = self.storage_info
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.video_file is not None:
            result['VideoFile'] = self.video_file
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('VideoTags') is not None:
            self.video_tags = m.get('VideoTags')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('StorageInfo') is not None:
            self.storage_info = m.get('StorageInfo')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('VideoFile') is not None:
            self.video_file = m.get('VideoFile')
        return self


class AddStorageVideoTaskResponseData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class AddStorageVideoTaskResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: AddStorageVideoTaskResponseData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = AddStorageVideoTaskResponseData()
            self.data = temp_model.from_map(m['Data'])
        return self


class AddStorageVideoTaskAdvanceRequest(TeaModel):
    def __init__(
        self,
        video_file_object: BinaryIO = None,
        instance_id: str = None,
        video_url: str = None,
        video_id: str = None,
        video_tags: str = None,
        callback_url: str = None,
        description: str = None,
        storage_info: int = None,
        client_token: str = None,
        sort: int = None,
    ):
        self.video_file_object = video_file_object
        self.instance_id = instance_id
        self.video_url = video_url
        self.video_id = video_id
        self.video_tags = video_tags
        self.callback_url = callback_url
        self.description = description
        self.storage_info = storage_info
        self.client_token = client_token
        self.sort = sort

    def validate(self):
        self.validate_required(self.video_file_object, 'video_file_object')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.video_id, 'video_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_file_object is not None:
            result['VideoFileObject'] = self.video_file_object
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.video_tags is not None:
            result['VideoTags'] = self.video_tags
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.description is not None:
            result['Description'] = self.description
        if self.storage_info is not None:
            result['StorageInfo'] = self.storage_info
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.sort is not None:
            result['Sort'] = self.sort
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoFileObject') is not None:
            self.video_file_object = m.get('VideoFileObject')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('VideoTags') is not None:
            self.video_tags = m.get('VideoTags')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('StorageInfo') is not None:
            self.storage_info = m.get('StorageInfo')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        return self


class GetInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetInstanceResponseData(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_name: str = None,
        create_time: int = None,
        region_id: str = None,
        instance_status: int = None,
        video_number: int = None,
        expire_time: int = None,
        concurrency_number: int = None,
        max_video_capacity: str = None,
        current_video_capacity: str = None,
        video_info_update_time: int = None,
        bundling_type: str = None,
    ):
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.create_time = create_time
        self.region_id = region_id
        self.instance_status = instance_status
        self.video_number = video_number
        self.expire_time = expire_time
        self.concurrency_number = concurrency_number
        self.max_video_capacity = max_video_capacity
        self.current_video_capacity = current_video_capacity
        self.video_info_update_time = video_info_update_time
        self.bundling_type = bundling_type

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.instance_name, 'instance_name')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.instance_status, 'instance_status')
        self.validate_required(self.video_number, 'video_number')
        self.validate_required(self.expire_time, 'expire_time')
        self.validate_required(self.concurrency_number, 'concurrency_number')
        self.validate_required(self.max_video_capacity, 'max_video_capacity')
        self.validate_required(self.current_video_capacity, 'current_video_capacity')
        self.validate_required(self.video_info_update_time, 'video_info_update_time')
        self.validate_required(self.bundling_type, 'bundling_type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.video_number is not None:
            result['VideoNumber'] = self.video_number
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.concurrency_number is not None:
            result['ConcurrencyNumber'] = self.concurrency_number
        if self.max_video_capacity is not None:
            result['MaxVideoCapacity'] = self.max_video_capacity
        if self.current_video_capacity is not None:
            result['CurrentVideoCapacity'] = self.current_video_capacity
        if self.video_info_update_time is not None:
            result['VideoInfoUpdateTime'] = self.video_info_update_time
        if self.bundling_type is not None:
            result['BundlingType'] = self.bundling_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('VideoNumber') is not None:
            self.video_number = m.get('VideoNumber')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('ConcurrencyNumber') is not None:
            self.concurrency_number = m.get('ConcurrencyNumber')
        if m.get('MaxVideoCapacity') is not None:
            self.max_video_capacity = m.get('MaxVideoCapacity')
        if m.get('CurrentVideoCapacity') is not None:
            self.current_video_capacity = m.get('CurrentVideoCapacity')
        if m.get('VideoInfoUpdateTime') is not None:
            self.video_info_update_time = m.get('VideoInfoUpdateTime')
        if m.get('BundlingType') is not None:
            self.bundling_type = m.get('BundlingType')
        return self


class GetInstanceResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GetInstanceResponseData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetInstanceResponseData()
            self.data = temp_model.from_map(m['Data'])
        return self


class AddDeletionVideoTaskRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        video_id: str = None,
        instance_id: str = None,
    ):
        self.client_token = client_token
        self.video_id = video_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class AddDeletionVideoTaskResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: bool = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')

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


class GetTaskStatusRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        task_id: str = None,
        instance_id: str = None,
    ):
        self.client_token = client_token
        self.task_id = task_id
        self.instance_id = instance_id

    def validate(self):
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetTaskStatusResponseTaskInfo(TeaModel):
    def __init__(
        self,
        analysis_use_time: int = None,
        duration: float = None,
        process_result_oss: str = None,
        resolution: str = None,
        status: int = None,
        submit_time: int = None,
        finish_time: int = None,
        task_id: int = None,
        error_info: str = None,
        storage_info: int = None,
        description: str = None,
        video_id: str = None,
        video_tags: str = None,
        video_url: str = None,
        query_tags: str = None,
        resource_type: str = None,
        replace_storage_threshold: str = None,
        storage_type: int = None,
    ):
        self.analysis_use_time = analysis_use_time
        self.duration = duration
        self.process_result_oss = process_result_oss
        self.resolution = resolution
        self.status = status
        self.submit_time = submit_time
        self.finish_time = finish_time
        self.task_id = task_id
        self.error_info = error_info
        self.storage_info = storage_info
        self.description = description
        self.video_id = video_id
        self.video_tags = video_tags
        self.video_url = video_url
        self.query_tags = query_tags
        self.resource_type = resource_type
        self.replace_storage_threshold = replace_storage_threshold
        self.storage_type = storage_type

    def validate(self):
        self.validate_required(self.analysis_use_time, 'analysis_use_time')
        self.validate_required(self.duration, 'duration')
        self.validate_required(self.process_result_oss, 'process_result_oss')
        self.validate_required(self.resolution, 'resolution')
        self.validate_required(self.status, 'status')
        self.validate_required(self.submit_time, 'submit_time')
        self.validate_required(self.finish_time, 'finish_time')
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.error_info, 'error_info')
        self.validate_required(self.storage_info, 'storage_info')
        self.validate_required(self.description, 'description')
        self.validate_required(self.video_id, 'video_id')
        self.validate_required(self.video_tags, 'video_tags')
        self.validate_required(self.video_url, 'video_url')
        self.validate_required(self.query_tags, 'query_tags')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.replace_storage_threshold, 'replace_storage_threshold')
        self.validate_required(self.storage_type, 'storage_type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analysis_use_time is not None:
            result['AnalysisUseTime'] = self.analysis_use_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.process_result_oss is not None:
            result['ProcessResultOss'] = self.process_result_oss
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        if self.status is not None:
            result['Status'] = self.status
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.error_info is not None:
            result['ErrorInfo'] = self.error_info
        if self.storage_info is not None:
            result['StorageInfo'] = self.storage_info
        if self.description is not None:
            result['Description'] = self.description
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.video_tags is not None:
            result['VideoTags'] = self.video_tags
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.query_tags is not None:
            result['QueryTags'] = self.query_tags
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.replace_storage_threshold is not None:
            result['ReplaceStorageThreshold'] = self.replace_storage_threshold
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnalysisUseTime') is not None:
            self.analysis_use_time = m.get('AnalysisUseTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('ProcessResultOss') is not None:
            self.process_result_oss = m.get('ProcessResultOss')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('ErrorInfo') is not None:
            self.error_info = m.get('ErrorInfo')
        if m.get('StorageInfo') is not None:
            self.storage_info = m.get('StorageInfo')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('VideoTags') is not None:
            self.video_tags = m.get('VideoTags')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        if m.get('QueryTags') is not None:
            self.query_tags = m.get('QueryTags')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ReplaceStorageThreshold') is not None:
            self.replace_storage_threshold = m.get('ReplaceStorageThreshold')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        return self


class GetTaskStatusResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: int = None,
        task_info: GetTaskStatusResponseTaskInfo = None,
    ):
        self.request_id = request_id
        self.data = data
        self.task_info = task_info

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        self.validate_required(self.task_info, 'task_info')
        if self.task_info:
            self.task_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.task_info is not None:
            result['TaskInfo'] = self.task_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('TaskInfo') is not None:
            temp_model = GetTaskStatusResponseTaskInfo()
            self.task_info = temp_model.from_map(m['TaskInfo'])
        return self


class AddSearchVideoTaskRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        video_url: str = None,
        video_id: str = None,
        video_tags: str = None,
        return_video_number: int = None,
        query_tags: str = None,
        storage_type: int = None,
        callback_url: str = None,
        replace_storage_threshold: float = None,
        instance_id: str = None,
        description: str = None,
        search_type: int = None,
        video_file: str = None,
        sort: int = None,
        need_feature_file: int = None,
    ):
        self.client_token = client_token
        self.video_url = video_url
        self.video_id = video_id
        self.video_tags = video_tags
        self.return_video_number = return_video_number
        self.query_tags = query_tags
        self.storage_type = storage_type
        self.callback_url = callback_url
        self.replace_storage_threshold = replace_storage_threshold
        self.instance_id = instance_id
        self.description = description
        self.search_type = search_type
        self.video_file = video_file
        self.sort = sort
        self.need_feature_file = need_feature_file

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.video_tags is not None:
            result['VideoTags'] = self.video_tags
        if self.return_video_number is not None:
            result['ReturnVideoNumber'] = self.return_video_number
        if self.query_tags is not None:
            result['QueryTags'] = self.query_tags
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.replace_storage_threshold is not None:
            result['ReplaceStorageThreshold'] = self.replace_storage_threshold
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.description is not None:
            result['Description'] = self.description
        if self.search_type is not None:
            result['SearchType'] = self.search_type
        if self.video_file is not None:
            result['VideoFile'] = self.video_file
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.need_feature_file is not None:
            result['NeedFeatureFile'] = self.need_feature_file
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('VideoTags') is not None:
            self.video_tags = m.get('VideoTags')
        if m.get('ReturnVideoNumber') is not None:
            self.return_video_number = m.get('ReturnVideoNumber')
        if m.get('QueryTags') is not None:
            self.query_tags = m.get('QueryTags')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('ReplaceStorageThreshold') is not None:
            self.replace_storage_threshold = m.get('ReplaceStorageThreshold')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SearchType') is not None:
            self.search_type = m.get('SearchType')
        if m.get('VideoFile') is not None:
            self.video_file = m.get('VideoFile')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('NeedFeatureFile') is not None:
            self.need_feature_file = m.get('NeedFeatureFile')
        return self


class AddSearchVideoTaskResponseData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class AddSearchVideoTaskResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: AddSearchVideoTaskResponseData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = AddSearchVideoTaskResponseData()
            self.data = temp_model.from_map(m['Data'])
        return self


class AddSearchVideoTaskAdvanceRequest(TeaModel):
    def __init__(
        self,
        video_file_object: BinaryIO = None,
        client_token: str = None,
        video_url: str = None,
        video_id: str = None,
        video_tags: str = None,
        return_video_number: int = None,
        query_tags: str = None,
        storage_type: int = None,
        callback_url: str = None,
        replace_storage_threshold: float = None,
        instance_id: str = None,
        description: str = None,
        search_type: int = None,
        sort: int = None,
        need_feature_file: int = None,
    ):
        self.video_file_object = video_file_object
        self.client_token = client_token
        self.video_url = video_url
        self.video_id = video_id
        self.video_tags = video_tags
        self.return_video_number = return_video_number
        self.query_tags = query_tags
        self.storage_type = storage_type
        self.callback_url = callback_url
        self.replace_storage_threshold = replace_storage_threshold
        self.instance_id = instance_id
        self.description = description
        self.search_type = search_type
        self.sort = sort
        self.need_feature_file = need_feature_file

    def validate(self):
        self.validate_required(self.video_file_object, 'video_file_object')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_file_object is not None:
            result['VideoFileObject'] = self.video_file_object
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.video_tags is not None:
            result['VideoTags'] = self.video_tags
        if self.return_video_number is not None:
            result['ReturnVideoNumber'] = self.return_video_number
        if self.query_tags is not None:
            result['QueryTags'] = self.query_tags
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.replace_storage_threshold is not None:
            result['ReplaceStorageThreshold'] = self.replace_storage_threshold
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.description is not None:
            result['Description'] = self.description
        if self.search_type is not None:
            result['SearchType'] = self.search_type
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.need_feature_file is not None:
            result['NeedFeatureFile'] = self.need_feature_file
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoFileObject') is not None:
            self.video_file_object = m.get('VideoFileObject')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('VideoTags') is not None:
            self.video_tags = m.get('VideoTags')
        if m.get('ReturnVideoNumber') is not None:
            self.return_video_number = m.get('ReturnVideoNumber')
        if m.get('QueryTags') is not None:
            self.query_tags = m.get('QueryTags')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('ReplaceStorageThreshold') is not None:
            self.replace_storage_threshold = m.get('ReplaceStorageThreshold')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SearchType') is not None:
            self.search_type = m.get('SearchType')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('NeedFeatureFile') is not None:
            self.need_feature_file = m.get('NeedFeatureFile')
        return self


