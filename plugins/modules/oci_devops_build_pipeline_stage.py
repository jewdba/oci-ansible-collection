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
module: oci_devops_build_pipeline_stage
short_description: Manage a BuildPipelineStage resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a BuildPipelineStage resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Stage.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    display_name:
        description:
            - Stage identifier which can be renamed and is not necessarily unique
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - Optional description about the Stage
            - This parameter is updatable.
        type: str
    build_pipeline_stage_type:
        description:
            - List of stage types. It includes 'Wait stage', 'Build Stage', 'Deliver Artifact Stage' and
              'Trigger Deployment Stage'.
            - Required for create using I(state=present), update using I(state=present) with build_pipeline_stage_id present.
        type: str
        choices:
            - "DELIVER_ARTIFACT"
            - "TRIGGER_DEPLOYMENT_PIPELINE"
            - "WAIT"
            - "BUILD"
    build_pipeline_id:
        description:
            - buildPipeline Identifier
            - Required for create using I(state=present).
        type: str
    build_pipeline_stage_predecessor_collection:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
            - Applicable when build_pipeline_stage_type is one of ['DELIVER_ARTIFACT', 'BUILD', 'TRIGGER_DEPLOYMENT_PIPELINE', 'WAIT']
        type: dict
        suboptions:
            items:
                description:
                    - A list of BuildPipelineStagePredecessors for a stage.
                    - Required when build_pipeline_stage_type is 'DELIVER_ARTIFACT'
                type: list
                elements: dict
                required: true
                suboptions:
                    id:
                        description:
                            - The id of the predecessor stage. If a stages is the first stage in the pipeline, then the id is the pipeline's id.
                            - Required when build_pipeline_stage_type is 'DELIVER_ARTIFACT'
                        type: str
                        required: true
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace. See L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    deliver_artifact_collection:
        description:
            - ""
            - This parameter is updatable.
            - Applicable when build_pipeline_stage_type is 'DELIVER_ARTIFACT'
            - Required when build_pipeline_stage_type is 'DELIVER_ARTIFACT'
        type: dict
        suboptions:
            items:
                description:
                    - Collection of Artifacts that were generated in the Build Stage and need to be pushed to the artifactory stores. In case of UPDATE
                      operation, replaces existing artifacts list. Merging with existing artifacts is not supported.
                    - Required when build_pipeline_stage_type is 'DELIVER_ARTIFACT'
                type: list
                elements: dict
                required: true
                suboptions:
                    artifact_name:
                        description:
                            - Name of the artifact specified in the build_spec.yml file.
                            - Required when build_pipeline_stage_type is 'DELIVER_ARTIFACT'
                        type: str
                        required: true
                    artifact_id:
                        description:
                            - Artifact Identifier which contains the Artifact Definition.
                            - Required when build_pipeline_stage_type is 'DELIVER_ARTIFACT'
                        type: str
                        required: true
    deploy_pipeline_id:
        description:
            - A target Pipeline ocid that will be run in this stage.
            - This parameter is updatable.
            - Applicable when build_pipeline_stage_type is 'TRIGGER_DEPLOYMENT_PIPELINE'
            - Required when build_pipeline_stage_type is 'TRIGGER_DEPLOYMENT_PIPELINE'
        type: str
    is_pass_all_parameters_enabled:
        description:
            - A boolean flag specifies whether the parameters should be passed during the deployment trigger.
            - This parameter is updatable.
            - Applicable when build_pipeline_stage_type is 'TRIGGER_DEPLOYMENT_PIPELINE'
            - Required when build_pipeline_stage_type is 'TRIGGER_DEPLOYMENT_PIPELINE'
        type: bool
    wait_criteria:
        description:
            - ""
            - This parameter is updatable.
            - Applicable when build_pipeline_stage_type is 'WAIT'
            - Required when build_pipeline_stage_type is 'WAIT'
        type: dict
        suboptions:
            wait_type:
                description:
                    - wait criteria sub type
                    - This parameter is updatable.
                type: str
                choices:
                    - "ABSOLUTE_WAIT"
                required: true
            wait_duration:
                description:
                    - The absolute wait duration.
                      Minimum waitDuration should be 5 seconds.
                      Maximum waitDuration can be up to 2 days.
                    - This parameter is updatable.
                    - Applicable when wait_type is 'ABSOLUTE_WAIT'
                type: str
    image:
        description:
            - Image name for the Build Environment
            - This parameter is updatable.
            - Applicable when build_pipeline_stage_type is 'BUILD'
            - Required when build_pipeline_stage_type is 'BUILD'
        type: str
    build_spec_file:
        description:
            - The path to the build specification file for this Environment. The default location if not specified is build_spec.yaml
            - This parameter is updatable.
            - Applicable when build_pipeline_stage_type is 'BUILD'
        type: str
    stage_execution_timeout_in_seconds:
        description:
            - Timeout for the Build Stage Execution. Value in seconds.
            - This parameter is updatable.
            - Applicable when build_pipeline_stage_type is 'BUILD'
        type: int
    build_source_collection:
        description:
            - ""
            - This parameter is updatable.
            - Applicable when build_pipeline_stage_type is 'BUILD'
            - Required when build_pipeline_stage_type is 'BUILD'
        type: dict
        suboptions:
            items:
                description:
                    - Collection of Build sources. In case of UPDATE operation, replaces existing Build sources list. Merging with existing Build Sources is not
                      supported.
                    - Required when build_pipeline_stage_type is 'BUILD'
                type: list
                elements: dict
                required: true
                suboptions:
                    name:
                        description:
                            - Name of the Build source. This must be unique within a BuildSourceCollection. The name can be used by customers to locate the
                              working directory pertinent to this repository.
                        type: str
                        required: true
                    connection_type:
                        description:
                            - The type of Source Provider.
                        type: str
                        choices:
                            - "GITHUB"
                            - "DEVOPS_CODE_REPOSITORY"
                            - "GITLAB"
                        required: true
                    repository_url:
                        description:
                            - Url for repository
                        type: str
                        required: true
                    branch:
                        description:
                            - branch name
                        type: str
                        required: true
                    connection_id:
                        description:
                            - Connection identifier pertinent to GITHUB source provider
                            - Required when connection_type is one of ['GITHUB', 'GITLAB']
                        type: str
                    repository_id:
                        description:
                            - The Devops Code Repository Id
                            - Required when connection_type is 'DEVOPS_CODE_REPOSITORY'
                        type: str
    primary_build_source:
        description:
            - Name of the BuildSource in which the build_spec.yml file need to be located. If not specified, the 1st entry in the BuildSource collection will be
              chosen as Primary.
            - This parameter is updatable.
            - Applicable when build_pipeline_stage_type is 'BUILD'
        type: str
    build_pipeline_stage_id:
        description:
            - Unique stage identifier.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the BuildPipelineStage.
            - Use I(state=present) to create or update a BuildPipelineStage.
            - Use I(state=absent) to delete a BuildPipelineStage.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create build_pipeline_stage
  oci_devops_build_pipeline_stage:
    build_pipeline_stage_type: BUILD
    build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"
    build_pipeline_stage_predecessor_collection:
      items:
      - id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    image: image_example
    build_source_collection:
      items:
      - name: name_example
        connection_type: GITHUB
        repository_url: repository_url_example
        branch: branch_example

