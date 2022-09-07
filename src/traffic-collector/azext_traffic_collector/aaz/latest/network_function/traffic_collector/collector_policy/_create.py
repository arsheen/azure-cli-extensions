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
    "network-function traffic-collector collector-policy create",
)
class Create(AAZCommand):
    """Create a Collector Policy

    :example: Create a new collector policy
        az network-function traffic-collector collector-policy create --resource-group rg1 --traffic-collector-name atc1 --name cp1 --location eastus --ingestion-policy {ingestion-sources:[{resource-id:/subscriptions/<subscription_id>/resourceGroups/<resource_group>/providers/Microsoft.Network/expressRouteCircuits/<cp_name>,source-type:Resource}],ingestion-type:IPFIX}
    """

    _aaz_info = {
        "version": "2022-08-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.networkfunction/azuretrafficcollectors/{}/collectorpolicies/{}", "2022-08-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.traffic_collector_name = AAZStrArg(
            options=["-t", "--traffic-collector-name"],
            help="Azure Traffic Collector name",
            required=True,
            id_part="name",
        )
        _args_schema.collector_policy_name = AAZStrArg(
            options=["-n", "--name", "--collector-policy-name"],
            help="Collector Policy Name",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Parameters"

        _args_schema = cls._args_schema
        _args_schema.location = AAZResourceLocationArg(
            arg_group="Parameters",
            help="Resource location.",
            required=True,
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Parameters",
            help="Resource tags.",
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.emission_policies = AAZListArg(
            options=["--emission-policies"],
            arg_group="Properties",
            help="Emission policies.",
        )
        _args_schema.ingestion_policy = AAZObjectArg(
            options=["--ingestion-policy"],
            arg_group="Properties",
            help="Ingestion policies.",
        )

        emission_policies = cls._args_schema.emission_policies
        emission_policies.Element = AAZObjectArg()

        _element = cls._args_schema.emission_policies.Element
        _element.emission_destinations = AAZListArg(
            options=["emission-destinations"],
            help="Emission policy destinations.",
        )
        _element.emission_type = AAZStrArg(
            options=["emission-type"],
            help="Emission format type.",
            enum={"IPFIX": "IPFIX"},
        )

        emission_destinations = cls._args_schema.emission_policies.Element.emission_destinations
        emission_destinations.Element = AAZObjectArg()

        _element = cls._args_schema.emission_policies.Element.emission_destinations.Element
        _element.destination_type = AAZStrArg(
            options=["destination-type"],
            help="Emission destination type.",
            enum={"AzureMonitor": "AzureMonitor"},
        )

        ingestion_policy = cls._args_schema.ingestion_policy
        ingestion_policy.ingestion_sources = AAZListArg(
            options=["ingestion-sources"],
            help="Ingestion Sources.",
        )
        ingestion_policy.ingestion_type = AAZStrArg(
            options=["ingestion-type"],
            help="The ingestion type.",
            enum={"IPFIX": "IPFIX"},
        )

        ingestion_sources = cls._args_schema.ingestion_policy.ingestion_sources
        ingestion_sources.Element = AAZObjectArg()

        _element = cls._args_schema.ingestion_policy.ingestion_sources.Element
        _element.resource_id = AAZStrArg(
            options=["resource-id"],
            help="Resource ID.",
        )
        _element.source_type = AAZStrArg(
            options=["source-type"],
            help="Ingestion source type.",
            enum={"Resource": "Resource"},
        )
        return cls._args_schema

    def _execute_operations(self):
        yield self.CollectorPoliciesCreateOrUpdate(ctx=self.ctx)()

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class CollectorPoliciesCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkFunction/azureTrafficCollectors/{azureTrafficCollectorName}/collectorPolicies/{collectorPolicyName}",
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
                    "azureTrafficCollectorName", self.ctx.args.traffic_collector_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "collectorPolicyName", self.ctx.args.collector_policy_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
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
                    "api-version", "2022-08-01",
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
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("location", AAZStrType, ".location", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("emissionPolicies", AAZListType, ".emission_policies")
                properties.set_prop("ingestionPolicy", AAZObjectType, ".ingestion_policy")

            emission_policies = _builder.get(".properties.emissionPolicies")
            if emission_policies is not None:
                emission_policies.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.emissionPolicies[]")
            if _elements is not None:
                _elements.set_prop("emissionDestinations", AAZListType, ".emission_destinations")
                _elements.set_prop("emissionType", AAZStrType, ".emission_type")

            emission_destinations = _builder.get(".properties.emissionPolicies[].emissionDestinations")
            if emission_destinations is not None:
                emission_destinations.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.emissionPolicies[].emissionDestinations[]")
            if _elements is not None:
                _elements.set_prop("destinationType", AAZStrType, ".destination_type")

            ingestion_policy = _builder.get(".properties.ingestionPolicy")
            if ingestion_policy is not None:
                ingestion_policy.set_prop("ingestionSources", AAZListType, ".ingestion_sources")
                ingestion_policy.set_prop("ingestionType", AAZStrType, ".ingestion_type")

            ingestion_sources = _builder.get(".properties.ingestionPolicy.ingestionSources")
            if ingestion_sources is not None:
                ingestion_sources.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.ingestionPolicy.ingestionSources[]")
            if _elements is not None:
                _elements.set_prop("resourceId", AAZStrType, ".resource_id")
                _elements.set_prop("sourceType", AAZStrType, ".source_type")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.etag = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200_201.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200_201.tags = AAZDictType()
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.emission_policies = AAZListType(
                serialized_name="emissionPolicies",
            )
            properties.ingestion_policy = AAZObjectType(
                serialized_name="ingestionPolicy",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )

            emission_policies = cls._schema_on_200_201.properties.emission_policies
            emission_policies.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.emission_policies.Element
            _element.emission_destinations = AAZListType(
                serialized_name="emissionDestinations",
            )
            _element.emission_type = AAZStrType(
                serialized_name="emissionType",
            )

            emission_destinations = cls._schema_on_200_201.properties.emission_policies.Element.emission_destinations
            emission_destinations.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.emission_policies.Element.emission_destinations.Element
            _element.destination_type = AAZStrType(
                serialized_name="destinationType",
            )

            ingestion_policy = cls._schema_on_200_201.properties.ingestion_policy
            ingestion_policy.ingestion_sources = AAZListType(
                serialized_name="ingestionSources",
            )
            ingestion_policy.ingestion_type = AAZStrType(
                serialized_name="ingestionType",
            )

            ingestion_sources = cls._schema_on_200_201.properties.ingestion_policy.ingestion_sources
            ingestion_sources.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.ingestion_policy.ingestion_sources.Element
            _element.resource_id = AAZStrType(
                serialized_name="resourceId",
            )
            _element.source_type = AAZStrType(
                serialized_name="sourceType",
            )

            system_data = cls._schema_on_200_201.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
                flags={"read_only": True},
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
                flags={"read_only": True},
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
                flags={"read_only": True},
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
                flags={"read_only": True},
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
                flags={"read_only": True},
            )

            tags = cls._schema_on_200_201.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200_201


__all__ = ["Create"]
