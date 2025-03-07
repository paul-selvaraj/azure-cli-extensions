# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "maintenance assignment update-parent",
    is_preview=True,
)
class UpdateParent(AAZCommand):
    """Update configuration for resource.

    :example: ConfigurationAssignments_UpdateParent
        az maintenance update-parent --name "workervmPolicy" --provider-name "Microsoft.Compute" --resource-group "examplerg" --resource-name "smdvm1" --resource-parent-name "smdtest1" --resource-parent-type "virtualMachineScaleSets" --resource-type "virtualMachines"
    """

    _aaz_info = {
        "version": "2022-07-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/{}/{}/{}/{}/{}/providers/microsoft.maintenance/configurationassignments/{}", "2022-07-01-preview"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.configuration_assignment_name = AAZStrArg(
            options=["-n", "--name", "--configuration-assignment-name"],
            help="Configuration assignment Name",
            required=True,
            id_part="child_name_2",
        )
        _args_schema.provider_name = AAZStrArg(
            options=["--provider-name"],
            help="Resource provider name",
            required=True,
            id_part="namespace",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.resource_name = AAZStrArg(
            options=["--resource-name"],
            help="Resource identifier",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.resource_parent_name = AAZStrArg(
            options=["--resource-parent-name"],
            help="Resource parent identifier",
            required=True,
            id_part="name",
        )
        _args_schema.resource_parent_type = AAZStrArg(
            options=["--resource-parent-type"],
            help="Resource parent type",
            required=True,
            id_part="type",
        )
        _args_schema.resource_type = AAZStrArg(
            options=["--resource-type"],
            help="Resource type",
            required=True,
            id_part="child_type_1",
        )

        # define Arg Group "ConfigurationAssignment"

        _args_schema = cls._args_schema
        _args_schema.location = AAZResourceLocationArg(
            arg_group="ConfigurationAssignment",
            help="Location of the resource",
            nullable=True,
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.maintenance_configuration_id = AAZStrArg(
            options=["--maintenance-configuration-id"],
            arg_group="Properties",
            help="The maintenance configuration Id",
            nullable=True,
        )
        _args_schema.resource_id = AAZStrArg(
            options=["--resource-id"],
            arg_group="Properties",
            help="The unique resourceId",
            nullable=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ConfigurationAssignmentsGetParent(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        self.ConfigurationAssignmentsCreateOrUpdateParent(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ConfigurationAssignmentsGetParent(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{providerName}/{resourceParentType}/{resourceParentName}/{resourceType}/{resourceName}/providers/Microsoft.Maintenance/configurationAssignments/{configurationAssignmentName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "configurationAssignmentName", self.ctx.args.configuration_assignment_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "providerName", self.ctx.args.provider_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceName", self.ctx.args.resource_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceParentName", self.ctx.args.resource_parent_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceParentType", self.ctx.args.resource_parent_type,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceType", self.ctx.args.resource_type,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-07-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _build_schema_configuration_assignment_read(cls._schema_on_200)

            return cls._schema_on_200

    class ConfigurationAssignmentsCreateOrUpdateParent(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{providerName}/{resourceParentType}/{resourceParentName}/{resourceType}/{resourceName}/providers/Microsoft.Maintenance/configurationAssignments/{configurationAssignmentName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "configurationAssignmentName", self.ctx.args.configuration_assignment_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "providerName", self.ctx.args.provider_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceName", self.ctx.args.resource_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceParentName", self.ctx.args.resource_parent_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceParentType", self.ctx.args.resource_parent_type,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceType", self.ctx.args.resource_type,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-07-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _build_schema_configuration_assignment_read(cls._schema_on_200)

            return cls._schema_on_200

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("location", AAZStrType, ".location")
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("maintenanceConfigurationId", AAZStrType, ".maintenance_configuration_id")
                properties.set_prop("resourceId", AAZStrType, ".resource_id")

            return _instance_value


_schema_configuration_assignment_read = None


def _build_schema_configuration_assignment_read(_schema):
    global _schema_configuration_assignment_read
    if _schema_configuration_assignment_read is not None:
        _schema.id = _schema_configuration_assignment_read.id
        _schema.location = _schema_configuration_assignment_read.location
        _schema.name = _schema_configuration_assignment_read.name
        _schema.properties = _schema_configuration_assignment_read.properties
        _schema.system_data = _schema_configuration_assignment_read.system_data
        _schema.type = _schema_configuration_assignment_read.type
        return

    _schema_configuration_assignment_read = AAZObjectType()

    configuration_assignment_read = _schema_configuration_assignment_read
    configuration_assignment_read.id = AAZStrType(
        flags={"read_only": True},
    )
    configuration_assignment_read.location = AAZStrType()
    configuration_assignment_read.name = AAZStrType(
        flags={"read_only": True},
    )
    configuration_assignment_read.properties = AAZObjectType(
        flags={"client_flatten": True},
    )
    configuration_assignment_read.system_data = AAZObjectType(
        serialized_name="systemData",
        flags={"read_only": True},
    )
    configuration_assignment_read.type = AAZStrType(
        flags={"read_only": True},
    )

    properties = _schema_configuration_assignment_read.properties
    properties.maintenance_configuration_id = AAZStrType(
        serialized_name="maintenanceConfigurationId",
    )
    properties.resource_id = AAZStrType(
        serialized_name="resourceId",
    )

    system_data = _schema_configuration_assignment_read.system_data
    system_data.created_at = AAZStrType(
        serialized_name="createdAt",
    )
    system_data.created_by = AAZStrType(
        serialized_name="createdBy",
    )
    system_data.created_by_type = AAZStrType(
        serialized_name="createdByType",
    )
    system_data.last_modified_at = AAZStrType(
        serialized_name="lastModifiedAt",
    )
    system_data.last_modified_by = AAZStrType(
        serialized_name="lastModifiedBy",
    )
    system_data.last_modified_by_type = AAZStrType(
        serialized_name="lastModifiedByType",
    )

    _schema.id = _schema_configuration_assignment_read.id
    _schema.location = _schema_configuration_assignment_read.location
    _schema.name = _schema_configuration_assignment_read.name
    _schema.properties = _schema_configuration_assignment_read.properties
    _schema.system_data = _schema_configuration_assignment_read.system_data
    _schema.type = _schema_configuration_assignment_read.type


__all__ = ["UpdateParent"]
