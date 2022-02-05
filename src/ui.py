# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  Copyright (c) Natsuneko. All rights reserved.
#  Licensed under the License Zero Parity 7.0.0 (see LICENSE-PARITY file) and MIT (contributions, see LICENSE-MIT file) with exception License Zero Patron 1.0.0 (see LICENSE-PATRON file)
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from bpy.types import Panel

from .operator import FbxBatchExportOperator
from .properties import FbxBatchExportProperties


class FbxBatchExportUI(Panel):
    bl_idname = "UI_PT_FbxBatchExport"
    bl_label = "FBX Batch Export Properties"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "FBX Batch Export"

    def draw(self, context):
        layout = self.layout

        column = layout.column()
        column.use_property_split = True

        props: FbxBatchExportProperties = context.scene.FbxBatchExportProperties

        column.label(text="Generic")
        column.prop(props, "export_path")

        column.separator()
        column.label(text="Export Settings")
        column.prop(props, "apply_unit_scale")
        column.prop(props, "apply_scale_options")
        column.prop(props, "bake_space_transform")
        column.prop(props, "use_mesh_modifiers")
        column.prop(props, "mesh_smooth_type")
        column.prop(props, "use_subsurf")
        column.prop(props, "use_mesh_edges")
        column.prop(props, "use_tangent_space")
        column.prop(props, "add_leaf_bones")
        column.prop(props, "primary_bone_axis")
        column.prop(props, "secondary_bone_axis")
        column.prop(props, "use_armature_deform_only")
        column.prop(props, "bake_animation")

        col_bake_animation = column.column()
        col_bake_animation.enabled = props.bake_animation
        col_bake_animation.prop(props, "bake_anim_use_all_bones")
        col_bake_animation.prop(props, "bake_anim_use_nla_strips")
        col_bake_animation.prop(props, "bake_anim_use_all_actions")
        col_bake_animation.prop(props, "bake_anim_force_startend_keying")
        col_bake_animation.prop(props, "bake_anim_step")
        col_bake_animation.prop(props, "bake_anim_simplify_factor")

        column.prop(props, "axis_forward")
        column.prop(props, "axis_up")

        layout.operator(FbxBatchExportOperator.bl_idname, text="Generate")