- name: Update build_pipeline_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_devops_build_pipeline_stage:
    display_name: display_name_example
    description: description_example
    build_pipeline_stage_type: BUILD
    build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"
    build_pipeline_stage_predecessor_collection:
      items:
      - id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    deliver_artifact_collection:
      items:
      - artifact_name: artifact_name_example
        artifact_id: "ocid1.artifact.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
    is_pass_all_parameters_enabled: true
    wait_criteria:
      wait_type: ABSOLUTE_WAIT
    image: image_example
    build_spec_file: build_spec_file_example
    stage_execution_timeout_in_seconds: 56
    build_source_collection:
      items:
      - name: name_example
        connection_type: GITHUB
        repository_url: repository_url_example
        branch: branch_example
    primary_build_source: primary_build_source_example

- name: Update build_pipeline_stage
  oci_devops_build_pipeline_stage:
    display_name: display_name_example
    description: description_example
    build_pipeline_stage_type: BUILD
    build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"
    build_pipeline_stage_predecessor_collection:
      items:
      - id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    image: image_example
    build_source_collection:
      items:
      - name: name_example
        connection_type: GITHUB
        repository_url: repository_url_example
        branch: branch_example
    build_pipeline_stage_id: "ocid1.buildpipelinestage.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete build_pipeline_stage
  oci_devops_build_pipeline_stage:
    build_pipeline_stage_id: "ocid1.buildpipelinestage.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete build_pipeline_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_devops_build_pipeline_stage:
    display_name: display_name_example
    state: absent

