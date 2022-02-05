# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  Copyright (c) Natsuneko. All rights reserved.
#  Licensed under the License Zero Parity 7.0.0 (see LICENSE-PARITY file) and MIT (contributions, see LICENSE-MIT file) with exception License Zero Patron 1.0.0 (see LICENSE-PATRON file)
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from __future__ import annotations

import bpy

from bpy.types import Object, Operator
from os import path

from .properties import FbxBatchExportProperties
from .utils import replace_invalid_filename_chars
from .wrapper import OperationWrapper


class FbxBatchExportOperator(Operator):
    bl_idname = "object.fbx_batch_export"
    bl_label = "FBX Batch Export Operation"

    def export_object(self, number: int, name: str, props: FbxBatchExportProperties, objects: list[Object]) -> int:
        try:
            filename = replace_invalid_filename_chars("%s.fbx" % (name))
            filepath = path.join(props.export_path, filename)

            OperationWrapper.export_fbx(context=bpy.context, filepath=filepath, objects=objects, props=props)
            return number + 1
        except RuntimeError as e:
            print(e)
            return number

    def export_objects(self, context, props: FbxBatchExportProperties):
        objects = context.selected_objects

        bpy.ops.object.mode_set(mode="OBJECT")

        for i, obj in enumerate(objects):
            objects = [obj]
            for child in bpy.data.objects:
                if child.parent == obj:
                    objects.append(child)

            self.export_object(i, obj.name, props, [objects])
        return

    def execute(self, context):
        props: FbxBatchExportProperties = context.scene.FbxBatchExportProperties
        self.export_objects(context, props)

        return {"FINISHED"}
