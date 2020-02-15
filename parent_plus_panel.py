# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/blender_parent_plus

import bpy
from bpy.types import Panel
from bpy.utils import register_class, unregister_class


class PARENT_PLUS_PT_panel(Panel):
    bl_idname = 'PARENT_PLUS_PT_panel'
    bl_label = 'Parent+'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Parent+'

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        box.label(text='Selection')
        box.operator('parent_plus.select_parents_chain', icon='SORT_DESC')
        box.operator('parent_plus.select_children_by_parent', icon='SORT_ASC')
        box = layout.box()
        box.label(text='Parenting')
        row = box.row()
        row.prop(context.window_manager.parent_plus_vars, 'empty_location', expand=True)
        operator = box.operator('parent_plus.parent_to_empty', icon='EMPTY_AXIS')
        operator.empty_location = context.window_manager.parent_plus_vars.empty_location


def register():
    register_class(PARENT_PLUS_PT_panel)


def unregister():
    unregister_class(PARENT_PLUS_PT_panel)