"""

RETURN = """
build_pipeline_stage:
    description:
        - Details of the BuildPipelineStage resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier that is immutable on creation
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Stage identifier which can be renamed and is not necessarily unique
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Optional description about the BuildStage
            returned: on success
            type: str
            sample: description_example
        project_id:
            description:
                - Project Identifier
            returned: on success
            type: str
            sample: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
        build_pipeline_id:
            description:
                - Build Pipeline Identifier
            returned: on success
            type: str
            sample: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - Compartment Identifier
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        build_pipeline_stage_type:
            description:
                - List of stage types. It includes 'Wait stage', 'Build Stage', 'Deliver Artifact Stage'
                  and 'Trigger Deployment Stage'.
            returned: on success
            type: str
            sample: WAIT
        time_created:
            description:
                - The time at which the Stage was created. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time at which the Stage was updated. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the Stage.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        build_pipeline_stage_predecessor_collection:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                items:
                    description:
                        - A list of BuildPipelineStagePredecessors for a stage.
                    returned: on success
                    type: complex
                    contains:
                        id:
                            description:
                                - The id of the predecessor stage. If a stages is the first stage in the pipeline, then the id is the pipeline's id.
                            returned: on success
                            type: str
                            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace. See L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces. See L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\":
                  \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
        image:
            description:
                - Image name for the Build Environment
            returned: on success
            type: str
            sample: OL7_X86_64_STANDARD_10
        build_spec_file:
            description:
                - The path to the build specification file for this Environment. The default location if not specified is build_spec.yaml
            returned: on success
            type: str
            sample: build_spec_file_example
        stage_execution_timeout_in_seconds:
            description:
                - Timeout for the Build Stage Execution. Value in seconds.
            returned: on success
            type: int
            sample: 56
        build_source_collection:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                items:
                    description:
                        - Collection of Build sources. In case of UPDATE operation, replaces existing Build sources list. Merging with existing Build Sources is
                          not supported.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - Name of the Build source. This must be unique within a BuildSourceCollection. The name can be used by customers to locate the
                                  working directory pertinent to this repository.
                            returned: on success
                            type: str
                            sample: name_example
                        connection_type:
                            description:
                                - The type of Source Provider.
                            returned: on success
                            type: str
                            sample: GITHUB
                        repository_url:
                            description:
                                - Url for repository
                            returned: on success
                            type: str
                            sample: repository_url_example
                        branch:
                            description:
                                - branch name
                            returned: on success
                            type: str
                            sample: branch_example
                        repository_id:
                            description:
                                - The Devops Code Repository Id
                            returned: on success
                            type: str
                            sample: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"
                        connection_id:
                            description:
                                - Connection identifier pertinent to GITHUB source provider
                            returned: on success
                            type: str
                            sample: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"
        primary_build_source:
            description:
                - Name of the BuildSource in which the build_spec.yml file need to be located. If not specified, the 1st entry in the BuildSource collection
                  will be chosen as Primary.
            returned: on success
            type: str
            sample: primary_build_source_example
        deliver_artifact_collection:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                items:
                    description:
                        - Collection of Artifacts that were generated in the Build Stage and need to be pushed to the artifactory stores. In case of UPDATE
                          operation, replaces existing artifacts list. Merging with existing artifacts is not supported.
                    returned: on success
                    type: complex
                    contains:
                        artifact_name:
                            description:
                                - Name of the artifact specified in the build_spec.yml file.
                            returned: on success
                            type: str
                            sample: artifact_name_example
                        artifact_id:
                            description:
                                - Artifact Identifier which contains the Artifact Definition.
                            returned: on success
                            type: str
                            sample: "ocid1.artifact.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_pipeline_id:
            description:
                - A target Pipeline ocid that will be run in this stage.
            returned: on success
            type: str
            sample: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
        is_pass_all_parameters_enabled:
            description:
                - A boolean flag specifies whether the parameters should be passed during the deployment trigger.
            returned: on success
            type: bool
            sample: true
        wait_criteria:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                wait_type:
                    description:
                        - Wait criteria type.
                    returned: on success
                    type: str
                    sample: ABSOLUTE_WAIT
                wait_duration:
                    description:
                        - The absolute wait duration. An ISO 8601 formatted duration string. Minimum waitDuration should be 5 seconds. Maximum waitDuration can
                          be up to 2 days.
                    returned: on success
                    type: str
                    sample: PT10M5S
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "project_id": "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx",
        "build_pipeline_id": "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "build_pipeline_stage_type": "WAIT",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "build_pipeline_stage_predecessor_collection": {
            "items": [{
                "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
            }]
        },
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "image": "OL7_X86_64_STANDARD_10",
        "build_spec_file": "build_spec_file_example",
        "stage_execution_timeout_in_seconds": 56,
        "build_source_collection": {
            "items": [{
                "name": "name_example",
                "connection_type": "GITHUB",
                "repository_url": "repository_url_example",
                "branch": "branch_example",
                "repository_id": "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx",
                "connection_id": "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"
            }]
        },
        "primary_build_source": "primary_build_source_example",
        "deliver_artifact_collection": {
            "items": [{
                "artifact_name": "artifact_name_example",
                "artifact_id": "ocid1.artifact.oc1..xxxxxxEXAMPLExxxxxx"
            }]
        },
        "deploy_pipeline_id": "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx",
        "is_pass_all_parameters_enabled": true,
        "wait_criteria": {
            "wait_type": "ABSOLUTE_WAIT",
            "wait_duration": "PT10M5S"
        }
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.devops import DevopsClient
    from oci.devops.models import CreateBuildPipelineStageDetails
    from oci.devops.models import UpdateBuildPipelineStageDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BuildPipelineStageHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "build_pipeline_stage_id"

    def get_module_resource_id(self):
        return self.module.params.get("build_pipeline_stage_id")

    def get_get_fn(self):
        return self.client.get_build_pipeline_stage

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_build_pipeline_stage,
            build_pipeline_stage_id=self.module.params.get("build_pipeline_stage_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["build_pipeline_id", "display_name"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_build_pipeline_stages, **kwargs
        )

    def get_create_model_class(self):
        return CreateBuildPipelineStageDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_build_pipeline_stage,
            call_fn_args=(),
            call_fn_kwargs=dict(create_build_pipeline_stage_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateBuildPipelineStageDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_build_pipeline_stage,
            call_fn_args=(),
            call_fn_kwargs=dict(
                build_pipeline_stage_id=self.module.params.get(
                    "build_pipeline_stage_id"
                ),
                update_build_pipeline_stage_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_build_pipeline_stage,
            call_fn_args=(),
            call_fn_kwargs=dict(
                build_pipeline_stage_id=self.module.params.get(
                    "build_pipeline_stage_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


BuildPipelineStageHelperCustom = get_custom_class("BuildPipelineStageHelperCustom")


class ResourceHelper(BuildPipelineStageHelperCustom, BuildPipelineStageHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            build_pipeline_stage_type=dict(
                type="str",
                choices=[
                    "DELIVER_ARTIFACT",
                    "TRIGGER_DEPLOYMENT_PIPELINE",
                    "WAIT",
                    "BUILD",
                ],
            ),
            build_pipeline_id=dict(type="str"),
            build_pipeline_stage_predecessor_collection=dict(
                type="dict",
                options=dict(
                    items=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(id=dict(type="str", required=True)),
                    )
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            deliver_artifact_collection=dict(
                type="dict",
                options=dict(
                    items=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(
                            artifact_name=dict(type="str", required=True),
                            artifact_id=dict(type="str", required=True),
                        ),
                    )
                ),
            ),
            deploy_pipeline_id=dict(type="str"),
            is_pass_all_parameters_enabled=dict(type="bool", no_log=True),
            wait_criteria=dict(
                type="dict",
                options=dict(
                    wait_type=dict(
                        type="str", required=True, choices=["ABSOLUTE_WAIT"]
                    ),
                    wait_duration=dict(type="str"),
                ),
            ),
            image=dict(type="str"),
            build_spec_file=dict(type="str"),
            stage_execution_timeout_in_seconds=dict(type="int"),
            build_source_collection=dict(
                type="dict",
                options=dict(
                    items=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(
                            name=dict(type="str", required=True),
                            connection_type=dict(
                                type="str",
                                required=True,
                                choices=["GITHUB", "DEVOPS_CODE_REPOSITORY", "GITLAB"],
                            ),
                            repository_url=dict(type="str", required=True),
                            branch=dict(type="str", required=True),
                            connection_id=dict(type="str"),
                            repository_id=dict(type="str"),
                        ),
                    )
                ),
            ),
            primary_build_source=dict(type="str"),
            build_pipeline_stage_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="build_pipeline_stage",
        service_client_class=DevopsClient,
        namespace="devops",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
