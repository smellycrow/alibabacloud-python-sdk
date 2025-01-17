# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class AddBuDBInstanceRelationRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        dbinstance_id: str = None,
        business_unit: str = None,
    ):
        self.owner_id = owner_id
        self.dbinstance_id = dbinstance_id
        self.business_unit = business_unit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.business_unit is not None:
            result['BusinessUnit'] = self.business_unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('BusinessUnit') is not None:
            self.business_unit = m.get('BusinessUnit')
        return self


class AddBuDBInstanceRelationResponseBody(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        request_id: str = None,
        business_unit: str = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.request_id = request_id
        self.business_unit = business_unit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.business_unit is not None:
            result['BusinessUnit'] = self.business_unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BusinessUnit') is not None:
            self.business_unit = m.get('BusinessUnit')
        return self


class AddBuDBInstanceRelationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddBuDBInstanceRelationResponseBody = None,
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
            temp_model = AddBuDBInstanceRelationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AllocateInstancePublicConnectionRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        dbinstance_id: str = None,
        connection_string_prefix: str = None,
        port: str = None,
        address_type: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.dbinstance_id = dbinstance_id
        self.connection_string_prefix = connection_string_prefix
        self.port = port
        self.address_type = address_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix
        if self.port is not None:
            result['Port'] = self.port
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        return self


class AllocateInstancePublicConnectionResponseBody(TeaModel):
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


class AllocateInstancePublicConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AllocateInstancePublicConnectionResponseBody = None,
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
            temp_model = AllocateInstancePublicConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckServiceLinkedRoleRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CheckServiceLinkedRoleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        has_service_linked_role: str = None,
        region_id: str = None,
    ):
        self.request_id = request_id
        self.has_service_linked_role = has_service_linked_role
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.has_service_linked_role is not None:
            result['HasServiceLinkedRole'] = self.has_service_linked_role
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HasServiceLinkedRole') is not None:
            self.has_service_linked_role = m.get('HasServiceLinkedRole')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CheckServiceLinkedRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckServiceLinkedRoleResponseBody = None,
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
            temp_model = CheckServiceLinkedRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAccountRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        dbinstance_id: str = None,
        database_name: str = None,
        account_name: str = None,
        account_password: str = None,
        account_description: str = None,
    ):
        self.owner_id = owner_id
        self.dbinstance_id = dbinstance_id
        self.database_name = database_name
        self.account_name = account_name
        self.account_password = account_password
        self.account_description = account_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        return self


class CreateAccountResponseBody(TeaModel):
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


class CreateAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAccountResponseBody = None,
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
            temp_model = CreateAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDBInstanceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        region_id: str = None,
        zone_id: str = None,
        engine_version: str = None,
        engine: str = None,
        dbinstance_class: str = None,
        dbinstance_group_count: str = None,
        dbinstance_description: str = None,
        security_iplist: str = None,
        pay_type: str = None,
        period: str = None,
        used_time: str = None,
        client_token: str = None,
        instance_network_type: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        private_ip_address: str = None,
    ):
        self.owner_id = owner_id
        self.region_id = region_id
        self.zone_id = zone_id
        self.engine_version = engine_version
        self.engine = engine
        self.dbinstance_class = dbinstance_class
        self.dbinstance_group_count = dbinstance_group_count
        self.dbinstance_description = dbinstance_description
        self.security_iplist = security_iplist
        self.pay_type = pay_type
        self.period = period
        self.used_time = used_time
        self.client_token = client_token
        self.instance_network_type = instance_network_type
        self.vpcid = vpcid
        self.v_switch_id = v_switch_id
        self.private_ip_address = private_ip_address

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class
        if self.dbinstance_group_count is not None:
            result['DBInstanceGroupCount'] = self.dbinstance_group_count
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period is not None:
            result['Period'] = self.period
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')
        if m.get('DBInstanceGroupCount') is not None:
            self.dbinstance_group_count = m.get('DBInstanceGroupCount')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        return self


class CreateDBInstanceResponseBody(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        request_id: str = None,
        port: str = None,
        connection_string: str = None,
        order_id: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.request_id = request_id
        self.port = port
        self.connection_string = connection_string
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.port is not None:
            result['Port'] = self.port
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateDBInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDBInstanceResponseBody = None,
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
            temp_model = CreateDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateECSDBInstanceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        region_id: str = None,
        zone_id: str = None,
        engine_version: str = None,
        engine: str = None,
        instance_spec: str = None,
        seg_node_num: int = None,
        seg_storage_type: str = None,
        storage_size: int = None,
        dbinstance_description: str = None,
        security_iplist: str = None,
        pay_type: str = None,
        period: str = None,
        used_time: str = None,
        client_token: str = None,
        instance_network_type: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        private_ip_address: str = None,
        encryption_key: str = None,
        encryption_type: str = None,
        master_node_num: int = None,
        src_db_instance_name: str = None,
        backup_id: str = None,
    ):
        self.owner_id = owner_id
        self.region_id = region_id
        self.zone_id = zone_id
        self.engine_version = engine_version
        self.engine = engine
        self.instance_spec = instance_spec
        self.seg_node_num = seg_node_num
        self.seg_storage_type = seg_storage_type
        self.storage_size = storage_size
        self.dbinstance_description = dbinstance_description
        self.security_iplist = security_iplist
        self.pay_type = pay_type
        self.period = period
        self.used_time = used_time
        self.client_token = client_token
        self.instance_network_type = instance_network_type
        self.vpcid = vpcid
        self.v_switch_id = v_switch_id
        self.private_ip_address = private_ip_address
        self.encryption_key = encryption_key
        self.encryption_type = encryption_type
        self.master_node_num = master_node_num
        self.src_db_instance_name = src_db_instance_name
        self.backup_id = backup_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec
        if self.seg_node_num is not None:
            result['SegNodeNum'] = self.seg_node_num
        if self.seg_storage_type is not None:
            result['SegStorageType'] = self.seg_storage_type
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period is not None:
            result['Period'] = self.period
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key
        if self.encryption_type is not None:
            result['EncryptionType'] = self.encryption_type
        if self.master_node_num is not None:
            result['MasterNodeNum'] = self.master_node_num
        if self.src_db_instance_name is not None:
            result['SrcDbInstanceName'] = self.src_db_instance_name
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')
        if m.get('SegNodeNum') is not None:
            self.seg_node_num = m.get('SegNodeNum')
        if m.get('SegStorageType') is not None:
            self.seg_storage_type = m.get('SegStorageType')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')
        if m.get('EncryptionType') is not None:
            self.encryption_type = m.get('EncryptionType')
        if m.get('MasterNodeNum') is not None:
            self.master_node_num = m.get('MasterNodeNum')
        if m.get('SrcDbInstanceName') is not None:
            self.src_db_instance_name = m.get('SrcDbInstanceName')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        return self


class CreateECSDBInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        dbinstance_id: str = None,
        port: str = None,
        connection_string: str = None,
        order_id: str = None,
    ):
        self.request_id = request_id
        self.dbinstance_id = dbinstance_id
        self.port = port
        self.connection_string = connection_string
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.port is not None:
            result['Port'] = self.port
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateECSDBInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateECSDBInstanceResponseBody = None,
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
            temp_model = CreateECSDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceLinkedRoleRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        owner_id: int = None,
    ):
        self.region_id = region_id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class CreateServiceLinkedRoleResponseBody(TeaModel):
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


class CreateServiceLinkedRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateServiceLinkedRoleResponseBody = None,
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
            temp_model = CreateServiceLinkedRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDatabaseRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        dbname: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.dbname = dbname

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbname is not None:
            result['DBName'] = self.dbname
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        return self


class DeleteDatabaseResponseBody(TeaModel):
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


class DeleteDatabaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDatabaseResponseBody = None,
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
            temp_model = DeleteDatabaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDBInstanceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        client_token: str = None,
        dbinstance_id: str = None,
    ):
        self.owner_id = owner_id
        self.client_token = client_token
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DeleteDBInstanceResponseBody(TeaModel):
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


class DeleteDBInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDBInstanceResponseBody = None,
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
            temp_model = DeleteDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccountsRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        account_name: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.account_name = account_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class DescribeAccountsResponseBodyAccountsDBInstanceAccount(TeaModel):
    def __init__(
        self,
        account_description: str = None,
        dbinstance_id: str = None,
        account_status: str = None,
        account_name: str = None,
    ):
        self.account_description = account_description
        self.dbinstance_id = dbinstance_id
        self.account_status = account_status
        self.account_name = account_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.account_status is not None:
            result['AccountStatus'] = self.account_status
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('AccountStatus') is not None:
            self.account_status = m.get('AccountStatus')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class DescribeAccountsResponseBodyAccounts(TeaModel):
    def __init__(
        self,
        dbinstance_account: List[DescribeAccountsResponseBodyAccountsDBInstanceAccount] = None,
    ):
        self.dbinstance_account = dbinstance_account

    def validate(self):
        if self.dbinstance_account:
            for k in self.dbinstance_account:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBInstanceAccount'] = []
        if self.dbinstance_account is not None:
            for k in self.dbinstance_account:
                result['DBInstanceAccount'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbinstance_account = []
        if m.get('DBInstanceAccount') is not None:
            for k in m.get('DBInstanceAccount'):
                temp_model = DescribeAccountsResponseBodyAccountsDBInstanceAccount()
                self.dbinstance_account.append(temp_model.from_map(k))
        return self


class DescribeAccountsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        accounts: DescribeAccountsResponseBodyAccounts = None,
    ):
        self.request_id = request_id
        self.accounts = accounts

    def validate(self):
        if self.accounts:
            self.accounts.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.accounts is not None:
            result['Accounts'] = self.accounts.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Accounts') is not None:
            temp_model = DescribeAccountsResponseBodyAccounts()
            self.accounts = temp_model.from_map(m['Accounts'])
        return self


class DescribeAccountsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAccountsResponseBody = None,
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
            temp_model = DescribeAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAvailableResourcesRequest(TeaModel):
    def __init__(
        self,
        region: str = None,
        zone_id: str = None,
        charge_type: str = None,
    ):
        self.region = region
        self.zone_id = zone_id
        self.charge_type = charge_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        return self


class DescribeAvailableResourcesResponseBodyResourcesSupportedEnginesSupportedInstanceClassesNodeCount(TeaModel):
    def __init__(
        self,
        step: str = None,
        min_count: str = None,
        max_count: str = None,
    ):
        self.step = step
        self.min_count = min_count
        self.max_count = max_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.step is not None:
            result['Step'] = self.step
        if self.min_count is not None:
            result['MinCount'] = self.min_count
        if self.max_count is not None:
            result['MaxCount'] = self.max_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Step') is not None:
            self.step = m.get('Step')
        if m.get('MinCount') is not None:
            self.min_count = m.get('MinCount')
        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')
        return self


class DescribeAvailableResourcesResponseBodyResourcesSupportedEnginesSupportedInstanceClassesStorageSize(TeaModel):
    def __init__(
        self,
        step: str = None,
        min_count: str = None,
        max_count: str = None,
    ):
        self.step = step
        self.min_count = min_count
        self.max_count = max_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.step is not None:
            result['Step'] = self.step
        if self.min_count is not None:
            result['MinCount'] = self.min_count
        if self.max_count is not None:
            result['MaxCount'] = self.max_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Step') is not None:
            self.step = m.get('Step')
        if m.get('MinCount') is not None:
            self.min_count = m.get('MinCount')
        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')
        return self


class DescribeAvailableResourcesResponseBodyResourcesSupportedEnginesSupportedInstanceClasses(TeaModel):
    def __init__(
        self,
        storage_type: str = None,
        description: str = None,
        display_class: str = None,
        instance_class: str = None,
        node_count: DescribeAvailableResourcesResponseBodyResourcesSupportedEnginesSupportedInstanceClassesNodeCount = None,
        storage_size: DescribeAvailableResourcesResponseBodyResourcesSupportedEnginesSupportedInstanceClassesStorageSize = None,
    ):
        self.storage_type = storage_type
        self.description = description
        self.display_class = display_class
        self.instance_class = instance_class
        self.node_count = node_count
        self.storage_size = storage_size

    def validate(self):
        if self.node_count:
            self.node_count.validate()
        if self.storage_size:
            self.storage_size.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.description is not None:
            result['Description'] = self.description
        if self.display_class is not None:
            result['DisplayClass'] = self.display_class
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.node_count is not None:
            result['NodeCount'] = self.node_count.to_map()
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayClass') is not None:
            self.display_class = m.get('DisplayClass')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('NodeCount') is not None:
            temp_model = DescribeAvailableResourcesResponseBodyResourcesSupportedEnginesSupportedInstanceClassesNodeCount()
            self.node_count = temp_model.from_map(m['NodeCount'])
        if m.get('StorageSize') is not None:
            temp_model = DescribeAvailableResourcesResponseBodyResourcesSupportedEnginesSupportedInstanceClassesStorageSize()
            self.storage_size = temp_model.from_map(m['StorageSize'])
        return self


