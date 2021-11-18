#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.
# GENERATED FILE - DO NOT EDIT - MANUAL CHANGES WILL BE OVERWRITTEN


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_certificates_management_association_facts
short_description: Fetches details about one or multiple Association resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Association resources in Oracle Cloud Infrastructure
    - Lists all associations that match the query parameters.
      Optionally, you can use the parameter `FilterByAssociationIdQueryParam` to limit the result set to a single item that matches the specified association.
    - If I(association_id) is specified, the details of a single Association will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    association_id:
        description:
            - The OCID of an association between a certificate-related resource and another Oracle Cloud Infrastructure resource.
            - Required to get a specific association.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - A filter that returns only resources that match the given compartment OCID.
        type: str
    certificates_resource_id:
        description:
            - A filter that returns only resources that match the given OCID of a certificate-related resource.
        type: str
    associated_resource_id:
        description:
            - A filter that returns only resources that match the given OCID of an associated Oracle Cloud Infrastructure resource.
        type: str
    name:
        description:
            - A filter that returns only resources that match the specified name.
        type: str
    sort_by:
        description:
            - The field to sort by. You can specify only one sort order. The default order for `TIMECREATED` is descending.
              The default order for `NAME` is ascending.
        type: str
        choices:
            - "NAME"
            - "TIMECREATED"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    association_type:
        description:
            - Type of associations to list. If the parameter is set to null, the service lists all types of associations.
        type: str
        choices:
            - "CERTIFICATE"
            - "CERTIFICATE_AUTHORITY"
            - "CA_BUNDLE"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List associations
  oci_certificates_management_association_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific association
  oci_certificates_management_association_facts:
    association_id: "ocid1.association.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
associations:
    description:
        - List of Association resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the association.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - "A user-friendly name generated by the service for the association, expressed in a format that follows the pattern:
                  [certificatesResourceEntityType]-[associatedResourceEntityType]-UUID."
            returned: on success
            type: str
            sample: name_example
        time_created:
            description:
                - "A property indicating when the association was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                  Example: `2019-04-03T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2019-04-03T21:10:29.600Z"
        lifecycle_state:
            description:
                - The current lifecycle state of the association.
            returned: on success
            type: str
            sample: CREATING
        certificates_resource_id:
            description:
                - The OCID of the certificate-related resource associated with another Oracle Cloud Infrastructure resource.
            returned: on success
            type: str
            sample: "ocid1.certificatesresource.oc1..xxxxxxEXAMPLExxxxxx"
        associated_resource_id:
            description:
                - The OCID of the associated resource.
            returned: on success
            type: str
            sample: "ocid1.associatedresource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The compartment OCID of the association, which is strongly tied to the compartment OCID of the certificate-related resource.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        association_type:
            description:
                - Type of the association.
            returned: on success
            type: str
            sample: CERTIFICATE
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "time_created": "2019-04-03T21:10:29.600Z",
        "lifecycle_state": "CREATING",
        "certificates_resource_id": "ocid1.certificatesresource.oc1..xxxxxxEXAMPLExxxxxx",
        "associated_resource_id": "ocid1.associatedresource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "association_type": "CERTIFICATE"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.certificates_management import CertificatesManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AssociationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "association_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_association,
            association_id=self.module.params.get("association_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "certificates_resource_id",
            "associated_resource_id",
            "association_id",
            "name",
            "sort_by",
            "sort_order",
            "association_type",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_associations, **optional_kwargs
        )


AssociationFactsHelperCustom = get_custom_class("AssociationFactsHelperCustom")


class ResourceFactsHelper(AssociationFactsHelperCustom, AssociationFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            association_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            certificates_resource_id=dict(type="str"),
            associated_resource_id=dict(type="str"),
            name=dict(type="str"),
            sort_by=dict(type="str", choices=["NAME", "TIMECREATED"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            association_type=dict(
                type="str",
                choices=["CERTIFICATE", "CERTIFICATE_AUTHORITY", "CA_BUNDLE"],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="association",
        service_client_class=CertificatesManagementClient,
        namespace="certificates_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(associations=result)


if __name__ == "__main__":
    main()
