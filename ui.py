
import bpy
from bpy.types import Panel
from . import algorithms


class PrepareForUnreal(bpy.types.Operator):

    bl_idname = "unreal_bastioni_post_process.prepare_for_unreal"
    bl_label = "Prepare for Unreal Engine"

    def execute(self, context):
        global mblab_humanoid
        global gui_status

        old_blender_mode = bpy.ops.object.mode
        bpy.ops.object.mode_set(mode='OBJECT')

        bpy.context.area.spaces[0].pivot_point = 'CURSOR'
        bpy.context.area.spaces[0].cursor_location = (0.0, 0.0, 0.0)

        if (len(bpy.context.selected_objects) != 1):
            self.report({'ERROR_INVALID_INPUT'},
                        "Need to select only one ManuelBastioniLAB character.")

        if (bpy.context.scene.remove_proxyfit_shapekeys):
            algorithms.remove_shapekeys_from_proxyfit_items(
                bpy.context.selected_objects[0])
        if (bpy.context.scene.rename_bones):
            algorithms.rename_bones(bpy.context.selected_objects[0])
        if (bpy.context.scene.correct_scale_and_rotation):
            algorithms.correct_scale_and_rotation(
                bpy.context.selected_objects[0])

        bpy.ops.object.mode_set(mode=old_blender_mode)
        self.report({'INFO'}, "Complete")
        return {'FINISHED'}


class ExportFbxFiles(bpy.types.Operator):

    bl_idname = "unreal_bastioni_post_process.export_fbx_files"
    bl_label = "Export Fbx Files"

    def execute(self, context):
        global mblab_humanoid
        global gui_status

        old_blender_mode = bpy.ops.object.mode
        bpy.ops.object.mode_set(mode='OBJECT')

        algorithms.export_individual_fbx_files(bpy.context.selected_objects[0])

        bpy.ops.object.mode_set(mode=old_blender_mode)
        self.report({'INFO'}, "Complete")
        return {'FINISHED'}


class MainPanel(Panel):
    bl_label = "Unreal Bastioni Post Process"
    bl_idname = "unreal_bastioni_post_process.main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Tools"
    bl_context = "objectmode"

    def draw(self, context):
        box = self.layout.box()
        box.label('Prepare for Unreal Engine')
        box.prop(bpy.context.scene, 'remove_proxyfit_shapekeys')
        box.prop(bpy.context.scene, 'rename_bones')
        box.prop(bpy.context.scene, 'correct_scale_and_rotation')
        box.operator(PrepareForUnreal.bl_idname)
        box.operator(ExportFbxFiles.bl_idname)


def register():
    bpy.utils.register_class(PrepareForUnreal)
    bpy.utils.register_class(MainPanel)


def unregister():
    bpy.utils.register_class(PrepareForUnreal)
    bpy.utils.unregister_class(MainPanel)
