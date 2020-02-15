# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/blender_parent_plus

from bpy.types import Panel
from bpy.utils import register_class, unregister_class


class PARENT_PLUS_PT_panel(Panel):
    bl_idname = 'PARENT_PLUS_PT_panel'
    bl_label = 'parent_plus'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'parent_plus'

    def draw(self, context):
        operator = self.layout.operator('parent_plus.main', icon='BLENDER', text='parent_plus execute')
        operator.param1 = context.window_manager.parent_plus_vars.param1
        self.layout.prop(context.window_manager.parent_plus_vars, 'param1')


def register():
    register_class(PARENT_PLUS_PT_panel)


def unregister():
    unregister_class(PARENT_PLUS_PT_panel)
