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
module: oci_usage_proxy_redeemable_user_facts
short_description: Fetches details about one or multiple RedeemableUser resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple RedeemableUser resources in Oracle Cloud Infrastructure
    - Provides emailids of redeemable users for the given subscriptionId
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    tenancy_id:
        description:
            - The OCID of the tenancy.
        type: str
        required: true
    subscription_id:
        description:
            - The subscriptionId for which rewards information is requested for.
        type: str
        required: true
    sort_order:
        description:
            - The sort order to use, can be ascending (ASC) or descending (DESC).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by, supports one sort Order.
        type: str
        choices:
            - "TIMECREATED"
            - "TIMESTART"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List redeemable_users
  oci_usage_proxy_redeemable_user_facts:
    tenancy_id: "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx"
    subscription_id: "ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
redeemable_users:
    description:
        - List of RedeemableUser resources
    returned: on success
    type: complex
    contains:
        email_id:
            description:
                - The email Id of Redeemable User.
            returned: on success
            type: str
            sample: "ocid1.email.oc1..xxxxxxEXAMPLExxxxxx"
    sample: [{
        "email_id": "ocid1.email.oc1..xxxxxxEXAMPLExxxxxx"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.usage import RewardsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RedeemableUserFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "tenancy_id",
            "subscription_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_redeemable_users,
            tenancy_id=self.module.params.get("tenancy_id"),
            subscription_id=self.module.params.get("subscription_id"),
            **optional_kwargs
        )


RedeemableUserFactsHelperCustom = get_custom_class("RedeemableUserFactsHelperCustom")


class ResourceFactsHelper(
    RedeemableUserFactsHelperCustom, RedeemableUserFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            tenancy_id=dict(type="str", required=True),
            subscription_id=dict(type="str", required=True),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["TIMECREATED", "TIMESTART"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="redeemable_user",
        service_client_class=RewardsClient,
        namespace="usage",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(redeemable_users=result)


if __name__ == "__main__":
    main()
