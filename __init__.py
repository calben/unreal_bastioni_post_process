
bl_info = {
    "name": "Unreal Bastioni Post Process",
    "description": "Single line describing my awesome script.",
    "author": "Aaron Powell",
    "version": (1, 0),
    "blender": (2, 78, 0),
    "location": "View 3D > Tools > Unreal Bastioni Post Process",
    "warning": "",  # used for warning icon and text in add-ons panel
    "wiki_url": "http://my.wiki.url",
    "tracker_url": "http://my.bugtracker.url",
    "support": "COMMUNITY",
    "category": "Characters"
}

import bpy


def register():
    from . import properties
    from . import ui
    properties.register()
    ui.register()


def unregister():
    from . import properties
    from . import ui
    properties.unregister()
    ui.unregister()


if __name__ == '__main__':
    register()
