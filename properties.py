
import bpy
from bpy.types import Scene


def register():
    Scene.remove_proxyfit_shapekeys = bpy.props.BoolProperty(
        name="Remove Proxy Fit Item Shapekeys", default=True)
    Scene.rename_bones = bpy.props.BoolProperty(
        name="Rename Bones for Unreal Mannequin", default=True)
    Scene.correct_scale_and_rotation = bpy.props.BoolProperty(
        name="Scale and Rotate", default=True)


def unregister():
    del Scene.remove_proxyfit_shapekeys
    del Scene.rename_bones
    del Scene.correct_scale_and_rotation
