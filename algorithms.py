import bpy


def remove_shapekeys_from_proxyfit_items(selected_character):
    for object in bpy.data.objects:
        print('checking ' + object.name)
        if (object.type == "MESH"):
            print('identified as mesh with armature ' +
                  object.find_armature().name + ' to compare to ' + selected_character.find_armature().name)
            if selected_character.find_armature().name == object.find_armature().name:
                print('removing shape keys from ' + object.name)
                if (len(list(filter(lambda x: "mbastlab_proxyfit" in x.name, object.data.shape_keys.key_blocks))) > 0):
                    object.select = True
                    bpy.context.scene.objects.active = object

                    def del_shape_key(name):
                        i = object.data.shape_keys.key_blocks.keys().index(name)
                        object.active_shape_key_index = i
                        bpy.ops.object.shape_key_remove()
                    del_shape_key("Basis")
                    del_shape_key("mbastlab_proxyfit")


def correct_scale_and_rotation(selected_character):
    bpy.context.scene.unit_settings.system = 'METRIC'
    bpy.context.scene.unit_settings.scale_length = 0.01
    k = 100  # scale constant
    for object in bpy.data.objects:
        if (object.type == "MESH"):
            if selected_character.find_armature().name == object.find_armature().name:
                print('adjusting ' + object.name)
                object.select = True
        if (object.type == "ARMATURE"):
            if (object.name == selected_character.find_armature().name):
                print('adjusting ' + object.name)
                object.select = True
    bpy.ops.transform.resize(value=(k, k, k))
    bpy.ops.object.transform_apply(scale=True)



def rename_bones(selected_character):
    namelist = [
        ["spine01", "spine_01"],
        ["spine02", "spine_02"],
        ["spine03", "spine_03"],
        ["neck", "neck_01"],
        ["upperarm_twist_L", "upperarm_twist_01_l"],
        ["upperarm_twist_R", "upperarm_twist_01_r"],
        ["lowerarm_twist_L", "lowerarm_twist_01_l"],
        ["lowerarm_twist_R", "lowerarm_twist_01_r"],
        ["thumb01_L", "thumb_01_l"],
        ["thumb02_L", "thumb_02_l"],
        ["thumb03_L", "thumb_03_l"],
        ["thumb01_R", "thumb_01_r"],
        ["thumb02_R", "thumb_02_r"],
        ["thumb03_R", "thumb_03_r"],
        ["index01_L", "index_01_l"],
        ["index02_L", "index_02_l"],
        ["index03_L", "index_03_l"],
        ["index01_R", "index_01_r"],
        ["index02_R", "index_02_r"],
        ["index03_R", "index_03_r"],
        ["middle01_L", "middle_01_l"],
        ["middle02_L", "middle_02_l"],
        ["middle03_L", "middle_03_l"],
        ["middle01_R", "middle_01_r"],
        ["middle02_R", "middle_02_r"],
        ["middle03_R", "middle_03_r"],
        ["ring01_L", "ring_01_l"],
        ["ring02_L", "ring_02_l"],
        ["ring03_L", "ring_03_l"],
        ["ring01_R", "ring_01_r"],
        ["ring02_R", "ring_02_r"],
        ["ring03_R", "ring_03_r"],
        ["pinky01_L", "pinky_01_l"],
        ["pinky02_L", "pinky_02_l"],
        ["pinky03_L", "pinky_03_l"],
        ["pinky01_R", "pinky_01_r"],
        ["pinky02_R", "pinky_02_r"],
        ["pinky03_R", "pinky_03_r"],
        ["thigh_twist_L", "thigh_twist_01_l"],
        ["thigh_twist_R", "thigh_twist_01_r"],
        ["calf_twist_L", "calf_twist_01_l"],
        ["calf_twist_R", "calf_twist_01_r"],
        ["toes_L", "ball_l"],
        ["toes_R", "ball_r"]
    ]

    armature = selected_character.find_armature()
    if armature:
        print('renaming bones for ' + armature.name)
        for name, new_name in namelist:
            pb = armature.pose.bones.get(name)
            if pb:
                pb.name = new_name
    else:
        print('failed to find armature')


def export_individual_fbx_files(selected_character):
    for object in bpy.data.objects:
        bpy.ops.object.select_all(action='DESELECT')
        object.select = True
        if (object.find_armature() != None):
            object.find_armature().select = True
        export_name = object.name
        if ("MBlab_bd" in object.name):
            export_name = bpy.context.scene.mblab_unreal_export_directory + "/" + export_name
        fn = os.path.join(export_name)
        print("exporting", object.name)
        print({o.name: o.select for o in bpy.data.objects})
        bpy.ops.export_scene.fbx(filepath=fn + ".fbx", check_existing=True, axis_up='Y', axis_forward='-Z', filter_glob="*.fbx",
                                 version='BIN7400', use_selection=True, global_scale=1.0, bake_space_transform=False, object_types={'MESH', 'ARMATURE'},
                                 use_mesh_modifiers=False, mesh_smooth_type='OFF', use_mesh_edges=False, use_tspace=False, use_custom_props=False,
                                 add_leaf_bones=False, primary_bone_axis='Y', secondary_bone_axis='X', use_armature_deform_only=False,
                                 bake_anim=True, bake_anim_use_all_bones=True, bake_anim_use_nla_strips=True, bake_anim_use_all_actions=True,
                                 bake_anim_step=1.0, bake_anim_simplify_factor=1.0, use_anim=True, use_anim_action_all=True, use_default_take=True,
                                 use_anim_optimize=True, anim_optimize_precision=6.0, path_mode='AUTO', embed_textures=False, batch_mode='OFF',
                                 use_batch_own_dir=True, use_metadata=True)