class DescribeAvailableResourcesResponseBodyResourcesSupportedEngines(TeaModel):
    def __init__(
        self,
        supported_engine_version: str = None,
        mode: str = None,
        supported_instance_classes: List[DescribeAvailableResourcesResponseBodyResourcesSupportedEnginesSupportedInstanceClasses] = None,
    ):
        self.supported_engine_version = supported_engine_version
        self.mode = mode
        self.supported_instance_classes = supported_instance_classes

    def validate(self):
        if self.supported_instance_classes:
            for k in self.supported_instance_classes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.supported_engine_version is not None:
            result['SupportedEngineVersion'] = self.supported_engine_version
        if self.mode is not None:
            result['Mode'] = self.mode
        result['SupportedInstanceClasses'] = []
        if self.supported_instance_classes is not None:
            for k in self.supported_instance_classes:
                result['SupportedInstanceClasses'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SupportedEngineVersion') is not None:
            self.supported_engine_version = m.get('SupportedEngineVersion')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        self.supported_instance_classes = []
        if m.get('SupportedInstanceClasses') is not None:
            for k in m.get('SupportedInstanceClasses'):
                temp_model = DescribeAvailableResourcesResponseBodyResourcesSupportedEnginesSupportedInstanceClasses()
                self.supported_instance_classes.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourcesResponseBodyResources(TeaModel):
    def __init__(
        self,
        zone_id: str = None,
        supported_engines: List[DescribeAvailableResourcesResponseBodyResourcesSupportedEngines] = None,
    ):
        self.zone_id = zone_id
        self.supported_engines = supported_engines

    def validate(self):
        if self.supported_engines:
            for k in self.supported_engines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        result['SupportedEngines'] = []
        if self.supported_engines is not None:
            for k in self.supported_engines:
                result['SupportedEngines'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        self.supported_engines = []
        if m.get('SupportedEngines') is not None:
            for k in m.get('SupportedEngines'):
                temp_model = DescribeAvailableResourcesResponseBodyResourcesSupportedEngines()
                self.supported_engines.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourcesResponseBody(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        request_id: str = None,
        resources: List[DescribeAvailableResourcesResponseBodyResources] = None,
    ):
        self.region_id = region_id
        self.request_id = request_id
        self.resources = resources

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = DescribeAvailableResourcesResponseBodyResources()
                self.resources.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAvailableResourcesResponseBody = None,
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
            temp_model = DescribeAvailableResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupPolicyRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
    ):
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeBackupPolicyResponseBody(TeaModel):
    def __init__(
        self,
        backup_retention_period: int = None,
        request_id: str = None,
        preferred_backup_period: str = None,
        preferred_backup_time: str = None,
        recovery_point_period: str = None,
        enable_recovery_point: bool = None,
    ):
        self.backup_retention_period = backup_retention_period
        self.request_id = request_id
        self.preferred_backup_period = preferred_backup_period
        self.preferred_backup_time = preferred_backup_time
        self.recovery_point_period = recovery_point_period
        self.enable_recovery_point = enable_recovery_point

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_retention_period is not None:
            result['BackupRetentionPeriod'] = self.backup_retention_period
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period
        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time
        if self.recovery_point_period is not None:
            result['RecoveryPointPeriod'] = self.recovery_point_period
        if self.enable_recovery_point is not None:
            result['EnableRecoveryPoint'] = self.enable_recovery_point
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')
        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')
        if m.get('RecoveryPointPeriod') is not None:
            self.recovery_point_period = m.get('RecoveryPointPeriod')
        if m.get('EnableRecoveryPoint') is not None:
            self.enable_recovery_point = m.get('EnableRecoveryPoint')
        return self


class DescribeBackupPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeBackupPolicyResponseBody = None,
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
            temp_model = DescribeBackupPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataBackupsRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        backup_id: str = None,
        start_time: str = None,
        end_time: str = None,
        page_size: int = None,
        page_number: int = None,
        data_type: str = None,
        backup_mode: str = None,
        backup_status: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.backup_id = backup_id
        self.start_time = start_time
        self.end_time = end_time
        self.page_size = page_size
        self.page_number = page_number
        self.data_type = data_type
        self.backup_mode = backup_mode
        self.backup_status = backup_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode
        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')
        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')
        return self


class DescribeDataBackupsResponseBodyItems(TeaModel):
    def __init__(
        self,
        data_type: str = None,
        consistent_time: int = None,
        backup_status: str = None,
        backup_start_time: str = None,
        backup_end_time: str = None,
        backup_end_time_local: str = None,
        backup_set_id: str = None,
        bakset_name: str = None,
        backup_size: int = None,
        backup_mode: str = None,
        backup_start_time_local: str = None,
        dbinstance_id: str = None,
    ):
        self.data_type = data_type
        self.consistent_time = consistent_time
        self.backup_status = backup_status
        self.backup_start_time = backup_start_time
        self.backup_end_time = backup_end_time
        self.backup_end_time_local = backup_end_time_local
        self.backup_set_id = backup_set_id
        self.bakset_name = bakset_name
        self.backup_size = backup_size
        self.backup_mode = backup_mode
        self.backup_start_time_local = backup_start_time_local
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.consistent_time is not None:
            result['ConsistentTime'] = self.consistent_time
        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status
        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time
        if self.backup_end_time is not None:
            result['BackupEndTime'] = self.backup_end_time
        if self.backup_end_time_local is not None:
            result['BackupEndTimeLocal'] = self.backup_end_time_local
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id
        if self.bakset_name is not None:
            result['BaksetName'] = self.bakset_name
        if self.backup_size is not None:
            result['BackupSize'] = self.backup_size
        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode
        if self.backup_start_time_local is not None:
            result['BackupStartTimeLocal'] = self.backup_start_time_local
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('ConsistentTime') is not None:
            self.consistent_time = m.get('ConsistentTime')
        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')
        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')
        if m.get('BackupEndTime') is not None:
            self.backup_end_time = m.get('BackupEndTime')
        if m.get('BackupEndTimeLocal') is not None:
            self.backup_end_time_local = m.get('BackupEndTimeLocal')
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')
        if m.get('BaksetName') is not None:
            self.bakset_name = m.get('BaksetName')
        if m.get('BackupSize') is not None:
            self.backup_size = m.get('BackupSize')
        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')
        if m.get('BackupStartTimeLocal') is not None:
            self.backup_start_time_local = m.get('BackupStartTimeLocal')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeDataBackupsResponseBody(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        total_count: int = None,
        items: List[DescribeDataBackupsResponseBodyItems] = None,
    ):
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.total_count = total_count
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeDataBackupsResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        return self


class DescribeDataBackupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDataBackupsResponseBody = None,
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
            temp_model = DescribeDataBackupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClusterPerformanceRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        key: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.key = key
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.key is not None:
            result['Key'] = self.key
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDBClusterPerformanceResponseBodyPerformanceKeysSeriesValues(TeaModel):
    def __init__(
        self,
        point: List[str] = None,
    ):
        self.point = point

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.point is not None:
            result['Point'] = self.point
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Point') is not None:
            self.point = m.get('Point')
        return self


class DescribeDBClusterPerformanceResponseBodyPerformanceKeysSeries(TeaModel):
    def __init__(
        self,
        role: str = None,
        name: str = None,
        values: List[DescribeDBClusterPerformanceResponseBodyPerformanceKeysSeriesValues] = None,
    ):
        self.role = role
        self.name = name
        self.values = values

    def validate(self):
        if self.values:
            for k in self.values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role is not None:
            result['Role'] = self.role
        if self.name is not None:
            result['Name'] = self.name
        result['Values'] = []
        if self.values is not None:
            for k in self.values:
                result['Values'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.values = []
        if m.get('Values') is not None:
            for k in m.get('Values'):
                temp_model = DescribeDBClusterPerformanceResponseBodyPerformanceKeysSeriesValues()
                self.values.append(temp_model.from_map(k))
        return self


class DescribeDBClusterPerformanceResponseBodyPerformanceKeys(TeaModel):
    def __init__(
        self,
        name: str = None,
        unit: str = None,
        series: List[DescribeDBClusterPerformanceResponseBodyPerformanceKeysSeries] = None,
    ):
        self.name = name
        self.unit = unit
        self.series = series

    def validate(self):
        if self.series:
            for k in self.series:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.unit is not None:
            result['Unit'] = self.unit
        result['Series'] = []
        if self.series is not None:
            for k in self.series:
                result['Series'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        self.series = []
        if m.get('Series') is not None:
            for k in m.get('Series'):
                temp_model = DescribeDBClusterPerformanceResponseBodyPerformanceKeysSeries()
                self.series.append(temp_model.from_map(k))
        return self


class DescribeDBClusterPerformanceResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        request_id: str = None,
        dbcluster_id: str = None,
        performance_keys: List[DescribeDBClusterPerformanceResponseBodyPerformanceKeys] = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.request_id = request_id
        self.dbcluster_id = dbcluster_id
        self.performance_keys = performance_keys

    def validate(self):
        if self.performance_keys:
            for k in self.performance_keys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        result['PerformanceKeys'] = []
        if self.performance_keys is not None:
            for k in self.performance_keys:
                result['PerformanceKeys'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        self.performance_keys = []
        if m.get('PerformanceKeys') is not None:
            for k in m.get('PerformanceKeys'):
                temp_model = DescribeDBClusterPerformanceResponseBodyPerformanceKeys()
                self.performance_keys.append(temp_model.from_map(k))
        return self


class DescribeDBClusterPerformanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDBClusterPerformanceResponseBody = None,
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
            temp_model = DescribeDBClusterPerformanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        dbinstance_id: str = None,
    ):
        self.owner_id = owner_id
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeTagsTag(TeaModel):
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


class DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeTags(TeaModel):
    def __init__(
        self,
        tag: List[DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttribute(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
        creation_time: str = None,
        dbinstance_cpu_cores: int = None,
        segment_counts: int = None,
        storage_per_node: int = None,
        dbinstance_memory: int = None,
        host_type: str = None,
        pay_type: str = None,
        storage_type: str = None,
        cpu_cores_per_node: int = None,
        availability_value: str = None,
        read_delay_time: str = None,
        connection_mode: str = None,
        port: str = None,
        lock_mode: str = None,
        engine_version: str = None,
        storage_unit: str = None,
        memory_per_node: int = None,
        connection_string: str = None,
        instance_network_type: str = None,
        security_iplist: str = None,
        memory_unit: str = None,
        dbinstance_class_type: str = None,
        dbinstance_description: str = None,
        dbinstance_group_count: str = None,
        expire_time: str = None,
        dbinstance_net_type: str = None,
        maintain_start_time: str = None,
        maintain_end_time: str = None,
        lock_reason: str = None,
        dbinstance_status: str = None,
        region_id: str = None,
        dbinstance_disk_mbps: int = None,
        dbinstance_storage: int = None,
        zone_id: str = None,
        max_connections: int = None,
        dbinstance_id: str = None,
        dbinstance_class: str = None,
        engine: str = None,
        tags: DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeTags = None,
    ):
        self.vpc_id = vpc_id
        self.creation_time = creation_time
        self.dbinstance_cpu_cores = dbinstance_cpu_cores
        self.segment_counts = segment_counts
        self.storage_per_node = storage_per_node
        self.dbinstance_memory = dbinstance_memory
        self.host_type = host_type
        self.pay_type = pay_type
        self.storage_type = storage_type
        self.cpu_cores_per_node = cpu_cores_per_node
        self.availability_value = availability_value
        self.read_delay_time = read_delay_time
        self.connection_mode = connection_mode
        self.port = port
        self.lock_mode = lock_mode
        self.engine_version = engine_version
        self.storage_unit = storage_unit
        self.memory_per_node = memory_per_node
        self.connection_string = connection_string
        self.instance_network_type = instance_network_type
        self.security_iplist = security_iplist
        self.memory_unit = memory_unit
        self.dbinstance_class_type = dbinstance_class_type
        self.dbinstance_description = dbinstance_description
        self.dbinstance_group_count = dbinstance_group_count
        self.expire_time = expire_time
        self.dbinstance_net_type = dbinstance_net_type
        self.maintain_start_time = maintain_start_time
        self.maintain_end_time = maintain_end_time
        self.lock_reason = lock_reason
        self.dbinstance_status = dbinstance_status
        self.region_id = region_id
        self.dbinstance_disk_mbps = dbinstance_disk_mbps
        self.dbinstance_storage = dbinstance_storage
        self.zone_id = zone_id
        self.max_connections = max_connections
        self.dbinstance_id = dbinstance_id
        self.dbinstance_class = dbinstance_class
        self.engine = engine
        self.tags = tags

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.dbinstance_cpu_cores is not None:
            result['DBInstanceCpuCores'] = self.dbinstance_cpu_cores
        if self.segment_counts is not None:
            result['SegmentCounts'] = self.segment_counts
        if self.storage_per_node is not None:
            result['StoragePerNode'] = self.storage_per_node
        if self.dbinstance_memory is not None:
            result['DBInstanceMemory'] = self.dbinstance_memory
        if self.host_type is not None:
            result['HostType'] = self.host_type
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.cpu_cores_per_node is not None:
            result['CpuCoresPerNode'] = self.cpu_cores_per_node
        if self.availability_value is not None:
            result['AvailabilityValue'] = self.availability_value
        if self.read_delay_time is not None:
            result['ReadDelayTime'] = self.read_delay_time
        if self.connection_mode is not None:
            result['ConnectionMode'] = self.connection_mode
        if self.port is not None:
            result['Port'] = self.port
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.storage_unit is not None:
            result['StorageUnit'] = self.storage_unit
        if self.memory_per_node is not None:
            result['MemoryPerNode'] = self.memory_per_node
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        if self.memory_unit is not None:
            result['MemoryUnit'] = self.memory_unit
        if self.dbinstance_class_type is not None:
            result['DBInstanceClassType'] = self.dbinstance_class_type
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.dbinstance_group_count is not None:
            result['DBInstanceGroupCount'] = self.dbinstance_group_count
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.dbinstance_net_type is not None:
            result['DBInstanceNetType'] = self.dbinstance_net_type
        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time
        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.dbinstance_status is not None:
            result['DBInstanceStatus'] = self.dbinstance_status
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_disk_mbps is not None:
            result['DBInstanceDiskMBPS'] = self.dbinstance_disk_mbps
        if self.dbinstance_storage is not None:
            result['DBInstanceStorage'] = self.dbinstance_storage
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.max_connections is not None:
            result['MaxConnections'] = self.max_connections
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DBInstanceCpuCores') is not None:
            self.dbinstance_cpu_cores = m.get('DBInstanceCpuCores')
        if m.get('SegmentCounts') is not None:
            self.segment_counts = m.get('SegmentCounts')
        if m.get('StoragePerNode') is not None:
            self.storage_per_node = m.get('StoragePerNode')
        if m.get('DBInstanceMemory') is not None:
            self.dbinstance_memory = m.get('DBInstanceMemory')
        if m.get('HostType') is not None:
            self.host_type = m.get('HostType')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('CpuCoresPerNode') is not None:
            self.cpu_cores_per_node = m.get('CpuCoresPerNode')
        if m.get('AvailabilityValue') is not None:
            self.availability_value = m.get('AvailabilityValue')
        if m.get('ReadDelayTime') is not None:
            self.read_delay_time = m.get('ReadDelayTime')
        if m.get('ConnectionMode') is not None:
            self.connection_mode = m.get('ConnectionMode')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('StorageUnit') is not None:
            self.storage_unit = m.get('StorageUnit')
        if m.get('MemoryPerNode') is not None:
            self.memory_per_node = m.get('MemoryPerNode')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        if m.get('MemoryUnit') is not None:
            self.memory_unit = m.get('MemoryUnit')
        if m.get('DBInstanceClassType') is not None:
            self.dbinstance_class_type = m.get('DBInstanceClassType')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBInstanceGroupCount') is not None:
            self.dbinstance_group_count = m.get('DBInstanceGroupCount')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('DBInstanceNetType') is not None:
            self.dbinstance_net_type = m.get('DBInstanceNetType')
        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')
        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('DBInstanceStatus') is not None:
            self.dbinstance_status = m.get('DBInstanceStatus')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceDiskMBPS') is not None:
            self.dbinstance_disk_mbps = m.get('DBInstanceDiskMBPS')
        if m.get('DBInstanceStorage') is not None:
            self.dbinstance_storage = m.get('DBInstanceStorage')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('MaxConnections') is not None:
            self.max_connections = m.get('MaxConnections')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('Tags') is not None:
            temp_model = DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttributeTags()
            self.tags = temp_model.from_map(m['Tags'])
        return self


class DescribeDBInstanceAttributeResponseBodyItems(TeaModel):
    def __init__(
        self,
        dbinstance_attribute: List[DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttribute] = None,
    ):
        self.dbinstance_attribute = dbinstance_attribute

    def validate(self):
        if self.dbinstance_attribute:
            for k in self.dbinstance_attribute:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBInstanceAttribute'] = []
        if self.dbinstance_attribute is not None:
            for k in self.dbinstance_attribute:
                result['DBInstanceAttribute'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbinstance_attribute = []
        if m.get('DBInstanceAttribute') is not None:
            for k in m.get('DBInstanceAttribute'):
                temp_model = DescribeDBInstanceAttributeResponseBodyItemsDBInstanceAttribute()
                self.dbinstance_attribute.append(temp_model.from_map(k))
        return self


class DescribeDBInstanceAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        items: DescribeDBInstanceAttributeResponseBodyItems = None,
    ):
        self.request_id = request_id
        self.items = items

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.items is not None:
            result['Items'] = self.items.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Items') is not None:
            temp_model = DescribeDBInstanceAttributeResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        return self


class DescribeDBInstanceAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDBInstanceAttributeResponseBody = None,
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
            temp_model = DescribeDBInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceIPArrayListRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
    ):
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeDBInstanceIPArrayListResponseBodyItemsDBInstanceIPArray(TeaModel):
    def __init__(
        self,
        dbinstance_iparray_attribute: str = None,
        dbinstance_iparray_name: str = None,
        security_iplist: str = None,
    ):
        self.dbinstance_iparray_attribute = dbinstance_iparray_attribute
        self.dbinstance_iparray_name = dbinstance_iparray_name
        self.security_iplist = security_iplist

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_iparray_attribute is not None:
            result['DBInstanceIPArrayAttribute'] = self.dbinstance_iparray_attribute
        if self.dbinstance_iparray_name is not None:
            result['DBInstanceIPArrayName'] = self.dbinstance_iparray_name
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceIPArrayAttribute') is not None:
            self.dbinstance_iparray_attribute = m.get('DBInstanceIPArrayAttribute')
        if m.get('DBInstanceIPArrayName') is not None:
            self.dbinstance_iparray_name = m.get('DBInstanceIPArrayName')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        return self


class DescribeDBInstanceIPArrayListResponseBodyItems(TeaModel):
    def __init__(
        self,
        dbinstance_iparray: List[DescribeDBInstanceIPArrayListResponseBodyItemsDBInstanceIPArray] = None,
    ):
        self.dbinstance_iparray = dbinstance_iparray

    def validate(self):
        if self.dbinstance_iparray:
            for k in self.dbinstance_iparray:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBInstanceIPArray'] = []
        if self.dbinstance_iparray is not None:
            for k in self.dbinstance_iparray:
                result['DBInstanceIPArray'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbinstance_iparray = []
        if m.get('DBInstanceIPArray') is not None:
            for k in m.get('DBInstanceIPArray'):
                temp_model = DescribeDBInstanceIPArrayListResponseBodyItemsDBInstanceIPArray()
                self.dbinstance_iparray.append(temp_model.from_map(k))
        return self


class DescribeDBInstanceIPArrayListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        items: DescribeDBInstanceIPArrayListResponseBodyItems = None,
    ):
        self.request_id = request_id
        self.items = items

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.items is not None:
            result['Items'] = self.items.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Items') is not None:
            temp_model = DescribeDBInstanceIPArrayListResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        return self


class DescribeDBInstanceIPArrayListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDBInstanceIPArrayListResponseBody = None,
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
            temp_model = DescribeDBInstanceIPArrayListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceNetInfoRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
    ):
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfosDBInstanceNetInfo(TeaModel):
    def __init__(
        self,
        v_switch_id: str = None,
        connection_string: str = None,
        iptype: str = None,
        port: str = None,
        vpc_instance_id: str = None,
        vpcid: str = None,
        ipaddress: str = None,
        address_type: str = None,
    ):
        self.v_switch_id = v_switch_id
        self.connection_string = connection_string
        self.iptype = iptype
        self.port = port
        self.vpc_instance_id = vpc_instance_id
        self.vpcid = vpcid
        self.ipaddress = ipaddress
        self.address_type = address_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.iptype is not None:
            result['IPType'] = self.iptype
        if self.port is not None:
            result['Port'] = self.port
        if self.vpc_instance_id is not None:
            result['VpcInstanceId'] = self.vpc_instance_id
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('IPType') is not None:
            self.iptype = m.get('IPType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('VpcInstanceId') is not None:
            self.vpc_instance_id = m.get('VpcInstanceId')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        return self


class DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfos(TeaModel):
    def __init__(
        self,
        dbinstance_net_info: List[DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfosDBInstanceNetInfo] = None,
    ):
        self.dbinstance_net_info = dbinstance_net_info

    def validate(self):
        if self.dbinstance_net_info:
            for k in self.dbinstance_net_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBInstanceNetInfo'] = []
        if self.dbinstance_net_info is not None:
            for k in self.dbinstance_net_info:
                result['DBInstanceNetInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbinstance_net_info = []
        if m.get('DBInstanceNetInfo') is not None:
            for k in m.get('DBInstanceNetInfo'):
                temp_model = DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfosDBInstanceNetInfo()
                self.dbinstance_net_info.append(temp_model.from_map(k))
        return self


class DescribeDBInstanceNetInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        dbinstance_net_infos: DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfos = None,
        instance_network_type: str = None,
    ):
        self.request_id = request_id
        self.dbinstance_net_infos = dbinstance_net_infos
        self.instance_network_type = instance_network_type

    def validate(self):
        if self.dbinstance_net_infos:
            self.dbinstance_net_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dbinstance_net_infos is not None:
            result['DBInstanceNetInfos'] = self.dbinstance_net_infos.to_map()
        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DBInstanceNetInfos') is not None:
            temp_model = DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfos()
            self.dbinstance_net_infos = temp_model.from_map(m['DBInstanceNetInfos'])
        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')
        return self


class DescribeDBInstanceNetInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDBInstanceNetInfoResponseBody = None,
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
            temp_model = DescribeDBInstanceNetInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceOnECSAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        dbinstance_id: str = None,
    ):
        self.owner_id = owner_id
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeDBInstanceOnECSAttributeResponseBodyItemsDBInstanceAttributeTagsTag(TeaModel):
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


class DescribeDBInstanceOnECSAttributeResponseBodyItemsDBInstanceAttributeTags(TeaModel):
    def __init__(
        self,
        tag: List[DescribeDBInstanceOnECSAttributeResponseBodyItemsDBInstanceAttributeTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeDBInstanceOnECSAttributeResponseBodyItemsDBInstanceAttributeTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDBInstanceOnECSAttributeResponseBodyItemsDBInstanceAttribute(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        vpc_id: str = None,
        encryption_type: str = None,
        instance_deploy_type: str = None,
        pay_type: str = None,
        tags: DescribeDBInstanceOnECSAttributeResponseBodyItemsDBInstanceAttributeTags = None,
        storage_type: str = None,
        connection_mode: str = None,
        port: str = None,
        lock_mode: str = None,
        engine_version: str = None,
        memory_size: int = None,
        seg_node_num: int = None,
        connection_string: str = None,
        instance_network_type: str = None,
        encryption_key: str = None,
        dbinstance_description: str = None,
        cpu_cores: int = None,
        expire_time: str = None,
        dbinstance_status: str = None,
        storage_size: int = None,
        region_id: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
        dbinstance_id: str = None,
        engine: str = None,
        dbinstance_class: str = None,
        support_restore: bool = None,
        minor_version: str = None,
        master_node_num: int = None,
    ):
        self.creation_time = creation_time
        self.vpc_id = vpc_id
        self.encryption_type = encryption_type
        self.instance_deploy_type = instance_deploy_type
        self.pay_type = pay_type
        self.tags = tags
        self.storage_type = storage_type
        self.connection_mode = connection_mode
        self.port = port
        self.lock_mode = lock_mode
        self.engine_version = engine_version
        self.memory_size = memory_size
        self.seg_node_num = seg_node_num
        self.connection_string = connection_string
        self.instance_network_type = instance_network_type
        self.encryption_key = encryption_key
        self.dbinstance_description = dbinstance_description
        self.cpu_cores = cpu_cores
        self.expire_time = expire_time
        self.dbinstance_status = dbinstance_status
        self.storage_size = storage_size
        self.region_id = region_id
        self.v_switch_id = v_switch_id
        self.zone_id = zone_id
        self.dbinstance_id = dbinstance_id
        self.engine = engine
        self.dbinstance_class = dbinstance_class
        self.support_restore = support_restore
        self.minor_version = minor_version
        self.master_node_num = master_node_num

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.encryption_type is not None:
            result['EncryptionType'] = self.encryption_type
        if self.instance_deploy_type is not None:
            result['InstanceDeployType'] = self.instance_deploy_type
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.connection_mode is not None:
            result['ConnectionMode'] = self.connection_mode
        if self.port is not None:
            result['Port'] = self.port
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size
        if self.seg_node_num is not None:
            result['SegNodeNum'] = self.seg_node_num
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type
        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.cpu_cores is not None:
            result['CpuCores'] = self.cpu_cores
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.dbinstance_status is not None:
            result['DBInstanceStatus'] = self.dbinstance_status
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class
        if self.support_restore is not None:
            result['SupportRestore'] = self.support_restore
        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version
        if self.master_node_num is not None:
            result['MasterNodeNum'] = self.master_node_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('EncryptionType') is not None:
            self.encryption_type = m.get('EncryptionType')
        if m.get('InstanceDeployType') is not None:
            self.instance_deploy_type = m.get('InstanceDeployType')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Tags') is not None:
            temp_model = DescribeDBInstanceOnECSAttributeResponseBodyItemsDBInstanceAttributeTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('ConnectionMode') is not None:
            self.connection_mode = m.get('ConnectionMode')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')
        if m.get('SegNodeNum') is not None:
            self.seg_node_num = m.get('SegNodeNum')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')
        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('CpuCores') is not None:
            self.cpu_cores = m.get('CpuCores')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('DBInstanceStatus') is not None:
            self.dbinstance_status = m.get('DBInstanceStatus')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')
        if m.get('SupportRestore') is not None:
            self.support_restore = m.get('SupportRestore')
        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')
        if m.get('MasterNodeNum') is not None:
            self.master_node_num = m.get('MasterNodeNum')
        return self


class DescribeDBInstanceOnECSAttributeResponseBodyItems(TeaModel):
    def __init__(
        self,
        dbinstance_attribute: List[DescribeDBInstanceOnECSAttributeResponseBodyItemsDBInstanceAttribute] = None,
    ):
        self.dbinstance_attribute = dbinstance_attribute

    def validate(self):
        if self.dbinstance_attribute:
            for k in self.dbinstance_attribute:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBInstanceAttribute'] = []
        if self.dbinstance_attribute is not None:
            for k in self.dbinstance_attribute:
                result['DBInstanceAttribute'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbinstance_attribute = []
        if m.get('DBInstanceAttribute') is not None:
            for k in m.get('DBInstanceAttribute'):
                temp_model = DescribeDBInstanceOnECSAttributeResponseBodyItemsDBInstanceAttribute()
                self.dbinstance_attribute.append(temp_model.from_map(k))
        return self


class DescribeDBInstanceOnECSAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        items: DescribeDBInstanceOnECSAttributeResponseBodyItems = None,
    ):
        self.request_id = request_id
        self.items = items

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.items is not None:
            result['Items'] = self.items.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Items') is not None:
            temp_model = DescribeDBInstanceOnECSAttributeResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        return self


class DescribeDBInstanceOnECSAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDBInstanceOnECSAttributeResponseBody = None,
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
            temp_model = DescribeDBInstanceOnECSAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstancePerformanceRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        key: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.key = key
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.key is not None:
            result['Key'] = self.key
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDBInstancePerformanceResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        dbinstance_id: str = None,
        engine: str = None,
        request_id: str = None,
        performance_keys: List[str] = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.dbinstance_id = dbinstance_id
        self.engine = engine
        self.request_id = request_id
        self.performance_keys = performance_keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.performance_keys is not None:
            result['PerformanceKeys'] = self.performance_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PerformanceKeys') is not None:
            self.performance_keys = m.get('PerformanceKeys')
        return self


class DescribeDBInstancePerformanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDBInstancePerformanceResponseBody = None,
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
            temp_model = DescribeDBInstancePerformanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstancesRequestTag(TeaModel):
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


class DescribeDBInstancesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        region_id: str = None,
        dbinstance_description: str = None,
        instance_network_type: str = None,
        dbinstance_ids: str = None,
        page_size: int = None,
        page_number: int = None,
        tag: List[DescribeDBInstancesRequestTag] = None,
    ):
        self.owner_id = owner_id
        self.region_id = region_id
        self.dbinstance_description = dbinstance_description
        self.instance_network_type = instance_network_type
        self.dbinstance_ids = dbinstance_ids
        self.page_size = page_size
        self.page_number = page_number
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type
        if self.dbinstance_ids is not None:
            result['DBInstanceIds'] = self.dbinstance_ids
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')
        if m.get('DBInstanceIds') is not None:
            self.dbinstance_ids = m.get('DBInstanceIds')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeDBInstancesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDBInstancesResponseBodyItemsDBInstanceTagsTag(TeaModel):
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


class DescribeDBInstancesResponseBodyItemsDBInstanceTags(TeaModel):
    def __init__(
        self,
        tag: List[DescribeDBInstancesResponseBodyItemsDBInstanceTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeDBInstancesResponseBodyItemsDBInstanceTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDBInstancesResponseBodyItemsDBInstance(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
        expire_time: str = None,
        dbinstance_net_type: str = None,
        instance_deploy_type: str = None,
        storage_type: str = None,
        create_time: str = None,
        pay_type: str = None,
        tags: DescribeDBInstancesResponseBodyItemsDBInstanceTags = None,
        lock_reason: str = None,
        dbinstance_status: str = None,
        connection_mode: str = None,
        lock_mode: str = None,
        engine_version: str = None,
        region_id: str = None,
        v_switch_id: str = None,
        instance_network_type: str = None,
        zone_id: str = None,
        dbinstance_id: str = None,
        engine: str = None,
        dbinstance_description: str = None,
        seg_node_num: str = None,
        storage_size: str = None,
        master_node_num: int = None,
    ):
        self.vpc_id = vpc_id
        self.expire_time = expire_time
        self.dbinstance_net_type = dbinstance_net_type
        self.instance_deploy_type = instance_deploy_type
        self.storage_type = storage_type
        self.create_time = create_time
        self.pay_type = pay_type
        self.tags = tags
        self.lock_reason = lock_reason
        self.dbinstance_status = dbinstance_status
        self.connection_mode = connection_mode
        self.lock_mode = lock_mode
        self.engine_version = engine_version
        self.region_id = region_id
        self.v_switch_id = v_switch_id
        self.instance_network_type = instance_network_type
        self.zone_id = zone_id
        self.dbinstance_id = dbinstance_id
        self.engine = engine
        self.dbinstance_description = dbinstance_description
        self.seg_node_num = seg_node_num
        self.storage_size = storage_size
        self.master_node_num = master_node_num

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.dbinstance_net_type is not None:
            result['DBInstanceNetType'] = self.dbinstance_net_type
        if self.instance_deploy_type is not None:
            result['InstanceDeployType'] = self.instance_deploy_type
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.dbinstance_status is not None:
            result['DBInstanceStatus'] = self.dbinstance_status
        if self.connection_mode is not None:
            result['ConnectionMode'] = self.connection_mode
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.seg_node_num is not None:
            result['SegNodeNum'] = self.seg_node_num
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        if self.master_node_num is not None:
            result['MasterNodeNum'] = self.master_node_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('DBInstanceNetType') is not None:
            self.dbinstance_net_type = m.get('DBInstanceNetType')
        if m.get('InstanceDeployType') is not None:
            self.instance_deploy_type = m.get('InstanceDeployType')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Tags') is not None:
            temp_model = DescribeDBInstancesResponseBodyItemsDBInstanceTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('DBInstanceStatus') is not None:
            self.dbinstance_status = m.get('DBInstanceStatus')
        if m.get('ConnectionMode') is not None:
            self.connection_mode = m.get('ConnectionMode')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('SegNodeNum') is not None:
            self.seg_node_num = m.get('SegNodeNum')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        if m.get('MasterNodeNum') is not None:
            self.master_node_num = m.get('MasterNodeNum')
        return self


class DescribeDBInstancesResponseBodyItems(TeaModel):
    def __init__(
        self,
        dbinstance: List[DescribeDBInstancesResponseBodyItemsDBInstance] = None,
    ):
        self.dbinstance = dbinstance

    def validate(self):
        if self.dbinstance:
            for k in self.dbinstance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBInstance'] = []
        if self.dbinstance is not None:
            for k in self.dbinstance:
                result['DBInstance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbinstance = []
        if m.get('DBInstance') is not None:
            for k in m.get('DBInstance'):
                temp_model = DescribeDBInstancesResponseBodyItemsDBInstance()
                self.dbinstance.append(temp_model.from_map(k))
        return self


class DescribeDBInstancesResponseBody(TeaModel):
    def __init__(
        self,
        total_record_count: int = None,
        page_record_count: int = None,
        request_id: str = None,
        page_number: int = None,
        items: DescribeDBInstancesResponseBodyItems = None,
    ):
        self.total_record_count = total_record_count
        self.page_record_count = page_record_count
        self.request_id = request_id
        self.page_number = page_number
        self.items = items

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.items is not None:
            result['Items'] = self.items.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Items') is not None:
            temp_model = DescribeDBInstancesResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        return self


class DescribeDBInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDBInstancesResponseBody = None,
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
            temp_model = DescribeDBInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceSQLPatternsRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        query_keywords: str = None,
        start_time: str = None,
        database: str = None,
        user: str = None,
        end_time: str = None,
        source_ip: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.query_keywords = query_keywords
        self.start_time = start_time
        self.database = database
        self.user = user
        self.end_time = end_time
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.query_keywords is not None:
            result['QueryKeywords'] = self.query_keywords
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.database is not None:
            result['Database'] = self.database
        if self.user is not None:
            result['User'] = self.user
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.source_ip is not None:
            result['SourceIP'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('QueryKeywords') is not None:
            self.query_keywords = m.get('QueryKeywords')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('User') is not None:
            self.user = m.get('User')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('SourceIP') is not None:
            self.source_ip = m.get('SourceIP')
        return self


class DescribeDBInstanceSQLPatternsResponseBodyPatterns(TeaModel):
    def __init__(
        self,
        name: str = None,
        values: Dict[str, Any] = None,
    ):
        self.name = name
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribeDBInstanceSQLPatternsResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
        dbcluster_id: str = None,
        patterns: List[DescribeDBInstanceSQLPatternsResponseBodyPatterns] = None,
    ):
        self.end_time = end_time
        self.request_id = request_id
        self.start_time = start_time
        self.dbcluster_id = dbcluster_id
        self.patterns = patterns

    def validate(self):
        if self.patterns:
            for k in self.patterns:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        result['Patterns'] = []
        if self.patterns is not None:
            for k in self.patterns:
                result['Patterns'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        self.patterns = []
        if m.get('Patterns') is not None:
            for k in m.get('Patterns'):
                temp_model = DescribeDBInstanceSQLPatternsResponseBodyPatterns()
                self.patterns.append(temp_model.from_map(k))
        return self


class DescribeDBInstanceSQLPatternsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDBInstanceSQLPatternsResponseBody = None,
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
            temp_model = DescribeDBInstanceSQLPatternsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceSSLRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
    ):
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeDBInstanceSSLResponseBody(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        request_id: str = None,
        sslenabled: bool = None,
        dbinstance_id: str = None,
        cert_common_name: str = None,
        sslexpired_time: str = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.request_id = request_id
        self.sslenabled = sslenabled
        self.dbinstance_id = dbinstance_id
        self.cert_common_name = cert_common_name
        self.sslexpired_time = sslexpired_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sslenabled is not None:
            result['SSLEnabled'] = self.sslenabled
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.cert_common_name is not None:
            result['CertCommonName'] = self.cert_common_name
        if self.sslexpired_time is not None:
            result['SSLExpiredTime'] = self.sslexpired_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SSLEnabled') is not None:
            self.sslenabled = m.get('SSLEnabled')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('CertCommonName') is not None:
            self.cert_common_name = m.get('CertCommonName')
        if m.get('SSLExpiredTime') is not None:
            self.sslexpired_time = m.get('SSLExpiredTime')
        return self


class DescribeDBInstanceSSLResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDBInstanceSSLResponseBody = None,
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
            temp_model = DescribeDBInstanceSSLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLogBackupsRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        start_time: str = None,
        end_time: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.start_time = start_time
        self.end_time = end_time
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeLogBackupsResponseBodyItems(TeaModel):
    def __init__(
        self,
        log_file_size: int = None,
        log_time: str = None,
        segment_name: str = None,
        log_file_name: str = None,
        dbinstance_id: str = None,
        backup_id: str = None,
    ):
        self.log_file_size = log_file_size
        self.log_time = log_time
        self.segment_name = segment_name
        self.log_file_name = log_file_name
        self.dbinstance_id = dbinstance_id
        self.backup_id = backup_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_file_size is not None:
            result['LogFileSize'] = self.log_file_size
        if self.log_time is not None:
            result['LogTime'] = self.log_time
        if self.segment_name is not None:
            result['SegmentName'] = self.segment_name
        if self.log_file_name is not None:
            result['LogFileName'] = self.log_file_name
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogFileSize') is not None:
            self.log_file_size = m.get('LogFileSize')
        if m.get('LogTime') is not None:
            self.log_time = m.get('LogTime')
        if m.get('SegmentName') is not None:
            self.segment_name = m.get('SegmentName')
        if m.get('LogFileName') is not None:
            self.log_file_name = m.get('LogFileName')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        return self


class DescribeLogBackupsResponseBody(TeaModel):
    def __init__(
        self,
        total_log_size: int = None,
        page_size: int = None,
        page_number: int = None,
        request_id: str = None,
        total_count: int = None,
        items: List[DescribeLogBackupsResponseBodyItems] = None,
    ):
        self.total_log_size = total_log_size
        self.page_size = page_size
        self.page_number = page_number
        self.request_id = request_id
        self.total_count = total_count
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_log_size is not None:
            result['TotalLogSize'] = self.total_log_size
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalLogSize') is not None:
            self.total_log_size = m.get('TotalLogSize')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeLogBackupsResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        return self


class DescribeLogBackupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeLogBackupsResponseBody = None,
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
            temp_model = DescribeLogBackupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeModifyParameterLogRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeModifyParameterLogResponseBodyChangelogs(TeaModel):
    def __init__(
        self,
        parameter_value_after: str = None,
        parameter_value_before: str = None,
        parameter_name: str = None,
        parameter_valid: str = None,
        effect_time: str = None,
    ):
        self.parameter_value_after = parameter_value_after
        self.parameter_value_before = parameter_value_before
        self.parameter_name = parameter_name
        self.parameter_valid = parameter_valid
        self.effect_time = effect_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_value_after is not None:
            result['ParameterValueAfter'] = self.parameter_value_after
        if self.parameter_value_before is not None:
            result['ParameterValueBefore'] = self.parameter_value_before
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.parameter_valid is not None:
            result['ParameterValid'] = self.parameter_valid
        if self.effect_time is not None:
            result['EffectTime'] = self.effect_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterValueAfter') is not None:
            self.parameter_value_after = m.get('ParameterValueAfter')
        if m.get('ParameterValueBefore') is not None:
            self.parameter_value_before = m.get('ParameterValueBefore')
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ParameterValid') is not None:
            self.parameter_valid = m.get('ParameterValid')
        if m.get('EffectTime') is not None:
            self.effect_time = m.get('EffectTime')
        return self


class DescribeModifyParameterLogResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        changelogs: List[DescribeModifyParameterLogResponseBodyChangelogs] = None,
    ):
        self.request_id = request_id
        self.changelogs = changelogs

    def validate(self):
        if self.changelogs:
            for k in self.changelogs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Changelogs'] = []
        if self.changelogs is not None:
            for k in self.changelogs:
                result['Changelogs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.changelogs = []
        if m.get('Changelogs') is not None:
            for k in m.get('Changelogs'):
                temp_model = DescribeModifyParameterLogResponseBodyChangelogs()
                self.changelogs.append(temp_model.from_map(k))
        return self


class DescribeModifyParameterLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeModifyParameterLogResponseBody = None,
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
            temp_model = DescribeModifyParameterLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeParametersRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
    ):
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeParametersResponseBodyParameters(TeaModel):
    def __init__(
        self,
        is_changeable_config: str = None,
        force_restart_instance: str = None,
        optional_range: str = None,
        parameter_name: str = None,
        parameter_value: str = None,
        parameter_description: str = None,
        current_value: str = None,
    ):
        self.is_changeable_config = is_changeable_config
        self.force_restart_instance = force_restart_instance
        self.optional_range = optional_range
        self.parameter_name = parameter_name
        self.parameter_value = parameter_value
        self.parameter_description = parameter_description
        self.current_value = current_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_changeable_config is not None:
            result['IsChangeableConfig'] = self.is_changeable_config
        if self.force_restart_instance is not None:
            result['ForceRestartInstance'] = self.force_restart_instance
        if self.optional_range is not None:
            result['OptionalRange'] = self.optional_range
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        if self.parameter_description is not None:
            result['ParameterDescription'] = self.parameter_description
        if self.current_value is not None:
            result['CurrentValue'] = self.current_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsChangeableConfig') is not None:
            self.is_changeable_config = m.get('IsChangeableConfig')
        if m.get('ForceRestartInstance') is not None:
            self.force_restart_instance = m.get('ForceRestartInstance')
        if m.get('OptionalRange') is not None:
            self.optional_range = m.get('OptionalRange')
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        if m.get('ParameterDescription') is not None:
            self.parameter_description = m.get('ParameterDescription')
        if m.get('CurrentValue') is not None:
            self.current_value = m.get('CurrentValue')
        return self


class DescribeParametersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        parameters: List[DescribeParametersResponseBodyParameters] = None,
    ):
        self.request_id = request_id
        self.parameters = parameters

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = DescribeParametersResponseBodyParameters()
                self.parameters.append(temp_model.from_map(k))
        return self


class DescribeParametersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeParametersResponseBody = None,
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
            temp_model = DescribeParametersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRdsVpcsRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        zone_id: str = None,
    ):
        self.security_token = security_token
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeRdsVpcsResponseBodyVpcsVpcVSwitchs(TeaModel):
    def __init__(
        self,
        status: str = None,
        v_switch_id: str = None,
        is_default: bool = None,
        cidr_block: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        iz_no: str = None,
        v_switch_name: str = None,
    ):
        self.status = status
        self.v_switch_id = v_switch_id
        self.is_default = is_default
        self.cidr_block = cidr_block
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.iz_no = iz_no
        self.v_switch_name = v_switch_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.iz_no is not None:
            result['IzNo'] = self.iz_no
        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('IzNo') is not None:
            self.iz_no = m.get('IzNo')
        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')
        return self


class DescribeRdsVpcsResponseBodyVpcsVpc(TeaModel):
    def __init__(
        self,
        status: str = None,
        vpc_name: str = None,
        vpc_id: str = None,
        is_default: bool = None,
        cidr_block: str = None,
        region_no: str = None,
        gmt_create: str = None,
        ali_uid: str = None,
        v_switchs: List[DescribeRdsVpcsResponseBodyVpcsVpcVSwitchs] = None,
        gmt_modified: str = None,
        bid: str = None,
    ):
        self.status = status
        self.vpc_name = vpc_name
        self.vpc_id = vpc_id
        self.is_default = is_default
        self.cidr_block = cidr_block
        self.region_no = region_no
        self.gmt_create = gmt_create
        self.ali_uid = ali_uid
        self.v_switchs = v_switchs
        self.gmt_modified = gmt_modified
        self.bid = bid

    def validate(self):
        if self.v_switchs:
            for k in self.v_switchs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        result['VSwitchs'] = []
        if self.v_switchs is not None:
            for k in self.v_switchs:
                result['VSwitchs'].append(k.to_map() if k else None)
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.bid is not None:
            result['Bid'] = self.bid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        self.v_switchs = []
        if m.get('VSwitchs') is not None:
            for k in m.get('VSwitchs'):
                temp_model = DescribeRdsVpcsResponseBodyVpcsVpcVSwitchs()
                self.v_switchs.append(temp_model.from_map(k))
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        return self


class DescribeRdsVpcsResponseBodyVpcs(TeaModel):
    def __init__(
        self,
        vpc: List[DescribeRdsVpcsResponseBodyVpcsVpc] = None,
    ):
        self.vpc = vpc

    def validate(self):
        if self.vpc:
            for k in self.vpc:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Vpc'] = []
        if self.vpc is not None:
            for k in self.vpc:
                result['Vpc'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vpc = []
        if m.get('Vpc') is not None:
            for k in m.get('Vpc'):
                temp_model = DescribeRdsVpcsResponseBodyVpcsVpc()
                self.vpc.append(temp_model.from_map(k))
        return self


class DescribeRdsVpcsResponseBody(TeaModel):
    def __init__(
        self,
        vpcs: DescribeRdsVpcsResponseBodyVpcs = None,
        request_id: str = None,
    ):
        self.vpcs = vpcs
        self.request_id = request_id

    def validate(self):
        if self.vpcs:
            self.vpcs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpcs is not None:
            result['Vpcs'] = self.vpcs.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Vpcs') is not None:
            temp_model = DescribeRdsVpcsResponseBodyVpcs()
            self.vpcs = temp_model.from_map(m['Vpcs'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRdsVpcsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRdsVpcsResponseBody = None,
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
            temp_model = DescribeRdsVpcsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRdsVSwitchsRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.security_token = security_token
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.vpc_id = vpc_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeRdsVSwitchsResponseBodyVSwitchesVSwitch(TeaModel):
    def __init__(
        self,
        status: str = None,
        is_default: bool = None,
        v_switch_id: str = None,
        cidr_block: str = None,
        region_no: str = None,
        gmt_create: str = None,
        ali_uid: str = None,
        gmt_modified: str = None,
        bid: str = None,
        iz_no: str = None,
        v_switch_name: str = None,
    ):
        self.status = status
        self.is_default = is_default
        self.v_switch_id = v_switch_id
        self.cidr_block = cidr_block
        self.region_no = region_no
        self.gmt_create = gmt_create
        self.ali_uid = ali_uid
        self.gmt_modified = gmt_modified
        self.bid = bid
        self.iz_no = iz_no
        self.v_switch_name = v_switch_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.iz_no is not None:
            result['IzNo'] = self.iz_no
        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('IzNo') is not None:
            self.iz_no = m.get('IzNo')
        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')
        return self


class DescribeRdsVSwitchsResponseBodyVSwitches(TeaModel):
    def __init__(
        self,
        v_switch: List[DescribeRdsVSwitchsResponseBodyVSwitchesVSwitch] = None,
    ):
        self.v_switch = v_switch

    def validate(self):
        if self.v_switch:
            for k in self.v_switch:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['VSwitch'] = []
        if self.v_switch is not None:
            for k in self.v_switch:
                result['VSwitch'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.v_switch = []
        if m.get('VSwitch') is not None:
            for k in m.get('VSwitch'):
                temp_model = DescribeRdsVSwitchsResponseBodyVSwitchesVSwitch()
                self.v_switch.append(temp_model.from_map(k))
        return self


class DescribeRdsVSwitchsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        v_switches: DescribeRdsVSwitchsResponseBodyVSwitches = None,
    ):
        self.request_id = request_id
        self.v_switches = v_switches

    def validate(self):
        if self.v_switches:
            self.v_switches.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VSwitches') is not None:
            temp_model = DescribeRdsVSwitchsResponseBodyVSwitches()
            self.v_switches = temp_model.from_map(m['VSwitches'])
        return self


class DescribeRdsVSwitchsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRdsVSwitchsResponseBody = None,
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
            temp_model = DescribeRdsVSwitchsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
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


class DescribeRegionsResponseBodyRegionsRegionZonesZone(TeaModel):
    def __init__(
        self,
        zone_id: str = None,
        vpc_enabled: bool = None,
    ):
        self.zone_id = zone_id
        self.vpc_enabled = vpc_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.vpc_enabled is not None:
            result['VpcEnabled'] = self.vpc_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('VpcEnabled') is not None:
            self.vpc_enabled = m.get('VpcEnabled')
        return self


class DescribeRegionsResponseBodyRegionsRegionZones(TeaModel):
    def __init__(
        self,
        zone: List[DescribeRegionsResponseBodyRegionsRegionZonesZone] = None,
    ):
        self.zone = zone

    def validate(self):
        if self.zone:
            for k in self.zone:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Zone'] = []
        if self.zone is not None:
            for k in self.zone:
                result['Zone'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.zone = []
        if m.get('Zone') is not None:
            for k in m.get('Zone'):
                temp_model = DescribeRegionsResponseBodyRegionsRegionZonesZone()
                self.zone.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        zones: DescribeRegionsResponseBodyRegionsRegionZones = None,
    ):
        self.region_id = region_id
        self.zones = zones

    def validate(self):
        if self.zones:
            self.zones.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zones is not None:
            result['Zones'] = self.zones.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Zones') is not None:
            temp_model = DescribeRegionsResponseBodyRegionsRegionZones()
            self.zones = temp_model.from_map(m['Zones'])
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region: List[DescribeRegionsResponseBodyRegionsRegion] = None,
    ):
        self.region = region

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Region'] = []
        if self.region is not None:
            for k in self.region:
                result['Region'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region = []
        if m.get('Region') is not None:
            for k in m.get('Region'):
                temp_model = DescribeRegionsResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        regions: DescribeRegionsResponseBodyRegions = None,
    ):
        self.request_id = request_id
        self.regions = regions

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRegionsResponseBody = None,
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeResourceUsageRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
    ):
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeResourceUsageResponseBody(TeaModel):
    def __init__(
        self,
        disk_used: int = None,
        data_size: int = None,
        request_id: str = None,
        backup_size: int = None,
        log_size: int = None,
        dbinstance_id: str = None,
        engine: str = None,
    ):
        self.disk_used = disk_used
        self.data_size = data_size
        self.request_id = request_id
        self.backup_size = backup_size
        self.log_size = log_size
        self.dbinstance_id = dbinstance_id
        self.engine = engine

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_used is not None:
            result['DiskUsed'] = self.disk_used
        if self.data_size is not None:
            result['DataSize'] = self.data_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.backup_size is not None:
            result['BackupSize'] = self.backup_size
        if self.log_size is not None:
            result['LogSize'] = self.log_size
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.engine is not None:
            result['Engine'] = self.engine
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskUsed') is not None:
            self.disk_used = m.get('DiskUsed')
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BackupSize') is not None:
            self.backup_size = m.get('BackupSize')
        if m.get('LogSize') is not None:
            self.log_size = m.get('LogSize')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        return self


class DescribeResourceUsageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeResourceUsageResponseBody = None,
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
            temp_model = DescribeResourceUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSlowLogRecordsRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        sqlid: int = None,
        start_time: str = None,
        end_time: str = None,
        dbname: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.sqlid = sqlid
        self.start_time = start_time
        self.end_time = end_time
        self.dbname = dbname
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.sqlid is not None:
            result['SQLId'] = self.sqlid
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('SQLId') is not None:
            self.sqlid = m.get('SQLId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeSlowLogRecordsResponseBodyItemsSQLSlowRecord(TeaModel):
    def __init__(
        self,
        execution_start_time: str = None,
        host_address: str = None,
        query_times: int = None,
        sqltext: str = None,
        return_row_counts: int = None,
        parse_row_counts: int = None,
        dbname: str = None,
        lock_times: int = None,
    ):
        self.execution_start_time = execution_start_time
        self.host_address = host_address
        self.query_times = query_times
        self.sqltext = sqltext
        self.return_row_counts = return_row_counts
        self.parse_row_counts = parse_row_counts
        self.dbname = dbname
        self.lock_times = lock_times

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution_start_time is not None:
            result['ExecutionStartTime'] = self.execution_start_time
        if self.host_address is not None:
            result['HostAddress'] = self.host_address
        if self.query_times is not None:
            result['QueryTimes'] = self.query_times
        if self.sqltext is not None:
            result['SQLText'] = self.sqltext
        if self.return_row_counts is not None:
            result['ReturnRowCounts'] = self.return_row_counts
        if self.parse_row_counts is not None:
            result['ParseRowCounts'] = self.parse_row_counts
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.lock_times is not None:
            result['LockTimes'] = self.lock_times
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutionStartTime') is not None:
            self.execution_start_time = m.get('ExecutionStartTime')
        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')
        if m.get('QueryTimes') is not None:
            self.query_times = m.get('QueryTimes')
        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')
        if m.get('ReturnRowCounts') is not None:
            self.return_row_counts = m.get('ReturnRowCounts')
        if m.get('ParseRowCounts') is not None:
            self.parse_row_counts = m.get('ParseRowCounts')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('LockTimes') is not None:
            self.lock_times = m.get('LockTimes')
        return self


class DescribeSlowLogRecordsResponseBodyItems(TeaModel):
    def __init__(
        self,
        sqlslow_record: List[DescribeSlowLogRecordsResponseBodyItemsSQLSlowRecord] = None,
    ):
        self.sqlslow_record = sqlslow_record

    def validate(self):
        if self.sqlslow_record:
            for k in self.sqlslow_record:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SQLSlowRecord'] = []
        if self.sqlslow_record is not None:
            for k in self.sqlslow_record:
                result['SQLSlowRecord'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sqlslow_record = []
        if m.get('SQLSlowRecord') is not None:
            for k in m.get('SQLSlowRecord'):
                temp_model = DescribeSlowLogRecordsResponseBodyItemsSQLSlowRecord()
                self.sqlslow_record.append(temp_model.from_map(k))
        return self


class DescribeSlowLogRecordsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        engine: str = None,
        request_id: str = None,
        page_record_count: int = None,
        total_record_count: int = None,
        items: DescribeSlowLogRecordsResponseBodyItems = None,
    ):
        self.page_number = page_number
        self.engine = engine
        self.request_id = request_id
        self.page_record_count = page_record_count
        self.total_record_count = total_record_count
        self.items = items

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        if self.items is not None:
            result['Items'] = self.items.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        if m.get('Items') is not None:
            temp_model = DescribeSlowLogRecordsResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        return self


class DescribeSlowLogRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSlowLogRecordsResponseBody = None,
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
            temp_model = DescribeSlowLogRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSlowSQLLogsRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        query_keywords: str = None,
        start_time: str = None,
        database: str = None,
        user: str = None,
        end_time: str = None,
        page_size: int = None,
        page_number: int = None,
        source_ip: str = None,
        execute_state: str = None,
        operation_class: str = None,
        operation_type: str = None,
        min_execute_cost: str = None,
        max_execute_cost: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.query_keywords = query_keywords
        self.start_time = start_time
        self.database = database
        self.user = user
        self.end_time = end_time
        self.page_size = page_size
        self.page_number = page_number
        self.source_ip = source_ip
        self.execute_state = execute_state
        self.operation_class = operation_class
        self.operation_type = operation_type
        self.min_execute_cost = min_execute_cost
        self.max_execute_cost = max_execute_cost

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.query_keywords is not None:
            result['QueryKeywords'] = self.query_keywords
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.database is not None:
            result['Database'] = self.database
        if self.user is not None:
            result['User'] = self.user
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.source_ip is not None:
            result['SourceIP'] = self.source_ip
        if self.execute_state is not None:
            result['ExecuteState'] = self.execute_state
        if self.operation_class is not None:
            result['OperationClass'] = self.operation_class
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.min_execute_cost is not None:
            result['MinExecuteCost'] = self.min_execute_cost
        if self.max_execute_cost is not None:
            result['MaxExecuteCost'] = self.max_execute_cost
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('QueryKeywords') is not None:
            self.query_keywords = m.get('QueryKeywords')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('User') is not None:
            self.user = m.get('User')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('SourceIP') is not None:
            self.source_ip = m.get('SourceIP')
        if m.get('ExecuteState') is not None:
            self.execute_state = m.get('ExecuteState')
        if m.get('OperationClass') is not None:
            self.operation_class = m.get('OperationClass')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('MinExecuteCost') is not None:
            self.min_execute_cost = m.get('MinExecuteCost')
        if m.get('MaxExecuteCost') is not None:
            self.max_execute_cost = m.get('MaxExecuteCost')
        return self


class DescribeSlowSQLLogsResponseBodyItems(TeaModel):
    def __init__(
        self,
        operation_class: str = None,
        execute_state: str = None,
        execute_cost: float = None,
        sqltext: str = None,
        source_port: int = None,
        dbrole: str = None,
        operation_type: str = None,
        source_ip: str = None,
        sqlplan: str = None,
        return_row_counts: int = None,
        dbname: str = None,
        operation_execute_time: str = None,
        scan_row_counts: int = None,
        account_name: str = None,
        query_id: str = None,
    ):
        self.operation_class = operation_class
        self.execute_state = execute_state
        self.execute_cost = execute_cost
        self.sqltext = sqltext
        self.source_port = source_port
        self.dbrole = dbrole
        self.operation_type = operation_type
        self.source_ip = source_ip
        self.sqlplan = sqlplan
        self.return_row_counts = return_row_counts
        self.dbname = dbname
        self.operation_execute_time = operation_execute_time
        self.scan_row_counts = scan_row_counts
        self.account_name = account_name
        self.query_id = query_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation_class is not None:
            result['OperationClass'] = self.operation_class
        if self.execute_state is not None:
            result['ExecuteState'] = self.execute_state
        if self.execute_cost is not None:
            result['ExecuteCost'] = self.execute_cost
        if self.sqltext is not None:
            result['SQLText'] = self.sqltext
        if self.source_port is not None:
            result['SourcePort'] = self.source_port
        if self.dbrole is not None:
            result['DBRole'] = self.dbrole
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.source_ip is not None:
            result['SourceIP'] = self.source_ip
        if self.sqlplan is not None:
            result['SQLPlan'] = self.sqlplan
        if self.return_row_counts is not None:
            result['ReturnRowCounts'] = self.return_row_counts
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.operation_execute_time is not None:
            result['OperationExecuteTime'] = self.operation_execute_time
        if self.scan_row_counts is not None:
            result['ScanRowCounts'] = self.scan_row_counts
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.query_id is not None:
            result['QueryId'] = self.query_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationClass') is not None:
            self.operation_class = m.get('OperationClass')
        if m.get('ExecuteState') is not None:
            self.execute_state = m.get('ExecuteState')
        if m.get('ExecuteCost') is not None:
            self.execute_cost = m.get('ExecuteCost')
        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')
        if m.get('SourcePort') is not None:
            self.source_port = m.get('SourcePort')
        if m.get('DBRole') is not None:
            self.dbrole = m.get('DBRole')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('SourceIP') is not None:
            self.source_ip = m.get('SourceIP')
        if m.get('SQLPlan') is not None:
            self.sqlplan = m.get('SQLPlan')
        if m.get('ReturnRowCounts') is not None:
            self.return_row_counts = m.get('ReturnRowCounts')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('OperationExecuteTime') is not None:
            self.operation_execute_time = m.get('OperationExecuteTime')
        if m.get('ScanRowCounts') is not None:
            self.scan_row_counts = m.get('ScanRowCounts')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')
        return self


class DescribeSlowSQLLogsResponseBody(TeaModel):
    def __init__(
        self,
        page_record_count: int = None,
        request_id: str = None,
        page_number: int = None,
        items: List[DescribeSlowSQLLogsResponseBodyItems] = None,
    ):
        self.page_record_count = page_record_count
        self.request_id = request_id
        self.page_number = page_number
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeSlowSQLLogsResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        return self


class DescribeSlowSQLLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSlowSQLLogsResponseBody = None,
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
            temp_model = DescribeSlowSQLLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSpecificationRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        dbinstance_id: str = None,
        storage_type: str = None,
        cpu_cores: int = None,
        total_node_num: int = None,
    ):
        self.owner_id = owner_id
        self.dbinstance_id = dbinstance_id
        self.storage_type = storage_type
        self.cpu_cores = cpu_cores
        self.total_node_num = total_node_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.cpu_cores is not None:
            result['CpuCores'] = self.cpu_cores
        if self.total_node_num is not None:
            result['TotalNodeNum'] = self.total_node_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('CpuCores') is not None:
            self.cpu_cores = m.get('CpuCores')
        if m.get('TotalNodeNum') is not None:
            self.total_node_num = m.get('TotalNodeNum')
        return self


class DescribeSpecificationResponseBodyDBInstanceClass(TeaModel):
    def __init__(
        self,
        value: str = None,
        text: str = None,
    ):
        self.value = value
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class DescribeSpecificationResponseBodyDBInstanceGroupCount(TeaModel):
    def __init__(
        self,
        value: str = None,
        text: str = None,
    ):
        self.value = value
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class DescribeSpecificationResponseBodyStorageNotice(TeaModel):
    def __init__(
        self,
        value: str = None,
        text: str = None,
    ):
        self.value = value
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class DescribeSpecificationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        dbinstance_class: List[DescribeSpecificationResponseBodyDBInstanceClass] = None,
        dbinstance_group_count: List[DescribeSpecificationResponseBodyDBInstanceGroupCount] = None,
        storage_notice: List[DescribeSpecificationResponseBodyStorageNotice] = None,
    ):
        self.request_id = request_id
        self.dbinstance_class = dbinstance_class
        self.dbinstance_group_count = dbinstance_group_count
        self.storage_notice = storage_notice

    def validate(self):
        if self.dbinstance_class:
            for k in self.dbinstance_class:
                if k:
                    k.validate()
        if self.dbinstance_group_count:
            for k in self.dbinstance_group_count:
                if k:
                    k.validate()
        if self.storage_notice:
            for k in self.storage_notice:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['DBInstanceClass'] = []
        if self.dbinstance_class is not None:
            for k in self.dbinstance_class:
                result['DBInstanceClass'].append(k.to_map() if k else None)
        result['DBInstanceGroupCount'] = []
        if self.dbinstance_group_count is not None:
            for k in self.dbinstance_group_count:
                result['DBInstanceGroupCount'].append(k.to_map() if k else None)
        result['StorageNotice'] = []
        if self.storage_notice is not None:
            for k in self.storage_notice:
                result['StorageNotice'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.dbinstance_class = []
        if m.get('DBInstanceClass') is not None:
            for k in m.get('DBInstanceClass'):
                temp_model = DescribeSpecificationResponseBodyDBInstanceClass()
                self.dbinstance_class.append(temp_model.from_map(k))
        self.dbinstance_group_count = []
        if m.get('DBInstanceGroupCount') is not None:
            for k in m.get('DBInstanceGroupCount'):
                temp_model = DescribeSpecificationResponseBodyDBInstanceGroupCount()
                self.dbinstance_group_count.append(temp_model.from_map(k))
        self.storage_notice = []
        if m.get('StorageNotice') is not None:
            for k in m.get('StorageNotice'):
                temp_model = DescribeSpecificationResponseBodyStorageNotice()
                self.storage_notice.append(temp_model.from_map(k))
        return self


class DescribeSpecificationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSpecificationResponseBody = None,
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
            temp_model = DescribeSpecificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSQLCollectorPolicyRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
    ):
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeSQLCollectorPolicyResponseBody(TeaModel):
    def __init__(
        self,
        sqlcollector_status: str = None,
        request_id: str = None,
    ):
        self.sqlcollector_status = sqlcollector_status
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sqlcollector_status is not None:
            result['SQLCollectorStatus'] = self.sqlcollector_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SQLCollectorStatus') is not None:
            self.sqlcollector_status = m.get('SQLCollectorStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSQLCollectorPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSQLCollectorPolicyResponseBody = None,
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
            temp_model = DescribeSQLCollectorPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSQLLogByQueryIdRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        query_id: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.query_id = query_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.query_id is not None:
            result['QueryId'] = self.query_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')
        return self


class DescribeSQLLogByQueryIdResponseBodyItems(TeaModel):
    def __init__(
        self,
        operation_class: str = None,
        execute_state: str = None,
        execute_cost: float = None,
        sqltext: str = None,
        source_port: int = None,
        dbrole: str = None,
        operation_type: str = None,
        source_ip: str = None,
        sqlplan: str = None,
        return_row_counts: int = None,
        dbname: str = None,
        operation_execute_time: str = None,
        scan_row_counts: int = None,
        account_name: str = None,
        query_id: str = None,
        slice_ids: List[str] = None,
    ):
        self.operation_class = operation_class
        self.execute_state = execute_state
        self.execute_cost = execute_cost
        self.sqltext = sqltext
        self.source_port = source_port
        self.dbrole = dbrole
        self.operation_type = operation_type
        self.source_ip = source_ip
        self.sqlplan = sqlplan
        self.return_row_counts = return_row_counts
        self.dbname = dbname
        self.operation_execute_time = operation_execute_time
        self.scan_row_counts = scan_row_counts
        self.account_name = account_name
        self.query_id = query_id
        self.slice_ids = slice_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation_class is not None:
            result['OperationClass'] = self.operation_class
        if self.execute_state is not None:
            result['ExecuteState'] = self.execute_state
        if self.execute_cost is not None:
            result['ExecuteCost'] = self.execute_cost
        if self.sqltext is not None:
            result['SQLText'] = self.sqltext
        if self.source_port is not None:
            result['SourcePort'] = self.source_port
        if self.dbrole is not None:
            result['DBRole'] = self.dbrole
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.source_ip is not None:
            result['SourceIP'] = self.source_ip
        if self.sqlplan is not None:
            result['SQLPlan'] = self.sqlplan
        if self.return_row_counts is not None:
            result['ReturnRowCounts'] = self.return_row_counts
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.operation_execute_time is not None:
            result['OperationExecuteTime'] = self.operation_execute_time
        if self.scan_row_counts is not None:
            result['ScanRowCounts'] = self.scan_row_counts
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.query_id is not None:
            result['QueryId'] = self.query_id
        if self.slice_ids is not None:
            result['SliceIds'] = self.slice_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationClass') is not None:
            self.operation_class = m.get('OperationClass')
        if m.get('ExecuteState') is not None:
            self.execute_state = m.get('ExecuteState')
        if m.get('ExecuteCost') is not None:
            self.execute_cost = m.get('ExecuteCost')
        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')
        if m.get('SourcePort') is not None:
            self.source_port = m.get('SourcePort')
        if m.get('DBRole') is not None:
            self.dbrole = m.get('DBRole')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('SourceIP') is not None:
            self.source_ip = m.get('SourceIP')
        if m.get('SQLPlan') is not None:
            self.sqlplan = m.get('SQLPlan')
        if m.get('ReturnRowCounts') is not None:
            self.return_row_counts = m.get('ReturnRowCounts')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('OperationExecuteTime') is not None:
            self.operation_execute_time = m.get('OperationExecuteTime')
        if m.get('ScanRowCounts') is not None:
            self.scan_row_counts = m.get('ScanRowCounts')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')
        if m.get('SliceIds') is not None:
            self.slice_ids = m.get('SliceIds')
        return self


class DescribeSQLLogByQueryIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        items: List[DescribeSQLLogByQueryIdResponseBodyItems] = None,
    ):
        self.request_id = request_id
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeSQLLogByQueryIdResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        return self


class DescribeSQLLogByQueryIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSQLLogByQueryIdResponseBody = None,
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
            temp_model = DescribeSQLLogByQueryIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSQLLogCountRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        query_keywords: str = None,
        start_time: str = None,
        database: str = None,
        user: str = None,
        end_time: str = None,
        execute_cost: str = None,
        source_ip: str = None,
        execute_state: str = None,
        operation_class: str = None,
        operation_type: str = None,
        max_execute_cost: str = None,
        min_execute_cost: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.query_keywords = query_keywords
        self.start_time = start_time
        self.database = database
        self.user = user
        self.end_time = end_time
        self.execute_cost = execute_cost
        self.source_ip = source_ip
        self.execute_state = execute_state
        self.operation_class = operation_class
        self.operation_type = operation_type
        self.max_execute_cost = max_execute_cost
        self.min_execute_cost = min_execute_cost

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.query_keywords is not None:
            result['QueryKeywords'] = self.query_keywords
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.database is not None:
            result['Database'] = self.database
        if self.user is not None:
            result['User'] = self.user
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.execute_cost is not None:
            result['ExecuteCost'] = self.execute_cost
        if self.source_ip is not None:
            result['SourceIP'] = self.source_ip
        if self.execute_state is not None:
            result['ExecuteState'] = self.execute_state
        if self.operation_class is not None:
            result['OperationClass'] = self.operation_class
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.max_execute_cost is not None:
            result['MaxExecuteCost'] = self.max_execute_cost
        if self.min_execute_cost is not None:
            result['MinExecuteCost'] = self.min_execute_cost
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('QueryKeywords') is not None:
            self.query_keywords = m.get('QueryKeywords')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('User') is not None:
            self.user = m.get('User')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExecuteCost') is not None:
            self.execute_cost = m.get('ExecuteCost')
        if m.get('SourceIP') is not None:
            self.source_ip = m.get('SourceIP')
        if m.get('ExecuteState') is not None:
            self.execute_state = m.get('ExecuteState')
        if m.get('OperationClass') is not None:
            self.operation_class = m.get('OperationClass')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('MaxExecuteCost') is not None:
            self.max_execute_cost = m.get('MaxExecuteCost')
        if m.get('MinExecuteCost') is not None:
            self.min_execute_cost = m.get('MinExecuteCost')
        return self


class DescribeSQLLogCountResponseBodyItemsSeriesValues(TeaModel):
    def __init__(
        self,
        point: List[str] = None,
    ):
        self.point = point

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.point is not None:
            result['Point'] = self.point
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Point') is not None:
            self.point = m.get('Point')
        return self


class DescribeSQLLogCountResponseBodyItemsSeries(TeaModel):
    def __init__(
        self,
        values: List[DescribeSQLLogCountResponseBodyItemsSeriesValues] = None,
    ):
        self.values = values

    def validate(self):
        if self.values:
            for k in self.values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Values'] = []
        if self.values is not None:
            for k in self.values:
                result['Values'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.values = []
        if m.get('Values') is not None:
            for k in m.get('Values'):
                temp_model = DescribeSQLLogCountResponseBodyItemsSeriesValues()
                self.values.append(temp_model.from_map(k))
        return self


class DescribeSQLLogCountResponseBodyItems(TeaModel):
    def __init__(
        self,
        series: List[DescribeSQLLogCountResponseBodyItemsSeries] = None,
        name: str = None,
    ):
        self.series = series
        self.name = name

    def validate(self):
        if self.series:
            for k in self.series:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Series'] = []
        if self.series is not None:
            for k in self.series:
                result['Series'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.series = []
        if m.get('Series') is not None:
            for k in m.get('Series'):
                temp_model = DescribeSQLLogCountResponseBodyItemsSeries()
                self.series.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeSQLLogCountResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
        dbcluster_id: str = None,
        items: List[DescribeSQLLogCountResponseBodyItems] = None,
    ):
        self.end_time = end_time
        self.request_id = request_id
        self.start_time = start_time
        self.dbcluster_id = dbcluster_id
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeSQLLogCountResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        return self


class DescribeSQLLogCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSQLLogCountResponseBody = None,
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
            temp_model = DescribeSQLLogCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSQLLogFilesRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        file_name: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.file_name = file_name
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeSQLLogFilesResponseBodyItemsLogFile(TeaModel):
    def __init__(
        self,
        file_id: str = None,
        log_start_time: str = None,
        log_size: str = None,
        log_download_url: str = None,
        log_end_time: str = None,
        log_status: str = None,
    ):
        self.file_id = file_id
        self.log_start_time = log_start_time
        self.log_size = log_size
        self.log_download_url = log_download_url
        self.log_end_time = log_end_time
        self.log_status = log_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileID'] = self.file_id
        if self.log_start_time is not None:
            result['LogStartTime'] = self.log_start_time
        if self.log_size is not None:
            result['LogSize'] = self.log_size
        if self.log_download_url is not None:
            result['LogDownloadURL'] = self.log_download_url
        if self.log_end_time is not None:
            result['LogEndTime'] = self.log_end_time
        if self.log_status is not None:
            result['LogStatus'] = self.log_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileID') is not None:
            self.file_id = m.get('FileID')
        if m.get('LogStartTime') is not None:
            self.log_start_time = m.get('LogStartTime')
        if m.get('LogSize') is not None:
            self.log_size = m.get('LogSize')
        if m.get('LogDownloadURL') is not None:
            self.log_download_url = m.get('LogDownloadURL')
        if m.get('LogEndTime') is not None:
            self.log_end_time = m.get('LogEndTime')
        if m.get('LogStatus') is not None:
            self.log_status = m.get('LogStatus')
        return self


class DescribeSQLLogFilesResponseBodyItems(TeaModel):
    def __init__(
        self,
        log_file: List[DescribeSQLLogFilesResponseBodyItemsLogFile] = None,
    ):
        self.log_file = log_file

    def validate(self):
        if self.log_file:
            for k in self.log_file:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LogFile'] = []
        if self.log_file is not None:
            for k in self.log_file:
                result['LogFile'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.log_file = []
        if m.get('LogFile') is not None:
            for k in m.get('LogFile'):
                temp_model = DescribeSQLLogFilesResponseBodyItemsLogFile()
                self.log_file.append(temp_model.from_map(k))
        return self


class DescribeSQLLogFilesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        page_number: int = None,
        page_record_count: int = None,
        total_record_count: int = None,
        items: DescribeSQLLogFilesResponseBodyItems = None,
    ):
        self.request_id = request_id
        self.page_number = page_number
        self.page_record_count = page_record_count
        self.total_record_count = total_record_count
        self.items = items

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        if self.items is not None:
            result['Items'] = self.items.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        if m.get('Items') is not None:
            temp_model = DescribeSQLLogFilesResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        return self


class DescribeSQLLogFilesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSQLLogFilesResponseBody = None,
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
            temp_model = DescribeSQLLogFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSQLLogRecordsRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        query_keywords: str = None,
        start_time: str = None,
        database: str = None,
        user: str = None,
        form: str = None,
        end_time: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.query_keywords = query_keywords
        self.start_time = start_time
        self.database = database
        self.user = user
        self.form = form
        self.end_time = end_time
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.query_keywords is not None:
            result['QueryKeywords'] = self.query_keywords
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.database is not None:
            result['Database'] = self.database
        if self.user is not None:
            result['User'] = self.user
        if self.form is not None:
            result['Form'] = self.form
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('QueryKeywords') is not None:
            self.query_keywords = m.get('QueryKeywords')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('User') is not None:
            self.user = m.get('User')
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeSQLLogRecordsResponseBodyItemsSQLRecord(TeaModel):
    def __init__(
        self,
        host_address: str = None,
        sqltext: str = None,
        return_row_counts: int = None,
        dbname: str = None,
        execute_time: str = None,
        thread_id: str = None,
        total_execution_times: int = None,
        account_name: str = None,
    ):
        self.host_address = host_address
        self.sqltext = sqltext
        self.return_row_counts = return_row_counts
        self.dbname = dbname
        self.execute_time = execute_time
        self.thread_id = thread_id
        self.total_execution_times = total_execution_times
        self.account_name = account_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_address is not None:
            result['HostAddress'] = self.host_address
        if self.sqltext is not None:
            result['SQLText'] = self.sqltext
        if self.return_row_counts is not None:
            result['ReturnRowCounts'] = self.return_row_counts
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time
        if self.thread_id is not None:
            result['ThreadID'] = self.thread_id
        if self.total_execution_times is not None:
            result['TotalExecutionTimes'] = self.total_execution_times
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')
        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')
        if m.get('ReturnRowCounts') is not None:
            self.return_row_counts = m.get('ReturnRowCounts')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')
        if m.get('ThreadID') is not None:
            self.thread_id = m.get('ThreadID')
        if m.get('TotalExecutionTimes') is not None:
            self.total_execution_times = m.get('TotalExecutionTimes')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class DescribeSQLLogRecordsResponseBodyItems(TeaModel):
    def __init__(
        self,
        sqlrecord: List[DescribeSQLLogRecordsResponseBodyItemsSQLRecord] = None,
    ):
        self.sqlrecord = sqlrecord

    def validate(self):
        if self.sqlrecord:
            for k in self.sqlrecord:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SQLRecord'] = []
        if self.sqlrecord is not None:
            for k in self.sqlrecord:
                result['SQLRecord'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sqlrecord = []
        if m.get('SQLRecord') is not None:
            for k in m.get('SQLRecord'):
                temp_model = DescribeSQLLogRecordsResponseBodyItemsSQLRecord()
                self.sqlrecord.append(temp_model.from_map(k))
        return self


class DescribeSQLLogRecordsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        page_number: int = None,
        page_record_count: int = None,
        total_record_count: int = None,
        items: DescribeSQLLogRecordsResponseBodyItems = None,
    ):
        self.request_id = request_id
        self.page_number = page_number
        self.page_record_count = page_record_count
        self.total_record_count = total_record_count
        self.items = items

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        if self.items is not None:
            result['Items'] = self.items.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        if m.get('Items') is not None:
            temp_model = DescribeSQLLogRecordsResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        return self


class DescribeSQLLogRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSQLLogRecordsResponseBody = None,
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
            temp_model = DescribeSQLLogRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSQLLogsRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        query_keywords: str = None,
        start_time: str = None,
        database: str = None,
        user: str = None,
        end_time: str = None,
        page_size: int = None,
        page_number: int = None,
        execute_cost: str = None,
        source_ip: str = None,
        execute_state: str = None,
        operation_class: str = None,
        operation_type: str = None,
        max_execute_cost: str = None,
        min_execute_cost: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.query_keywords = query_keywords
        self.start_time = start_time
        self.database = database
        self.user = user
        self.end_time = end_time
        self.page_size = page_size
        self.page_number = page_number
        self.execute_cost = execute_cost
        self.source_ip = source_ip
        self.execute_state = execute_state
        self.operation_class = operation_class
        self.operation_type = operation_type
        self.max_execute_cost = max_execute_cost
        self.min_execute_cost = min_execute_cost

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.query_keywords is not None:
            result['QueryKeywords'] = self.query_keywords
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.database is not None:
            result['Database'] = self.database
        if self.user is not None:
            result['User'] = self.user
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.execute_cost is not None:
            result['ExecuteCost'] = self.execute_cost
        if self.source_ip is not None:
            result['SourceIP'] = self.source_ip
        if self.execute_state is not None:
            result['ExecuteState'] = self.execute_state
        if self.operation_class is not None:
            result['OperationClass'] = self.operation_class
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.max_execute_cost is not None:
            result['MaxExecuteCost'] = self.max_execute_cost
        if self.min_execute_cost is not None:
            result['MinExecuteCost'] = self.min_execute_cost
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('QueryKeywords') is not None:
            self.query_keywords = m.get('QueryKeywords')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('User') is not None:
            self.user = m.get('User')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ExecuteCost') is not None:
            self.execute_cost = m.get('ExecuteCost')
        if m.get('SourceIP') is not None:
            self.source_ip = m.get('SourceIP')
        if m.get('ExecuteState') is not None:
            self.execute_state = m.get('ExecuteState')
        if m.get('OperationClass') is not None:
            self.operation_class = m.get('OperationClass')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('MaxExecuteCost') is not None:
            self.max_execute_cost = m.get('MaxExecuteCost')
        if m.get('MinExecuteCost') is not None:
            self.min_execute_cost = m.get('MinExecuteCost')
        return self


class DescribeSQLLogsResponseBodyItems(TeaModel):
    def __init__(
        self,
        operation_class: str = None,
        execute_state: str = None,
        execute_cost: float = None,
        sqltext: str = None,
        source_port: int = None,
        dbrole: str = None,
        operation_type: str = None,
        source_ip: str = None,
        sqlplan: str = None,
        return_row_counts: int = None,
        dbname: str = None,
        operation_execute_time: str = None,
        scan_row_counts: int = None,
        account_name: str = None,
    ):
        self.operation_class = operation_class
        self.execute_state = execute_state
        self.execute_cost = execute_cost
        self.sqltext = sqltext
        self.source_port = source_port
        self.dbrole = dbrole
        self.operation_type = operation_type
        self.source_ip = source_ip
        self.sqlplan = sqlplan
        self.return_row_counts = return_row_counts
        self.dbname = dbname
        self.operation_execute_time = operation_execute_time
        self.scan_row_counts = scan_row_counts
        self.account_name = account_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation_class is not None:
            result['OperationClass'] = self.operation_class
        if self.execute_state is not None:
            result['ExecuteState'] = self.execute_state
        if self.execute_cost is not None:
            result['ExecuteCost'] = self.execute_cost
        if self.sqltext is not None:
            result['SQLText'] = self.sqltext
        if self.source_port is not None:
            result['SourcePort'] = self.source_port
        if self.dbrole is not None:
            result['DBRole'] = self.dbrole
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.source_ip is not None:
            result['SourceIP'] = self.source_ip
        if self.sqlplan is not None:
            result['SQLPlan'] = self.sqlplan
        if self.return_row_counts is not None:
            result['ReturnRowCounts'] = self.return_row_counts
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.operation_execute_time is not None:
            result['OperationExecuteTime'] = self.operation_execute_time
        if self.scan_row_counts is not None:
            result['ScanRowCounts'] = self.scan_row_counts
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationClass') is not None:
            self.operation_class = m.get('OperationClass')
        if m.get('ExecuteState') is not None:
            self.execute_state = m.get('ExecuteState')
        if m.get('ExecuteCost') is not None:
            self.execute_cost = m.get('ExecuteCost')
        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')
        if m.get('SourcePort') is not None:
            self.source_port = m.get('SourcePort')
        if m.get('DBRole') is not None:
            self.dbrole = m.get('DBRole')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('SourceIP') is not None:
            self.source_ip = m.get('SourceIP')
        if m.get('SQLPlan') is not None:
            self.sqlplan = m.get('SQLPlan')
        if m.get('ReturnRowCounts') is not None:
            self.return_row_counts = m.get('ReturnRowCounts')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('OperationExecuteTime') is not None:
            self.operation_execute_time = m.get('OperationExecuteTime')
        if m.get('ScanRowCounts') is not None:
            self.scan_row_counts = m.get('ScanRowCounts')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class DescribeSQLLogsResponseBody(TeaModel):
    def __init__(
        self,
        page_record_count: int = None,
        request_id: str = None,
        page_number: int = None,
        items: List[DescribeSQLLogsResponseBodyItems] = None,
    ):
        self.page_record_count = page_record_count
        self.request_id = request_id
        self.page_number = page_number
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeSQLLogsResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        return self


class DescribeSQLLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSQLLogsResponseBody = None,
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
            temp_model = DescribeSQLLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSQLLogsOnSliceRequest(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        page_number: int = None,
        max_execute_cost: str = None,
        min_execute_cost: str = None,
        execute_state: str = None,
        dbinstance_id: str = None,
        query_id: str = None,
        slice_id: str = None,
    ):
        self.page_size = page_size
        self.page_number = page_number
        self.max_execute_cost = max_execute_cost
        self.min_execute_cost = min_execute_cost
        self.execute_state = execute_state
        self.dbinstance_id = dbinstance_id
        self.query_id = query_id
        self.slice_id = slice_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.max_execute_cost is not None:
            result['MaxExecuteCost'] = self.max_execute_cost
        if self.min_execute_cost is not None:
            result['MinExecuteCost'] = self.min_execute_cost
        if self.execute_state is not None:
            result['ExecuteState'] = self.execute_state
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.query_id is not None:
            result['QueryId'] = self.query_id
        if self.slice_id is not None:
            result['SliceId'] = self.slice_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('MaxExecuteCost') is not None:
            self.max_execute_cost = m.get('MaxExecuteCost')
        if m.get('MinExecuteCost') is not None:
            self.min_execute_cost = m.get('MinExecuteCost')
        if m.get('ExecuteState') is not None:
            self.execute_state = m.get('ExecuteState')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')
        if m.get('SliceId') is not None:
            self.slice_id = m.get('SliceId')
        return self


class DescribeSQLLogsOnSliceResponseBodySliceLogItems(TeaModel):
    def __init__(
        self,
        execute_status: str = None,
        execute_cost: float = None,
        return_row_counts: int = None,
        operation_execute_time: str = None,
        segment_id: str = None,
        peak_memory: float = None,
        operation_execute_end_time: str = None,
        segment_name: str = None,
    ):
        self.execute_status = execute_status
        self.execute_cost = execute_cost
        self.return_row_counts = return_row_counts
        self.operation_execute_time = operation_execute_time
        self.segment_id = segment_id
        self.peak_memory = peak_memory
        self.operation_execute_end_time = operation_execute_end_time
        self.segment_name = segment_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execute_status is not None:
            result['ExecuteStatus'] = self.execute_status
        if self.execute_cost is not None:
            result['ExecuteCost'] = self.execute_cost
        if self.return_row_counts is not None:
            result['ReturnRowCounts'] = self.return_row_counts
        if self.operation_execute_time is not None:
            result['OperationExecuteTime'] = self.operation_execute_time
        if self.segment_id is not None:
            result['SegmentId'] = self.segment_id
        if self.peak_memory is not None:
            result['PeakMemory'] = self.peak_memory
        if self.operation_execute_end_time is not None:
            result['OperationExecuteEndTime'] = self.operation_execute_end_time
        if self.segment_name is not None:
            result['SegmentName'] = self.segment_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecuteStatus') is not None:
            self.execute_status = m.get('ExecuteStatus')
        if m.get('ExecuteCost') is not None:
            self.execute_cost = m.get('ExecuteCost')
        if m.get('ReturnRowCounts') is not None:
            self.return_row_counts = m.get('ReturnRowCounts')
        if m.get('OperationExecuteTime') is not None:
            self.operation_execute_time = m.get('OperationExecuteTime')
        if m.get('SegmentId') is not None:
            self.segment_id = m.get('SegmentId')
        if m.get('PeakMemory') is not None:
            self.peak_memory = m.get('PeakMemory')
        if m.get('OperationExecuteEndTime') is not None:
            self.operation_execute_end_time = m.get('OperationExecuteEndTime')
        if m.get('SegmentName') is not None:
            self.segment_name = m.get('SegmentName')
        return self


class DescribeSQLLogsOnSliceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        page_record_count: int = None,
        page_number: int = None,
        slice_log_items: List[DescribeSQLLogsOnSliceResponseBodySliceLogItems] = None,
    ):
        self.request_id = request_id
        self.page_record_count = page_record_count
        self.page_number = page_number
        self.slice_log_items = slice_log_items

    def validate(self):
        if self.slice_log_items:
            for k in self.slice_log_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['SliceLogItems'] = []
        if self.slice_log_items is not None:
            for k in self.slice_log_items:
                result['SliceLogItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.slice_log_items = []
        if m.get('SliceLogItems') is not None:
            for k in m.get('SliceLogItems'):
                temp_model = DescribeSQLLogsOnSliceResponseBodySliceLogItems()
                self.slice_log_items.append(temp_model.from_map(k))
        return self


class DescribeSQLLogsOnSliceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSQLLogsOnSliceResponseBody = None,
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
            temp_model = DescribeSQLLogsOnSliceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTagsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        resource_type: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class DescribeTagsResponseBodyTags(TeaModel):
    def __init__(
        self,
        tag_value: str = None,
        tag_key: str = None,
    ):
        self.tag_value = tag_value
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class DescribeTagsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tags: List[DescribeTagsResponseBodyTags] = None,
    ):
        self.request_id = request_id
        self.tags = tags

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeTagsResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        return self


class DescribeTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeTagsResponseBody = None,
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
            temp_model = DescribeTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserEncryptionKeyListRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        page_number: str = None,
        page_size: str = None,
    ):
        self.region_id = region_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeUserEncryptionKeyListResponseBodyKmsKeys(TeaModel):
    def __init__(
        self,
        key_id: str = None,
    ):
        self.key_id = key_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        return self


class DescribeUserEncryptionKeyListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        kms_keys: List[DescribeUserEncryptionKeyListResponseBodyKmsKeys] = None,
    ):
        self.request_id = request_id
        self.kms_keys = kms_keys

    def validate(self):
        if self.kms_keys:
            for k in self.kms_keys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['KmsKeys'] = []
        if self.kms_keys is not None:
            for k in self.kms_keys:
                result['KmsKeys'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.kms_keys = []
        if m.get('KmsKeys') is not None:
            for k in m.get('KmsKeys'):
                temp_model = DescribeUserEncryptionKeyListResponseBodyKmsKeys()
                self.kms_keys.append(temp_model.from_map(k))
        return self


class DescribeUserEncryptionKeyListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUserEncryptionKeyListResponseBody = None,
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
            temp_model = DescribeUserEncryptionKeyListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
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


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        resource_type: str = None,
        next_token: str = None,
        resource_id: List[str] = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.resource_type = resource_type
        self.next_token = next_token
        self.resource_id = resource_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        tag_value: str = None,
        resource_id: str = None,
        tag_key: str = None,
    ):
        self.resource_type = resource_type
        self.tag_value = tag_value
        self.resource_id = resource_id
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        tag_resource: List[ListTagResourcesResponseBodyTagResourcesTagResource] = None,
    ):
        self.tag_resource = tag_resource

    def validate(self):
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['TagResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_resource = []
        if m.get('TagResource') is not None:
            for k in m.get('TagResource'):
                temp_model = ListTagResourcesResponseBodyTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: ListTagResourcesResponseBodyTagResources = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagResources') is not None:
            temp_model = ListTagResourcesResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(m['TagResources'])
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTagResourcesResponseBody = None,
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
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAccountDescriptionRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        account_name: str = None,
        account_description: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.account_name = account_name
        self.account_description = account_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        return self


class ModifyAccountDescriptionResponseBody(TeaModel):
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


class ModifyAccountDescriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyAccountDescriptionResponseBody = None,
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
            temp_model = ModifyAccountDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBackupPolicyRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        preferred_backup_time: str = None,
        preferred_backup_period: str = None,
        backup_retention_period: int = None,
        enable_recovery_point: bool = None,
        recovery_point_period: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.preferred_backup_time = preferred_backup_time
        self.preferred_backup_period = preferred_backup_period
        self.backup_retention_period = backup_retention_period
        self.enable_recovery_point = enable_recovery_point
        self.recovery_point_period = recovery_point_period

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time
        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period
        if self.backup_retention_period is not None:
            result['BackupRetentionPeriod'] = self.backup_retention_period
        if self.enable_recovery_point is not None:
            result['EnableRecoveryPoint'] = self.enable_recovery_point
        if self.recovery_point_period is not None:
            result['RecoveryPointPeriod'] = self.recovery_point_period
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')
        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')
        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')
        if m.get('EnableRecoveryPoint') is not None:
            self.enable_recovery_point = m.get('EnableRecoveryPoint')
        if m.get('RecoveryPointPeriod') is not None:
            self.recovery_point_period = m.get('RecoveryPointPeriod')
        return self


class ModifyBackupPolicyResponseBody(TeaModel):
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


class ModifyBackupPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyBackupPolicyResponseBody = None,
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
            temp_model = ModifyBackupPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceConnectionModeRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        connection_mode: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.connection_mode = connection_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.connection_mode is not None:
            result['ConnectionMode'] = self.connection_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ConnectionMode') is not None:
            self.connection_mode = m.get('ConnectionMode')
        return self


class ModifyDBInstanceConnectionModeResponseBody(TeaModel):
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


class ModifyDBInstanceConnectionModeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDBInstanceConnectionModeResponseBody = None,
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
            temp_model = ModifyDBInstanceConnectionModeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceConnectionStringRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        connection_string_prefix: str = None,
        port: str = None,
        current_connection_string: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.connection_string_prefix = connection_string_prefix
        self.port = port
        self.current_connection_string = current_connection_string

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix
        if self.port is not None:
            result['Port'] = self.port
        if self.current_connection_string is not None:
            result['CurrentConnectionString'] = self.current_connection_string
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('CurrentConnectionString') is not None:
            self.current_connection_string = m.get('CurrentConnectionString')
        return self


class ModifyDBInstanceConnectionStringResponseBody(TeaModel):
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


class ModifyDBInstanceConnectionStringResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDBInstanceConnectionStringResponseBody = None,
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
            temp_model = ModifyDBInstanceConnectionStringResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceDescriptionRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        dbinstance_description: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.dbinstance_description = dbinstance_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        return self


class ModifyDBInstanceDescriptionResponseBody(TeaModel):
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


class ModifyDBInstanceDescriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDBInstanceDescriptionResponseBody = None,
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
            temp_model = ModifyDBInstanceDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceMaintainTimeRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class ModifyDBInstanceMaintainTimeResponseBody(TeaModel):
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


class ModifyDBInstanceMaintainTimeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDBInstanceMaintainTimeResponseBody = None,
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
            temp_model = ModifyDBInstanceMaintainTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceNetworkTypeRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        instance_network_type: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        private_ip_address: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.instance_network_type = instance_network_type
        self.vpcid = vpcid
        self.v_switch_id = v_switch_id
        self.private_ip_address = private_ip_address

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        return self


class ModifyDBInstanceNetworkTypeResponseBody(TeaModel):
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


class ModifyDBInstanceNetworkTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDBInstanceNetworkTypeResponseBody = None,
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
            temp_model = ModifyDBInstanceNetworkTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceSSLRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        connection_string: str = None,
        sslenabled: int = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.connection_string = connection_string
        self.sslenabled = sslenabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.sslenabled is not None:
            result['SSLEnabled'] = self.sslenabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('SSLEnabled') is not None:
            self.sslenabled = m.get('SSLEnabled')
        return self


class ModifyDBInstanceSSLResponseBody(TeaModel):
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


class ModifyDBInstanceSSLResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDBInstanceSSLResponseBody = None,
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
            temp_model = ModifyDBInstanceSSLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyParametersRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        parameters: str = None,
        force_restart_instance: bool = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.parameters = parameters
        self.force_restart_instance = force_restart_instance

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.force_restart_instance is not None:
            result['ForceRestartInstance'] = self.force_restart_instance
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('ForceRestartInstance') is not None:
            self.force_restart_instance = m.get('ForceRestartInstance')
        return self


class ModifyParametersResponseBody(TeaModel):
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


class ModifyParametersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyParametersResponseBody = None,
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
            temp_model = ModifyParametersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySecurityIpsRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        security_iplist: str = None,
        dbinstance_iparray_name: str = None,
        dbinstance_iparray_attribute: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.security_iplist = security_iplist
        self.dbinstance_iparray_name = dbinstance_iparray_name
        self.dbinstance_iparray_attribute = dbinstance_iparray_attribute

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        if self.dbinstance_iparray_name is not None:
            result['DBInstanceIPArrayName'] = self.dbinstance_iparray_name
        if self.dbinstance_iparray_attribute is not None:
            result['DBInstanceIPArrayAttribute'] = self.dbinstance_iparray_attribute
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        if m.get('DBInstanceIPArrayName') is not None:
            self.dbinstance_iparray_name = m.get('DBInstanceIPArrayName')
        if m.get('DBInstanceIPArrayAttribute') is not None:
            self.dbinstance_iparray_attribute = m.get('DBInstanceIPArrayAttribute')
        return self


class ModifySecurityIpsResponseBody(TeaModel):
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


class ModifySecurityIpsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifySecurityIpsResponseBody = None,
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
            temp_model = ModifySecurityIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySQLCollectorPolicyRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        sqlcollector_status: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.sqlcollector_status = sqlcollector_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.sqlcollector_status is not None:
            result['SQLCollectorStatus'] = self.sqlcollector_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('SQLCollectorStatus') is not None:
            self.sqlcollector_status = m.get('SQLCollectorStatus')
        return self


class ModifySQLCollectorPolicyResponseBody(TeaModel):
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


class ModifySQLCollectorPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifySQLCollectorPolicyResponseBody = None,
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
            temp_model = ModifySQLCollectorPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseInstancePublicConnectionRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        current_connection_string: str = None,
        address_type: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.current_connection_string = current_connection_string
        self.address_type = address_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.current_connection_string is not None:
            result['CurrentConnectionString'] = self.current_connection_string
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('CurrentConnectionString') is not None:
            self.current_connection_string = m.get('CurrentConnectionString')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        return self


class ReleaseInstancePublicConnectionResponseBody(TeaModel):
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


class ReleaseInstancePublicConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReleaseInstancePublicConnectionResponseBody = None,
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
            temp_model = ReleaseInstancePublicConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetAccountPasswordRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        account_name: str = None,
        account_password: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.account_name = account_name
        self.account_password = account_password

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        return self


class ResetAccountPasswordResponseBody(TeaModel):
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


class ResetAccountPasswordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ResetAccountPasswordResponseBody = None,
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
            temp_model = ResetAccountPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartDBInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dbinstance_id: str = None,
    ):
        self.client_token = client_token
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class RestartDBInstanceResponseBody(TeaModel):
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


class RestartDBInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RestartDBInstanceResponseBody = None,
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
            temp_model = RestartDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SwitchDBInstanceNetTypeRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        connection_string_prefix: str = None,
        port: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.connection_string_prefix = connection_string_prefix
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class SwitchDBInstanceNetTypeResponseBody(TeaModel):
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


class SwitchDBInstanceNetTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SwitchDBInstanceNetTypeResponseBody = None,
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
            temp_model = SwitchDBInstanceNetTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
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


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        resource_type: str = None,
        resource_id: List[str] = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
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


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TagResourcesResponseBody = None,
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
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        resource_type: str = None,
        all: bool = None,
        resource_id: List[str] = None,
        tag_key: List[str] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.resource_type = resource_type
        self.all = all
        self.resource_id = resource_id
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.all is not None:
            result['All'] = self.all
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
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


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UntagResourcesResponseBody = None,
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
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeDBInstanceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        region_id: str = None,
        dbinstance_class: str = None,
        dbinstance_group_count: str = None,
        dbinstance_id: str = None,
        pay_type: str = None,
    ):
        self.owner_id = owner_id
        self.region_id = region_id
        self.dbinstance_class = dbinstance_class
        self.dbinstance_group_count = dbinstance_group_count
        self.dbinstance_id = dbinstance_id
        self.pay_type = pay_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class
        if self.dbinstance_group_count is not None:
            result['DBInstanceGroupCount'] = self.dbinstance_group_count
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')
        if m.get('DBInstanceGroupCount') is not None:
            self.dbinstance_group_count = m.get('DBInstanceGroupCount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        return self


class UpgradeDBInstanceResponseBody(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        request_id: str = None,
        order_id: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.request_id = request_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class UpgradeDBInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpgradeDBInstanceResponseBody = None,
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
            temp_model = UpgradeDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeDBVersionRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        region_id: str = None,
        dbinstance_id: str = None,
        minor_version: str = None,
        major_version: str = None,
        switch_time_mode: str = None,
        switch_time: str = None,
    ):
        self.owner_id = owner_id
        self.region_id = region_id
        self.dbinstance_id = dbinstance_id
        self.minor_version = minor_version
        self.major_version = major_version
        self.switch_time_mode = switch_time_mode
        self.switch_time = switch_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version
        if self.major_version is not None:
            result['MajorVersion'] = self.major_version
        if self.switch_time_mode is not None:
            result['SwitchTimeMode'] = self.switch_time_mode
        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')
        if m.get('MajorVersion') is not None:
            self.major_version = m.get('MajorVersion')
        if m.get('SwitchTimeMode') is not None:
            self.switch_time_mode = m.get('SwitchTimeMode')
        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')
        return self


class UpgradeDBVersionResponseBody(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        dbinstance_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.dbinstance_id = dbinstance_id
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class UpgradeDBVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpgradeDBVersionResponseBody = None,
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
            temp_model = UpgradeDBVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


