# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddHDMInstanceRequest(TeaModel):
    def __init__(
        self,
        engine: str = None,
        flush_account: str = None,
        instance_alias: str = None,
        instance_area: str = None,
        instance_id: str = None,
        ip: str = None,
        network_type: str = None,
        password: str = None,
        port: str = None,
        region: str = None,
        username: str = None,
        vpc_id: str = None,
        context: str = None,
    ):
        self.engine = engine
        self.flush_account = flush_account
        self.instance_alias = instance_alias
        self.instance_area = instance_area
        self.instance_id = instance_id
        self.ip = ip
        self.network_type = network_type
        self.password = password
        self.port = port
        self.region = region
        self.username = username
        self.vpc_id = vpc_id
        self.context = context

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.flush_account is not None:
            result['FlushAccount'] = self.flush_account
        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias
        if self.instance_area is not None:
            result['InstanceArea'] = self.instance_area
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.password is not None:
            result['Password'] = self.password
        if self.port is not None:
            result['Port'] = self.port
        if self.region is not None:
            result['Region'] = self.region
        if self.username is not None:
            result['Username'] = self.username
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.context is not None:
            result['__context'] = self.context
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('FlushAccount') is not None:
            self.flush_account = m.get('FlushAccount')
        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')
        if m.get('InstanceArea') is not None:
            self.instance_area = m.get('InstanceArea')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        return self


class AddHDMInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        caller_uid: str = None,
        code: int = None,
        error: str = None,
        instance_id: str = None,
        ip: str = None,
        owner_id: str = None,
        port: int = None,
        role: str = None,
        tenant_id: str = None,
        token: str = None,
        uuid: str = None,
        vpc_id: str = None,
    ):
        self.caller_uid = caller_uid
        self.code = code
        self.error = error
        self.instance_id = instance_id
        self.ip = ip
        self.owner_id = owner_id
        self.port = port
        self.role = role
        self.tenant_id = tenant_id
        self.token = token
        self.uuid = uuid
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caller_uid is not None:
            result['CallerUid'] = self.caller_uid
        if self.code is not None:
            result['Code'] = self.code
        if self.error is not None:
            result['Error'] = self.error
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.port is not None:
            result['Port'] = self.port
        if self.role is not None:
            result['Role'] = self.role
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.token is not None:
            result['Token'] = self.token
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallerUid') is not None:
            self.caller_uid = m.get('CallerUid')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class AddHDMInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: AddHDMInstanceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
        synchro: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success
        self.synchro = synchro

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AddHDMInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class AddHDMInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddHDMInstanceResponseBody = None,
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
            temp_model = AddHDMInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAdamBenchTaskRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        dst_instance_id: str = None,
        dst_super_account: str = None,
        dst_super_password: str = None,
        rate: int = None,
        request_duration: int = None,
        request_start_time: int = None,
        src_engine: str = None,
        src_engine_version: str = None,
        src_max_qps: float = None,
        src_mean_qps: float = None,
        src_sql_oss_addr: str = None,
    ):
        self.description = description
        self.dst_instance_id = dst_instance_id
        self.dst_super_account = dst_super_account
        self.dst_super_password = dst_super_password
        self.rate = rate
        self.request_duration = request_duration
        self.request_start_time = request_start_time
        self.src_engine = src_engine
        self.src_engine_version = src_engine_version
        self.src_max_qps = src_max_qps
        self.src_mean_qps = src_mean_qps
        self.src_sql_oss_addr = src_sql_oss_addr

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.dst_instance_id is not None:
            result['DstInstanceId'] = self.dst_instance_id
        if self.dst_super_account is not None:
            result['DstSuperAccount'] = self.dst_super_account
        if self.dst_super_password is not None:
            result['DstSuperPassword'] = self.dst_super_password
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.request_duration is not None:
            result['RequestDuration'] = self.request_duration
        if self.request_start_time is not None:
            result['RequestStartTime'] = self.request_start_time
        if self.src_engine is not None:
            result['SrcEngine'] = self.src_engine
        if self.src_engine_version is not None:
            result['SrcEngineVersion'] = self.src_engine_version
        if self.src_max_qps is not None:
            result['SrcMaxQps'] = self.src_max_qps
        if self.src_mean_qps is not None:
            result['SrcMeanQps'] = self.src_mean_qps
        if self.src_sql_oss_addr is not None:
            result['SrcSqlOssAddr'] = self.src_sql_oss_addr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DstInstanceId') is not None:
            self.dst_instance_id = m.get('DstInstanceId')
        if m.get('DstSuperAccount') is not None:
            self.dst_super_account = m.get('DstSuperAccount')
        if m.get('DstSuperPassword') is not None:
            self.dst_super_password = m.get('DstSuperPassword')
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('RequestDuration') is not None:
            self.request_duration = m.get('RequestDuration')
        if m.get('RequestStartTime') is not None:
            self.request_start_time = m.get('RequestStartTime')
        if m.get('SrcEngine') is not None:
            self.src_engine = m.get('SrcEngine')
        if m.get('SrcEngineVersion') is not None:
            self.src_engine_version = m.get('SrcEngineVersion')
        if m.get('SrcMaxQps') is not None:
            self.src_max_qps = m.get('SrcMaxQps')
        if m.get('SrcMeanQps') is not None:
            self.src_mean_qps = m.get('SrcMeanQps')
        if m.get('SrcSqlOssAddr') is not None:
            self.src_sql_oss_addr = m.get('SrcSqlOssAddr')
        return self


class CreateAdamBenchTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateAdamBenchTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAdamBenchTaskResponseBody = None,
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
            temp_model = CreateAdamBenchTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCacheAnalysisJobRequest(TeaModel):
    def __init__(
        self,
        backup_set_id: str = None,
        instance_id: str = None,
        node_id: str = None,
    ):
        self.backup_set_id = backup_set_id
        self.instance_id = instance_id
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class CreateCacheAnalysisJobResponseBodyDataBigKeysKeyInfo(TeaModel):
    def __init__(
        self,
        bytes: int = None,
        count: int = None,
        db: int = None,
        encoding: str = None,
        expiration_time_millis: int = None,
        key: str = None,
        node_id: str = None,
        type: str = None,
    ):
        self.bytes = bytes
        self.count = count
        self.db = db
        self.encoding = encoding
        self.expiration_time_millis = expiration_time_millis
        self.key = key
        self.node_id = node_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bytes is not None:
            result['Bytes'] = self.bytes
        if self.count is not None:
            result['Count'] = self.count
        if self.db is not None:
            result['Db'] = self.db
        if self.encoding is not None:
            result['Encoding'] = self.encoding
        if self.expiration_time_millis is not None:
            result['ExpirationTimeMillis'] = self.expiration_time_millis
        if self.key is not None:
            result['Key'] = self.key
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bytes') is not None:
            self.bytes = m.get('Bytes')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Db') is not None:
            self.db = m.get('Db')
        if m.get('Encoding') is not None:
            self.encoding = m.get('Encoding')
        if m.get('ExpirationTimeMillis') is not None:
            self.expiration_time_millis = m.get('ExpirationTimeMillis')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateCacheAnalysisJobResponseBodyDataBigKeys(TeaModel):
    def __init__(
        self,
        key_info: List[CreateCacheAnalysisJobResponseBodyDataBigKeysKeyInfo] = None,
    ):
        self.key_info = key_info

    def validate(self):
        if self.key_info:
            for k in self.key_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['KeyInfo'] = []
        if self.key_info is not None:
            for k in self.key_info:
                result['KeyInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.key_info = []
        if m.get('KeyInfo') is not None:
            for k in m.get('KeyInfo'):
                temp_model = CreateCacheAnalysisJobResponseBodyDataBigKeysKeyInfo()
                self.key_info.append(temp_model.from_map(k))
        return self


class CreateCacheAnalysisJobResponseBodyData(TeaModel):
    def __init__(
        self,
        big_keys: CreateCacheAnalysisJobResponseBodyDataBigKeys = None,
        instance_id: str = None,
        job_id: str = None,
        message: str = None,
        node_id: str = None,
        task_state: str = None,
    ):
        self.big_keys = big_keys
        self.instance_id = instance_id
        self.job_id = job_id
        self.message = message
        self.node_id = node_id
        self.task_state = task_state

    def validate(self):
        if self.big_keys:
            self.big_keys.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.big_keys is not None:
            result['BigKeys'] = self.big_keys.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.message is not None:
            result['Message'] = self.message
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.task_state is not None:
            result['TaskState'] = self.task_state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BigKeys') is not None:
            temp_model = CreateCacheAnalysisJobResponseBodyDataBigKeys()
            self.big_keys = temp_model.from_map(m['BigKeys'])
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('TaskState') is not None:
            self.task_state = m.get('TaskState')
        return self


class CreateCacheAnalysisJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateCacheAnalysisJobResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateCacheAnalysisJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateCacheAnalysisJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateCacheAnalysisJobResponseBody = None,
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
            temp_model = CreateCacheAnalysisJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCloudBenchTasksRequest(TeaModel):
    def __init__(
        self,
        amount: str = None,
        backup_id: str = None,
        backup_time: str = None,
        client_type: str = None,
        description: str = None,
        dst_connection_string: str = None,
        dst_instance_id: str = None,
        dst_port: str = None,
        dst_super_account: str = None,
        dst_super_password: str = None,
        dst_type: str = None,
        dts_job_class: str = None,
        dts_job_id: str = None,
        end_state: str = None,
        gateway_vpc_id: str = None,
        gateway_vpc_ip: str = None,
        rate: str = None,
        request_duration: str = None,
        request_end_time: str = None,
        request_start_time: str = None,
        smart_pressure_time: str = None,
        src_instance_id: str = None,
        src_public_ip: str = None,
        src_super_account: str = None,
        src_super_password: str = None,
        task_type: str = None,
        work_dir: str = None,
    ):
        self.amount = amount
        self.backup_id = backup_id
        self.backup_time = backup_time
        self.client_type = client_type
        self.description = description
        self.dst_connection_string = dst_connection_string
        self.dst_instance_id = dst_instance_id
        self.dst_port = dst_port
        self.dst_super_account = dst_super_account
        self.dst_super_password = dst_super_password
        self.dst_type = dst_type
        self.dts_job_class = dts_job_class
        self.dts_job_id = dts_job_id
        self.end_state = end_state
        self.gateway_vpc_id = gateway_vpc_id
        self.gateway_vpc_ip = gateway_vpc_ip
        self.rate = rate
        self.request_duration = request_duration
        self.request_end_time = request_end_time
        self.request_start_time = request_start_time
        self.smart_pressure_time = smart_pressure_time
        self.src_instance_id = src_instance_id
        self.src_public_ip = src_public_ip
        self.src_super_account = src_super_account
        self.src_super_password = src_super_password
        self.task_type = task_type
        self.work_dir = work_dir

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.backup_time is not None:
            result['BackupTime'] = self.backup_time
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.description is not None:
            result['Description'] = self.description
        if self.dst_connection_string is not None:
            result['DstConnectionString'] = self.dst_connection_string
        if self.dst_instance_id is not None:
            result['DstInstanceId'] = self.dst_instance_id
        if self.dst_port is not None:
            result['DstPort'] = self.dst_port
        if self.dst_super_account is not None:
            result['DstSuperAccount'] = self.dst_super_account
        if self.dst_super_password is not None:
            result['DstSuperPassword'] = self.dst_super_password
        if self.dst_type is not None:
            result['DstType'] = self.dst_type
        if self.dts_job_class is not None:
            result['DtsJobClass'] = self.dts_job_class
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.end_state is not None:
            result['EndState'] = self.end_state
        if self.gateway_vpc_id is not None:
            result['GatewayVpcId'] = self.gateway_vpc_id
        if self.gateway_vpc_ip is not None:
            result['GatewayVpcIp'] = self.gateway_vpc_ip
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.request_duration is not None:
            result['RequestDuration'] = self.request_duration
        if self.request_end_time is not None:
            result['RequestEndTime'] = self.request_end_time
        if self.request_start_time is not None:
            result['RequestStartTime'] = self.request_start_time
        if self.smart_pressure_time is not None:
            result['SmartPressureTime'] = self.smart_pressure_time
        if self.src_instance_id is not None:
            result['SrcInstanceId'] = self.src_instance_id
        if self.src_public_ip is not None:
            result['SrcPublicIp'] = self.src_public_ip
        if self.src_super_account is not None:
            result['SrcSuperAccount'] = self.src_super_account
        if self.src_super_password is not None:
            result['SrcSuperPassword'] = self.src_super_password
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.work_dir is not None:
            result['WorkDir'] = self.work_dir
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('BackupTime') is not None:
            self.backup_time = m.get('BackupTime')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DstConnectionString') is not None:
            self.dst_connection_string = m.get('DstConnectionString')
        if m.get('DstInstanceId') is not None:
            self.dst_instance_id = m.get('DstInstanceId')
        if m.get('DstPort') is not None:
            self.dst_port = m.get('DstPort')
        if m.get('DstSuperAccount') is not None:
            self.dst_super_account = m.get('DstSuperAccount')
        if m.get('DstSuperPassword') is not None:
            self.dst_super_password = m.get('DstSuperPassword')
        if m.get('DstType') is not None:
            self.dst_type = m.get('DstType')
        if m.get('DtsJobClass') is not None:
            self.dts_job_class = m.get('DtsJobClass')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('EndState') is not None:
            self.end_state = m.get('EndState')
        if m.get('GatewayVpcId') is not None:
            self.gateway_vpc_id = m.get('GatewayVpcId')
        if m.get('GatewayVpcIp') is not None:
            self.gateway_vpc_ip = m.get('GatewayVpcIp')
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('RequestDuration') is not None:
            self.request_duration = m.get('RequestDuration')
        if m.get('RequestEndTime') is not None:
            self.request_end_time = m.get('RequestEndTime')
        if m.get('RequestStartTime') is not None:
            self.request_start_time = m.get('RequestStartTime')
        if m.get('SmartPressureTime') is not None:
            self.smart_pressure_time = m.get('SmartPressureTime')
        if m.get('SrcInstanceId') is not None:
            self.src_instance_id = m.get('SrcInstanceId')
        if m.get('SrcPublicIp') is not None:
            self.src_public_ip = m.get('SrcPublicIp')
        if m.get('SrcSuperAccount') is not None:
            self.src_super_account = m.get('SrcSuperAccount')
        if m.get('SrcSuperPassword') is not None:
            self.src_super_password = m.get('SrcSuperPassword')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('WorkDir') is not None:
            self.work_dir = m.get('WorkDir')
        return self


class CreateCloudBenchTasksResponseBodyData(TeaModel):
    def __init__(
        self,
        task_ids: List[str] = None,
    ):
        self.task_ids = task_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_ids is not None:
            result['taskIds'] = self.task_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskIds') is not None:
            self.task_ids = m.get('taskIds')
        return self


class CreateCloudBenchTasksResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateCloudBenchTasksResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateCloudBenchTasksResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateCloudBenchTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateCloudBenchTasksResponseBody = None,
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
            temp_model = CreateCloudBenchTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDiagnosticReportRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        end_time: str = None,
        start_time: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class CreateDiagnosticReportResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateDiagnosticReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDiagnosticReportResponseBody = None,
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
            temp_model = CreateDiagnosticReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRequestDiagnosisRequest(TeaModel):
    def __init__(
        self,
        database: str = None,
        instance_id: str = None,
        node_id: str = None,
        sql: str = None,
    ):
        self.database = database
        self.instance_id = instance_id
        self.node_id = node_id
        self.sql = sql

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['Database'] = self.database
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.sql is not None:
            result['Sql'] = self.sql
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Sql') is not None:
            self.sql = m.get('Sql')
        return self


class CreateRequestDiagnosisResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateRequestDiagnosisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRequestDiagnosisResponseBody = None,
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
            temp_model = CreateRequestDiagnosisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCacheAnalysisJobRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        job_id: str = None,
    ):
        self.instance_id = instance_id
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class DescribeCacheAnalysisJobResponseBodyDataBigKeysKeyInfo(TeaModel):
    def __init__(
        self,
        bytes: int = None,
        count: int = None,
        db: int = None,
        encoding: str = None,
        expiration_time_millis: int = None,
        key: str = None,
        node_id: str = None,
        type: str = None,
    ):
        self.bytes = bytes
        self.count = count
        self.db = db
        self.encoding = encoding
        self.expiration_time_millis = expiration_time_millis
        self.key = key
        self.node_id = node_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bytes is not None:
            result['Bytes'] = self.bytes
        if self.count is not None:
            result['Count'] = self.count
        if self.db is not None:
            result['Db'] = self.db
        if self.encoding is not None:
            result['Encoding'] = self.encoding
        if self.expiration_time_millis is not None:
            result['ExpirationTimeMillis'] = self.expiration_time_millis
        if self.key is not None:
            result['Key'] = self.key
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bytes') is not None:
            self.bytes = m.get('Bytes')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Db') is not None:
            self.db = m.get('Db')
        if m.get('Encoding') is not None:
            self.encoding = m.get('Encoding')
        if m.get('ExpirationTimeMillis') is not None:
            self.expiration_time_millis = m.get('ExpirationTimeMillis')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeCacheAnalysisJobResponseBodyDataBigKeys(TeaModel):
    def __init__(
        self,
        key_info: List[DescribeCacheAnalysisJobResponseBodyDataBigKeysKeyInfo] = None,
    ):
        self.key_info = key_info

    def validate(self):
        if self.key_info:
            for k in self.key_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['KeyInfo'] = []
        if self.key_info is not None:
            for k in self.key_info:
                result['KeyInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.key_info = []
        if m.get('KeyInfo') is not None:
            for k in m.get('KeyInfo'):
                temp_model = DescribeCacheAnalysisJobResponseBodyDataBigKeysKeyInfo()
                self.key_info.append(temp_model.from_map(k))
        return self


class DescribeCacheAnalysisJobResponseBodyDataKeyPrefixesPrefix(TeaModel):
    def __init__(
        self,
        bytes: int = None,
        count: int = None,
        key_num: int = None,
        prefix: str = None,
        type: str = None,
    ):
        self.bytes = bytes
        self.count = count
        self.key_num = key_num
        self.prefix = prefix
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bytes is not None:
            result['Bytes'] = self.bytes
        if self.count is not None:
            result['Count'] = self.count
        if self.key_num is not None:
            result['KeyNum'] = self.key_num
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bytes') is not None:
            self.bytes = m.get('Bytes')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('KeyNum') is not None:
            self.key_num = m.get('KeyNum')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeCacheAnalysisJobResponseBodyDataKeyPrefixes(TeaModel):
    def __init__(
        self,
        prefix: List[DescribeCacheAnalysisJobResponseBodyDataKeyPrefixesPrefix] = None,
    ):
        self.prefix = prefix

    def validate(self):
        if self.prefix:
            for k in self.prefix:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Prefix'] = []
        if self.prefix is not None:
            for k in self.prefix:
                result['Prefix'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.prefix = []
        if m.get('Prefix') is not None:
            for k in m.get('Prefix'):
                temp_model = DescribeCacheAnalysisJobResponseBodyDataKeyPrefixesPrefix()
                self.prefix.append(temp_model.from_map(k))
        return self


class DescribeCacheAnalysisJobResponseBodyData(TeaModel):
    def __init__(
        self,
        big_keys: DescribeCacheAnalysisJobResponseBodyDataBigKeys = None,
        instance_id: str = None,
        job_id: str = None,
        key_prefixes: DescribeCacheAnalysisJobResponseBodyDataKeyPrefixes = None,
        message: str = None,
        node_id: str = None,
        task_state: str = None,
    ):
        self.big_keys = big_keys
        self.instance_id = instance_id
        self.job_id = job_id
        self.key_prefixes = key_prefixes
        self.message = message
        self.node_id = node_id
        self.task_state = task_state

    def validate(self):
        if self.big_keys:
            self.big_keys.validate()
        if self.key_prefixes:
            self.key_prefixes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.big_keys is not None:
            result['BigKeys'] = self.big_keys.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.key_prefixes is not None:
            result['KeyPrefixes'] = self.key_prefixes.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.task_state is not None:
            result['TaskState'] = self.task_state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BigKeys') is not None:
            temp_model = DescribeCacheAnalysisJobResponseBodyDataBigKeys()
            self.big_keys = temp_model.from_map(m['BigKeys'])
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('KeyPrefixes') is not None:
            temp_model = DescribeCacheAnalysisJobResponseBodyDataKeyPrefixes()
            self.key_prefixes = temp_model.from_map(m['KeyPrefixes'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('TaskState') is not None:
            self.task_state = m.get('TaskState')
        return self


class DescribeCacheAnalysisJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeCacheAnalysisJobResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeCacheAnalysisJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCacheAnalysisJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCacheAnalysisJobResponseBody = None,
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
            temp_model = DescribeCacheAnalysisJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCacheAnalysisJobsRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        instance_id: str = None,
        page_no: str = None,
        page_size: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.instance_id = instance_id
        self.page_no = page_no
        self.page_size = page_size
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeCacheAnalysisJobsResponseBodyDataListCacheAnalysisJobBigKeysKeyInfo(TeaModel):
    def __init__(
        self,
        bytes: int = None,
        count: int = None,
        db: int = None,
        encoding: str = None,
        expiration_time_millis: int = None,
        key: str = None,
        node_id: str = None,
        type: str = None,
    ):
        self.bytes = bytes
        self.count = count
        self.db = db
        self.encoding = encoding
        self.expiration_time_millis = expiration_time_millis
        self.key = key
        self.node_id = node_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bytes is not None:
            result['Bytes'] = self.bytes
        if self.count is not None:
            result['Count'] = self.count
        if self.db is not None:
            result['Db'] = self.db
        if self.encoding is not None:
            result['Encoding'] = self.encoding
        if self.expiration_time_millis is not None:
            result['ExpirationTimeMillis'] = self.expiration_time_millis
        if self.key is not None:
            result['Key'] = self.key
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bytes') is not None:
            self.bytes = m.get('Bytes')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Db') is not None:
            self.db = m.get('Db')
        if m.get('Encoding') is not None:
            self.encoding = m.get('Encoding')
        if m.get('ExpirationTimeMillis') is not None:
            self.expiration_time_millis = m.get('ExpirationTimeMillis')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeCacheAnalysisJobsResponseBodyDataListCacheAnalysisJobBigKeys(TeaModel):
    def __init__(
        self,
        key_info: List[DescribeCacheAnalysisJobsResponseBodyDataListCacheAnalysisJobBigKeysKeyInfo] = None,
    ):
        self.key_info = key_info

    def validate(self):
        if self.key_info:
            for k in self.key_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['KeyInfo'] = []
        if self.key_info is not None:
            for k in self.key_info:
                result['KeyInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.key_info = []
        if m.get('KeyInfo') is not None:
            for k in m.get('KeyInfo'):
                temp_model = DescribeCacheAnalysisJobsResponseBodyDataListCacheAnalysisJobBigKeysKeyInfo()
                self.key_info.append(temp_model.from_map(k))
        return self


class DescribeCacheAnalysisJobsResponseBodyDataListCacheAnalysisJob(TeaModel):
    def __init__(
        self,
        big_keys: DescribeCacheAnalysisJobsResponseBodyDataListCacheAnalysisJobBigKeys = None,
        instance_id: str = None,
        job_id: str = None,
        message: str = None,
        node_id: str = None,
        task_state: str = None,
    ):
        self.big_keys = big_keys
        self.instance_id = instance_id
        self.job_id = job_id
        self.message = message
        self.node_id = node_id
        self.task_state = task_state

    def validate(self):
        if self.big_keys:
            self.big_keys.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.big_keys is not None:
            result['BigKeys'] = self.big_keys.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.message is not None:
            result['Message'] = self.message
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.task_state is not None:
            result['TaskState'] = self.task_state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BigKeys') is not None:
            temp_model = DescribeCacheAnalysisJobsResponseBodyDataListCacheAnalysisJobBigKeys()
            self.big_keys = temp_model.from_map(m['BigKeys'])
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('TaskState') is not None:
            self.task_state = m.get('TaskState')
        return self


class DescribeCacheAnalysisJobsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        cache_analysis_job: List[DescribeCacheAnalysisJobsResponseBodyDataListCacheAnalysisJob] = None,
    ):
        self.cache_analysis_job = cache_analysis_job

    def validate(self):
        if self.cache_analysis_job:
            for k in self.cache_analysis_job:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CacheAnalysisJob'] = []
        if self.cache_analysis_job is not None:
            for k in self.cache_analysis_job:
                result['CacheAnalysisJob'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cache_analysis_job = []
        if m.get('CacheAnalysisJob') is not None:
            for k in m.get('CacheAnalysisJob'):
                temp_model = DescribeCacheAnalysisJobsResponseBodyDataListCacheAnalysisJob()
                self.cache_analysis_job.append(temp_model.from_map(k))
        return self


class DescribeCacheAnalysisJobsResponseBodyData(TeaModel):
    def __init__(
        self,
        extra: str = None,
        list: DescribeCacheAnalysisJobsResponseBodyDataList = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.extra = extra
        self.list = list
        self.page_no = page_no
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            self.list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.list is not None:
            result['List'] = self.list.to_map()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('List') is not None:
            temp_model = DescribeCacheAnalysisJobsResponseBodyDataList()
            self.list = temp_model.from_map(m['List'])
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeCacheAnalysisJobsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeCacheAnalysisJobsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeCacheAnalysisJobsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCacheAnalysisJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCacheAnalysisJobsResponseBody = None,
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
            temp_model = DescribeCacheAnalysisJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCloudBenchTasksRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        page_no: str = None,
        page_size: str = None,
        start_time: str = None,
        status: str = None,
        task_type: str = None,
    ):
        self.end_time = end_time
        self.page_no = page_no
        self.page_size = page_size
        self.start_time = start_time
        self.status = status
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class DescribeCloudBenchTasksResponseBodyDataListCloudbenchTasks(TeaModel):
    def __init__(
        self,
        archive_job_id: str = None,
        archive_oss_table_name: str = None,
        archive_state: int = None,
        backup_id: str = None,
        backup_type: str = None,
        bench_step: str = None,
        bench_step_status: str = None,
        client_gateway_id: str = None,
        client_type: str = None,
        description: str = None,
        dst_instance_uuid: str = None,
        dst_ip: str = None,
        dst_port: int = None,
        dst_type: str = None,
        dts_job_class: str = None,
        dts_job_id: str = None,
        dts_job_name: str = None,
        dts_job_state: int = None,
        dts_job_status: str = None,
        ecs_instance_id: str = None,
        end_state: str = None,
        error_code: str = None,
        error_message: str = None,
        external: str = None,
        rate: int = None,
        request_duration: int = None,
        smart_pressure_time: int = None,
        source: str = None,
        sql_complete_reuse: str = None,
        src_instance_area: str = None,
        src_instance_uuid: str = None,
        src_public_ip: str = None,
        state: str = None,
        status: str = None,
        table_schema: str = None,
        task_id: str = None,
        task_type: str = None,
        topic: str = None,
        user_id: str = None,
        version: str = None,
        work_dir: str = None,
    ):
        self.archive_job_id = archive_job_id
        self.archive_oss_table_name = archive_oss_table_name
        self.archive_state = archive_state
        self.backup_id = backup_id
        self.backup_type = backup_type
        self.bench_step = bench_step
        self.bench_step_status = bench_step_status
        self.client_gateway_id = client_gateway_id
        self.client_type = client_type
        self.description = description
        self.dst_instance_uuid = dst_instance_uuid
        self.dst_ip = dst_ip
        self.dst_port = dst_port
        self.dst_type = dst_type
        self.dts_job_class = dts_job_class
        self.dts_job_id = dts_job_id
        self.dts_job_name = dts_job_name
        self.dts_job_state = dts_job_state
        self.dts_job_status = dts_job_status
        self.ecs_instance_id = ecs_instance_id
        self.end_state = end_state
        self.error_code = error_code
        self.error_message = error_message
        self.external = external
        self.rate = rate
        self.request_duration = request_duration
        self.smart_pressure_time = smart_pressure_time
        self.source = source
        self.sql_complete_reuse = sql_complete_reuse
        self.src_instance_area = src_instance_area
        self.src_instance_uuid = src_instance_uuid
        self.src_public_ip = src_public_ip
        self.state = state
        self.status = status
        self.table_schema = table_schema
        self.task_id = task_id
        self.task_type = task_type
        self.topic = topic
        self.user_id = user_id
        self.version = version
        self.work_dir = work_dir

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.archive_job_id is not None:
            result['ArchiveJobId'] = self.archive_job_id
        if self.archive_oss_table_name is not None:
            result['ArchiveOssTableName'] = self.archive_oss_table_name
        if self.archive_state is not None:
            result['ArchiveState'] = self.archive_state
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.bench_step is not None:
            result['BenchStep'] = self.bench_step
        if self.bench_step_status is not None:
            result['BenchStepStatus'] = self.bench_step_status
        if self.client_gateway_id is not None:
            result['ClientGatewayId'] = self.client_gateway_id
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.description is not None:
            result['Description'] = self.description
        if self.dst_instance_uuid is not None:
            result['DstInstanceUuid'] = self.dst_instance_uuid
        if self.dst_ip is not None:
            result['DstIp'] = self.dst_ip
        if self.dst_port is not None:
            result['DstPort'] = self.dst_port
        if self.dst_type is not None:
            result['DstType'] = self.dst_type
        if self.dts_job_class is not None:
            result['DtsJobClass'] = self.dts_job_class
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.dts_job_name is not None:
            result['DtsJobName'] = self.dts_job_name
        if self.dts_job_state is not None:
            result['DtsJobState'] = self.dts_job_state
        if self.dts_job_status is not None:
            result['DtsJobStatus'] = self.dts_job_status
        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id
        if self.end_state is not None:
            result['EndState'] = self.end_state
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.external is not None:
            result['External'] = self.external
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.request_duration is not None:
            result['RequestDuration'] = self.request_duration
        if self.smart_pressure_time is not None:
            result['SmartPressureTime'] = self.smart_pressure_time
        if self.source is not None:
            result['Source'] = self.source
        if self.sql_complete_reuse is not None:
            result['SqlCompleteReuse'] = self.sql_complete_reuse
        if self.src_instance_area is not None:
            result['SrcInstanceArea'] = self.src_instance_area
        if self.src_instance_uuid is not None:
            result['SrcInstanceUuid'] = self.src_instance_uuid
        if self.src_public_ip is not None:
            result['SrcPublicIp'] = self.src_public_ip
        if self.state is not None:
            result['State'] = self.state
        if self.status is not None:
            result['Status'] = self.status
        if self.table_schema is not None:
            result['TableSchema'] = self.table_schema
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.version is not None:
            result['Version'] = self.version
        if self.work_dir is not None:
            result['WorkDir'] = self.work_dir
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchiveJobId') is not None:
            self.archive_job_id = m.get('ArchiveJobId')
        if m.get('ArchiveOssTableName') is not None:
            self.archive_oss_table_name = m.get('ArchiveOssTableName')
        if m.get('ArchiveState') is not None:
            self.archive_state = m.get('ArchiveState')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('BenchStep') is not None:
            self.bench_step = m.get('BenchStep')
        if m.get('BenchStepStatus') is not None:
            self.bench_step_status = m.get('BenchStepStatus')
        if m.get('ClientGatewayId') is not None:
            self.client_gateway_id = m.get('ClientGatewayId')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DstInstanceUuid') is not None:
            self.dst_instance_uuid = m.get('DstInstanceUuid')
        if m.get('DstIp') is not None:
            self.dst_ip = m.get('DstIp')
        if m.get('DstPort') is not None:
            self.dst_port = m.get('DstPort')
        if m.get('DstType') is not None:
            self.dst_type = m.get('DstType')
        if m.get('DtsJobClass') is not None:
            self.dts_job_class = m.get('DtsJobClass')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('DtsJobName') is not None:
            self.dts_job_name = m.get('DtsJobName')
        if m.get('DtsJobState') is not None:
            self.dts_job_state = m.get('DtsJobState')
        if m.get('DtsJobStatus') is not None:
            self.dts_job_status = m.get('DtsJobStatus')
        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')
        if m.get('EndState') is not None:
            self.end_state = m.get('EndState')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('External') is not None:
            self.external = m.get('External')
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('RequestDuration') is not None:
            self.request_duration = m.get('RequestDuration')
        if m.get('SmartPressureTime') is not None:
            self.smart_pressure_time = m.get('SmartPressureTime')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SqlCompleteReuse') is not None:
            self.sql_complete_reuse = m.get('SqlCompleteReuse')
        if m.get('SrcInstanceArea') is not None:
            self.src_instance_area = m.get('SrcInstanceArea')
        if m.get('SrcInstanceUuid') is not None:
            self.src_instance_uuid = m.get('SrcInstanceUuid')
        if m.get('SrcPublicIp') is not None:
            self.src_public_ip = m.get('SrcPublicIp')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TableSchema') is not None:
            self.table_schema = m.get('TableSchema')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('WorkDir') is not None:
            self.work_dir = m.get('WorkDir')
        return self


class DescribeCloudBenchTasksResponseBodyDataList(TeaModel):
    def __init__(
        self,
        cloudbench_tasks: List[DescribeCloudBenchTasksResponseBodyDataListCloudbenchTasks] = None,
    ):
        self.cloudbench_tasks = cloudbench_tasks

    def validate(self):
        if self.cloudbench_tasks:
            for k in self.cloudbench_tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['cloudbenchTasks'] = []
        if self.cloudbench_tasks is not None:
            for k in self.cloudbench_tasks:
                result['cloudbenchTasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cloudbench_tasks = []
        if m.get('cloudbenchTasks') is not None:
            for k in m.get('cloudbenchTasks'):
                temp_model = DescribeCloudBenchTasksResponseBodyDataListCloudbenchTasks()
                self.cloudbench_tasks.append(temp_model.from_map(k))
        return self


class DescribeCloudBenchTasksResponseBodyData(TeaModel):
    def __init__(
        self,
        extra: str = None,
        list: DescribeCloudBenchTasksResponseBodyDataList = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.extra = extra
        self.list = list
        self.page_no = page_no
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            self.list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.list is not None:
            result['List'] = self.list.to_map()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('List') is not None:
            temp_model = DescribeCloudBenchTasksResponseBodyDataList()
            self.list = temp_model.from_map(m['List'])
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeCloudBenchTasksResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeCloudBenchTasksResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeCloudBenchTasksResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCloudBenchTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCloudBenchTasksResponseBody = None,
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
            temp_model = DescribeCloudBenchTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCloudbenchTaskRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

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


class DescribeCloudbenchTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        archive_job_id: str = None,
        archive_oss_table_name: str = None,
        archive_state: int = None,
        backup_id: str = None,
        backup_type: str = None,
        bench_step: str = None,
        bench_step_status: str = None,
        client_gateway_id: str = None,
        client_type: str = None,
        description: str = None,
        dst_instance_uuid: str = None,
        dst_ip: str = None,
        dst_port: int = None,
        dst_type: str = None,
        dts_job_class: str = None,
        dts_job_id: str = None,
        dts_job_name: str = None,
        dts_job_state: int = None,
        dts_job_status: str = None,
        ecs_instance_id: str = None,
        end_state: str = None,
        error_code: str = None,
        error_message: str = None,
        external: str = None,
        rate: int = None,
        request_duration: int = None,
        smart_pressure_time: int = None,
        source: str = None,
        sql_complete_reuse: str = None,
        src_instance_area: str = None,
        src_instance_uuid: str = None,
        src_public_ip: str = None,
        state: str = None,
        status: str = None,
        table_schema: str = None,
        task_id: str = None,
        task_type: str = None,
        topic: str = None,
        user_id: str = None,
        version: str = None,
        work_dir: str = None,
    ):
        self.archive_job_id = archive_job_id
        self.archive_oss_table_name = archive_oss_table_name
        self.archive_state = archive_state
        self.backup_id = backup_id
        self.backup_type = backup_type
        self.bench_step = bench_step
        self.bench_step_status = bench_step_status
        self.client_gateway_id = client_gateway_id
        self.client_type = client_type
        self.description = description
        self.dst_instance_uuid = dst_instance_uuid
        self.dst_ip = dst_ip
        self.dst_port = dst_port
        self.dst_type = dst_type
        self.dts_job_class = dts_job_class
        self.dts_job_id = dts_job_id
        self.dts_job_name = dts_job_name
        self.dts_job_state = dts_job_state
        self.dts_job_status = dts_job_status
        self.ecs_instance_id = ecs_instance_id
        self.end_state = end_state
        self.error_code = error_code
        self.error_message = error_message
        self.external = external
        self.rate = rate
        self.request_duration = request_duration
        self.smart_pressure_time = smart_pressure_time
        self.source = source
        self.sql_complete_reuse = sql_complete_reuse
        self.src_instance_area = src_instance_area
        self.src_instance_uuid = src_instance_uuid
        self.src_public_ip = src_public_ip
        self.state = state
        self.status = status
        self.table_schema = table_schema
        self.task_id = task_id
        self.task_type = task_type
        self.topic = topic
        self.user_id = user_id
        self.version = version
        self.work_dir = work_dir

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.archive_job_id is not None:
            result['ArchiveJobId'] = self.archive_job_id
        if self.archive_oss_table_name is not None:
            result['ArchiveOssTableName'] = self.archive_oss_table_name
        if self.archive_state is not None:
            result['ArchiveState'] = self.archive_state
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.bench_step is not None:
            result['BenchStep'] = self.bench_step
        if self.bench_step_status is not None:
            result['BenchStepStatus'] = self.bench_step_status
        if self.client_gateway_id is not None:
            result['ClientGatewayId'] = self.client_gateway_id
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.description is not None:
            result['Description'] = self.description
        if self.dst_instance_uuid is not None:
            result['DstInstanceUuid'] = self.dst_instance_uuid
        if self.dst_ip is not None:
            result['DstIp'] = self.dst_ip
        if self.dst_port is not None:
            result['DstPort'] = self.dst_port
        if self.dst_type is not None:
            result['DstType'] = self.dst_type
        if self.dts_job_class is not None:
            result['DtsJobClass'] = self.dts_job_class
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.dts_job_name is not None:
            result['DtsJobName'] = self.dts_job_name
        if self.dts_job_state is not None:
            result['DtsJobState'] = self.dts_job_state
        if self.dts_job_status is not None:
            result['DtsJobStatus'] = self.dts_job_status
        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id
        if self.end_state is not None:
            result['EndState'] = self.end_state
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.external is not None:
            result['External'] = self.external
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.request_duration is not None:
            result['RequestDuration'] = self.request_duration
        if self.smart_pressure_time is not None:
            result['SmartPressureTime'] = self.smart_pressure_time
        if self.source is not None:
            result['Source'] = self.source
        if self.sql_complete_reuse is not None:
            result['SqlCompleteReuse'] = self.sql_complete_reuse
        if self.src_instance_area is not None:
            result['SrcInstanceArea'] = self.src_instance_area
        if self.src_instance_uuid is not None:
            result['SrcInstanceUuid'] = self.src_instance_uuid
        if self.src_public_ip is not None:
            result['SrcPublicIp'] = self.src_public_ip
        if self.state is not None:
            result['State'] = self.state
        if self.status is not None:
            result['Status'] = self.status
        if self.table_schema is not None:
            result['TableSchema'] = self.table_schema
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.version is not None:
            result['Version'] = self.version
        if self.work_dir is not None:
            result['WorkDir'] = self.work_dir
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchiveJobId') is not None:
            self.archive_job_id = m.get('ArchiveJobId')
        if m.get('ArchiveOssTableName') is not None:
            self.archive_oss_table_name = m.get('ArchiveOssTableName')
        if m.get('ArchiveState') is not None:
            self.archive_state = m.get('ArchiveState')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('BenchStep') is not None:
            self.bench_step = m.get('BenchStep')
        if m.get('BenchStepStatus') is not None:
            self.bench_step_status = m.get('BenchStepStatus')
        if m.get('ClientGatewayId') is not None:
            self.client_gateway_id = m.get('ClientGatewayId')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DstInstanceUuid') is not None:
            self.dst_instance_uuid = m.get('DstInstanceUuid')
        if m.get('DstIp') is not None:
            self.dst_ip = m.get('DstIp')
        if m.get('DstPort') is not None:
            self.dst_port = m.get('DstPort')
        if m.get('DstType') is not None:
            self.dst_type = m.get('DstType')
        if m.get('DtsJobClass') is not None:
            self.dts_job_class = m.get('DtsJobClass')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('DtsJobName') is not None:
            self.dts_job_name = m.get('DtsJobName')
        if m.get('DtsJobState') is not None:
            self.dts_job_state = m.get('DtsJobState')
        if m.get('DtsJobStatus') is not None:
            self.dts_job_status = m.get('DtsJobStatus')
        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')
        if m.get('EndState') is not None:
            self.end_state = m.get('EndState')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('External') is not None:
            self.external = m.get('External')
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('RequestDuration') is not None:
            self.request_duration = m.get('RequestDuration')
        if m.get('SmartPressureTime') is not None:
            self.smart_pressure_time = m.get('SmartPressureTime')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SqlCompleteReuse') is not None:
            self.sql_complete_reuse = m.get('SqlCompleteReuse')
        if m.get('SrcInstanceArea') is not None:
            self.src_instance_area = m.get('SrcInstanceArea')
        if m.get('SrcInstanceUuid') is not None:
            self.src_instance_uuid = m.get('SrcInstanceUuid')
        if m.get('SrcPublicIp') is not None:
            self.src_public_ip = m.get('SrcPublicIp')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TableSchema') is not None:
            self.table_schema = m.get('TableSchema')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('WorkDir') is not None:
            self.work_dir = m.get('WorkDir')
        return self


class DescribeCloudbenchTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeCloudbenchTaskResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeCloudbenchTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCloudbenchTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCloudbenchTaskResponseBody = None,
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
            temp_model = DescribeCloudbenchTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCloudbenchTaskConfigRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

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


class DescribeCloudbenchTaskConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        archive_folder: str = None,
        bench_cmd: str = None,
        client_jar_path: str = None,
        jar_on_oss: str = None,
        load_cmd: str = None,
        meta_file_name: str = None,
        meta_file_on_oss: str = None,
        meta_file_path: str = None,
        parse_cmd: str = None,
        parse_file_path: str = None,
        rocks_db_path: str = None,
        sql_file_name: str = None,
        sql_file_on_oss: str = None,
        sql_file_path: str = None,
        task_id: str = None,
        user_id: str = None,
        work_dir: str = None,
    ):
        self.archive_folder = archive_folder
        self.bench_cmd = bench_cmd
        self.client_jar_path = client_jar_path
        self.jar_on_oss = jar_on_oss
        self.load_cmd = load_cmd
        self.meta_file_name = meta_file_name
        self.meta_file_on_oss = meta_file_on_oss
        self.meta_file_path = meta_file_path
        self.parse_cmd = parse_cmd
        self.parse_file_path = parse_file_path
        self.rocks_db_path = rocks_db_path
        self.sql_file_name = sql_file_name
        self.sql_file_on_oss = sql_file_on_oss
        self.sql_file_path = sql_file_path
        self.task_id = task_id
        self.user_id = user_id
        self.work_dir = work_dir

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.archive_folder is not None:
            result['ArchiveFolder'] = self.archive_folder
        if self.bench_cmd is not None:
            result['BenchCmd'] = self.bench_cmd
        if self.client_jar_path is not None:
            result['ClientJarPath'] = self.client_jar_path
        if self.jar_on_oss is not None:
            result['JarOnOss'] = self.jar_on_oss
        if self.load_cmd is not None:
            result['LoadCmd'] = self.load_cmd
        if self.meta_file_name is not None:
            result['MetaFileName'] = self.meta_file_name
        if self.meta_file_on_oss is not None:
            result['MetaFileOnOss'] = self.meta_file_on_oss
        if self.meta_file_path is not None:
            result['MetaFilePath'] = self.meta_file_path
        if self.parse_cmd is not None:
            result['ParseCmd'] = self.parse_cmd
        if self.parse_file_path is not None:
            result['ParseFilePath'] = self.parse_file_path
        if self.rocks_db_path is not None:
            result['RocksDbPath'] = self.rocks_db_path
        if self.sql_file_name is not None:
            result['SqlFileName'] = self.sql_file_name
        if self.sql_file_on_oss is not None:
            result['SqlFileOnOss'] = self.sql_file_on_oss
        if self.sql_file_path is not None:
            result['SqlFilePath'] = self.sql_file_path
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.work_dir is not None:
            result['WorkDir'] = self.work_dir
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchiveFolder') is not None:
            self.archive_folder = m.get('ArchiveFolder')
        if m.get('BenchCmd') is not None:
            self.bench_cmd = m.get('BenchCmd')
        if m.get('ClientJarPath') is not None:
            self.client_jar_path = m.get('ClientJarPath')
        if m.get('JarOnOss') is not None:
            self.jar_on_oss = m.get('JarOnOss')
        if m.get('LoadCmd') is not None:
            self.load_cmd = m.get('LoadCmd')
        if m.get('MetaFileName') is not None:
            self.meta_file_name = m.get('MetaFileName')
        if m.get('MetaFileOnOss') is not None:
            self.meta_file_on_oss = m.get('MetaFileOnOss')
        if m.get('MetaFilePath') is not None:
            self.meta_file_path = m.get('MetaFilePath')
        if m.get('ParseCmd') is not None:
            self.parse_cmd = m.get('ParseCmd')
        if m.get('ParseFilePath') is not None:
            self.parse_file_path = m.get('ParseFilePath')
        if m.get('RocksDbPath') is not None:
            self.rocks_db_path = m.get('RocksDbPath')
        if m.get('SqlFileName') is not None:
            self.sql_file_name = m.get('SqlFileName')
        if m.get('SqlFileOnOss') is not None:
            self.sql_file_on_oss = m.get('SqlFileOnOss')
        if m.get('SqlFilePath') is not None:
            self.sql_file_path = m.get('SqlFilePath')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorkDir') is not None:
            self.work_dir = m.get('WorkDir')
        return self


class DescribeCloudbenchTaskConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeCloudbenchTaskConfigResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeCloudbenchTaskConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCloudbenchTaskConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCloudbenchTaskConfigResponseBody = None,
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
            temp_model = DescribeCloudbenchTaskConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDiagnosticReportListRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        end_time: str = None,
        page_no: str = None,
        page_size: str = None,
        start_time: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.end_time = end_time
        self.page_no = page_no
        self.page_size = page_size
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDiagnosticReportListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
        synchro: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success
        self.synchro = synchro

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class DescribeDiagnosticReportListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDiagnosticReportListResponseBody = None,
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
            temp_model = DescribeDiagnosticReportListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHotBigKeysRequest(TeaModel):
    def __init__(
        self,
        console_context: str = None,
        instance_id: str = None,
        node_id: str = None,
    ):
        self.console_context = console_context
        self.instance_id = instance_id
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class DescribeHotBigKeysResponseBodyDataBigKeysBigKey(TeaModel):
    def __init__(
        self,
        db: int = None,
        key: str = None,
        key_type: str = None,
        node_id: str = None,
        size: int = None,
    ):
        self.db = db
        self.key = key
        self.key_type = key_type
        self.node_id = node_id
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db is not None:
            result['Db'] = self.db
        if self.key is not None:
            result['Key'] = self.key
        if self.key_type is not None:
            result['KeyType'] = self.key_type
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Db') is not None:
            self.db = m.get('Db')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('KeyType') is not None:
            self.key_type = m.get('KeyType')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DescribeHotBigKeysResponseBodyDataBigKeys(TeaModel):
    def __init__(
        self,
        big_key: List[DescribeHotBigKeysResponseBodyDataBigKeysBigKey] = None,
    ):
        self.big_key = big_key

    def validate(self):
        if self.big_key:
            for k in self.big_key:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BigKey'] = []
        if self.big_key is not None:
            for k in self.big_key:
                result['BigKey'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.big_key = []
        if m.get('BigKey') is not None:
            for k in m.get('BigKey'):
                temp_model = DescribeHotBigKeysResponseBodyDataBigKeysBigKey()
                self.big_key.append(temp_model.from_map(k))
        return self


class DescribeHotBigKeysResponseBodyDataHotKeysHotKey(TeaModel):
    def __init__(
        self,
        db: int = None,
        hot: str = None,
        key: str = None,
        key_type: str = None,
        lfu: int = None,
        node_id: str = None,
    ):
        self.db = db
        self.hot = hot
        self.key = key
        self.key_type = key_type
        self.lfu = lfu
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db is not None:
            result['Db'] = self.db
        if self.hot is not None:
            result['Hot'] = self.hot
        if self.key is not None:
            result['Key'] = self.key
        if self.key_type is not None:
            result['KeyType'] = self.key_type
        if self.lfu is not None:
            result['Lfu'] = self.lfu
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Db') is not None:
            self.db = m.get('Db')
        if m.get('Hot') is not None:
            self.hot = m.get('Hot')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('KeyType') is not None:
            self.key_type = m.get('KeyType')
        if m.get('Lfu') is not None:
            self.lfu = m.get('Lfu')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class DescribeHotBigKeysResponseBodyDataHotKeys(TeaModel):
    def __init__(
        self,
        hot_key: List[DescribeHotBigKeysResponseBodyDataHotKeysHotKey] = None,
    ):
        self.hot_key = hot_key

    def validate(self):
        if self.hot_key:
            for k in self.hot_key:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HotKey'] = []
        if self.hot_key is not None:
            for k in self.hot_key:
                result['HotKey'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hot_key = []
        if m.get('HotKey') is not None:
            for k in m.get('HotKey'):
                temp_model = DescribeHotBigKeysResponseBodyDataHotKeysHotKey()
                self.hot_key.append(temp_model.from_map(k))
        return self


class DescribeHotBigKeysResponseBodyData(TeaModel):
    def __init__(
        self,
        big_key_msg: str = None,
        big_keys: DescribeHotBigKeysResponseBodyDataBigKeys = None,
        hot_key_msg: str = None,
        hot_keys: DescribeHotBigKeysResponseBodyDataHotKeys = None,
    ):
        self.big_key_msg = big_key_msg
        self.big_keys = big_keys
        self.hot_key_msg = hot_key_msg
        self.hot_keys = hot_keys

    def validate(self):
        if self.big_keys:
            self.big_keys.validate()
        if self.hot_keys:
            self.hot_keys.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.big_key_msg is not None:
            result['BigKeyMsg'] = self.big_key_msg
        if self.big_keys is not None:
            result['BigKeys'] = self.big_keys.to_map()
        if self.hot_key_msg is not None:
            result['HotKeyMsg'] = self.hot_key_msg
        if self.hot_keys is not None:
            result['HotKeys'] = self.hot_keys.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BigKeyMsg') is not None:
            self.big_key_msg = m.get('BigKeyMsg')
        if m.get('BigKeys') is not None:
            temp_model = DescribeHotBigKeysResponseBodyDataBigKeys()
            self.big_keys = temp_model.from_map(m['BigKeys'])
        if m.get('HotKeyMsg') is not None:
            self.hot_key_msg = m.get('HotKeyMsg')
        if m.get('HotKeys') is not None:
            temp_model = DescribeHotBigKeysResponseBodyDataHotKeys()
            self.hot_keys = temp_model.from_map(m['HotKeys'])
        return self


class DescribeHotBigKeysResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeHotBigKeysResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeHotBigKeysResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeHotBigKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeHotBigKeysResponseBody = None,
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
            temp_model = DescribeHotBigKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHotKeysRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        node_id: str = None,
    ):
        self.instance_id = instance_id
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class DescribeHotKeysResponseBodyDataHotKey(TeaModel):
    def __init__(
        self,
        db: int = None,
        hot: str = None,
        key: str = None,
        key_type: str = None,
        size: int = None,
    ):
        self.db = db
        self.hot = hot
        self.key = key
        self.key_type = key_type
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db is not None:
            result['Db'] = self.db
        if self.hot is not None:
            result['Hot'] = self.hot
        if self.key is not None:
            result['Key'] = self.key
        if self.key_type is not None:
            result['KeyType'] = self.key_type
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Db') is not None:
            self.db = m.get('Db')
        if m.get('Hot') is not None:
            self.hot = m.get('Hot')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('KeyType') is not None:
            self.key_type = m.get('KeyType')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DescribeHotKeysResponseBodyData(TeaModel):
    def __init__(
        self,
        hot_key: List[DescribeHotKeysResponseBodyDataHotKey] = None,
    ):
        self.hot_key = hot_key

    def validate(self):
        if self.hot_key:
            for k in self.hot_key:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HotKey'] = []
        if self.hot_key is not None:
            for k in self.hot_key:
                result['HotKey'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hot_key = []
        if m.get('HotKey') is not None:
            for k in m.get('HotKey'):
                temp_model = DescribeHotKeysResponseBodyDataHotKey()
                self.hot_key.append(temp_model.from_map(k))
        return self


class DescribeHotKeysResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeHotKeysResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeHotKeysResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeHotKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeHotKeysResponseBody = None,
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
            temp_model = DescribeHotKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTopBigKeysRequest(TeaModel):
    def __init__(
        self,
        console_context: str = None,
        end_time: str = None,
        instance_id: str = None,
        node_id: str = None,
        start_time: str = None,
    ):
        self.console_context = console_context
        self.end_time = end_time
        self.instance_id = instance_id
        self.node_id = node_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeTopBigKeysResponseBodyDataBigKey(TeaModel):
    def __init__(
        self,
        db: int = None,
        key: str = None,
        key_type: str = None,
        node_id: str = None,
        size: int = None,
    ):
        self.db = db
        self.key = key
        self.key_type = key_type
        self.node_id = node_id
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db is not None:
            result['Db'] = self.db
        if self.key is not None:
            result['Key'] = self.key
        if self.key_type is not None:
            result['KeyType'] = self.key_type
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Db') is not None:
            self.db = m.get('Db')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('KeyType') is not None:
            self.key_type = m.get('KeyType')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DescribeTopBigKeysResponseBodyData(TeaModel):
    def __init__(
        self,
        big_key: List[DescribeTopBigKeysResponseBodyDataBigKey] = None,
    ):
        self.big_key = big_key

    def validate(self):
        if self.big_key:
            for k in self.big_key:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BigKey'] = []
        if self.big_key is not None:
            for k in self.big_key:
                result['BigKey'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.big_key = []
        if m.get('BigKey') is not None:
            for k in m.get('BigKey'):
                temp_model = DescribeTopBigKeysResponseBodyDataBigKey()
                self.big_key.append(temp_model.from_map(k))
        return self


class DescribeTopBigKeysResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeTopBigKeysResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeTopBigKeysResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeTopBigKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeTopBigKeysResponseBody = None,
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
            temp_model = DescribeTopBigKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTopHotKeysRequest(TeaModel):
    def __init__(
        self,
        console_context: str = None,
        end_time: str = None,
        instance_id: str = None,
        node_id: str = None,
        start_time: str = None,
    ):
        self.console_context = console_context
        self.end_time = end_time
        self.instance_id = instance_id
        self.node_id = node_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeTopHotKeysResponseBodyDataHotKey(TeaModel):
    def __init__(
        self,
        db: int = None,
        hot: str = None,
        key: str = None,
        key_type: str = None,
        lfu: int = None,
        node_id: str = None,
    ):
        self.db = db
        self.hot = hot
        self.key = key
        self.key_type = key_type
        self.lfu = lfu
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db is not None:
            result['Db'] = self.db
        if self.hot is not None:
            result['Hot'] = self.hot
        if self.key is not None:
            result['Key'] = self.key
        if self.key_type is not None:
            result['KeyType'] = self.key_type
        if self.lfu is not None:
            result['Lfu'] = self.lfu
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Db') is not None:
            self.db = m.get('Db')
        if m.get('Hot') is not None:
            self.hot = m.get('Hot')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('KeyType') is not None:
            self.key_type = m.get('KeyType')
        if m.get('Lfu') is not None:
            self.lfu = m.get('Lfu')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class DescribeTopHotKeysResponseBodyData(TeaModel):
    def __init__(
        self,
        hot_key: List[DescribeTopHotKeysResponseBodyDataHotKey] = None,
    ):
        self.hot_key = hot_key

    def validate(self):
        if self.hot_key:
            for k in self.hot_key:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HotKey'] = []
        if self.hot_key is not None:
            for k in self.hot_key:
                result['HotKey'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hot_key = []
        if m.get('HotKey') is not None:
            for k in m.get('HotKey'):
                temp_model = DescribeTopHotKeysResponseBodyDataHotKey()
                self.hot_key.append(temp_model.from_map(k))
        return self


class DescribeTopHotKeysResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeTopHotKeysResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeTopHotKeysResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeTopHotKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeTopHotKeysResponseBody = None,
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
            temp_model = DescribeTopHotKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableAllSqlConcurrencyControlRulesRequest(TeaModel):
    def __init__(
        self,
        console_context: str = None,
        instance_id: str = None,
    ):
        self.console_context = console_context
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DisableAllSqlConcurrencyControlRulesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DisableAllSqlConcurrencyControlRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableAllSqlConcurrencyControlRulesResponseBody = None,
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
            temp_model = DisableAllSqlConcurrencyControlRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableSqlConcurrencyControlRequest(TeaModel):
    def __init__(
        self,
        console_context: str = None,
        instance_id: str = None,
        item_id: int = None,
    ):
        self.console_context = console_context
        self.instance_id = instance_id
        self.item_id = item_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        return self


class DisableSqlConcurrencyControlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DisableSqlConcurrencyControlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableSqlConcurrencyControlResponseBody = None,
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
            temp_model = DisableSqlConcurrencyControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableSqlConcurrencyControlRequest(TeaModel):
    def __init__(
        self,
        concurrency_control_time: int = None,
        console_context: str = None,
        instance_id: str = None,
        max_concurrency: int = None,
        sql_keywords: str = None,
        sql_type: str = None,
    ):
        self.concurrency_control_time = concurrency_control_time
        self.console_context = console_context
        self.instance_id = instance_id
        self.max_concurrency = max_concurrency
        self.sql_keywords = sql_keywords
        self.sql_type = sql_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.concurrency_control_time is not None:
            result['ConcurrencyControlTime'] = self.concurrency_control_time
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency
        if self.sql_keywords is not None:
            result['SqlKeywords'] = self.sql_keywords
        if self.sql_type is not None:
            result['SqlType'] = self.sql_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConcurrencyControlTime') is not None:
            self.concurrency_control_time = m.get('ConcurrencyControlTime')
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')
        if m.get('SqlKeywords') is not None:
            self.sql_keywords = m.get('SqlKeywords')
        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')
        return self


class EnableSqlConcurrencyControlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnableSqlConcurrencyControlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableSqlConcurrencyControlResponseBody = None,
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
            temp_model = EnableSqlConcurrencyControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAutoResourceOptimizeConfigRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        instance_id: str = None,
        signature: str = None,
        uid: str = None,
        user_id: str = None,
        context: str = None,
    ):
        self.access_key = access_key
        self.instance_id = instance_id
        self.signature = signature
        self.uid = uid
        self.user_id = user_id
        self.context = context

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.context is not None:
            result['__context'] = self.context
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        return self


class GetAutoResourceOptimizeConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
        synchro: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success
        self.synchro = synchro

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class GetAutoResourceOptimizeConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAutoResourceOptimizeConfigResponseBody = None,
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
            temp_model = GetAutoResourceOptimizeConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAutonomousNotifyEventContentRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        span_id: str = None,
        context: str = None,
    ):
        self.instance_id = instance_id
        self.span_id = span_id
        self.context = context

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.span_id is not None:
            result['SpanId'] = self.span_id
        if self.context is not None:
            result['__context'] = self.context
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SpanId') is not None:
            self.span_id = m.get('SpanId')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        return self


class GetAutonomousNotifyEventContentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAutonomousNotifyEventContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAutonomousNotifyEventContentResponseBody = None,
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
            temp_model = GetAutonomousNotifyEventContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAutonomousNotifyEventDetailRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        span_id: str = None,
        context: str = None,
    ):
        self.instance_id = instance_id
        self.span_id = span_id
        self.context = context

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.span_id is not None:
            result['SpanId'] = self.span_id
        if self.context is not None:
            result['__context'] = self.context
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SpanId') is not None:
            self.span_id = m.get('SpanId')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        return self


class GetAutonomousNotifyEventDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAutonomousNotifyEventDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAutonomousNotifyEventDetailResponseBody = None,
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
            temp_model = GetAutonomousNotifyEventDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAutonomousNotifyEventsRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        event_context: str = None,
        instance_id: str = None,
        level: str = None,
        min_level: str = None,
        node_id: str = None,
        page_offset: str = None,
        page_size: str = None,
        start_time: str = None,
        context: str = None,
    ):
        self.end_time = end_time
        self.event_context = event_context
        self.instance_id = instance_id
        self.level = level
        self.min_level = min_level
        self.node_id = node_id
        self.page_offset = page_offset
        self.page_size = page_size
        self.start_time = start_time
        self.context = context

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event_context is not None:
            result['EventContext'] = self.event_context
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.level is not None:
            result['Level'] = self.level
        if self.min_level is not None:
            result['MinLevel'] = self.min_level
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.page_offset is not None:
            result['PageOffset'] = self.page_offset
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.context is not None:
            result['__context'] = self.context
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EventContext') is not None:
            self.event_context = m.get('EventContext')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('MinLevel') is not None:
            self.min_level = m.get('MinLevel')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('PageOffset') is not None:
            self.page_offset = m.get('PageOffset')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        return self


class GetAutonomousNotifyEventsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAutonomousNotifyEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAutonomousNotifyEventsResponseBody = None,
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
            temp_model = GetAutonomousNotifyEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAutonomousNotifyEventsInRangeRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        event_context: str = None,
        instance_id: str = None,
        level: str = None,
        min_level: str = None,
        node_id: str = None,
        page_offset: str = None,
        page_size: str = None,
        start_time: str = None,
        context: str = None,
    ):
        self.end_time = end_time
        self.event_context = event_context
        self.instance_id = instance_id
        self.level = level
        self.min_level = min_level
        self.node_id = node_id
        self.page_offset = page_offset
        self.page_size = page_size
        self.start_time = start_time
        self.context = context

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event_context is not None:
            result['EventContext'] = self.event_context
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.level is not None:
            result['Level'] = self.level
        if self.min_level is not None:
            result['MinLevel'] = self.min_level
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.page_offset is not None:
            result['PageOffset'] = self.page_offset
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.context is not None:
            result['__context'] = self.context
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EventContext') is not None:
            self.event_context = m.get('EventContext')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('MinLevel') is not None:
            self.min_level = m.get('MinLevel')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('PageOffset') is not None:
            self.page_offset = m.get('PageOffset')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        return self


class GetAutonomousNotifyEventsInRangeResponseBodyDataList(TeaModel):
    def __init__(
        self,
        t: List[str] = None,
    ):
        self.t = t

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.t is not None:
            result['T'] = self.t
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('T') is not None:
            self.t = m.get('T')
        return self


class GetAutonomousNotifyEventsInRangeResponseBodyData(TeaModel):
    def __init__(
        self,
        extra: str = None,
        list: GetAutonomousNotifyEventsInRangeResponseBodyDataList = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.extra = extra
        self.list = list
        self.page_no = page_no
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            self.list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.list is not None:
            result['List'] = self.list.to_map()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('List') is not None:
            temp_model = GetAutonomousNotifyEventsInRangeResponseBodyDataList()
            self.list = temp_model.from_map(m['List'])
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetAutonomousNotifyEventsInRangeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetAutonomousNotifyEventsInRangeResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetAutonomousNotifyEventsInRangeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAutonomousNotifyEventsInRangeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAutonomousNotifyEventsInRangeResponseBody = None,
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
            temp_model = GetAutonomousNotifyEventsInRangeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEndpointSwitchTaskRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        uid: str = None,
        user_id: str = None,
        context: str = None,
        access_key: str = None,
        signature: str = None,
        skip_auth: str = None,
        timestamp: str = None,
    ):
        self.task_id = task_id
        self.uid = uid
        self.user_id = user_id
        self.context = context
        self.access_key = access_key
        self.signature = signature
        self.skip_auth = skip_auth
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.context is not None:
            result['__context'] = self.context
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.signature is not None:
            result['signature'] = self.signature
        if self.skip_auth is not None:
            result['skipAuth'] = self.skip_auth
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('skipAuth') is not None:
            self.skip_auth = m.get('skipAuth')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        return self


class GetEndpointSwitchTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        db_link_id: int = None,
        err_msg: str = None,
        ori_uuid: str = None,
        status: str = None,
        task_id: str = None,
        uuid: str = None,
    ):
        self.account_id = account_id
        self.db_link_id = db_link_id
        self.err_msg = err_msg
        self.ori_uuid = ori_uuid
        self.status = status
        self.task_id = task_id
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.db_link_id is not None:
            result['DbLinkId'] = self.db_link_id
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.ori_uuid is not None:
            result['OriUuid'] = self.ori_uuid
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DbLinkId') is not None:
            self.db_link_id = m.get('DbLinkId')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('OriUuid') is not None:
            self.ori_uuid = m.get('OriUuid')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class GetEndpointSwitchTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetEndpointSwitchTaskResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
        synchro: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success
        self.synchro = synchro

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetEndpointSwitchTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class GetEndpointSwitchTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetEndpointSwitchTaskResponseBody = None,
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
            temp_model = GetEndpointSwitchTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEventOverviewRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        instance_id: str = None,
        min_level: str = None,
        start_time: str = None,
        tags: str = None,
        ticket_id: str = None,
    ):
        self.end_time = end_time
        self.instance_id = instance_id
        self.min_level = min_level
        self.start_time = start_time
        self.tags = tags
        self.ticket_id = ticket_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.min_level is not None:
            result['MinLevel'] = self.min_level
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MinLevel') is not None:
            self.min_level = m.get('MinLevel')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')
        return self


class GetEventOverviewResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetEventOverviewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetEventOverviewResponseBody = None,
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
            temp_model = GetEventOverviewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHDMAliyunResourceSyncResultRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        uid: str = None,
        user_id: str = None,
        context: str = None,
        access_key: str = None,
        signature: str = None,
        skip_auth: str = None,
        timestamp: str = None,
    ):
        self.task_id = task_id
        self.uid = uid
        self.user_id = user_id
        self.context = context
        self.access_key = access_key
        self.signature = signature
        self.skip_auth = skip_auth
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.context is not None:
            result['__context'] = self.context
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.signature is not None:
            result['signature'] = self.signature
        if self.skip_auth is not None:
            result['skipAuth'] = self.skip_auth
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('skipAuth') is not None:
            self.skip_auth = m.get('skipAuth')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        return self


class GetHDMAliyunResourceSyncResultResponseBodyDataSubResultsResourceSyncSubResult(TeaModel):
    def __init__(
        self,
        err_msg: str = None,
        resource_type: str = None,
        success: bool = None,
        sync_count: int = None,
    ):
        self.err_msg = err_msg
        self.resource_type = resource_type
        self.success = success
        self.sync_count = sync_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.success is not None:
            result['Success'] = self.success
        if self.sync_count is not None:
            result['SyncCount'] = self.sync_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SyncCount') is not None:
            self.sync_count = m.get('SyncCount')
        return self


class GetHDMAliyunResourceSyncResultResponseBodyDataSubResults(TeaModel):
    def __init__(
        self,
        resource_sync_sub_result: List[GetHDMAliyunResourceSyncResultResponseBodyDataSubResultsResourceSyncSubResult] = None,
    ):
        self.resource_sync_sub_result = resource_sync_sub_result

    def validate(self):
        if self.resource_sync_sub_result:
            for k in self.resource_sync_sub_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResourceSyncSubResult'] = []
        if self.resource_sync_sub_result is not None:
            for k in self.resource_sync_sub_result:
                result['ResourceSyncSubResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_sync_sub_result = []
        if m.get('ResourceSyncSubResult') is not None:
            for k in m.get('ResourceSyncSubResult'):
                temp_model = GetHDMAliyunResourceSyncResultResponseBodyDataSubResultsResourceSyncSubResult()
                self.resource_sync_sub_result.append(temp_model.from_map(k))
        return self


class GetHDMAliyunResourceSyncResultResponseBodyData(TeaModel):
    def __init__(
        self,
        error_msg: str = None,
        results: str = None,
        sub_results: GetHDMAliyunResourceSyncResultResponseBodyDataSubResults = None,
        sync_status: str = None,
    ):
        self.error_msg = error_msg
        self.results = results
        self.sub_results = sub_results
        self.sync_status = sync_status

    def validate(self):
        if self.sub_results:
            self.sub_results.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.results is not None:
            result['Results'] = self.results
        if self.sub_results is not None:
            result['SubResults'] = self.sub_results.to_map()
        if self.sync_status is not None:
            result['SyncStatus'] = self.sync_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Results') is not None:
            self.results = m.get('Results')
        if m.get('SubResults') is not None:
            temp_model = GetHDMAliyunResourceSyncResultResponseBodyDataSubResults()
            self.sub_results = temp_model.from_map(m['SubResults'])
        if m.get('SyncStatus') is not None:
            self.sync_status = m.get('SyncStatus')
        return self


class GetHDMAliyunResourceSyncResultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetHDMAliyunResourceSyncResultResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
        synchro: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success
        self.synchro = synchro

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetHDMAliyunResourceSyncResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class GetHDMAliyunResourceSyncResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetHDMAliyunResourceSyncResultResponseBody = None,
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
            temp_model = GetHDMAliyunResourceSyncResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHDMLastAliyunResourceSyncResultRequest(TeaModel):
    def __init__(
        self,
        uid: str = None,
        user_id: str = None,
        context: str = None,
        access_key: str = None,
        signature: str = None,
        skip_auth: str = None,
        timestamp: str = None,
    ):
        self.uid = uid
        self.user_id = user_id
        self.context = context
        self.access_key = access_key
        self.signature = signature
        self.skip_auth = skip_auth
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.context is not None:
            result['__context'] = self.context
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.signature is not None:
            result['signature'] = self.signature
        if self.skip_auth is not None:
            result['skipAuth'] = self.skip_auth
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('skipAuth') is not None:
            self.skip_auth = m.get('skipAuth')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        return self


class GetHDMLastAliyunResourceSyncResultResponseBodyDataSubResultsResourceSyncSubResult(TeaModel):
    def __init__(
        self,
        err_msg: str = None,
        resource_type: str = None,
        success: bool = None,
        sync_count: int = None,
    ):
        self.err_msg = err_msg
        self.resource_type = resource_type
        self.success = success
        self.sync_count = sync_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.success is not None:
            result['Success'] = self.success
        if self.sync_count is not None:
            result['SyncCount'] = self.sync_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SyncCount') is not None:
            self.sync_count = m.get('SyncCount')
        return self


class GetHDMLastAliyunResourceSyncResultResponseBodyDataSubResults(TeaModel):
    def __init__(
        self,
        resource_sync_sub_result: List[GetHDMLastAliyunResourceSyncResultResponseBodyDataSubResultsResourceSyncSubResult] = None,
    ):
        self.resource_sync_sub_result = resource_sync_sub_result

    def validate(self):
        if self.resource_sync_sub_result:
            for k in self.resource_sync_sub_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResourceSyncSubResult'] = []
        if self.resource_sync_sub_result is not None:
            for k in self.resource_sync_sub_result:
                result['ResourceSyncSubResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_sync_sub_result = []
        if m.get('ResourceSyncSubResult') is not None:
            for k in m.get('ResourceSyncSubResult'):
                temp_model = GetHDMLastAliyunResourceSyncResultResponseBodyDataSubResultsResourceSyncSubResult()
                self.resource_sync_sub_result.append(temp_model.from_map(k))
        return self


class GetHDMLastAliyunResourceSyncResultResponseBodyData(TeaModel):
    def __init__(
        self,
        error_msg: str = None,
        results: str = None,
        sub_results: GetHDMLastAliyunResourceSyncResultResponseBodyDataSubResults = None,
        sync_status: str = None,
    ):
        self.error_msg = error_msg
        self.results = results
        self.sub_results = sub_results
        self.sync_status = sync_status

    def validate(self):
        if self.sub_results:
            self.sub_results.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.results is not None:
            result['Results'] = self.results
        if self.sub_results is not None:
            result['SubResults'] = self.sub_results.to_map()
        if self.sync_status is not None:
            result['SyncStatus'] = self.sync_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Results') is not None:
            self.results = m.get('Results')
        if m.get('SubResults') is not None:
            temp_model = GetHDMLastAliyunResourceSyncResultResponseBodyDataSubResults()
            self.sub_results = temp_model.from_map(m['SubResults'])
        if m.get('SyncStatus') is not None:
            self.sync_status = m.get('SyncStatus')
        return self


class GetHDMLastAliyunResourceSyncResultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetHDMLastAliyunResourceSyncResultResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
        synchro: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success
        self.synchro = synchro

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetHDMLastAliyunResourceSyncResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class GetHDMLastAliyunResourceSyncResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetHDMLastAliyunResourceSyncResultResponseBody = None,
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
            temp_model = GetHDMLastAliyunResourceSyncResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceInspectionsRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        engine: str = None,
        instance_area: str = None,
        page_no: str = None,
        page_size: str = None,
        search_map: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.engine = engine
        self.instance_area = instance_area
        self.page_no = page_no
        self.page_size = page_size
        self.search_map = search_map
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.instance_area is not None:
            result['InstanceArea'] = self.instance_area
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_map is not None:
            result['SearchMap'] = self.search_map
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('InstanceArea') is not None:
            self.instance_area = m.get('InstanceArea')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchMap') is not None:
            self.search_map = m.get('SearchMap')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetInstanceInspectionsResponseBodyDataListBaseInspectionInstance(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        engine: str = None,
        engine_version: str = None,
        instance_area: str = None,
        instance_class: str = None,
        instance_id: str = None,
        network_type: str = None,
        node_id: str = None,
        region: str = None,
        uuid: str = None,
        vpc_id: str = None,
    ):
        self.account_id = account_id
        self.engine = engine
        self.engine_version = engine_version
        self.instance_area = instance_area
        self.instance_class = instance_class
        self.instance_id = instance_id
        self.network_type = network_type
        self.node_id = node_id
        self.region = region
        self.uuid = uuid
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.instance_area is not None:
            result['InstanceArea'] = self.instance_area
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.region is not None:
            result['Region'] = self.region
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('InstanceArea') is not None:
            self.instance_area = m.get('InstanceArea')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class GetInstanceInspectionsResponseBodyDataListBaseInspection(TeaModel):
    def __init__(
        self,
        data: str = None,
        end_time: int = None,
        gmt_create: int = None,
        instance: GetInstanceInspectionsResponseBodyDataListBaseInspectionInstance = None,
        score: int = None,
        score_map: str = None,
        start_time: int = None,
    ):
        self.data = data
        self.end_time = end_time
        self.gmt_create = gmt_create
        self.instance = instance
        self.score = score
        self.score_map = score_map
        self.start_time = start_time

    def validate(self):
        if self.instance:
            self.instance.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.instance is not None:
            result['Instance'] = self.instance.to_map()
        if self.score is not None:
            result['Score'] = self.score
        if self.score_map is not None:
            result['ScoreMap'] = self.score_map
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Instance') is not None:
            temp_model = GetInstanceInspectionsResponseBodyDataListBaseInspectionInstance()
            self.instance = temp_model.from_map(m['Instance'])
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('ScoreMap') is not None:
            self.score_map = m.get('ScoreMap')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetInstanceInspectionsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        base_inspection: List[GetInstanceInspectionsResponseBodyDataListBaseInspection] = None,
    ):
        self.base_inspection = base_inspection

    def validate(self):
        if self.base_inspection:
            for k in self.base_inspection:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BaseInspection'] = []
        if self.base_inspection is not None:
            for k in self.base_inspection:
                result['BaseInspection'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.base_inspection = []
        if m.get('BaseInspection') is not None:
            for k in m.get('BaseInspection'):
                temp_model = GetInstanceInspectionsResponseBodyDataListBaseInspection()
                self.base_inspection.append(temp_model.from_map(k))
        return self


class GetInstanceInspectionsResponseBodyData(TeaModel):
    def __init__(
        self,
        list: GetInstanceInspectionsResponseBodyDataList = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page_no = page_no
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            self.list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list is not None:
            result['List'] = self.list.to_map()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('List') is not None:
            temp_model = GetInstanceInspectionsResponseBodyDataList()
            self.list = temp_model.from_map(m['List'])
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetInstanceInspectionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetInstanceInspectionsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetInstanceInspectionsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetInstanceInspectionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetInstanceInspectionsResponseBody = None,
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
            temp_model = GetInstanceInspectionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRequestDiagnosisPageRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        instance_id: str = None,
        node_id: str = None,
        page_no: str = None,
        page_size: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.instance_id = instance_id
        self.node_id = node_id
        self.page_no = page_no
        self.page_size = page_size
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetRequestDiagnosisPageResponseBodyDataList(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        db_schema: str = None,
        engine: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        message_id: str = None,
        param: str = None,
        result: str = None,
        sql_id: str = None,
        state: int = None,
        uuid: str = None,
    ):
        self.account_id = account_id
        self.db_schema = db_schema
        self.engine = engine
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.message_id = message_id
        self.param = param
        self.result = result
        self.sql_id = sql_id
        self.state = state
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.db_schema is not None:
            result['dbSchema'] = self.db_schema
        if self.engine is not None:
            result['engine'] = self.engine
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.message_id is not None:
            result['messageId'] = self.message_id
        if self.param is not None:
            result['param'] = self.param
        if self.result is not None:
            result['result'] = self.result
        if self.sql_id is not None:
            result['sqlId'] = self.sql_id
        if self.state is not None:
            result['state'] = self.state
        if self.uuid is not None:
            result['uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('dbSchema') is not None:
            self.db_schema = m.get('dbSchema')
        if m.get('engine') is not None:
            self.engine = m.get('engine')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('messageId') is not None:
            self.message_id = m.get('messageId')
        if m.get('param') is not None:
            self.param = m.get('param')
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('sqlId') is not None:
            self.sql_id = m.get('sqlId')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        return self


class GetRequestDiagnosisPageResponseBodyData(TeaModel):
    def __init__(
        self,
        extra: str = None,
        list: List[GetRequestDiagnosisPageResponseBodyDataList] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.extra = extra
        self.list = list
        self.page_no = page_no
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra is not None:
            result['extra'] = self.extra
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = GetRequestDiagnosisPageResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class GetRequestDiagnosisPageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetRequestDiagnosisPageResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetRequestDiagnosisPageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetRequestDiagnosisPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRequestDiagnosisPageResponseBody = None,
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
            temp_model = GetRequestDiagnosisPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRequestDiagnosisResultRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        message_id: str = None,
        node_id: str = None,
    ):
        self.instance_id = instance_id
        self.message_id = message_id
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class GetRequestDiagnosisResultResponseBodyData(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        db_schema: str = None,
        engine: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        message_id: str = None,
        param: str = None,
        result: str = None,
        sql_id: str = None,
        state: int = None,
        uuid: str = None,
    ):
        self.account_id = account_id
        self.db_schema = db_schema
        self.engine = engine
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.message_id = message_id
        self.param = param
        self.result = result
        self.sql_id = sql_id
        self.state = state
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.db_schema is not None:
            result['dbSchema'] = self.db_schema
        if self.engine is not None:
            result['engine'] = self.engine
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.message_id is not None:
            result['messageId'] = self.message_id
        if self.param is not None:
            result['param'] = self.param
        if self.result is not None:
            result['result'] = self.result
        if self.sql_id is not None:
            result['sqlId'] = self.sql_id
        if self.state is not None:
            result['state'] = self.state
        if self.uuid is not None:
            result['uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('dbSchema') is not None:
            self.db_schema = m.get('dbSchema')
        if m.get('engine') is not None:
            self.engine = m.get('engine')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('messageId') is not None:
            self.message_id = m.get('messageId')
        if m.get('param') is not None:
            self.param = m.get('param')
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('sqlId') is not None:
            self.sql_id = m.get('sqlId')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        return self


class GetRequestDiagnosisResultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetRequestDiagnosisResultResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetRequestDiagnosisResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetRequestDiagnosisResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRequestDiagnosisResultResponseBody = None,
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
            temp_model = GetRequestDiagnosisResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceOptimizeHistoryListRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        end_time: str = None,
        instance_id: str = None,
        page: int = None,
        page_size: int = None,
        signature: str = None,
        start_time: str = None,
        uid: str = None,
        user_id: str = None,
        context: str = None,
    ):
        self.access_key = access_key
        self.end_time = end_time
        self.instance_id = instance_id
        self.page = page
        self.page_size = page_size
        self.signature = signature
        self.start_time = start_time
        self.uid = uid
        self.user_id = user_id
        self.context = context

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.context is not None:
            result['__context'] = self.context
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        return self


class GetResourceOptimizeHistoryListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
        synchro: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success
        self.synchro = synchro

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class GetResourceOptimizeHistoryListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetResourceOptimizeHistoryListResponseBody = None,
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
            temp_model = GetResourceOptimizeHistoryListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRunningSqlConcurrencyControlRulesRequest(TeaModel):
    def __init__(
        self,
        console_context: str = None,
        instance_id: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        self.console_context = console_context
        self.instance_id = instance_id
        self.page_no = page_no
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetRunningSqlConcurrencyControlRulesResponseBodyDataListRunningRules(TeaModel):
    def __init__(
        self,
        concurrency_control_time: int = None,
        instance_id: str = None,
        item_id: int = None,
        keywords_hash: str = None,
        max_concurrency: str = None,
        sql_keywords: str = None,
        sql_type: str = None,
        start_time: int = None,
        status: str = None,
        user_id: str = None,
    ):
        self.concurrency_control_time = concurrency_control_time
        self.instance_id = instance_id
        self.item_id = item_id
        self.keywords_hash = keywords_hash
        self.max_concurrency = max_concurrency
        self.sql_keywords = sql_keywords
        self.sql_type = sql_type
        self.start_time = start_time
        self.status = status
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.concurrency_control_time is not None:
            result['ConcurrencyControlTime'] = self.concurrency_control_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.keywords_hash is not None:
            result['KeywordsHash'] = self.keywords_hash
        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency
        if self.sql_keywords is not None:
            result['SqlKeywords'] = self.sql_keywords
        if self.sql_type is not None:
            result['SqlType'] = self.sql_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConcurrencyControlTime') is not None:
            self.concurrency_control_time = m.get('ConcurrencyControlTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('KeywordsHash') is not None:
            self.keywords_hash = m.get('KeywordsHash')
        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')
        if m.get('SqlKeywords') is not None:
            self.sql_keywords = m.get('SqlKeywords')
        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetRunningSqlConcurrencyControlRulesResponseBodyDataList(TeaModel):
    def __init__(
        self,
        running_rules: List[GetRunningSqlConcurrencyControlRulesResponseBodyDataListRunningRules] = None,
    ):
        self.running_rules = running_rules

    def validate(self):
        if self.running_rules:
            for k in self.running_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['runningRules'] = []
        if self.running_rules is not None:
            for k in self.running_rules:
                result['runningRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.running_rules = []
        if m.get('runningRules') is not None:
            for k in m.get('runningRules'):
                temp_model = GetRunningSqlConcurrencyControlRulesResponseBodyDataListRunningRules()
                self.running_rules.append(temp_model.from_map(k))
        return self


class GetRunningSqlConcurrencyControlRulesResponseBodyData(TeaModel):
    def __init__(
        self,
        list: GetRunningSqlConcurrencyControlRulesResponseBodyDataList = None,
        total: int = None,
    ):
        self.list = list
        self.total = total

    def validate(self):
        if self.list:
            self.list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list is not None:
            result['List'] = self.list.to_map()
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('List') is not None:
            temp_model = GetRunningSqlConcurrencyControlRulesResponseBodyDataList()
            self.list = temp_model.from_map(m['List'])
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetRunningSqlConcurrencyControlRulesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetRunningSqlConcurrencyControlRulesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetRunningSqlConcurrencyControlRulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetRunningSqlConcurrencyControlRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRunningSqlConcurrencyControlRulesResponseBody = None,
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
            temp_model = GetRunningSqlConcurrencyControlRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSqlConcurrencyControlRulesHistoryRequest(TeaModel):
    def __init__(
        self,
        console_context: str = None,
        instance_id: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        self.console_context = console_context
        self.instance_id = instance_id
        self.page_no = page_no
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetSqlConcurrencyControlRulesHistoryResponseBodyDataListRules(TeaModel):
    def __init__(
        self,
        concurrency_control_time: int = None,
        instance_id: str = None,
        item_id: int = None,
        keywords_hash: str = None,
        max_concurrency: int = None,
        sql_keywords: str = None,
        sql_type: str = None,
        start_time: int = None,
        status: str = None,
        user_id: str = None,
    ):
        self.concurrency_control_time = concurrency_control_time
        self.instance_id = instance_id
        self.item_id = item_id
        self.keywords_hash = keywords_hash
        self.max_concurrency = max_concurrency
        self.sql_keywords = sql_keywords
        self.sql_type = sql_type
        self.start_time = start_time
        self.status = status
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.concurrency_control_time is not None:
            result['ConcurrencyControlTime'] = self.concurrency_control_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.keywords_hash is not None:
            result['KeywordsHash'] = self.keywords_hash
        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency
        if self.sql_keywords is not None:
            result['SqlKeywords'] = self.sql_keywords
        if self.sql_type is not None:
            result['SqlType'] = self.sql_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConcurrencyControlTime') is not None:
            self.concurrency_control_time = m.get('ConcurrencyControlTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('KeywordsHash') is not None:
            self.keywords_hash = m.get('KeywordsHash')
        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')
        if m.get('SqlKeywords') is not None:
            self.sql_keywords = m.get('SqlKeywords')
        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetSqlConcurrencyControlRulesHistoryResponseBodyDataList(TeaModel):
    def __init__(
        self,
        rules: List[GetSqlConcurrencyControlRulesHistoryResponseBodyDataListRules] = None,
    ):
        self.rules = rules

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rules = []
        if m.get('rules') is not None:
            for k in m.get('rules'):
                temp_model = GetSqlConcurrencyControlRulesHistoryResponseBodyDataListRules()
                self.rules.append(temp_model.from_map(k))
        return self


class GetSqlConcurrencyControlRulesHistoryResponseBodyData(TeaModel):
    def __init__(
        self,
        list: GetSqlConcurrencyControlRulesHistoryResponseBodyDataList = None,
        total: int = None,
    ):
        self.list = list
        self.total = total

    def validate(self):
        if self.list:
            self.list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list is not None:
            result['List'] = self.list.to_map()
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('List') is not None:
            temp_model = GetSqlConcurrencyControlRulesHistoryResponseBodyDataList()
            self.list = temp_model.from_map(m['List'])
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetSqlConcurrencyControlRulesHistoryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetSqlConcurrencyControlRulesHistoryResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetSqlConcurrencyControlRulesHistoryResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSqlConcurrencyControlRulesHistoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSqlConcurrencyControlRulesHistoryResponseBody = None,
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
            temp_model = GetSqlConcurrencyControlRulesHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSqlOptimizeAdviceRequest(TeaModel):
    def __init__(
        self,
        console_context: str = None,
        end_dt: str = None,
        engine: str = None,
        instance_ids: str = None,
        start_dt: str = None,
    ):
        self.console_context = console_context
        self.end_dt = end_dt
        self.engine = engine
        self.instance_ids = instance_ids
        self.start_dt = start_dt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context
        if self.end_dt is not None:
            result['EndDt'] = self.end_dt
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.start_dt is not None:
            result['StartDt'] = self.start_dt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')
        if m.get('EndDt') is not None:
            self.end_dt = m.get('EndDt')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('StartDt') is not None:
            self.start_dt = m.get('StartDt')
        return self


class GetSqlOptimizeAdviceResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        download_url: str = None,
        expire_time: str = None,
        status: str = None,
        status_code: str = None,
        task_id: str = None,
    ):
        self.create_time = create_time
        self.download_url = download_url
        self.expire_time = expire_time
        self.status = status
        self.status_code = status_code
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.status is not None:
            result['Status'] = self.status
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetSqlOptimizeAdviceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetSqlOptimizeAdviceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetSqlOptimizeAdviceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSqlOptimizeAdviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSqlOptimizeAdviceResponseBody = None,
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
            temp_model = GetSqlOptimizeAdviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunCloudBenchTaskRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

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


class RunCloudBenchTaskResponseBodyDataPreCheckItem(TeaModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        message: str = None,
        name: str = None,
        order: int = None,
        status: str = None,
    ):
        self.code = code
        self.details = details
        self.message = message
        self.name = name
        self.order = order
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class RunCloudBenchTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        pre_check_item: List[RunCloudBenchTaskResponseBodyDataPreCheckItem] = None,
    ):
        self.pre_check_item = pre_check_item

    def validate(self):
        if self.pre_check_item:
            for k in self.pre_check_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PreCheckItem'] = []
        if self.pre_check_item is not None:
            for k in self.pre_check_item:
                result['PreCheckItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.pre_check_item = []
        if m.get('PreCheckItem') is not None:
            for k in m.get('PreCheckItem'):
                temp_model = RunCloudBenchTaskResponseBodyDataPreCheckItem()
                self.pre_check_item.append(temp_model.from_map(k))
        return self


class RunCloudBenchTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: RunCloudBenchTaskResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = RunCloudBenchTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RunCloudBenchTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RunCloudBenchTaskResponseBody = None,
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
            temp_model = RunCloudBenchTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopCloudBenchTaskRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

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


class StopCloudBenchTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StopCloudBenchTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopCloudBenchTaskResponseBody = None,
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
            temp_model = StopCloudBenchTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopOrRollbackOptimizeTaskRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        instance_id: str = None,
        signature: str = None,
        stop_or_rollback: str = None,
        task_type: str = None,
        task_uuid: str = None,
        uid: str = None,
        user_id: str = None,
        context: str = None,
    ):
        self.access_key = access_key
        self.instance_id = instance_id
        self.signature = signature
        self.stop_or_rollback = stop_or_rollback
        self.task_type = task_type
        self.task_uuid = task_uuid
        self.uid = uid
        self.user_id = user_id
        self.context = context

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.stop_or_rollback is not None:
            result['StopOrRollback'] = self.stop_or_rollback
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_uuid is not None:
            result['TaskUuid'] = self.task_uuid
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.context is not None:
            result['__context'] = self.context
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('StopOrRollback') is not None:
            self.stop_or_rollback = m.get('StopOrRollback')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskUuid') is not None:
            self.task_uuid = m.get('TaskUuid')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        return self


class StopOrRollbackOptimizeTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
        synchro: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success
        self.synchro = synchro

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class StopOrRollbackOptimizeTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopOrRollbackOptimizeTaskResponseBody = None,
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
            temp_model = StopOrRollbackOptimizeTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncHDMAliyunResourceRequest(TeaModel):
    def __init__(
        self,
        async_: str = None,
        resource_types: str = None,
        uid: str = None,
        user_id: str = None,
        wait_for_modify_security_ips: str = None,
        context: str = None,
        access_key: str = None,
        signature: str = None,
        skip_auth: str = None,
        timestamp: str = None,
    ):
        self.async_ = async_
        self.resource_types = resource_types
        self.uid = uid
        self.user_id = user_id
        self.wait_for_modify_security_ips = wait_for_modify_security_ips
        self.context = context
        self.access_key = access_key
        self.signature = signature
        self.skip_auth = skip_auth
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_ is not None:
            result['Async'] = self.async_
        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.wait_for_modify_security_ips is not None:
            result['WaitForModifySecurityIps'] = self.wait_for_modify_security_ips
        if self.context is not None:
            result['__context'] = self.context
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.signature is not None:
            result['signature'] = self.signature
        if self.skip_auth is not None:
            result['skipAuth'] = self.skip_auth
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WaitForModifySecurityIps') is not None:
            self.wait_for_modify_security_ips = m.get('WaitForModifySecurityIps')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('skipAuth') is not None:
            self.skip_auth = m.get('skipAuth')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        return self


class SyncHDMAliyunResourceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
        synchro: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success
        self.synchro = synchro

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class SyncHDMAliyunResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SyncHDMAliyunResourceResponseBody = None,
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
            temp_model = SyncHDMAliyunResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TurnOffAutoResourceOptimizeRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        instance_id: str = None,
        signature: str = None,
        uid: str = None,
        user_id: str = None,
        context: str = None,
    ):
        self.access_key = access_key
        self.instance_id = instance_id
        self.signature = signature
        self.uid = uid
        self.user_id = user_id
        self.context = context

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.context is not None:
            result['__context'] = self.context
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        return self


class TurnOffAutoResourceOptimizeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
        synchro: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success
        self.synchro = synchro

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class TurnOffAutoResourceOptimizeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TurnOffAutoResourceOptimizeResponseBody = None,
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
            temp_model = TurnOffAutoResourceOptimizeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAutoResourceOptimizeConfigRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        auto_defragment: int = None,
        auto_duplicate_index_delete: int = None,
        instance_id: str = None,
        signature: str = None,
        table_fragmentation_ratio: float = None,
        table_space_size: float = None,
        uid: str = None,
        user_id: str = None,
        context: str = None,
    ):
        self.access_key = access_key
        self.auto_defragment = auto_defragment
        self.auto_duplicate_index_delete = auto_duplicate_index_delete
        self.instance_id = instance_id
        self.signature = signature
        self.table_fragmentation_ratio = table_fragmentation_ratio
        self.table_space_size = table_space_size
        self.uid = uid
        self.user_id = user_id
        self.context = context

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.auto_defragment is not None:
            result['AutoDefragment'] = self.auto_defragment
        if self.auto_duplicate_index_delete is not None:
            result['AutoDuplicateIndexDelete'] = self.auto_duplicate_index_delete
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.table_fragmentation_ratio is not None:
            result['TableFragmentationRatio'] = self.table_fragmentation_ratio
        if self.table_space_size is not None:
            result['TableSpaceSize'] = self.table_space_size
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.context is not None:
            result['__context'] = self.context
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('AutoDefragment') is not None:
            self.auto_defragment = m.get('AutoDefragment')
        if m.get('AutoDuplicateIndexDelete') is not None:
            self.auto_duplicate_index_delete = m.get('AutoDuplicateIndexDelete')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('TableFragmentationRatio') is not None:
            self.table_fragmentation_ratio = m.get('TableFragmentationRatio')
        if m.get('TableSpaceSize') is not None:
            self.table_space_size = m.get('TableSpaceSize')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        return self


class UpdateAutoResourceOptimizeConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
        synchro: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success
        self.synchro = synchro

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class UpdateAutoResourceOptimizeConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAutoResourceOptimizeConfigResponseBody = None,
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
            temp_model = UpdateAutoResourceOptimizeConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


