# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  Copyright (c) Natsuneko. All rights reserved.
#  Licensed under the License Zero Parity 7.0.0 (see LICENSE-PARITY file) and MIT (contributions, see LICENSE-MIT file) with exception License Zero Patron 1.0.0 (see LICENSE-PATRON file)
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from bpy.props import BoolProperty, EnumProperty, FloatProperty, StringProperty
from bpy.types import PropertyGroup


class FbxBatchExportProperties(PropertyGroup):
    def scale_options(self, _):
        return [
            ("FBX_SCALE_NONE", "None",
             "All Local, Apply custom scaling and units scaling to each object transformation, FBX scale remains at 1.0."),
            ("FBX_SCALE_UNITS", "Units",
             "FBX Units Scale, Apply custom scaling to each object transformation, and units scaling to FBX scale."),
            ("FBX_SCALE_CUSTOM", "Custom",
             "FBX Custom Scale, Apply custom scaling to FBX scale, and units scaling to each object transformation."),
            ("FBX_SCALE_ALL", "All", " FBX All, Apply custom scaling and units scaling to FBX scale.")
        ]

    def _mesh_smooth_type(self, _):
        return [
            ("OFF", "Normals Only", "Export only normals instead of writing edge or face smoothing data"),
            ("FACE", "Face", "Write face smoothing data"),
            ("EDGE", "Edge", "Write edge smoothing data"),
        ]

    def axis(self, _):
        return [
            ("X", "X", "X axis"),
            ("Y", "Y", "Y axis"),
            ("Z", "Z", "Z axis"),
            ("-X", "-X", "-X axis"),
            ("-Y", "-Y", "-Y axis"),
            ("-Z", "-Z", "-Z axis"),
        ]

    def _armature_nodetype(self, _):
        return [
            ("NULL", "Null", "'Null' FBX node, similar to Blender's Empty (default)."),
            ("ROOT", "Root", "'Root' FBX node, supposed to be the root of chains of bones...."),
            ("LIMBBONE", "Limbbone", "'LimbNode' FBX node, a regular joint between two bones..."),
        ]

    # generic
    export_path: StringProperty(default="", name="Export Directory",
                                description="Export FBX files to", subtype="DIR_PATH", options={'HIDDEN'})

    # export
    apply_unit_scale: BoolProperty(default=True, name="Apply Unit Scale",
                                   description="Apply Unit, Take into account current Blender units settings (if unset, raw Blender Units values are used as-is)", options={'HIDDEN'})
    apply_scale_options: EnumProperty(default=3, items=scale_options, name="Apply Scale Options",
                                      description="Apply Scalings, How to apply custom and units scalings in generated FBX file (Blender uses FBX scale to detect units on import, but many other applications do not handle the same way)", options={'HIDDEN'})
    bake_space_transform: BoolProperty(default=False, name="Bake Space Transform",
                                       description="!EXPERIMENTAL! Apply Transform, Bake space transform into object data, avoids getting unwanted rotations to objects when target space is not aligned with Blender's space (WARNING! experimental option, use at own risks, known broken with armatures/animations)", options={'HIDDEN'})
    use_mesh_modifiers: BoolProperty(default=False, name="Apply Modifiers",
                                     description="Apply Modifiers, Apply modifiers to mesh objects (except Armature ones) - WARNING: prevents exporting shape keys", options={'HIDDEN'})
    mesh_smooth_type: BoolProperty(default=0, items=_mesh_smooth_type, name="Smoothing",
                                   description="Smoothing, Export smoothed mesh if available", options={'HIDDEN'})
    use_subsurf: BoolProperty(default=False, name="Export Subdivision Surface",
                              description=" Export the last Catmull-Rom subidivion modifier as FBX subdivision (Does not apply the modifier even if 'Apply Modifiers' is enabled)", options={'HIDDEN'})
    use_mesh_edges: BoolProperty(default=False, name="Loose Edges",
                                 description="Export loose edges (as two-vertices polygons)", options={'HIDDEN'})
    use_tangent_space: BoolProperty(default=False, name="Tangent Space",
                                    description=" Add binormal and tangent vectors, together with normal they form the tangent space (will only work correctly with tris/quads only meshes!)", options={'HIDDEN'})
    add_leaf_bones: BoolProperty(default=False, name="Add Leaf Bones",
                                 description="Append a final bone to the end of each chain to specify last bone length (use this when you intend to edit the armature from exported data)", options={'HIDDEN'})
    primary_bone_axis: EnumProperty(default=1, items=axis, name="Primary Bone Axis",
                                    description="Primary Bone Axis", options={'HIDDEN'})
    secondary_bone_axis: EnumProperty(default=0, items=axis, name="Secondary Bone Axis",
                                      description="Secondary Bone Axis", options={'HIDDEN'})
    use_armature_deform_only: BoolProperty(default=False, name="Only Deform Bones",
                                           description="Only write deforming bones (and non-deforming ones when they have deforming children)", options={'HIDDEN'})
    armature_nodetype: EnumProperty(default=0, items=_armature_nodetype, name="Armature FBXNode Type",
                                    description="FBX type of node (object) used to represent Blender's armatures (use Null one unless you experience issues with other app, other choices may no import back perfectly in Blender...)", options={'HIDDEN'})
    bake_animation: BoolProperty(default=False, name="Baked Animation",
                                 description="Export baked keyframe animation", options={'HIDDEN'})
    bake_anim_use_all_bones: BoolProperty(
        default=True, name="Bake Key All Bones", description="Force exporting at least one key of animation for all bones (needed with some target applications, like UE4)", options={'HIDDEN'})
    bake_anim_use_nla_strips: BoolProperty(
        default=False, name="NLA Strips", description="Export each non-muted NLA strip as a separated FBX's AnimStack, if any, instead of global scene animation", options={'HIDDEN'})
    bake_anim_use_all_actions: BoolProperty(default=True, name="Bake All Actions",
                                            description="Export each action as a separated FBX's AnimStack, instead of global scene animation (note that animated objects will get all actions compatible with them, others will get no animation at all)", options={'HIDDEN'})
    bake_anim_force_startend_keying: BoolProperty(default=False, name="Bake Force Start/End Keying",
                                                  description="Always add a keyframe at start and end of actions for animated channels", options={'HIDDEN'})
    bake_anim_step: FloatProperty(default=1.0, min=0.01, max=100.0, name="Sampling Rate",
                                  description=" How often to evaluate animated values (in frames)", options={'HIDDEN'})
    bake_anim_simplify_factor: FloatProperty(default=1.0, min=0.0, max=100.0, name="Simplify",
                                             description="How much to simplify baked values (0.0 to disable, the higher the more simplified)", options={'HIDDEN'})
    axis_forward: EnumProperty(default=5, items=axis, name="Axis Forward",
                               description="Axis Forward", options={'HIDDEN'})
    axis_up: EnumProperty(default=1, items=axis, name="Axis Up", description="Axis Up", options={'HIDDEN'})
