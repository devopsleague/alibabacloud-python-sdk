# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class BackflowFeatureConsistencyCheckJobDataRequest(TeaModel):
    def __init__(
        self,
        feature_consistency_check_job_config_id: str = None,
        instance_id: str = None,
        item_features: str = None,
        log_item_id: str = None,
        log_request_id: str = None,
        log_request_time: int = None,
        log_user_id: str = None,
        scene_name: str = None,
        scores: str = None,
        user_features: str = None,
    ):
        self.feature_consistency_check_job_config_id = feature_consistency_check_job_config_id
        self.instance_id = instance_id
        self.item_features = item_features
        self.log_item_id = log_item_id
        self.log_request_id = log_request_id
        self.log_request_time = log_request_time
        self.log_user_id = log_user_id
        self.scene_name = scene_name
        self.scores = scores
        self.user_features = user_features

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_consistency_check_job_config_id is not None:
            result['FeatureConsistencyCheckJobConfigId'] = self.feature_consistency_check_job_config_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.item_features is not None:
            result['ItemFeatures'] = self.item_features
        if self.log_item_id is not None:
            result['LogItemId'] = self.log_item_id
        if self.log_request_id is not None:
            result['LogRequestId'] = self.log_request_id
        if self.log_request_time is not None:
            result['LogRequestTime'] = self.log_request_time
        if self.log_user_id is not None:
            result['LogUserId'] = self.log_user_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.scores is not None:
            result['Scores'] = self.scores
        if self.user_features is not None:
            result['UserFeatures'] = self.user_features
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureConsistencyCheckJobConfigId') is not None:
            self.feature_consistency_check_job_config_id = m.get('FeatureConsistencyCheckJobConfigId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ItemFeatures') is not None:
            self.item_features = m.get('ItemFeatures')
        if m.get('LogItemId') is not None:
            self.log_item_id = m.get('LogItemId')
        if m.get('LogRequestId') is not None:
            self.log_request_id = m.get('LogRequestId')
        if m.get('LogRequestTime') is not None:
            self.log_request_time = m.get('LogRequestTime')
        if m.get('LogUserId') is not None:
            self.log_user_id = m.get('LogUserId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('Scores') is not None:
            self.scores = m.get('Scores')
        if m.get('UserFeatures') is not None:
            self.user_features = m.get('UserFeatures')
        return self


class BackflowFeatureConsistencyCheckJobDataResponseBody(TeaModel):
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


class BackflowFeatureConsistencyCheckJobDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BackflowFeatureConsistencyCheckJobDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BackflowFeatureConsistencyCheckJobDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloneExperimentRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CloneExperimentResponseBody(TeaModel):
    def __init__(
        self,
        experiment_id: str = None,
        request_id: str = None,
    ):
        self.experiment_id = experiment_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CloneExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CloneExperimentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CloneExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloneExperimentGroupRequest(TeaModel):
    def __init__(
        self,
        environment: str = None,
        instance_id: str = None,
        layer_id: str = None,
    ):
        self.environment = environment
        self.instance_id = instance_id
        self.layer_id = layer_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.layer_id is not None:
            result['LayerId'] = self.layer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LayerId') is not None:
            self.layer_id = m.get('LayerId')
        return self


class CloneExperimentGroupResponseBody(TeaModel):
    def __init__(
        self,
        experiment_group_id: str = None,
        request_id: str = None,
    ):
        self.experiment_group_id = experiment_group_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_group_id is not None:
            result['ExperimentGroupId'] = self.experiment_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentGroupId') is not None:
            self.experiment_group_id = m.get('ExperimentGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CloneExperimentGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CloneExperimentGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CloneExperimentGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloneFeatureConsistencyCheckJobConfigRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CloneFeatureConsistencyCheckJobConfigResponseBody(TeaModel):
    def __init__(
        self,
        feature_consistency_check_id: str = None,
        request_id: str = None,
    ):
        self.feature_consistency_check_id = feature_consistency_check_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_consistency_check_id is not None:
            result['FeatureConsistencyCheckId'] = self.feature_consistency_check_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureConsistencyCheckId') is not None:
            self.feature_consistency_check_id = m.get('FeatureConsistencyCheckId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CloneFeatureConsistencyCheckJobConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CloneFeatureConsistencyCheckJobConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CloneFeatureConsistencyCheckJobConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloneLaboratoryRequest(TeaModel):
    def __init__(
        self,
        clone_experiment_group: bool = None,
        environment: str = None,
        instance_id: str = None,
    ):
        self.clone_experiment_group = clone_experiment_group
        self.environment = environment
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clone_experiment_group is not None:
            result['CloneExperimentGroup'] = self.clone_experiment_group
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloneExperimentGroup') is not None:
            self.clone_experiment_group = m.get('CloneExperimentGroup')
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CloneLaboratoryResponseBody(TeaModel):
    def __init__(
        self,
        laboratory_id: str = None,
        request_id: str = None,
    ):
        self.laboratory_id = laboratory_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.laboratory_id is not None:
            result['LaboratoryId'] = self.laboratory_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LaboratoryId') is not None:
            self.laboratory_id = m.get('LaboratoryId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CloneLaboratoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CloneLaboratoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CloneLaboratoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCrowdRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        instance_id: str = None,
        label: str = None,
        name: str = None,
        source: str = None,
        users: str = None,
    ):
        self.description = description
        self.instance_id = instance_id
        self.label = label
        self.name = name
        self.source = source
        self.users = users

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.label is not None:
            result['Label'] = self.label
        if self.name is not None:
            result['Name'] = self.name
        if self.source is not None:
            result['Source'] = self.source
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class CreateCrowdResponseBody(TeaModel):
    def __init__(
        self,
        crowd_id: str = None,
        request_id: str = None,
    ):
        self.crowd_id = crowd_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.crowd_id is not None:
            result['CrowdId'] = self.crowd_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CrowdId') is not None:
            self.crowd_id = m.get('CrowdId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCrowdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCrowdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateCrowdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateExperimentRequest(TeaModel):
    def __init__(
        self,
        config: str = None,
        debug_crowd_id: str = None,
        debug_users: str = None,
        description: str = None,
        experiment_group_id: str = None,
        flow_percent: int = None,
        instance_id: str = None,
        name: str = None,
        type: str = None,
    ):
        self.config = config
        self.debug_crowd_id = debug_crowd_id
        self.debug_users = debug_users
        self.description = description
        self.experiment_group_id = experiment_group_id
        self.flow_percent = flow_percent
        self.instance_id = instance_id
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.debug_crowd_id is not None:
            result['DebugCrowdId'] = self.debug_crowd_id
        if self.debug_users is not None:
            result['DebugUsers'] = self.debug_users
        if self.description is not None:
            result['Description'] = self.description
        if self.experiment_group_id is not None:
            result['ExperimentGroupId'] = self.experiment_group_id
        if self.flow_percent is not None:
            result['FlowPercent'] = self.flow_percent
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('DebugCrowdId') is not None:
            self.debug_crowd_id = m.get('DebugCrowdId')
        if m.get('DebugUsers') is not None:
            self.debug_users = m.get('DebugUsers')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExperimentGroupId') is not None:
            self.experiment_group_id = m.get('ExperimentGroupId')
        if m.get('FlowPercent') is not None:
            self.flow_percent = m.get('FlowPercent')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateExperimentResponseBody(TeaModel):
    def __init__(
        self,
        experiment_id: str = None,
        request_id: str = None,
    ):
        self.experiment_id = experiment_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateExperimentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateExperimentGroupRequest(TeaModel):
    def __init__(
        self,
        config: str = None,
        crowd_id: str = None,
        debug_crowd_id: str = None,
        debug_users: str = None,
        description: str = None,
        distribution_time_duration: int = None,
        distribution_type: str = None,
        filter: str = None,
        instance_id: str = None,
        layer_id: str = None,
        name: str = None,
        need_aa: bool = None,
        reserved_buckets: str = None,
    ):
        self.config = config
        self.crowd_id = crowd_id
        self.debug_crowd_id = debug_crowd_id
        self.debug_users = debug_users
        self.description = description
        self.distribution_time_duration = distribution_time_duration
        self.distribution_type = distribution_type
        self.filter = filter
        self.instance_id = instance_id
        self.layer_id = layer_id
        self.name = name
        self.need_aa = need_aa
        self.reserved_buckets = reserved_buckets

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.crowd_id is not None:
            result['CrowdId'] = self.crowd_id
        if self.debug_crowd_id is not None:
            result['DebugCrowdId'] = self.debug_crowd_id
        if self.debug_users is not None:
            result['DebugUsers'] = self.debug_users
        if self.description is not None:
            result['Description'] = self.description
        if self.distribution_time_duration is not None:
            result['DistributionTimeDuration'] = self.distribution_time_duration
        if self.distribution_type is not None:
            result['DistributionType'] = self.distribution_type
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.layer_id is not None:
            result['LayerId'] = self.layer_id
        if self.name is not None:
            result['Name'] = self.name
        if self.need_aa is not None:
            result['NeedAA'] = self.need_aa
        if self.reserved_buckets is not None:
            result['ReservedBuckets'] = self.reserved_buckets
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('CrowdId') is not None:
            self.crowd_id = m.get('CrowdId')
        if m.get('DebugCrowdId') is not None:
            self.debug_crowd_id = m.get('DebugCrowdId')
        if m.get('DebugUsers') is not None:
            self.debug_users = m.get('DebugUsers')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DistributionTimeDuration') is not None:
            self.distribution_time_duration = m.get('DistributionTimeDuration')
        if m.get('DistributionType') is not None:
            self.distribution_type = m.get('DistributionType')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LayerId') is not None:
            self.layer_id = m.get('LayerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NeedAA') is not None:
            self.need_aa = m.get('NeedAA')
        if m.get('ReservedBuckets') is not None:
            self.reserved_buckets = m.get('ReservedBuckets')
        return self


class CreateExperimentGroupResponseBody(TeaModel):
    def __init__(
        self,
        experiment_group_id: str = None,
        request_id: str = None,
    ):
        self.experiment_group_id = experiment_group_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_group_id is not None:
            result['ExperimentGroupId'] = self.experiment_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentGroupId') is not None:
            self.experiment_group_id = m.get('ExperimentGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateExperimentGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateExperimentGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateExperimentGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFeatureConsistencyCheckJobRequest(TeaModel):
    def __init__(
        self,
        environment: str = None,
        feature_consistency_check_job_config_id: str = None,
        instance_id: str = None,
        sampling_duration: int = None,
    ):
        self.environment = environment
        self.feature_consistency_check_job_config_id = feature_consistency_check_job_config_id
        self.instance_id = instance_id
        self.sampling_duration = sampling_duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.feature_consistency_check_job_config_id is not None:
            result['FeatureConsistencyCheckJobConfigId'] = self.feature_consistency_check_job_config_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.sampling_duration is not None:
            result['SamplingDuration'] = self.sampling_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('FeatureConsistencyCheckJobConfigId') is not None:
            self.feature_consistency_check_job_config_id = m.get('FeatureConsistencyCheckJobConfigId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SamplingDuration') is not None:
            self.sampling_duration = m.get('SamplingDuration')
        return self


class CreateFeatureConsistencyCheckJobResponseBody(TeaModel):
    def __init__(
        self,
        feature_consistency_check_job_id: str = None,
        request_id: str = None,
    ):
        self.feature_consistency_check_job_id = feature_consistency_check_job_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_consistency_check_job_id is not None:
            result['FeatureConsistencyCheckJobId'] = self.feature_consistency_check_job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureConsistencyCheckJobId') is not None:
            self.feature_consistency_check_job_id = m.get('FeatureConsistencyCheckJobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFeatureConsistencyCheckJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFeatureConsistencyCheckJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFeatureConsistencyCheckJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFeatureConsistencyCheckJobConfigRequest(TeaModel):
    def __init__(
        self,
        compare_feature: bool = None,
        eas_service_name: str = None,
        easy_rec_package_path: str = None,
        easy_rec_version: str = None,
        feature_display_exclude: str = None,
        feature_landing_resource_id: str = None,
        feature_priority: str = None,
        fg_jar_version: str = None,
        fg_json_file_name: str = None,
        generate_zip: bool = None,
        instance_id: str = None,
        item_id_field: str = None,
        item_table: str = None,
        item_table_partition_field: str = None,
        item_table_partition_field_format: str = None,
        name: str = None,
        oss_resource_id: str = None,
        sample_rate: float = None,
        scene_id: str = None,
        service_id: str = None,
        user_id_field: str = None,
        user_table: str = None,
        user_table_partition_field: str = None,
        user_table_partition_field_format: str = None,
        workflow_name: str = None,
    ):
        self.compare_feature = compare_feature
        self.eas_service_name = eas_service_name
        self.easy_rec_package_path = easy_rec_package_path
        self.easy_rec_version = easy_rec_version
        self.feature_display_exclude = feature_display_exclude
        self.feature_landing_resource_id = feature_landing_resource_id
        self.feature_priority = feature_priority
        self.fg_jar_version = fg_jar_version
        self.fg_json_file_name = fg_json_file_name
        self.generate_zip = generate_zip
        self.instance_id = instance_id
        self.item_id_field = item_id_field
        self.item_table = item_table
        self.item_table_partition_field = item_table_partition_field
        self.item_table_partition_field_format = item_table_partition_field_format
        self.name = name
        self.oss_resource_id = oss_resource_id
        self.sample_rate = sample_rate
        self.scene_id = scene_id
        self.service_id = service_id
        self.user_id_field = user_id_field
        self.user_table = user_table
        self.user_table_partition_field = user_table_partition_field
        self.user_table_partition_field_format = user_table_partition_field_format
        self.workflow_name = workflow_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compare_feature is not None:
            result['CompareFeature'] = self.compare_feature
        if self.eas_service_name is not None:
            result['EasServiceName'] = self.eas_service_name
        if self.easy_rec_package_path is not None:
            result['EasyRecPackagePath'] = self.easy_rec_package_path
        if self.easy_rec_version is not None:
            result['EasyRecVersion'] = self.easy_rec_version
        if self.feature_display_exclude is not None:
            result['FeatureDisplayExclude'] = self.feature_display_exclude
        if self.feature_landing_resource_id is not None:
            result['FeatureLandingResourceId'] = self.feature_landing_resource_id
        if self.feature_priority is not None:
            result['FeaturePriority'] = self.feature_priority
        if self.fg_jar_version is not None:
            result['FgJarVersion'] = self.fg_jar_version
        if self.fg_json_file_name is not None:
            result['FgJsonFileName'] = self.fg_json_file_name
        if self.generate_zip is not None:
            result['GenerateZip'] = self.generate_zip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.item_id_field is not None:
            result['ItemIdField'] = self.item_id_field
        if self.item_table is not None:
            result['ItemTable'] = self.item_table
        if self.item_table_partition_field is not None:
            result['ItemTablePartitionField'] = self.item_table_partition_field
        if self.item_table_partition_field_format is not None:
            result['ItemTablePartitionFieldFormat'] = self.item_table_partition_field_format
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_resource_id is not None:
            result['OssResourceId'] = self.oss_resource_id
        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.user_id_field is not None:
            result['UserIdField'] = self.user_id_field
        if self.user_table is not None:
            result['UserTable'] = self.user_table
        if self.user_table_partition_field is not None:
            result['UserTablePartitionField'] = self.user_table_partition_field
        if self.user_table_partition_field_format is not None:
            result['UserTablePartitionFieldFormat'] = self.user_table_partition_field_format
        if self.workflow_name is not None:
            result['WorkflowName'] = self.workflow_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompareFeature') is not None:
            self.compare_feature = m.get('CompareFeature')
        if m.get('EasServiceName') is not None:
            self.eas_service_name = m.get('EasServiceName')
        if m.get('EasyRecPackagePath') is not None:
            self.easy_rec_package_path = m.get('EasyRecPackagePath')
        if m.get('EasyRecVersion') is not None:
            self.easy_rec_version = m.get('EasyRecVersion')
        if m.get('FeatureDisplayExclude') is not None:
            self.feature_display_exclude = m.get('FeatureDisplayExclude')
        if m.get('FeatureLandingResourceId') is not None:
            self.feature_landing_resource_id = m.get('FeatureLandingResourceId')
        if m.get('FeaturePriority') is not None:
            self.feature_priority = m.get('FeaturePriority')
        if m.get('FgJarVersion') is not None:
            self.fg_jar_version = m.get('FgJarVersion')
        if m.get('FgJsonFileName') is not None:
            self.fg_json_file_name = m.get('FgJsonFileName')
        if m.get('GenerateZip') is not None:
            self.generate_zip = m.get('GenerateZip')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ItemIdField') is not None:
            self.item_id_field = m.get('ItemIdField')
        if m.get('ItemTable') is not None:
            self.item_table = m.get('ItemTable')
        if m.get('ItemTablePartitionField') is not None:
            self.item_table_partition_field = m.get('ItemTablePartitionField')
        if m.get('ItemTablePartitionFieldFormat') is not None:
            self.item_table_partition_field_format = m.get('ItemTablePartitionFieldFormat')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssResourceId') is not None:
            self.oss_resource_id = m.get('OssResourceId')
        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('UserIdField') is not None:
            self.user_id_field = m.get('UserIdField')
        if m.get('UserTable') is not None:
            self.user_table = m.get('UserTable')
        if m.get('UserTablePartitionField') is not None:
            self.user_table_partition_field = m.get('UserTablePartitionField')
        if m.get('UserTablePartitionFieldFormat') is not None:
            self.user_table_partition_field_format = m.get('UserTablePartitionFieldFormat')
        if m.get('WorkflowName') is not None:
            self.workflow_name = m.get('WorkflowName')
        return self


class CreateFeatureConsistencyCheckJobConfigResponseBody(TeaModel):
    def __init__(
        self,
        feature_consistency_check_job_config_id: str = None,
        request_id: str = None,
    ):
        self.feature_consistency_check_job_config_id = feature_consistency_check_job_config_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_consistency_check_job_config_id is not None:
            result['FeatureConsistencyCheckJobConfigId'] = self.feature_consistency_check_job_config_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureConsistencyCheckJobConfigId') is not None:
            self.feature_consistency_check_job_config_id = m.get('FeatureConsistencyCheckJobConfigId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFeatureConsistencyCheckJobConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFeatureConsistencyCheckJobConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFeatureConsistencyCheckJobConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLaboratoryRequest(TeaModel):
    def __init__(
        self,
        bucket_count: int = None,
        bucket_type: str = None,
        buckets: str = None,
        debug_crowd_id: str = None,
        debug_users: str = None,
        description: str = None,
        environment: str = None,
        filter: str = None,
        instance_id: str = None,
        name: str = None,
        scene_id: str = None,
        type: str = None,
    ):
        self.bucket_count = bucket_count
        self.bucket_type = bucket_type
        self.buckets = buckets
        self.debug_crowd_id = debug_crowd_id
        self.debug_users = debug_users
        self.description = description
        self.environment = environment
        self.filter = filter
        self.instance_id = instance_id
        self.name = name
        self.scene_id = scene_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_count is not None:
            result['BucketCount'] = self.bucket_count
        if self.bucket_type is not None:
            result['BucketType'] = self.bucket_type
        if self.buckets is not None:
            result['Buckets'] = self.buckets
        if self.debug_crowd_id is not None:
            result['DebugCrowdId'] = self.debug_crowd_id
        if self.debug_users is not None:
            result['DebugUsers'] = self.debug_users
        if self.description is not None:
            result['Description'] = self.description
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketCount') is not None:
            self.bucket_count = m.get('BucketCount')
        if m.get('BucketType') is not None:
            self.bucket_type = m.get('BucketType')
        if m.get('Buckets') is not None:
            self.buckets = m.get('Buckets')
        if m.get('DebugCrowdId') is not None:
            self.debug_crowd_id = m.get('DebugCrowdId')
        if m.get('DebugUsers') is not None:
            self.debug_users = m.get('DebugUsers')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateLaboratoryResponseBody(TeaModel):
    def __init__(
        self,
        laboratory_id: str = None,
        request_id: str = None,
    ):
        self.laboratory_id = laboratory_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.laboratory_id is not None:
            result['LaboratoryId'] = self.laboratory_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LaboratoryId') is not None:
            self.laboratory_id = m.get('LaboratoryId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateLaboratoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLaboratoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateLaboratoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLayerRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        instance_id: str = None,
        laboratory_id: str = None,
        name: str = None,
    ):
        self.description = description
        self.instance_id = instance_id
        self.laboratory_id = laboratory_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.laboratory_id is not None:
            result['LaboratoryId'] = self.laboratory_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LaboratoryId') is not None:
            self.laboratory_id = m.get('LaboratoryId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateLayerResponseBody(TeaModel):
    def __init__(
        self,
        layer_id: str = None,
        request_id: str = None,
    ):
        self.layer_id = layer_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.layer_id is not None:
            result['LayerId'] = self.layer_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LayerId') is not None:
            self.layer_id = m.get('LayerId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateLayerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLayerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateLayerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateParamRequest(TeaModel):
    def __init__(
        self,
        environment: str = None,
        instance_id: str = None,
        name: str = None,
        scene_id: str = None,
        value: str = None,
    ):
        self.environment = environment
        self.instance_id = instance_id
        self.name = name
        self.scene_id = scene_id
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateParamResponseBody(TeaModel):
    def __init__(
        self,
        param_id: int = None,
        request_id: str = None,
    ):
        self.param_id = param_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param_id is not None:
            result['ParamId'] = self.param_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamId') is not None:
            self.param_id = m.get('ParamId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateParamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateParamResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateParamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSceneRequestFlows(TeaModel):
    def __init__(
        self,
        flow_code: str = None,
        flow_name: str = None,
    ):
        self.flow_code = flow_code
        self.flow_name = flow_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        return self


class CreateSceneRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        flows: List[CreateSceneRequestFlows] = None,
        instance_id: str = None,
        name: str = None,
    ):
        self.description = description
        self.flows = flows
        self.instance_id = instance_id
        self.name = name

    def validate(self):
        if self.flows:
            for k in self.flows:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        result['Flows'] = []
        if self.flows is not None:
            for k in self.flows:
                result['Flows'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.flows = []
        if m.get('Flows') is not None:
            for k in m.get('Flows'):
                temp_model = CreateSceneRequestFlows()
                self.flows.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateSceneResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        scene_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class CreateSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSceneResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSubCrowdRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        source: str = None,
        users: str = None,
    ):
        self.instance_id = instance_id
        self.source = source
        self.users = users

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.source is not None:
            result['Source'] = self.source
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class CreateSubCrowdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sub_crowd_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.sub_crowd_id = sub_crowd_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_crowd_id is not None:
            result['SubCrowdId'] = self.sub_crowd_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCrowdId') is not None:
            self.sub_crowd_id = m.get('SubCrowdId')
        return self


class CreateSubCrowdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSubCrowdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateSubCrowdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCrowdRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteCrowdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class DeleteCrowdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCrowdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteCrowdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteExperimentRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteExperimentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class DeleteExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteExperimentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteExperimentGroupRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteExperimentGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class DeleteExperimentGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteExperimentGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteExperimentGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLaboratoryRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteLaboratoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class DeleteLaboratoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteLaboratoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteLaboratoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLayerRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteLayerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class DeleteLayerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteLayerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteLayerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteParamRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteParamResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class DeleteParamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteParamResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteParamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSceneRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteSceneResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class DeleteSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSceneResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSubCrowdRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteSubCrowdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class DeleteSubCrowdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSubCrowdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteSubCrowdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExperimentRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetExperimentResponseBody(TeaModel):
    def __init__(
        self,
        alias_experiment_id: str = None,
        buckets: str = None,
        config: str = None,
        debug_crowd_id: str = None,
        debug_users: str = None,
        description: str = None,
        experiment_group_id: str = None,
        flow_percent: int = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        laboratory_id: str = None,
        layer_id: str = None,
        name: str = None,
        request_id: str = None,
        scene_id: str = None,
        status: str = None,
        type: str = None,
    ):
        self.alias_experiment_id = alias_experiment_id
        self.buckets = buckets
        self.config = config
        self.debug_crowd_id = debug_crowd_id
        self.debug_users = debug_users
        self.description = description
        self.experiment_group_id = experiment_group_id
        self.flow_percent = flow_percent
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.laboratory_id = laboratory_id
        self.layer_id = layer_id
        self.name = name
        # Id of the request
        self.request_id = request_id
        self.scene_id = scene_id
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_experiment_id is not None:
            result['AliasExperimentId'] = self.alias_experiment_id
        if self.buckets is not None:
            result['Buckets'] = self.buckets
        if self.config is not None:
            result['Config'] = self.config
        if self.debug_crowd_id is not None:
            result['DebugCrowdId'] = self.debug_crowd_id
        if self.debug_users is not None:
            result['DebugUsers'] = self.debug_users
        if self.description is not None:
            result['Description'] = self.description
        if self.experiment_group_id is not None:
            result['ExperimentGroupId'] = self.experiment_group_id
        if self.flow_percent is not None:
            result['FlowPercent'] = self.flow_percent
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.laboratory_id is not None:
            result['LaboratoryId'] = self.laboratory_id
        if self.layer_id is not None:
            result['LayerId'] = self.layer_id
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasExperimentId') is not None:
            self.alias_experiment_id = m.get('AliasExperimentId')
        if m.get('Buckets') is not None:
            self.buckets = m.get('Buckets')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('DebugCrowdId') is not None:
            self.debug_crowd_id = m.get('DebugCrowdId')
        if m.get('DebugUsers') is not None:
            self.debug_users = m.get('DebugUsers')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExperimentGroupId') is not None:
            self.experiment_group_id = m.get('ExperimentGroupId')
        if m.get('FlowPercent') is not None:
            self.flow_percent = m.get('FlowPercent')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('LaboratoryId') is not None:
            self.laboratory_id = m.get('LaboratoryId')
        if m.get('LayerId') is not None:
            self.layer_id = m.get('LayerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetExperimentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExperimentGroupRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetExperimentGroupResponseBody(TeaModel):
    def __init__(
        self,
        config: str = None,
        crowd_id: str = None,
        debug_crowd_id: str = None,
        debug_users: str = None,
        description: str = None,
        distribution_time_duration: int = None,
        distribution_type: str = None,
        filter: str = None,
        laboratory_id: str = None,
        layer_id: str = None,
        name: str = None,
        need_aa: bool = None,
        owner: str = None,
        request_id: str = None,
        reserved_buckets: str = None,
        scene_id: str = None,
        status: str = None,
    ):
        self.config = config
        self.crowd_id = crowd_id
        self.debug_crowd_id = debug_crowd_id
        self.debug_users = debug_users
        self.description = description
        self.distribution_time_duration = distribution_time_duration
        self.distribution_type = distribution_type
        self.filter = filter
        self.laboratory_id = laboratory_id
        self.layer_id = layer_id
        self.name = name
        self.need_aa = need_aa
        self.owner = owner
        # Id of the request
        self.request_id = request_id
        self.reserved_buckets = reserved_buckets
        self.scene_id = scene_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.crowd_id is not None:
            result['CrowdId'] = self.crowd_id
        if self.debug_crowd_id is not None:
            result['DebugCrowdId'] = self.debug_crowd_id
        if self.debug_users is not None:
            result['DebugUsers'] = self.debug_users
        if self.description is not None:
            result['Description'] = self.description
        if self.distribution_time_duration is not None:
            result['DistributionTimeDuration'] = self.distribution_time_duration
        if self.distribution_type is not None:
            result['DistributionType'] = self.distribution_type
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.laboratory_id is not None:
            result['LaboratoryId'] = self.laboratory_id
        if self.layer_id is not None:
            result['LayerId'] = self.layer_id
        if self.name is not None:
            result['Name'] = self.name
        if self.need_aa is not None:
            result['NeedAA'] = self.need_aa
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.reserved_buckets is not None:
            result['ReservedBuckets'] = self.reserved_buckets
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('CrowdId') is not None:
            self.crowd_id = m.get('CrowdId')
        if m.get('DebugCrowdId') is not None:
            self.debug_crowd_id = m.get('DebugCrowdId')
        if m.get('DebugUsers') is not None:
            self.debug_users = m.get('DebugUsers')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DistributionTimeDuration') is not None:
            self.distribution_time_duration = m.get('DistributionTimeDuration')
        if m.get('DistributionType') is not None:
            self.distribution_type = m.get('DistributionType')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('LaboratoryId') is not None:
            self.laboratory_id = m.get('LaboratoryId')
        if m.get('LayerId') is not None:
            self.layer_id = m.get('LayerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NeedAA') is not None:
            self.need_aa = m.get('NeedAA')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ReservedBuckets') is not None:
            self.reserved_buckets = m.get('ReservedBuckets')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetExperimentGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetExperimentGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetExperimentGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFeatureConsistencyCheckJobRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetFeatureConsistencyCheckJobResponseBody(TeaModel):
    def __init__(
        self,
        config: str = None,
        feature_consistency_check_job_config_id: str = None,
        feature_consistency_check_job_config_name: str = None,
        gmt_end_time: str = None,
        gmt_start_time: str = None,
        logs: List[str] = None,
        request_id: str = None,
        status: str = None,
    ):
        self.config = config
        self.feature_consistency_check_job_config_id = feature_consistency_check_job_config_id
        self.feature_consistency_check_job_config_name = feature_consistency_check_job_config_name
        self.gmt_end_time = gmt_end_time
        self.gmt_start_time = gmt_start_time
        self.logs = logs
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.feature_consistency_check_job_config_id is not None:
            result['FeatureConsistencyCheckJobConfigId'] = self.feature_consistency_check_job_config_id
        if self.feature_consistency_check_job_config_name is not None:
            result['FeatureConsistencyCheckJobConfigName'] = self.feature_consistency_check_job_config_name
        if self.gmt_end_time is not None:
            result['GmtEndTime'] = self.gmt_end_time
        if self.gmt_start_time is not None:
            result['GmtStartTime'] = self.gmt_start_time
        if self.logs is not None:
            result['Logs'] = self.logs
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('FeatureConsistencyCheckJobConfigId') is not None:
            self.feature_consistency_check_job_config_id = m.get('FeatureConsistencyCheckJobConfigId')
        if m.get('FeatureConsistencyCheckJobConfigName') is not None:
            self.feature_consistency_check_job_config_name = m.get('FeatureConsistencyCheckJobConfigName')
        if m.get('GmtEndTime') is not None:
            self.gmt_end_time = m.get('GmtEndTime')
        if m.get('GmtStartTime') is not None:
            self.gmt_start_time = m.get('GmtStartTime')
        if m.get('Logs') is not None:
            self.logs = m.get('Logs')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetFeatureConsistencyCheckJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFeatureConsistencyCheckJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFeatureConsistencyCheckJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFeatureConsistencyCheckJobConfigRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetFeatureConsistencyCheckJobConfigResponseBody(TeaModel):
    def __init__(
        self,
        compare_feature: bool = None,
        eas_service_name: str = None,
        easy_rec_package_path: str = None,
        easy_rec_version: str = None,
        feature_display_exclude: str = None,
        feature_landing_resource_id: str = None,
        feature_landing_resource_uri: str = None,
        feature_priority: str = None,
        fg_jar_version: str = None,
        fg_json_file_name: str = None,
        generate_zip: bool = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        item_id_field: str = None,
        item_table: str = None,
        item_table_partition_field: str = None,
        item_table_partition_field_format: str = None,
        latest_job_gmt_sampling_end_time: str = None,
        latest_job_gmt_sampling_start_time: str = None,
        latest_job_id: str = None,
        name: str = None,
        oss_bucket: str = None,
        oss_resource_id: str = None,
        request_id: str = None,
        sample_rate: str = None,
        scene_id: str = None,
        scene_name: str = None,
        service_id: str = None,
        service_name: str = None,
        status: str = None,
        user_id_field: str = None,
        user_table: str = None,
        user_table_partition_field: str = None,
        user_table_partition_field_format: str = None,
        workflow_name: str = None,
    ):
        self.compare_feature = compare_feature
        self.eas_service_name = eas_service_name
        self.easy_rec_package_path = easy_rec_package_path
        self.easy_rec_version = easy_rec_version
        self.feature_display_exclude = feature_display_exclude
        self.feature_landing_resource_id = feature_landing_resource_id
        self.feature_landing_resource_uri = feature_landing_resource_uri
        self.feature_priority = feature_priority
        self.fg_jar_version = fg_jar_version
        self.fg_json_file_name = fg_json_file_name
        self.generate_zip = generate_zip
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.item_id_field = item_id_field
        self.item_table = item_table
        self.item_table_partition_field = item_table_partition_field
        self.item_table_partition_field_format = item_table_partition_field_format
        self.latest_job_gmt_sampling_end_time = latest_job_gmt_sampling_end_time
        self.latest_job_gmt_sampling_start_time = latest_job_gmt_sampling_start_time
        self.latest_job_id = latest_job_id
        self.name = name
        self.oss_bucket = oss_bucket
        self.oss_resource_id = oss_resource_id
        self.request_id = request_id
        self.sample_rate = sample_rate
        self.scene_id = scene_id
        self.scene_name = scene_name
        self.service_id = service_id
        self.service_name = service_name
        self.status = status
        self.user_id_field = user_id_field
        self.user_table = user_table
        self.user_table_partition_field = user_table_partition_field
        self.user_table_partition_field_format = user_table_partition_field_format
        self.workflow_name = workflow_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compare_feature is not None:
            result['CompareFeature'] = self.compare_feature
        if self.eas_service_name is not None:
            result['EasServiceName'] = self.eas_service_name
        if self.easy_rec_package_path is not None:
            result['EasyRecPackagePath'] = self.easy_rec_package_path
        if self.easy_rec_version is not None:
            result['EasyRecVersion'] = self.easy_rec_version
        if self.feature_display_exclude is not None:
            result['FeatureDisplayExclude'] = self.feature_display_exclude
        if self.feature_landing_resource_id is not None:
            result['FeatureLandingResourceId'] = self.feature_landing_resource_id
        if self.feature_landing_resource_uri is not None:
            result['FeatureLandingResourceUri'] = self.feature_landing_resource_uri
        if self.feature_priority is not None:
            result['FeaturePriority'] = self.feature_priority
        if self.fg_jar_version is not None:
            result['FgJarVersion'] = self.fg_jar_version
        if self.fg_json_file_name is not None:
            result['FgJsonFileName'] = self.fg_json_file_name
        if self.generate_zip is not None:
            result['GenerateZip'] = self.generate_zip
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.item_id_field is not None:
            result['ItemIdField'] = self.item_id_field
        if self.item_table is not None:
            result['ItemTable'] = self.item_table
        if self.item_table_partition_field is not None:
            result['ItemTablePartitionField'] = self.item_table_partition_field
        if self.item_table_partition_field_format is not None:
            result['ItemTablePartitionFieldFormat'] = self.item_table_partition_field_format
        if self.latest_job_gmt_sampling_end_time is not None:
            result['LatestJobGmtSamplingEndTime'] = self.latest_job_gmt_sampling_end_time
        if self.latest_job_gmt_sampling_start_time is not None:
            result['LatestJobGmtSamplingStartTime'] = self.latest_job_gmt_sampling_start_time
        if self.latest_job_id is not None:
            result['LatestJobId'] = self.latest_job_id
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.oss_resource_id is not None:
            result['OssResourceId'] = self.oss_resource_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id_field is not None:
            result['UserIdField'] = self.user_id_field
        if self.user_table is not None:
            result['UserTable'] = self.user_table
        if self.user_table_partition_field is not None:
            result['UserTablePartitionField'] = self.user_table_partition_field
        if self.user_table_partition_field_format is not None:
            result['UserTablePartitionFieldFormat'] = self.user_table_partition_field_format
        if self.workflow_name is not None:
            result['WorkflowName'] = self.workflow_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompareFeature') is not None:
            self.compare_feature = m.get('CompareFeature')
        if m.get('EasServiceName') is not None:
            self.eas_service_name = m.get('EasServiceName')
        if m.get('EasyRecPackagePath') is not None:
            self.easy_rec_package_path = m.get('EasyRecPackagePath')
        if m.get('EasyRecVersion') is not None:
            self.easy_rec_version = m.get('EasyRecVersion')
        if m.get('FeatureDisplayExclude') is not None:
            self.feature_display_exclude = m.get('FeatureDisplayExclude')
        if m.get('FeatureLandingResourceId') is not None:
            self.feature_landing_resource_id = m.get('FeatureLandingResourceId')
        if m.get('FeatureLandingResourceUri') is not None:
            self.feature_landing_resource_uri = m.get('FeatureLandingResourceUri')
        if m.get('FeaturePriority') is not None:
            self.feature_priority = m.get('FeaturePriority')
        if m.get('FgJarVersion') is not None:
            self.fg_jar_version = m.get('FgJarVersion')
        if m.get('FgJsonFileName') is not None:
            self.fg_json_file_name = m.get('FgJsonFileName')
        if m.get('GenerateZip') is not None:
            self.generate_zip = m.get('GenerateZip')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('ItemIdField') is not None:
            self.item_id_field = m.get('ItemIdField')
        if m.get('ItemTable') is not None:
            self.item_table = m.get('ItemTable')
        if m.get('ItemTablePartitionField') is not None:
            self.item_table_partition_field = m.get('ItemTablePartitionField')
        if m.get('ItemTablePartitionFieldFormat') is not None:
            self.item_table_partition_field_format = m.get('ItemTablePartitionFieldFormat')
        if m.get('LatestJobGmtSamplingEndTime') is not None:
            self.latest_job_gmt_sampling_end_time = m.get('LatestJobGmtSamplingEndTime')
        if m.get('LatestJobGmtSamplingStartTime') is not None:
            self.latest_job_gmt_sampling_start_time = m.get('LatestJobGmtSamplingStartTime')
        if m.get('LatestJobId') is not None:
            self.latest_job_id = m.get('LatestJobId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('OssResourceId') is not None:
            self.oss_resource_id = m.get('OssResourceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserIdField') is not None:
            self.user_id_field = m.get('UserIdField')
        if m.get('UserTable') is not None:
            self.user_table = m.get('UserTable')
        if m.get('UserTablePartitionField') is not None:
            self.user_table_partition_field = m.get('UserTablePartitionField')
        if m.get('UserTablePartitionFieldFormat') is not None:
            self.user_table_partition_field_format = m.get('UserTablePartitionFieldFormat')
        if m.get('WorkflowName') is not None:
            self.workflow_name = m.get('WorkflowName')
        return self


class GetFeatureConsistencyCheckJobConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFeatureConsistencyCheckJobConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFeatureConsistencyCheckJobConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceResponseBodyConfigDataManagements(TeaModel):
    def __init__(
        self,
        component_code: str = None,
        meta: Dict[str, Any] = None,
        type: str = None,
    ):
        self.component_code = component_code
        self.meta = meta
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_code is not None:
            result['ComponentCode'] = self.component_code
        if self.meta is not None:
            result['Meta'] = self.meta
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentCode') is not None:
            self.component_code = m.get('ComponentCode')
        if m.get('Meta') is not None:
            self.meta = m.get('Meta')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetInstanceResponseBodyConfigEngines(TeaModel):
    def __init__(
        self,
        component_code: str = None,
        meta: Dict[str, Any] = None,
        type: str = None,
    ):
        self.component_code = component_code
        self.meta = meta
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_code is not None:
            result['ComponentCode'] = self.component_code
        if self.meta is not None:
            result['Meta'] = self.meta
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentCode') is not None:
            self.component_code = m.get('ComponentCode')
        if m.get('Meta') is not None:
            self.meta = m.get('Meta')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetInstanceResponseBodyConfigMonitors(TeaModel):
    def __init__(
        self,
        component_code: str = None,
        meta: Dict[str, Any] = None,
        type: str = None,
    ):
        self.component_code = component_code
        self.meta = meta
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_code is not None:
            result['ComponentCode'] = self.component_code
        if self.meta is not None:
            result['Meta'] = self.meta
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentCode') is not None:
            self.component_code = m.get('ComponentCode')
        if m.get('Meta') is not None:
            self.meta = m.get('Meta')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetInstanceResponseBodyConfig(TeaModel):
    def __init__(
        self,
        data_managements: List[GetInstanceResponseBodyConfigDataManagements] = None,
        engines: List[GetInstanceResponseBodyConfigEngines] = None,
        monitors: List[GetInstanceResponseBodyConfigMonitors] = None,
    ):
        self.data_managements = data_managements
        self.engines = engines
        self.monitors = monitors

    def validate(self):
        if self.data_managements:
            for k in self.data_managements:
                if k:
                    k.validate()
        if self.engines:
            for k in self.engines:
                if k:
                    k.validate()
        if self.monitors:
            for k in self.monitors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataManagements'] = []
        if self.data_managements is not None:
            for k in self.data_managements:
                result['DataManagements'].append(k.to_map() if k else None)
        result['Engines'] = []
        if self.engines is not None:
            for k in self.engines:
                result['Engines'].append(k.to_map() if k else None)
        result['Monitors'] = []
        if self.monitors is not None:
            for k in self.monitors:
                result['Monitors'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_managements = []
        if m.get('DataManagements') is not None:
            for k in m.get('DataManagements'):
                temp_model = GetInstanceResponseBodyConfigDataManagements()
                self.data_managements.append(temp_model.from_map(k))
        self.engines = []
        if m.get('Engines') is not None:
            for k in m.get('Engines'):
                temp_model = GetInstanceResponseBodyConfigEngines()
                self.engines.append(temp_model.from_map(k))
        self.monitors = []
        if m.get('Monitors') is not None:
            for k in m.get('Monitors'):
                temp_model = GetInstanceResponseBodyConfigMonitors()
                self.monitors.append(temp_model.from_map(k))
        return self


class GetInstanceResponseBody(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        commodity_code: str = None,
        config: GetInstanceResponseBodyConfig = None,
        expired_time: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        instance_id: str = None,
        region_id: str = None,
        request_id: str = None,
        status: str = None,
        type: str = None,
    ):
        self.charge_type = charge_type
        self.commodity_code = commodity_code
        self.config = config
        self.expired_time = expired_time
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.instance_id = instance_id
        self.region_id = region_id
        self.request_id = request_id
        self.status = status
        self.type = type

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.config is not None:
            result['Config'] = self.config.to_map()
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('Config') is not None:
            temp_model = GetInstanceResponseBodyConfig()
            self.config = temp_model.from_map(m['Config'])
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLaboratoryRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetLaboratoryResponseBody(TeaModel):
    def __init__(
        self,
        bucket_count: int = None,
        bucket_type: str = None,
        buckets: str = None,
        crowd_id: str = None,
        debug_crowd_id: str = None,
        debug_users: str = None,
        description: str = None,
        environment: str = None,
        filter: str = None,
        name: str = None,
        request_id: str = None,
        scene_id: str = None,
        status: str = None,
        type: str = None,
    ):
        self.bucket_count = bucket_count
        self.bucket_type = bucket_type
        self.buckets = buckets
        self.crowd_id = crowd_id
        self.debug_crowd_id = debug_crowd_id
        self.debug_users = debug_users
        self.description = description
        self.environment = environment
        self.filter = filter
        self.name = name
        # Id of the request
        self.request_id = request_id
        self.scene_id = scene_id
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_count is not None:
            result['BucketCount'] = self.bucket_count
        if self.bucket_type is not None:
            result['BucketType'] = self.bucket_type
        if self.buckets is not None:
            result['Buckets'] = self.buckets
        if self.crowd_id is not None:
            result['CrowdId'] = self.crowd_id
        if self.debug_crowd_id is not None:
            result['DebugCrowdId'] = self.debug_crowd_id
        if self.debug_users is not None:
            result['DebugUsers'] = self.debug_users
        if self.description is not None:
            result['Description'] = self.description
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketCount') is not None:
            self.bucket_count = m.get('BucketCount')
        if m.get('BucketType') is not None:
            self.bucket_type = m.get('BucketType')
        if m.get('Buckets') is not None:
            self.buckets = m.get('Buckets')
        if m.get('CrowdId') is not None:
            self.crowd_id = m.get('CrowdId')
        if m.get('DebugCrowdId') is not None:
            self.debug_crowd_id = m.get('DebugCrowdId')
        if m.get('DebugUsers') is not None:
            self.debug_users = m.get('DebugUsers')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetLaboratoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLaboratoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetLaboratoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLayerRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetLayerResponseBody(TeaModel):
    def __init__(
        self,
        description: str = None,
        laboratory_id: str = None,
        name: str = None,
        request_id: str = None,
        scene_id: str = None,
    ):
        self.description = description
        self.laboratory_id = laboratory_id
        self.name = name
        # Id of the request
        self.request_id = request_id
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.laboratory_id is not None:
            result['LaboratoryId'] = self.laboratory_id
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LaboratoryId') is not None:
            self.laboratory_id = m.get('LaboratoryId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class GetLayerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLayerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetLayerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSceneRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetSceneResponseBodyFlows(TeaModel):
    def __init__(
        self,
        flow_code: str = None,
        flow_name: str = None,
    ):
        self.flow_code = flow_code
        self.flow_name = flow_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        return self


class GetSceneResponseBody(TeaModel):
    def __init__(
        self,
        description: str = None,
        flows: List[GetSceneResponseBodyFlows] = None,
        name: str = None,
        request_id: str = None,
    ):
        self.description = description
        self.flows = flows
        self.name = name
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.flows:
            for k in self.flows:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        result['Flows'] = []
        if self.flows is not None:
            for k in self.flows:
                result['Flows'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.flows = []
        if m.get('Flows') is not None:
            for k in m.get('Flows'):
                temp_model = GetSceneResponseBodyFlows()
                self.flows.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSceneResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSubCrowdRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetSubCrowdResponseBody(TeaModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        quantity: str = None,
        request_id: str = None,
        source: str = None,
        users: str = None,
    ):
        self.gmt_create_time = gmt_create_time
        self.quantity = quantity
        # Id of the request
        self.request_id = request_id
        self.source = source
        self.users = users

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.source is not None:
            result['Source'] = self.source
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class GetSubCrowdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSubCrowdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetSubCrowdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCrowdUsersRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListCrowdUsersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        users: List[str] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count
        self.users = users

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class ListCrowdUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCrowdUsersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListCrowdUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCrowdsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListCrowdsResponseBodyCrowds(TeaModel):
    def __init__(
        self,
        crowd_id: str = None,
        description: str = None,
        gmt_create_time: str = None,
        label: str = None,
        name: str = None,
        quantity: str = None,
        source: str = None,
        users: str = None,
    ):
        self.crowd_id = crowd_id
        self.description = description
        self.gmt_create_time = gmt_create_time
        self.label = label
        self.name = name
        self.quantity = quantity
        self.source = source
        self.users = users

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.crowd_id is not None:
            result['CrowdId'] = self.crowd_id
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.label is not None:
            result['Label'] = self.label
        if self.name is not None:
            result['Name'] = self.name
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.source is not None:
            result['Source'] = self.source
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CrowdId') is not None:
            self.crowd_id = m.get('CrowdId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class ListCrowdsResponseBody(TeaModel):
    def __init__(
        self,
        crowds: List[ListCrowdsResponseBodyCrowds] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.crowds = crowds
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.crowds:
            for k in self.crowds:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Crowds'] = []
        if self.crowds is not None:
            for k in self.crowds:
                result['Crowds'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.crowds = []
        if m.get('Crowds') is not None:
            for k in m.get('Crowds'):
                temp_model = ListCrowdsResponseBodyCrowds()
                self.crowds.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCrowdsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCrowdsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListCrowdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExperimentGroupsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        layer_id: str = None,
        status: str = None,
    ):
        self.instance_id = instance_id
        self.layer_id = layer_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.layer_id is not None:
            result['LayerId'] = self.layer_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LayerId') is not None:
            self.layer_id = m.get('LayerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListExperimentGroupsResponseBodyExperimentGroups(TeaModel):
    def __init__(
        self,
        config: str = None,
        crowd_id: str = None,
        debug_crowd_id: str = None,
        debug_users: str = None,
        description: str = None,
        distribution_time_duration: int = None,
        distribution_type: str = None,
        experiment_group_id: str = None,
        filter: str = None,
        laboratory_id: str = None,
        layer_id: str = None,
        name: str = None,
        need_aa: bool = None,
        owner: str = None,
        reserved_buckets: str = None,
        scene_id: str = None,
        status: str = None,
    ):
        self.config = config
        self.crowd_id = crowd_id
        self.debug_crowd_id = debug_crowd_id
        self.debug_users = debug_users
        self.description = description
        self.distribution_time_duration = distribution_time_duration
        self.distribution_type = distribution_type
        self.experiment_group_id = experiment_group_id
        self.filter = filter
        self.laboratory_id = laboratory_id
        self.layer_id = layer_id
        self.name = name
        self.need_aa = need_aa
        self.owner = owner
        self.reserved_buckets = reserved_buckets
        self.scene_id = scene_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.crowd_id is not None:
            result['CrowdId'] = self.crowd_id
        if self.debug_crowd_id is not None:
            result['DebugCrowdId'] = self.debug_crowd_id
        if self.debug_users is not None:
            result['DebugUsers'] = self.debug_users
        if self.description is not None:
            result['Description'] = self.description
        if self.distribution_time_duration is not None:
            result['DistributionTimeDuration'] = self.distribution_time_duration
        if self.distribution_type is not None:
            result['DistributionType'] = self.distribution_type
        if self.experiment_group_id is not None:
            result['ExperimentGroupId'] = self.experiment_group_id
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.laboratory_id is not None:
            result['LaboratoryId'] = self.laboratory_id
        if self.layer_id is not None:
            result['LayerId'] = self.layer_id
        if self.name is not None:
            result['Name'] = self.name
        if self.need_aa is not None:
            result['NeedAA'] = self.need_aa
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.reserved_buckets is not None:
            result['ReservedBuckets'] = self.reserved_buckets
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('CrowdId') is not None:
            self.crowd_id = m.get('CrowdId')
        if m.get('DebugCrowdId') is not None:
            self.debug_crowd_id = m.get('DebugCrowdId')
        if m.get('DebugUsers') is not None:
            self.debug_users = m.get('DebugUsers')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DistributionTimeDuration') is not None:
            self.distribution_time_duration = m.get('DistributionTimeDuration')
        if m.get('DistributionType') is not None:
            self.distribution_type = m.get('DistributionType')
        if m.get('ExperimentGroupId') is not None:
            self.experiment_group_id = m.get('ExperimentGroupId')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('LaboratoryId') is not None:
            self.laboratory_id = m.get('LaboratoryId')
        if m.get('LayerId') is not None:
            self.layer_id = m.get('LayerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NeedAA') is not None:
            self.need_aa = m.get('NeedAA')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('ReservedBuckets') is not None:
            self.reserved_buckets = m.get('ReservedBuckets')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListExperimentGroupsResponseBody(TeaModel):
    def __init__(
        self,
        experiment_groups: List[ListExperimentGroupsResponseBodyExperimentGroups] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.experiment_groups = experiment_groups
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.experiment_groups:
            for k in self.experiment_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ExperimentGroups'] = []
        if self.experiment_groups is not None:
            for k in self.experiment_groups:
                result['ExperimentGroups'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.experiment_groups = []
        if m.get('ExperimentGroups') is not None:
            for k in m.get('ExperimentGroups'):
                temp_model = ListExperimentGroupsResponseBodyExperimentGroups()
                self.experiment_groups.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListExperimentGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListExperimentGroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListExperimentGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExperimentsRequest(TeaModel):
    def __init__(
        self,
        experiment_group_id: str = None,
        instance_id: str = None,
        query: str = None,
        status: str = None,
    ):
        self.experiment_group_id = experiment_group_id
        self.instance_id = instance_id
        self.query = query
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_group_id is not None:
            result['ExperimentGroupId'] = self.experiment_group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.query is not None:
            result['Query'] = self.query
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentGroupId') is not None:
            self.experiment_group_id = m.get('ExperimentGroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListExperimentsResponseBodyExperiments(TeaModel):
    def __init__(
        self,
        alias_experiment_id: str = None,
        buckets: str = None,
        config: str = None,
        debug_crowd_id: str = None,
        debug_users: str = None,
        description: str = None,
        experiment_group_id: str = None,
        experiment_id: str = None,
        flow_percent: int = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        laboratory_id: str = None,
        layer_id: str = None,
        name: str = None,
        scene_id: str = None,
        status: str = None,
        type: str = None,
    ):
        self.alias_experiment_id = alias_experiment_id
        self.buckets = buckets
        self.config = config
        self.debug_crowd_id = debug_crowd_id
        self.debug_users = debug_users
        self.description = description
        self.experiment_group_id = experiment_group_id
        self.experiment_id = experiment_id
        self.flow_percent = flow_percent
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.laboratory_id = laboratory_id
        self.layer_id = layer_id
        self.name = name
        self.scene_id = scene_id
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_experiment_id is not None:
            result['AliasExperimentId'] = self.alias_experiment_id
        if self.buckets is not None:
            result['Buckets'] = self.buckets
        if self.config is not None:
            result['Config'] = self.config
        if self.debug_crowd_id is not None:
            result['DebugCrowdId'] = self.debug_crowd_id
        if self.debug_users is not None:
            result['DebugUsers'] = self.debug_users
        if self.description is not None:
            result['Description'] = self.description
        if self.experiment_group_id is not None:
            result['ExperimentGroupId'] = self.experiment_group_id
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.flow_percent is not None:
            result['FlowPercent'] = self.flow_percent
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.laboratory_id is not None:
            result['LaboratoryId'] = self.laboratory_id
        if self.layer_id is not None:
            result['LayerId'] = self.layer_id
        if self.name is not None:
            result['Name'] = self.name
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasExperimentId') is not None:
            self.alias_experiment_id = m.get('AliasExperimentId')
        if m.get('Buckets') is not None:
            self.buckets = m.get('Buckets')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('DebugCrowdId') is not None:
            self.debug_crowd_id = m.get('DebugCrowdId')
        if m.get('DebugUsers') is not None:
            self.debug_users = m.get('DebugUsers')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExperimentGroupId') is not None:
            self.experiment_group_id = m.get('ExperimentGroupId')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('FlowPercent') is not None:
            self.flow_percent = m.get('FlowPercent')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('LaboratoryId') is not None:
            self.laboratory_id = m.get('LaboratoryId')
        if m.get('LayerId') is not None:
            self.layer_id = m.get('LayerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListExperimentsResponseBody(TeaModel):
    def __init__(
        self,
        experiments: List[ListExperimentsResponseBodyExperiments] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.experiments = experiments
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.experiments:
            for k in self.experiments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Experiments'] = []
        if self.experiments is not None:
            for k in self.experiments:
                result['Experiments'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.experiments = []
        if m.get('Experiments') is not None:
            for k in m.get('Experiments'):
                temp_model = ListExperimentsResponseBodyExperiments()
                self.experiments.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListExperimentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListExperimentsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListExperimentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFeatureConsistencyCheckJobConfigsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        order: str = None,
        page_number: str = None,
        page_size: str = None,
        sort_by: str = None,
    ):
        self.instance_id = instance_id
        self.order = order
        self.page_number = page_number
        self.page_size = page_size
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        return self


class ListFeatureConsistencyCheckJobConfigsResponseBodyFeatureConsistencyCheckConfigs(TeaModel):
    def __init__(
        self,
        compare_feature: bool = None,
        eas_service_name: str = None,
        easy_rec_package_path: str = None,
        easy_rec_version: str = None,
        feature_consistency_check_job_config_id: str = None,
        feature_display_exclude: str = None,
        feature_landing_resource_id: str = None,
        feature_landing_resource_uri: str = None,
        feature_priority: str = None,
        fg_jar_version: str = None,
        fg_json_file_name: str = None,
        generate_zip: bool = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        item_id_field: str = None,
        item_table: str = None,
        item_table_partition_field: str = None,
        item_table_partition_field_format: str = None,
        latest_job_gmt_sampling_end_time: str = None,
        latest_job_gmt_sampling_start_time: str = None,
        latest_job_id: str = None,
        name: str = None,
        oss_bucket: str = None,
        oss_resource_id: str = None,
        sample_rate: str = None,
        scene_id: str = None,
        scene_name: str = None,
        service_id: str = None,
        service_name: str = None,
        status: str = None,
        user_id_field: str = None,
        user_table: str = None,
        user_table_partition_field: str = None,
        user_table_partition_field_format: str = None,
        workflow_name: str = None,
    ):
        self.compare_feature = compare_feature
        self.eas_service_name = eas_service_name
        self.easy_rec_package_path = easy_rec_package_path
        self.easy_rec_version = easy_rec_version
        self.feature_consistency_check_job_config_id = feature_consistency_check_job_config_id
        self.feature_display_exclude = feature_display_exclude
        self.feature_landing_resource_id = feature_landing_resource_id
        self.feature_landing_resource_uri = feature_landing_resource_uri
        self.feature_priority = feature_priority
        self.fg_jar_version = fg_jar_version
        self.fg_json_file_name = fg_json_file_name
        self.generate_zip = generate_zip
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.item_id_field = item_id_field
        self.item_table = item_table
        self.item_table_partition_field = item_table_partition_field
        self.item_table_partition_field_format = item_table_partition_field_format
        self.latest_job_gmt_sampling_end_time = latest_job_gmt_sampling_end_time
        self.latest_job_gmt_sampling_start_time = latest_job_gmt_sampling_start_time
        self.latest_job_id = latest_job_id
        self.name = name
        self.oss_bucket = oss_bucket
        self.oss_resource_id = oss_resource_id
        self.sample_rate = sample_rate
        self.scene_id = scene_id
        self.scene_name = scene_name
        self.service_id = service_id
        self.service_name = service_name
        self.status = status
        self.user_id_field = user_id_field
        self.user_table = user_table
        self.user_table_partition_field = user_table_partition_field
        self.user_table_partition_field_format = user_table_partition_field_format
        self.workflow_name = workflow_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compare_feature is not None:
            result['CompareFeature'] = self.compare_feature
        if self.eas_service_name is not None:
            result['EasServiceName'] = self.eas_service_name
        if self.easy_rec_package_path is not None:
            result['EasyRecPackagePath'] = self.easy_rec_package_path
        if self.easy_rec_version is not None:
            result['EasyRecVersion'] = self.easy_rec_version
        if self.feature_consistency_check_job_config_id is not None:
            result['FeatureConsistencyCheckJobConfigId'] = self.feature_consistency_check_job_config_id
        if self.feature_display_exclude is not None:
            result['FeatureDisplayExclude'] = self.feature_display_exclude
        if self.feature_landing_resource_id is not None:
            result['FeatureLandingResourceId'] = self.feature_landing_resource_id
        if self.feature_landing_resource_uri is not None:
            result['FeatureLandingResourceUri'] = self.feature_landing_resource_uri
        if self.feature_priority is not None:
            result['FeaturePriority'] = self.feature_priority
        if self.fg_jar_version is not None:
            result['FgJarVersion'] = self.fg_jar_version
        if self.fg_json_file_name is not None:
            result['FgJsonFileName'] = self.fg_json_file_name
        if self.generate_zip is not None:
            result['GenerateZip'] = self.generate_zip
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.item_id_field is not None:
            result['ItemIdField'] = self.item_id_field
        if self.item_table is not None:
            result['ItemTable'] = self.item_table
        if self.item_table_partition_field is not None:
            result['ItemTablePartitionField'] = self.item_table_partition_field
        if self.item_table_partition_field_format is not None:
            result['ItemTablePartitionFieldFormat'] = self.item_table_partition_field_format
        if self.latest_job_gmt_sampling_end_time is not None:
            result['LatestJobGmtSamplingEndTime'] = self.latest_job_gmt_sampling_end_time
        if self.latest_job_gmt_sampling_start_time is not None:
            result['LatestJobGmtSamplingStartTime'] = self.latest_job_gmt_sampling_start_time
        if self.latest_job_id is not None:
            result['LatestJobId'] = self.latest_job_id
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.oss_resource_id is not None:
            result['OssResourceId'] = self.oss_resource_id
        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id_field is not None:
            result['UserIdField'] = self.user_id_field
        if self.user_table is not None:
            result['UserTable'] = self.user_table
        if self.user_table_partition_field is not None:
            result['UserTablePartitionField'] = self.user_table_partition_field
        if self.user_table_partition_field_format is not None:
            result['UserTablePartitionFieldFormat'] = self.user_table_partition_field_format
        if self.workflow_name is not None:
            result['WorkflowName'] = self.workflow_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompareFeature') is not None:
            self.compare_feature = m.get('CompareFeature')
        if m.get('EasServiceName') is not None:
            self.eas_service_name = m.get('EasServiceName')
        if m.get('EasyRecPackagePath') is not None:
            self.easy_rec_package_path = m.get('EasyRecPackagePath')
        if m.get('EasyRecVersion') is not None:
            self.easy_rec_version = m.get('EasyRecVersion')
        if m.get('FeatureConsistencyCheckJobConfigId') is not None:
            self.feature_consistency_check_job_config_id = m.get('FeatureConsistencyCheckJobConfigId')
        if m.get('FeatureDisplayExclude') is not None:
            self.feature_display_exclude = m.get('FeatureDisplayExclude')
        if m.get('FeatureLandingResourceId') is not None:
            self.feature_landing_resource_id = m.get('FeatureLandingResourceId')
        if m.get('FeatureLandingResourceUri') is not None:
            self.feature_landing_resource_uri = m.get('FeatureLandingResourceUri')
        if m.get('FeaturePriority') is not None:
            self.feature_priority = m.get('FeaturePriority')
        if m.get('FgJarVersion') is not None:
            self.fg_jar_version = m.get('FgJarVersion')
        if m.get('FgJsonFileName') is not None:
            self.fg_json_file_name = m.get('FgJsonFileName')
        if m.get('GenerateZip') is not None:
            self.generate_zip = m.get('GenerateZip')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('ItemIdField') is not None:
            self.item_id_field = m.get('ItemIdField')
        if m.get('ItemTable') is not None:
            self.item_table = m.get('ItemTable')
        if m.get('ItemTablePartitionField') is not None:
            self.item_table_partition_field = m.get('ItemTablePartitionField')
        if m.get('ItemTablePartitionFieldFormat') is not None:
            self.item_table_partition_field_format = m.get('ItemTablePartitionFieldFormat')
        if m.get('LatestJobGmtSamplingEndTime') is not None:
            self.latest_job_gmt_sampling_end_time = m.get('LatestJobGmtSamplingEndTime')
        if m.get('LatestJobGmtSamplingStartTime') is not None:
            self.latest_job_gmt_sampling_start_time = m.get('LatestJobGmtSamplingStartTime')
        if m.get('LatestJobId') is not None:
            self.latest_job_id = m.get('LatestJobId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('OssResourceId') is not None:
            self.oss_resource_id = m.get('OssResourceId')
        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserIdField') is not None:
            self.user_id_field = m.get('UserIdField')
        if m.get('UserTable') is not None:
            self.user_table = m.get('UserTable')
        if m.get('UserTablePartitionField') is not None:
            self.user_table_partition_field = m.get('UserTablePartitionField')
        if m.get('UserTablePartitionFieldFormat') is not None:
            self.user_table_partition_field_format = m.get('UserTablePartitionFieldFormat')
        if m.get('WorkflowName') is not None:
            self.workflow_name = m.get('WorkflowName')
        return self


class ListFeatureConsistencyCheckJobConfigsResponseBody(TeaModel):
    def __init__(
        self,
        feature_consistency_check_configs: List[ListFeatureConsistencyCheckJobConfigsResponseBodyFeatureConsistencyCheckConfigs] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.feature_consistency_check_configs = feature_consistency_check_configs
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.feature_consistency_check_configs:
            for k in self.feature_consistency_check_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FeatureConsistencyCheckConfigs'] = []
        if self.feature_consistency_check_configs is not None:
            for k in self.feature_consistency_check_configs:
                result['FeatureConsistencyCheckConfigs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.feature_consistency_check_configs = []
        if m.get('FeatureConsistencyCheckConfigs') is not None:
            for k in m.get('FeatureConsistencyCheckConfigs'):
                temp_model = ListFeatureConsistencyCheckJobConfigsResponseBodyFeatureConsistencyCheckConfigs()
                self.feature_consistency_check_configs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListFeatureConsistencyCheckJobConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFeatureConsistencyCheckJobConfigsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListFeatureConsistencyCheckJobConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFeatureConsistencyCheckJobFeatureReportsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        log_item_id: str = None,
        log_request_id: str = None,
        log_user_id: str = None,
    ):
        self.instance_id = instance_id
        self.log_item_id = log_item_id
        self.log_request_id = log_request_id
        self.log_user_id = log_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.log_item_id is not None:
            result['LogItemId'] = self.log_item_id
        if self.log_request_id is not None:
            result['LogRequestId'] = self.log_request_id
        if self.log_user_id is not None:
            result['LogUserId'] = self.log_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LogItemId') is not None:
            self.log_item_id = m.get('LogItemId')
        if m.get('LogRequestId') is not None:
            self.log_request_id = m.get('LogRequestId')
        if m.get('LogUserId') is not None:
            self.log_user_id = m.get('LogUserId')
        return self


class ListFeatureConsistencyCheckJobFeatureReportsResponseBodyReportsOfFeatureDiff(TeaModel):
    def __init__(
        self,
        feature_name: str = None,
        log_item_id: str = None,
        log_request_id: str = None,
        log_user_id: str = None,
        offline_value: str = None,
        online_value: str = None,
    ):
        self.feature_name = feature_name
        self.log_item_id = log_item_id
        self.log_request_id = log_request_id
        self.log_user_id = log_user_id
        self.offline_value = offline_value
        self.online_value = online_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name
        if self.log_item_id is not None:
            result['LogItemId'] = self.log_item_id
        if self.log_request_id is not None:
            result['LogRequestId'] = self.log_request_id
        if self.log_user_id is not None:
            result['LogUserId'] = self.log_user_id
        if self.offline_value is not None:
            result['OfflineValue'] = self.offline_value
        if self.online_value is not None:
            result['OnlineValue'] = self.online_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')
        if m.get('LogItemId') is not None:
            self.log_item_id = m.get('LogItemId')
        if m.get('LogRequestId') is not None:
            self.log_request_id = m.get('LogRequestId')
        if m.get('LogUserId') is not None:
            self.log_user_id = m.get('LogUserId')
        if m.get('OfflineValue') is not None:
            self.offline_value = m.get('OfflineValue')
        if m.get('OnlineValue') is not None:
            self.online_value = m.get('OnlineValue')
        return self


class ListFeatureConsistencyCheckJobFeatureReportsResponseBody(TeaModel):
    def __init__(
        self,
        data_path: str = None,
        oss_path: str = None,
        reports_of_feature_diff: List[ListFeatureConsistencyCheckJobFeatureReportsResponseBodyReportsOfFeatureDiff] = None,
        request_id: str = None,
    ):
        self.data_path = data_path
        self.oss_path = oss_path
        self.reports_of_feature_diff = reports_of_feature_diff
        self.request_id = request_id

    def validate(self):
        if self.reports_of_feature_diff:
            for k in self.reports_of_feature_diff:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_path is not None:
            result['DataPath'] = self.data_path
        if self.oss_path is not None:
            result['OssPath'] = self.oss_path
        result['ReportsOfFeatureDiff'] = []
        if self.reports_of_feature_diff is not None:
            for k in self.reports_of_feature_diff:
                result['ReportsOfFeatureDiff'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataPath') is not None:
            self.data_path = m.get('DataPath')
        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')
        self.reports_of_feature_diff = []
        if m.get('ReportsOfFeatureDiff') is not None:
            for k in m.get('ReportsOfFeatureDiff'):
                temp_model = ListFeatureConsistencyCheckJobFeatureReportsResponseBodyReportsOfFeatureDiff()
                self.reports_of_feature_diff.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFeatureConsistencyCheckJobFeatureReportsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFeatureConsistencyCheckJobFeatureReportsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListFeatureConsistencyCheckJobFeatureReportsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFeatureConsistencyCheckJobScoreReportsRequest(TeaModel):
    def __init__(
        self,
        exclude_request_ids: List[str] = None,
        instance_id: str = None,
    ):
        self.exclude_request_ids = exclude_request_ids
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exclude_request_ids is not None:
            result['ExcludeRequestIds'] = self.exclude_request_ids
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExcludeRequestIds') is not None:
            self.exclude_request_ids = m.get('ExcludeRequestIds')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListFeatureConsistencyCheckJobScoreReportsShrinkRequest(TeaModel):
    def __init__(
        self,
        exclude_request_ids_shrink: str = None,
        instance_id: str = None,
    ):
        self.exclude_request_ids_shrink = exclude_request_ids_shrink
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exclude_request_ids_shrink is not None:
            result['ExcludeRequestIds'] = self.exclude_request_ids_shrink
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExcludeRequestIds') is not None:
            self.exclude_request_ids_shrink = m.get('ExcludeRequestIds')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListFeatureConsistencyCheckJobScoreReportsResponseBodyReportsOfScoreDiff(TeaModel):
    def __init__(
        self,
        log_item_id: str = None,
        log_request_id: str = None,
        log_user_id: str = None,
        score_diff: str = None,
        score_diff_detail: str = None,
    ):
        self.log_item_id = log_item_id
        self.log_request_id = log_request_id
        self.log_user_id = log_user_id
        self.score_diff = score_diff
        self.score_diff_detail = score_diff_detail

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_item_id is not None:
            result['LogItemId'] = self.log_item_id
        if self.log_request_id is not None:
            result['LogRequestId'] = self.log_request_id
        if self.log_user_id is not None:
            result['LogUserId'] = self.log_user_id
        if self.score_diff is not None:
            result['ScoreDiff'] = self.score_diff
        if self.score_diff_detail is not None:
            result['ScoreDiffDetail'] = self.score_diff_detail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogItemId') is not None:
            self.log_item_id = m.get('LogItemId')
        if m.get('LogRequestId') is not None:
            self.log_request_id = m.get('LogRequestId')
        if m.get('LogUserId') is not None:
            self.log_user_id = m.get('LogUserId')
        if m.get('ScoreDiff') is not None:
            self.score_diff = m.get('ScoreDiff')
        if m.get('ScoreDiffDetail') is not None:
            self.score_diff_detail = m.get('ScoreDiffDetail')
        return self


class ListFeatureConsistencyCheckJobScoreReportsResponseBody(TeaModel):
    def __init__(
        self,
        data_path: str = None,
        oss_path: str = None,
        reports_of_score_diff: List[ListFeatureConsistencyCheckJobScoreReportsResponseBodyReportsOfScoreDiff] = None,
        request_id: str = None,
    ):
        self.data_path = data_path
        self.oss_path = oss_path
        self.reports_of_score_diff = reports_of_score_diff
        self.request_id = request_id

    def validate(self):
        if self.reports_of_score_diff:
            for k in self.reports_of_score_diff:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_path is not None:
            result['DataPath'] = self.data_path
        if self.oss_path is not None:
            result['OssPath'] = self.oss_path
        result['ReportsOfScoreDiff'] = []
        if self.reports_of_score_diff is not None:
            for k in self.reports_of_score_diff:
                result['ReportsOfScoreDiff'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataPath') is not None:
            self.data_path = m.get('DataPath')
        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')
        self.reports_of_score_diff = []
        if m.get('ReportsOfScoreDiff') is not None:
            for k in m.get('ReportsOfScoreDiff'):
                temp_model = ListFeatureConsistencyCheckJobScoreReportsResponseBodyReportsOfScoreDiff()
                self.reports_of_score_diff.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFeatureConsistencyCheckJobScoreReportsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFeatureConsistencyCheckJobScoreReportsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListFeatureConsistencyCheckJobScoreReportsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFeatureConsistencyCheckJobsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        order: str = None,
        page_number: str = None,
        page_size: str = None,
        sort_by: str = None,
        status: str = None,
    ):
        self.instance_id = instance_id
        self.order = order
        self.page_number = page_number
        self.page_size = page_size
        self.sort_by = sort_by
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListFeatureConsistencyCheckJobsResponseBodyFeatureConsistencyCheckJobs(TeaModel):
    def __init__(
        self,
        config: str = None,
        feature_consistency_check_job_config_id: str = None,
        feature_consistency_check_job_config_name: str = None,
        feature_consistency_check_job_id: str = None,
        gmt_end_time: str = None,
        gmt_start_time: str = None,
        logs: List[str] = None,
        status: str = None,
    ):
        self.config = config
        self.feature_consistency_check_job_config_id = feature_consistency_check_job_config_id
        self.feature_consistency_check_job_config_name = feature_consistency_check_job_config_name
        self.feature_consistency_check_job_id = feature_consistency_check_job_id
        self.gmt_end_time = gmt_end_time
        self.gmt_start_time = gmt_start_time
        self.logs = logs
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.feature_consistency_check_job_config_id is not None:
            result['FeatureConsistencyCheckJobConfigId'] = self.feature_consistency_check_job_config_id
        if self.feature_consistency_check_job_config_name is not None:
            result['FeatureConsistencyCheckJobConfigName'] = self.feature_consistency_check_job_config_name
        if self.feature_consistency_check_job_id is not None:
            result['FeatureConsistencyCheckJobId'] = self.feature_consistency_check_job_id
        if self.gmt_end_time is not None:
            result['GmtEndTime'] = self.gmt_end_time
        if self.gmt_start_time is not None:
            result['GmtStartTime'] = self.gmt_start_time
        if self.logs is not None:
            result['Logs'] = self.logs
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('FeatureConsistencyCheckJobConfigId') is not None:
            self.feature_consistency_check_job_config_id = m.get('FeatureConsistencyCheckJobConfigId')
        if m.get('FeatureConsistencyCheckJobConfigName') is not None:
            self.feature_consistency_check_job_config_name = m.get('FeatureConsistencyCheckJobConfigName')
        if m.get('FeatureConsistencyCheckJobId') is not None:
            self.feature_consistency_check_job_id = m.get('FeatureConsistencyCheckJobId')
        if m.get('GmtEndTime') is not None:
            self.gmt_end_time = m.get('GmtEndTime')
        if m.get('GmtStartTime') is not None:
            self.gmt_start_time = m.get('GmtStartTime')
        if m.get('Logs') is not None:
            self.logs = m.get('Logs')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListFeatureConsistencyCheckJobsResponseBody(TeaModel):
    def __init__(
        self,
        feature_consistency_check_jobs: List[ListFeatureConsistencyCheckJobsResponseBodyFeatureConsistencyCheckJobs] = None,
        request_id: str = None,
        total_count: str = None,
    ):
        self.feature_consistency_check_jobs = feature_consistency_check_jobs
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.feature_consistency_check_jobs:
            for k in self.feature_consistency_check_jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FeatureConsistencyCheckJobs'] = []
        if self.feature_consistency_check_jobs is not None:
            for k in self.feature_consistency_check_jobs:
                result['FeatureConsistencyCheckJobs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.feature_consistency_check_jobs = []
        if m.get('FeatureConsistencyCheckJobs') is not None:
            for k in m.get('FeatureConsistencyCheckJobs'):
                temp_model = ListFeatureConsistencyCheckJobsResponseBodyFeatureConsistencyCheckJobs()
                self.feature_consistency_check_jobs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListFeatureConsistencyCheckJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFeatureConsistencyCheckJobsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListFeatureConsistencyCheckJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: str = None,
        type: str = None,
    ):
        self.instance_id = instance_id
        self.order = order
        self.page_number = page_number
        self.page_size = page_size
        self.sort_by = sort_by
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListInstancesResponseBodyInstancesConfigDataManagements(TeaModel):
    def __init__(
        self,
        component_code: str = None,
        meta: Dict[str, Any] = None,
        type: str = None,
    ):
        self.component_code = component_code
        self.meta = meta
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_code is not None:
            result['ComponentCode'] = self.component_code
        if self.meta is not None:
            result['Meta'] = self.meta
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentCode') is not None:
            self.component_code = m.get('ComponentCode')
        if m.get('Meta') is not None:
            self.meta = m.get('Meta')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListInstancesResponseBodyInstancesConfigEngines(TeaModel):
    def __init__(
        self,
        component_code: str = None,
        meta: Dict[str, Any] = None,
        type: str = None,
    ):
        self.component_code = component_code
        self.meta = meta
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_code is not None:
            result['ComponentCode'] = self.component_code
        if self.meta is not None:
            result['Meta'] = self.meta
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentCode') is not None:
            self.component_code = m.get('ComponentCode')
        if m.get('Meta') is not None:
            self.meta = m.get('Meta')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListInstancesResponseBodyInstancesConfigMonitors(TeaModel):
    def __init__(
        self,
        component_code: str = None,
        meta: Dict[str, Any] = None,
        type: str = None,
    ):
        self.component_code = component_code
        self.meta = meta
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_code is not None:
            result['ComponentCode'] = self.component_code
        if self.meta is not None:
            result['Meta'] = self.meta
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentCode') is not None:
            self.component_code = m.get('ComponentCode')
        if m.get('Meta') is not None:
            self.meta = m.get('Meta')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListInstancesResponseBodyInstancesConfig(TeaModel):
    def __init__(
        self,
        data_managements: List[ListInstancesResponseBodyInstancesConfigDataManagements] = None,
        engines: List[ListInstancesResponseBodyInstancesConfigEngines] = None,
        monitors: List[ListInstancesResponseBodyInstancesConfigMonitors] = None,
    ):
        self.data_managements = data_managements
        self.engines = engines
        self.monitors = monitors

    def validate(self):
        if self.data_managements:
            for k in self.data_managements:
                if k:
                    k.validate()
        if self.engines:
            for k in self.engines:
                if k:
                    k.validate()
        if self.monitors:
            for k in self.monitors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataManagements'] = []
        if self.data_managements is not None:
            for k in self.data_managements:
                result['DataManagements'].append(k.to_map() if k else None)
        result['Engines'] = []
        if self.engines is not None:
            for k in self.engines:
                result['Engines'].append(k.to_map() if k else None)
        result['Monitors'] = []
        if self.monitors is not None:
            for k in self.monitors:
                result['Monitors'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_managements = []
        if m.get('DataManagements') is not None:
            for k in m.get('DataManagements'):
                temp_model = ListInstancesResponseBodyInstancesConfigDataManagements()
                self.data_managements.append(temp_model.from_map(k))
        self.engines = []
        if m.get('Engines') is not None:
            for k in m.get('Engines'):
                temp_model = ListInstancesResponseBodyInstancesConfigEngines()
                self.engines.append(temp_model.from_map(k))
        self.monitors = []
        if m.get('Monitors') is not None:
            for k in m.get('Monitors'):
                temp_model = ListInstancesResponseBodyInstancesConfigMonitors()
                self.monitors.append(temp_model.from_map(k))
        return self


class ListInstancesResponseBodyInstances(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        commodity_code: str = None,
        config: ListInstancesResponseBodyInstancesConfig = None,
        expired_time: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        instance_id: str = None,
        region_id: str = None,
        status: str = None,
        type: str = None,
    ):
        self.charge_type = charge_type
        self.commodity_code = commodity_code
        self.config = config
        self.expired_time = expired_time
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.instance_id = instance_id
        self.region_id = region_id
        self.status = status
        self.type = type

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.config is not None:
            result['Config'] = self.config.to_map()
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('Config') is not None:
            temp_model = ListInstancesResponseBodyInstancesConfig()
            self.config = temp_model.from_map(m['Config'])
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListInstancesResponseBody(TeaModel):
    def __init__(
        self,
        instances: List[ListInstancesResponseBodyInstances] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.instances = instances
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = ListInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLaboratoriesRequest(TeaModel):
    def __init__(
        self,
        environment: str = None,
        instance_id: str = None,
        scene_id: str = None,
        status: str = None,
    ):
        self.environment = environment
        self.instance_id = instance_id
        self.scene_id = scene_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListLaboratoriesResponseBodyLaboratories(TeaModel):
    def __init__(
        self,
        bucket_count: int = None,
        bucket_type: str = None,
        buckets: str = None,
        crowd_id: str = None,
        debug_crowd_id: str = None,
        debug_users: str = None,
        description: str = None,
        environment: str = None,
        filter: str = None,
        laboratory_id: str = None,
        name: str = None,
        scene_id: str = None,
        status: str = None,
        type: str = None,
    ):
        self.bucket_count = bucket_count
        self.bucket_type = bucket_type
        self.buckets = buckets
        self.crowd_id = crowd_id
        self.debug_crowd_id = debug_crowd_id
        self.debug_users = debug_users
        self.description = description
        self.environment = environment
        self.filter = filter
        self.laboratory_id = laboratory_id
        self.name = name
        self.scene_id = scene_id
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_count is not None:
            result['BucketCount'] = self.bucket_count
        if self.bucket_type is not None:
            result['BucketType'] = self.bucket_type
        if self.buckets is not None:
            result['Buckets'] = self.buckets
        if self.crowd_id is not None:
            result['CrowdId'] = self.crowd_id
        if self.debug_crowd_id is not None:
            result['DebugCrowdId'] = self.debug_crowd_id
        if self.debug_users is not None:
            result['DebugUsers'] = self.debug_users
        if self.description is not None:
            result['Description'] = self.description
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.laboratory_id is not None:
            result['LaboratoryId'] = self.laboratory_id
        if self.name is not None:
            result['Name'] = self.name
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketCount') is not None:
            self.bucket_count = m.get('BucketCount')
        if m.get('BucketType') is not None:
            self.bucket_type = m.get('BucketType')
        if m.get('Buckets') is not None:
            self.buckets = m.get('Buckets')
        if m.get('CrowdId') is not None:
            self.crowd_id = m.get('CrowdId')
        if m.get('DebugCrowdId') is not None:
            self.debug_crowd_id = m.get('DebugCrowdId')
        if m.get('DebugUsers') is not None:
            self.debug_users = m.get('DebugUsers')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('LaboratoryId') is not None:
            self.laboratory_id = m.get('LaboratoryId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListLaboratoriesResponseBody(TeaModel):
    def __init__(
        self,
        laboratories: List[ListLaboratoriesResponseBodyLaboratories] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.laboratories = laboratories
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.laboratories:
            for k in self.laboratories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Laboratories'] = []
        if self.laboratories is not None:
            for k in self.laboratories:
                result['Laboratories'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.laboratories = []
        if m.get('Laboratories') is not None:
            for k in m.get('Laboratories'):
                temp_model = ListLaboratoriesResponseBodyLaboratories()
                self.laboratories.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListLaboratoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLaboratoriesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListLaboratoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLayersRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        laboratory_id: str = None,
    ):
        self.instance_id = instance_id
        self.laboratory_id = laboratory_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.laboratory_id is not None:
            result['LaboratoryId'] = self.laboratory_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LaboratoryId') is not None:
            self.laboratory_id = m.get('LaboratoryId')
        return self


class ListLayersResponseBodyLayers(TeaModel):
    def __init__(
        self,
        description: str = None,
        laboratory_id: str = None,
        layer_id: str = None,
        name: str = None,
        scene_id: str = None,
    ):
        self.description = description
        self.laboratory_id = laboratory_id
        self.layer_id = layer_id
        self.name = name
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.laboratory_id is not None:
            result['LaboratoryId'] = self.laboratory_id
        if self.layer_id is not None:
            result['LayerId'] = self.layer_id
        if self.name is not None:
            result['Name'] = self.name
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LaboratoryId') is not None:
            self.laboratory_id = m.get('LaboratoryId')
        if m.get('LayerId') is not None:
            self.layer_id = m.get('LayerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class ListLayersResponseBody(TeaModel):
    def __init__(
        self,
        layers: List[ListLayersResponseBodyLayers] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.layers = layers
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.layers:
            for k in self.layers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Layers'] = []
        if self.layers is not None:
            for k in self.layers:
                result['Layers'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.layers = []
        if m.get('Layers') is not None:
            for k in m.get('Layers'):
                temp_model = ListLayersResponseBodyLayers()
                self.layers.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListLayersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLayersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListLayersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListParamsRequest(TeaModel):
    def __init__(
        self,
        environment: str = None,
        instance_id: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        scene_id: str = None,
    ):
        self.environment = environment
        self.instance_id = instance_id
        self.name = name
        self.page_number = page_number
        self.page_size = page_size
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class ListParamsResponseBodyParams(TeaModel):
    def __init__(
        self,
        environment: str = None,
        gmt_modified_time: str = None,
        name: str = None,
        param_id: str = None,
        value: str = None,
    ):
        self.environment = environment
        self.gmt_modified_time = gmt_modified_time
        self.name = name
        self.param_id = param_id
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.param_id is not None:
            result['ParamId'] = self.param_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParamId') is not None:
            self.param_id = m.get('ParamId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListParamsResponseBody(TeaModel):
    def __init__(
        self,
        params: List[ListParamsResponseBodyParams] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.params = params
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.params:
            for k in self.params:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Params'] = []
        if self.params is not None:
            for k in self.params:
                result['Params'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.params = []
        if m.get('Params') is not None:
            for k in m.get('Params'):
                temp_model = ListParamsResponseBodyParams()
                self.params.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListParamsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListParamsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListParamsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListScenesRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        name: str = None,
    ):
        self.instance_id = instance_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListScenesResponseBodyScenesFlows(TeaModel):
    def __init__(
        self,
        flow_code: str = None,
        flow_name: str = None,
    ):
        self.flow_code = flow_code
        self.flow_name = flow_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        return self


class ListScenesResponseBodyScenes(TeaModel):
    def __init__(
        self,
        description: str = None,
        flows: List[ListScenesResponseBodyScenesFlows] = None,
        name: str = None,
        scene_id: str = None,
    ):
        self.description = description
        self.flows = flows
        self.name = name
        self.scene_id = scene_id

    def validate(self):
        if self.flows:
            for k in self.flows:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        result['Flows'] = []
        if self.flows is not None:
            for k in self.flows:
                result['Flows'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.flows = []
        if m.get('Flows') is not None:
            for k in m.get('Flows'):
                temp_model = ListScenesResponseBodyScenesFlows()
                self.flows.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class ListScenesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        scenes: List[ListScenesResponseBodyScenes] = None,
        total_count: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.scenes = scenes
        self.total_count = total_count

    def validate(self):
        if self.scenes:
            for k in self.scenes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Scenes'] = []
        if self.scenes is not None:
            for k in self.scenes:
                result['Scenes'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.scenes = []
        if m.get('Scenes') is not None:
            for k in m.get('Scenes'):
                temp_model = ListScenesResponseBodyScenes()
                self.scenes.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListScenesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListScenesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListScenesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSubCrowdsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListSubCrowdsResponseBodySubCrowds(TeaModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        quantity: int = None,
        source: str = None,
        sub_crowd_id: str = None,
        users: str = None,
    ):
        self.gmt_create_time = gmt_create_time
        self.quantity = quantity
        self.source = source
        self.sub_crowd_id = sub_crowd_id
        self.users = users

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.source is not None:
            result['Source'] = self.source
        if self.sub_crowd_id is not None:
            result['SubCrowdId'] = self.sub_crowd_id
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SubCrowdId') is not None:
            self.sub_crowd_id = m.get('SubCrowdId')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class ListSubCrowdsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sub_crowds: List[ListSubCrowdsResponseBodySubCrowds] = None,
        total_count: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.sub_crowds = sub_crowds
        self.total_count = total_count

    def validate(self):
        if self.sub_crowds:
            for k in self.sub_crowds:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SubCrowds'] = []
        if self.sub_crowds is not None:
            for k in self.sub_crowds:
                result['SubCrowds'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sub_crowds = []
        if m.get('SubCrowds') is not None:
            for k in m.get('SubCrowds'):
                temp_model = ListSubCrowdsResponseBodySubCrowds()
                self.sub_crowds.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSubCrowdsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSubCrowdsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSubCrowdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OfflineExperimentRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OfflineExperimentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class OfflineExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OfflineExperimentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OfflineExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OfflineExperimentGroupRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OfflineExperimentGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class OfflineExperimentGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OfflineExperimentGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OfflineExperimentGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OfflineLaboratoryRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OfflineLaboratoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class OfflineLaboratoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OfflineLaboratoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OfflineLaboratoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnlineExperimentRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnlineExperimentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class OnlineExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OnlineExperimentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OnlineExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnlineExperimentGroupRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnlineExperimentGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class OnlineExperimentGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OnlineExperimentGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OnlineExperimentGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnlineLaboratoryRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnlineLaboratoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class OnlineLaboratoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OnlineLaboratoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OnlineLaboratoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushAllExperimentRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class PushAllExperimentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class PushAllExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PushAllExperimentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PushAllExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncFeatureConsistencyCheckJobReplayLogRequest(TeaModel):
    def __init__(
        self,
        context_features: str = None,
        feature_consistency_check_job_config_id: str = None,
        generated_features: str = None,
        instance_id: str = None,
        log_item_id: str = None,
        log_request_id: str = None,
        log_request_time: int = None,
        log_user_id: str = None,
        raw_features: str = None,
        scene_name: str = None,
    ):
        self.context_features = context_features
        self.feature_consistency_check_job_config_id = feature_consistency_check_job_config_id
        self.generated_features = generated_features
        self.instance_id = instance_id
        self.log_item_id = log_item_id
        self.log_request_id = log_request_id
        self.log_request_time = log_request_time
        self.log_user_id = log_user_id
        self.raw_features = raw_features
        self.scene_name = scene_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.context_features is not None:
            result['ContextFeatures'] = self.context_features
        if self.feature_consistency_check_job_config_id is not None:
            result['FeatureConsistencyCheckJobConfigId'] = self.feature_consistency_check_job_config_id
        if self.generated_features is not None:
            result['GeneratedFeatures'] = self.generated_features
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.log_item_id is not None:
            result['LogItemId'] = self.log_item_id
        if self.log_request_id is not None:
            result['LogRequestId'] = self.log_request_id
        if self.log_request_time is not None:
            result['LogRequestTime'] = self.log_request_time
        if self.log_user_id is not None:
            result['LogUserId'] = self.log_user_id
        if self.raw_features is not None:
            result['RawFeatures'] = self.raw_features
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContextFeatures') is not None:
            self.context_features = m.get('ContextFeatures')
        if m.get('FeatureConsistencyCheckJobConfigId') is not None:
            self.feature_consistency_check_job_config_id = m.get('FeatureConsistencyCheckJobConfigId')
        if m.get('GeneratedFeatures') is not None:
            self.generated_features = m.get('GeneratedFeatures')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LogItemId') is not None:
            self.log_item_id = m.get('LogItemId')
        if m.get('LogRequestId') is not None:
            self.log_request_id = m.get('LogRequestId')
        if m.get('LogRequestTime') is not None:
            self.log_request_time = m.get('LogRequestTime')
        if m.get('LogUserId') is not None:
            self.log_user_id = m.get('LogUserId')
        if m.get('RawFeatures') is not None:
            self.raw_features = m.get('RawFeatures')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        return self


class SyncFeatureConsistencyCheckJobReplayLogResponseBody(TeaModel):
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


class SyncFeatureConsistencyCheckJobReplayLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SyncFeatureConsistencyCheckJobReplayLogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SyncFeatureConsistencyCheckJobReplayLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TerminateFeatureConsistencyCheckJobRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class TerminateFeatureConsistencyCheckJobResponseBody(TeaModel):
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


class TerminateFeatureConsistencyCheckJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TerminateFeatureConsistencyCheckJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TerminateFeatureConsistencyCheckJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCrowdRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        instance_id: str = None,
        name: str = None,
    ):
        self.description = description
        self.instance_id = instance_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateCrowdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class UpdateCrowdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateCrowdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateCrowdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateExperimentRequest(TeaModel):
    def __init__(
        self,
        config: str = None,
        debug_crowd_id: str = None,
        debug_users: str = None,
        description: str = None,
        flow_percent: int = None,
        instance_id: str = None,
        name: str = None,
        type: str = None,
    ):
        self.config = config
        self.debug_crowd_id = debug_crowd_id
        self.debug_users = debug_users
        self.description = description
        self.flow_percent = flow_percent
        self.instance_id = instance_id
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.debug_crowd_id is not None:
            result['DebugCrowdId'] = self.debug_crowd_id
        if self.debug_users is not None:
            result['DebugUsers'] = self.debug_users
        if self.description is not None:
            result['Description'] = self.description
        if self.flow_percent is not None:
            result['FlowPercent'] = self.flow_percent
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('DebugCrowdId') is not None:
            self.debug_crowd_id = m.get('DebugCrowdId')
        if m.get('DebugUsers') is not None:
            self.debug_users = m.get('DebugUsers')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FlowPercent') is not None:
            self.flow_percent = m.get('FlowPercent')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateExperimentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class UpdateExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateExperimentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateExperimentGroupRequest(TeaModel):
    def __init__(
        self,
        config: str = None,
        crowd_id: str = None,
        debug_crowd_id: str = None,
        debug_users: str = None,
        description: str = None,
        distribution_time_duration: int = None,
        distribution_type: str = None,
        filter: str = None,
        instance_id: str = None,
        layer_id: str = None,
        name: str = None,
        need_aa: bool = None,
        reservced_buckets: str = None,
    ):
        self.config = config
        self.crowd_id = crowd_id
        self.debug_crowd_id = debug_crowd_id
        self.debug_users = debug_users
        self.description = description
        self.distribution_time_duration = distribution_time_duration
        self.distribution_type = distribution_type
        self.filter = filter
        self.instance_id = instance_id
        self.layer_id = layer_id
        self.name = name
        self.need_aa = need_aa
        self.reservced_buckets = reservced_buckets

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.crowd_id is not None:
            result['CrowdId'] = self.crowd_id
        if self.debug_crowd_id is not None:
            result['DebugCrowdId'] = self.debug_crowd_id
        if self.debug_users is not None:
            result['DebugUsers'] = self.debug_users
        if self.description is not None:
            result['Description'] = self.description
        if self.distribution_time_duration is not None:
            result['DistributionTimeDuration'] = self.distribution_time_duration
        if self.distribution_type is not None:
            result['DistributionType'] = self.distribution_type
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.layer_id is not None:
            result['LayerId'] = self.layer_id
        if self.name is not None:
            result['Name'] = self.name
        if self.need_aa is not None:
            result['NeedAA'] = self.need_aa
        if self.reservced_buckets is not None:
            result['ReservcedBuckets'] = self.reservced_buckets
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('CrowdId') is not None:
            self.crowd_id = m.get('CrowdId')
        if m.get('DebugCrowdId') is not None:
            self.debug_crowd_id = m.get('DebugCrowdId')
        if m.get('DebugUsers') is not None:
            self.debug_users = m.get('DebugUsers')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DistributionTimeDuration') is not None:
            self.distribution_time_duration = m.get('DistributionTimeDuration')
        if m.get('DistributionType') is not None:
            self.distribution_type = m.get('DistributionType')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LayerId') is not None:
            self.layer_id = m.get('LayerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NeedAA') is not None:
            self.need_aa = m.get('NeedAA')
        if m.get('ReservcedBuckets') is not None:
            self.reservced_buckets = m.get('ReservcedBuckets')
        return self


class UpdateExperimentGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class UpdateExperimentGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateExperimentGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateExperimentGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFeatureConsistencyCheckJobConfigRequest(TeaModel):
    def __init__(
        self,
        compare_feature: bool = None,
        eas_service_name: str = None,
        easy_rec_package_path: str = None,
        easy_rec_version: str = None,
        feature_display_exclude: str = None,
        feature_landing_resource_id: str = None,
        feature_priority: str = None,
        fg_jar_version: str = None,
        fg_json_file_name: str = None,
        generate_zip: bool = None,
        instance_id: str = None,
        item_id_field: str = None,
        item_table: str = None,
        item_table_partition_field: str = None,
        item_table_partition_field_format: str = None,
        name: str = None,
        oss_resource_id: str = None,
        sample_rate: float = None,
        scene_id: str = None,
        service_id: str = None,
        user_id_field: str = None,
        user_table: str = None,
        user_table_partition_field: str = None,
        user_table_partition_field_format: str = None,
        workflow_name: str = None,
    ):
        self.compare_feature = compare_feature
        self.eas_service_name = eas_service_name
        self.easy_rec_package_path = easy_rec_package_path
        self.easy_rec_version = easy_rec_version
        self.feature_display_exclude = feature_display_exclude
        self.feature_landing_resource_id = feature_landing_resource_id
        self.feature_priority = feature_priority
        self.fg_jar_version = fg_jar_version
        self.fg_json_file_name = fg_json_file_name
        self.generate_zip = generate_zip
        self.instance_id = instance_id
        self.item_id_field = item_id_field
        self.item_table = item_table
        self.item_table_partition_field = item_table_partition_field
        self.item_table_partition_field_format = item_table_partition_field_format
        self.name = name
        self.oss_resource_id = oss_resource_id
        self.sample_rate = sample_rate
        self.scene_id = scene_id
        self.service_id = service_id
        self.user_id_field = user_id_field
        self.user_table = user_table
        self.user_table_partition_field = user_table_partition_field
        self.user_table_partition_field_format = user_table_partition_field_format
        self.workflow_name = workflow_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compare_feature is not None:
            result['CompareFeature'] = self.compare_feature
        if self.eas_service_name is not None:
            result['EasServiceName'] = self.eas_service_name
        if self.easy_rec_package_path is not None:
            result['EasyRecPackagePath'] = self.easy_rec_package_path
        if self.easy_rec_version is not None:
            result['EasyRecVersion'] = self.easy_rec_version
        if self.feature_display_exclude is not None:
            result['FeatureDisplayExclude'] = self.feature_display_exclude
        if self.feature_landing_resource_id is not None:
            result['FeatureLandingResourceId'] = self.feature_landing_resource_id
        if self.feature_priority is not None:
            result['FeaturePriority'] = self.feature_priority
        if self.fg_jar_version is not None:
            result['FgJarVersion'] = self.fg_jar_version
        if self.fg_json_file_name is not None:
            result['FgJsonFileName'] = self.fg_json_file_name
        if self.generate_zip is not None:
            result['GenerateZip'] = self.generate_zip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.item_id_field is not None:
            result['ItemIdField'] = self.item_id_field
        if self.item_table is not None:
            result['ItemTable'] = self.item_table
        if self.item_table_partition_field is not None:
            result['ItemTablePartitionField'] = self.item_table_partition_field
        if self.item_table_partition_field_format is not None:
            result['ItemTablePartitionFieldFormat'] = self.item_table_partition_field_format
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_resource_id is not None:
            result['OssResourceId'] = self.oss_resource_id
        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.user_id_field is not None:
            result['UserIdField'] = self.user_id_field
        if self.user_table is not None:
            result['UserTable'] = self.user_table
        if self.user_table_partition_field is not None:
            result['UserTablePartitionField'] = self.user_table_partition_field
        if self.user_table_partition_field_format is not None:
            result['UserTablePartitionFieldFormat'] = self.user_table_partition_field_format
        if self.workflow_name is not None:
            result['WorkflowName'] = self.workflow_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompareFeature') is not None:
            self.compare_feature = m.get('CompareFeature')
        if m.get('EasServiceName') is not None:
            self.eas_service_name = m.get('EasServiceName')
        if m.get('EasyRecPackagePath') is not None:
            self.easy_rec_package_path = m.get('EasyRecPackagePath')
        if m.get('EasyRecVersion') is not None:
            self.easy_rec_version = m.get('EasyRecVersion')
        if m.get('FeatureDisplayExclude') is not None:
            self.feature_display_exclude = m.get('FeatureDisplayExclude')
        if m.get('FeatureLandingResourceId') is not None:
            self.feature_landing_resource_id = m.get('FeatureLandingResourceId')
        if m.get('FeaturePriority') is not None:
            self.feature_priority = m.get('FeaturePriority')
        if m.get('FgJarVersion') is not None:
            self.fg_jar_version = m.get('FgJarVersion')
        if m.get('FgJsonFileName') is not None:
            self.fg_json_file_name = m.get('FgJsonFileName')
        if m.get('GenerateZip') is not None:
            self.generate_zip = m.get('GenerateZip')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ItemIdField') is not None:
            self.item_id_field = m.get('ItemIdField')
        if m.get('ItemTable') is not None:
            self.item_table = m.get('ItemTable')
        if m.get('ItemTablePartitionField') is not None:
            self.item_table_partition_field = m.get('ItemTablePartitionField')
        if m.get('ItemTablePartitionFieldFormat') is not None:
            self.item_table_partition_field_format = m.get('ItemTablePartitionFieldFormat')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssResourceId') is not None:
            self.oss_resource_id = m.get('OssResourceId')
        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('UserIdField') is not None:
            self.user_id_field = m.get('UserIdField')
        if m.get('UserTable') is not None:
            self.user_table = m.get('UserTable')
        if m.get('UserTablePartitionField') is not None:
            self.user_table_partition_field = m.get('UserTablePartitionField')
        if m.get('UserTablePartitionFieldFormat') is not None:
            self.user_table_partition_field_format = m.get('UserTablePartitionFieldFormat')
        if m.get('WorkflowName') is not None:
            self.workflow_name = m.get('WorkflowName')
        return self


class UpdateFeatureConsistencyCheckJobConfigResponseBody(TeaModel):
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


class UpdateFeatureConsistencyCheckJobConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateFeatureConsistencyCheckJobConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateFeatureConsistencyCheckJobConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLaboratoryRequest(TeaModel):
    def __init__(
        self,
        bucket_count: int = None,
        bucket_type: str = None,
        buckets: str = None,
        debug_crowd_id: str = None,
        debug_users: str = None,
        description: str = None,
        environment: str = None,
        filter: str = None,
        instance_id: str = None,
        name: str = None,
        type: str = None,
    ):
        self.bucket_count = bucket_count
        self.bucket_type = bucket_type
        self.buckets = buckets
        self.debug_crowd_id = debug_crowd_id
        self.debug_users = debug_users
        self.description = description
        self.environment = environment
        self.filter = filter
        self.instance_id = instance_id
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_count is not None:
            result['BucketCount'] = self.bucket_count
        if self.bucket_type is not None:
            result['BucketType'] = self.bucket_type
        if self.buckets is not None:
            result['Buckets'] = self.buckets
        if self.debug_crowd_id is not None:
            result['DebugCrowdId'] = self.debug_crowd_id
        if self.debug_users is not None:
            result['DebugUsers'] = self.debug_users
        if self.description is not None:
            result['Description'] = self.description
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketCount') is not None:
            self.bucket_count = m.get('BucketCount')
        if m.get('BucketType') is not None:
            self.bucket_type = m.get('BucketType')
        if m.get('Buckets') is not None:
            self.buckets = m.get('Buckets')
        if m.get('DebugCrowdId') is not None:
            self.debug_crowd_id = m.get('DebugCrowdId')
        if m.get('DebugUsers') is not None:
            self.debug_users = m.get('DebugUsers')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateLaboratoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class UpdateLaboratoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateLaboratoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateLaboratoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLayerRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        instance_id: str = None,
        name: str = None,
    ):
        self.description = description
        self.instance_id = instance_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateLayerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class UpdateLayerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateLayerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateLayerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateParamRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        value: str = None,
    ):
        self.instance_id = instance_id
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateParamResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class UpdateParamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateParamResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateParamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSceneRequestFlows(TeaModel):
    def __init__(
        self,
        flow_code: str = None,
        flow_name: str = None,
    ):
        self.flow_code = flow_code
        self.flow_name = flow_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        return self


class UpdateSceneRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        flows: List[UpdateSceneRequestFlows] = None,
        instance_id: str = None,
        name: str = None,
    ):
        self.description = description
        self.flows = flows
        self.instance_id = instance_id
        self.name = name

    def validate(self):
        if self.flows:
            for k in self.flows:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        result['Flows'] = []
        if self.flows is not None:
            for k in self.flows:
                result['Flows'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.flows = []
        if m.get('Flows') is not None:
            for k in m.get('Flows'):
                temp_model = UpdateSceneRequestFlows()
                self.flows.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateSceneResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class UpdateSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSceneResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self

