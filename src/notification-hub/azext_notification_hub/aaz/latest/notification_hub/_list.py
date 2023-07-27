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
    "notification-hub list",
    is_experimental=True,
)
class List(AAZCommand):
    """List the notification hubs associated with a namespace.

    :example: List the notification hubs
        az notification-hub list --resource-group MyResourceGroup --namespace-name my-namespace
    """

    _aaz_info = {
        "version": "2017-04-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.notificationhubs/namespaces/{}/notificationhubs", "2017-04-01"],
        ]
    }

    AZ_SUPPORT_PAGINATION = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.namespace_name = AAZStrArg(
            options=["--namespace-name"],
            help="The namespace name.",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.NotificationHubsList(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class NotificationHubsList(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NotificationHubs/namespaces/{namespaceName}/notificationHubs",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "namespaceName", self.ctx.args.namespace_name,
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
                    "api-version", "2017-04-01",
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
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.location = AAZStrType()
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.sku = AAZObjectType()
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.adm_credential = AAZObjectType(
                serialized_name="admCredential",
            )
            properties.apns_credential = AAZObjectType(
                serialized_name="apnsCredential",
            )
            properties.authorization_rules = AAZListType(
                serialized_name="authorizationRules",
            )
            properties.baidu_credential = AAZObjectType(
                serialized_name="baiduCredential",
            )
            properties.gcm_credential = AAZObjectType(
                serialized_name="gcmCredential",
            )
            properties.mpns_credential = AAZObjectType(
                serialized_name="mpnsCredential",
            )
            properties.name = AAZStrType()
            properties.registration_ttl = AAZStrType(
                serialized_name="registrationTtl",
            )
            properties.wns_credential = AAZObjectType(
                serialized_name="wnsCredential",
            )

            adm_credential = cls._schema_on_200.value.Element.properties.adm_credential
            adm_credential.properties = AAZObjectType(
                flags={"client_flatten": True},
            )

            properties = cls._schema_on_200.value.Element.properties.adm_credential.properties
            properties.auth_token_url = AAZStrType(
                serialized_name="authTokenUrl",
            )
            properties.client_id = AAZStrType(
                serialized_name="clientId",
            )
            properties.client_secret = AAZStrType(
                serialized_name="clientSecret",
            )

            apns_credential = cls._schema_on_200.value.Element.properties.apns_credential
            apns_credential.properties = AAZObjectType(
                flags={"client_flatten": True},
            )

            properties = cls._schema_on_200.value.Element.properties.apns_credential.properties
            properties.apns_certificate = AAZStrType(
                serialized_name="apnsCertificate",
            )
            properties.app_id = AAZStrType(
                serialized_name="appId",
            )
            properties.app_name = AAZStrType(
                serialized_name="appName",
            )
            properties.certificate_key = AAZStrType(
                serialized_name="certificateKey",
            )
            properties.endpoint = AAZStrType()
            properties.key_id = AAZStrType(
                serialized_name="keyId",
            )
            properties.thumbprint = AAZStrType()
            properties.token = AAZStrType()

            authorization_rules = cls._schema_on_200.value.Element.properties.authorization_rules
            authorization_rules.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.authorization_rules.Element
            _element.claim_type = AAZStrType(
                serialized_name="claimType",
                flags={"read_only": True},
            )
            _element.claim_value = AAZStrType(
                serialized_name="claimValue",
                flags={"read_only": True},
            )
            _element.created_time = AAZStrType(
                serialized_name="createdTime",
                flags={"read_only": True},
            )
            _element.key_name = AAZStrType(
                serialized_name="keyName",
                flags={"read_only": True},
            )
            _element.modified_time = AAZStrType(
                serialized_name="modifiedTime",
                flags={"read_only": True},
            )
            _element.primary_key = AAZStrType(
                serialized_name="primaryKey",
                flags={"read_only": True},
            )
            _element.revision = AAZIntType(
                flags={"read_only": True},
            )
            _element.rights = AAZListType()
            _element.secondary_key = AAZStrType(
                serialized_name="secondaryKey",
                flags={"read_only": True},
            )

            rights = cls._schema_on_200.value.Element.properties.authorization_rules.Element.rights
            rights.Element = AAZStrType()

            baidu_credential = cls._schema_on_200.value.Element.properties.baidu_credential
            baidu_credential.properties = AAZObjectType(
                flags={"client_flatten": True},
            )

            properties = cls._schema_on_200.value.Element.properties.baidu_credential.properties
            properties.baidu_api_key = AAZStrType(
                serialized_name="baiduApiKey",
            )
            properties.baidu_end_point = AAZStrType(
                serialized_name="baiduEndPoint",
            )
            properties.baidu_secret_key = AAZStrType(
                serialized_name="baiduSecretKey",
            )

            gcm_credential = cls._schema_on_200.value.Element.properties.gcm_credential
            gcm_credential.properties = AAZObjectType(
                flags={"client_flatten": True},
            )

            properties = cls._schema_on_200.value.Element.properties.gcm_credential.properties
            properties.gcm_endpoint = AAZStrType(
                serialized_name="gcmEndpoint",
            )
            properties.google_api_key = AAZStrType(
                serialized_name="googleApiKey",
            )

            mpns_credential = cls._schema_on_200.value.Element.properties.mpns_credential
            mpns_credential.properties = AAZObjectType(
                flags={"client_flatten": True},
            )

            properties = cls._schema_on_200.value.Element.properties.mpns_credential.properties
            properties.certificate_key = AAZStrType(
                serialized_name="certificateKey",
            )
            properties.mpns_certificate = AAZStrType(
                serialized_name="mpnsCertificate",
            )
            properties.thumbprint = AAZStrType()

            wns_credential = cls._schema_on_200.value.Element.properties.wns_credential
            wns_credential.properties = AAZObjectType(
                flags={"client_flatten": True},
            )

            properties = cls._schema_on_200.value.Element.properties.wns_credential.properties
            properties.package_sid = AAZStrType(
                serialized_name="packageSid",
            )
            properties.secret_key = AAZStrType(
                serialized_name="secretKey",
            )
            properties.windows_live_endpoint = AAZStrType(
                serialized_name="windowsLiveEndpoint",
            )

            sku = cls._schema_on_200.value.Element.sku
            sku.capacity = AAZIntType()
            sku.family = AAZStrType()
            sku.name = AAZStrType(
                flags={"required": True},
            )
            sku.size = AAZStrType()
            sku.tier = AAZStrType()

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""


__all__ = ["List"]
