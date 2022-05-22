# ------------------------------------------------------------------------------------------
#  Copyright (c) Natsuneko. All rights reserved.
#  Licensed under the MIT License. See LICENSE in the project root for license information.
# ------------------------------------------------------------------------------------------

from __future__ import annotations

from bpy import ops
from bpy.types import Context, Object

from .properties import FbxBatchExportProperties


class OperationWrapper:

    @staticmethod
    def export_fbx(context: Context, filepath: str, objects: list[Object], props: FbxBatchExportProperties) -> None:
        override = context.copy()
        override["selected_objects"] = objects

        ops.export_scene.fbx(
            override,
            filepath=filepath,
            check_existing=True,
            filter_glob="*.fbx",
            use_selection=True,
            use_active_collection=False,
            global_scale=1.0,
            apply_unit_scale=props.apply_unit_scale,
            apply_scale_options=props.apply_scale_options,
            bake_space_transform=props.bake_space_transform,
            object_types={"ARMATURE", "MESH", "OTHER"},
            use_mesh_modifiers=props.use_mesh_modifiers,
            use_mesh_modifiers_render=False,
            mesh_smooth_type=props.mesh_smooth_type,
            use_subsurf=props.use_subsurf,
            use_mesh_edges=props.use_mesh_edges,
            use_tspace=props.use_tangent_space,
            use_custom_props=False,
            add_leaf_bones=props.add_leaf_bones,
            primary_bone_axis=props.primary_bone_axis,
            secondary_bone_axis=props.secondary_bone_axis,
            use_armature_deform_only=props.use_armature_deform_only,
            armature_nodetype=props.armature_nodetype,
            bake_anim=props.bake_animation,
            bake_anim_use_all_bones=props.bake_anim_use_all_bones,
            bake_anim_use_nla_strips=props.bake_anim_use_nla_strips,
            bake_anim_use_all_actions=props.bake_anim_use_all_actions,
            bake_anim_force_startend_keying=props.bake_anim_force_startend_keying,
            bake_anim_step=props.bake_anim_step,
            bake_anim_simplify_factor=props.bake_anim_simplify_factor,
            path_mode="AUTO",
            embed_textures=False,
            batch_mode="OFF",
            use_metadata=True,
            axis_forward=props.axis_forward,
            axis_up=props.axis_up,
        )
