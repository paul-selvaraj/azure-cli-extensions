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
    "maintenance assignment delete-parent",
    is_preview=True,
    confirmation="Are you sure you want to perform this operation?",
)
class DeleteParent(AAZCommand):
    """Delete configuration for resource.

    :example: ConfigurationAssignments_DeleteParent
        az maintenance assignment delete-parent --name "workervmConfiguration" --provider-name "Microsoft.Compute" --resource-group "examplerg" --resource-name "smdvm1" --resource-parent-name "smdtest1" --resource-parent-type "virtualMachineScaleSets" --resource-type "virtualMachines"
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
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ConfigurationAssignmentsDeleteParent(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ConfigurationAssignmentsDeleteParent(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)
            if session.http_response.status_code in [204]:
                return self.on_204(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{providerName}/{resourceParentType}/{resourceParentName}/{resourceType}/{resourceName}/providers/Microsoft.Maintenance/configurationAssignments/{configurationAssignmentName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "DELETE"

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

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.location = AAZStrType()
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.maintenance_configuration_id = AAZStrType(
                serialized_name="maintenanceConfigurationId",
            )
            properties.resource_id = AAZStrType(
                serialized_name="resourceId",
            )

            system_data = cls._schema_on_200.system_data
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

            return cls._schema_on_200

        def on_204(self, session):
            pass


__all__ = ["DeleteParent"]
