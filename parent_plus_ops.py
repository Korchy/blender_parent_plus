# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/blender_parent_plus

import bpy
from bpy.props import PointerProperty, EnumProperty
from bpy.types import Operator, PropertyGroup, WindowManager
from bpy.utils import register_class, unregister_class
from .parent_plus import ParentPlus


class PARENT_PLUS_OT_select_children_by_parent(Operator):
    bl_idname = 'parent_plus.select_children_by_parent'
    bl_label = 'Select All Children'
    bl_description = 'Select all children of active parent object'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if context.active_object and context.active_object.mode == 'EDIT':
            bpy.ops.object.mode_set(mode='OBJECT')
        ParentPlus.select_children_by_parent(parents=context.selected_objects)
        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        if context.selected_objects:
            return True
        else:
            return False


class PARENT_PLUS_OT_select_parents_chain(Operator):
    bl_idname = 'parent_plus.select_parents_chain'
    bl_label = 'Select All Parents'
    bl_description = 'Select all parents chain by active object'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if context.active_object and context.active_object.mode == 'EDIT':
            bpy.ops.object.mode_set(mode='OBJECT')
        ParentPlus.select_parents_chain(children=context.selected_objects)
        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        if context.selected_objects:
            return True
        else:
            return False


class PARENT_PLUS_OT_parent_to_empty(Operator):
    bl_idname = 'parent_plus.parent_to_empty'
    bl_label = 'Parent Selection To Empty'
    bl_description = 'Parent all selection to new empty'
    bl_options = {'REGISTER', 'UNDO'}

    empty_location: EnumProperty(
        items=[
            ('CURSOR', 'cursor', 'cursor'),
            ('CENTER', 'center', 'center'),
            ('ACTIVE', 'active', 'active'),
            ('WORLD', 'world', 'world')
        ],
        default='CURSOR'
    )

    def execute(self, context):
        if context.active_object and context.active_object.mode == 'EDIT':
            bpy.ops.object.mode_set(mode='OBJECT')
        if self.empty_location == 'CURSOR':
            empty_location = context.scene.cursor.location
        elif self.empty_location == 'CENTER':
            _x_list = [obj.location.x for obj in context.selected_objects]
            _y_list = [obj.location.y for obj in context.selected_objects]
            _z_list = [obj.location.z for obj in context.selected_objects]
            _len = len(context.selected_objects)
            _x = sum(_x_list) / _len
            _y = sum(_y_list) / _len
            _z = sum(_z_list) / _len
            empty_location = (_x, _y, _z)
        elif self.empty_location == 'ACTIVE':
            empty_location = context.active_object.location
        else:
            # WORLD
            empty_location = (0.0, 0.0, 0.0)
        ParentPlus.parent_to_empty(
            context=context,
            selection=context.selected_objects,
            empty_pos=empty_location
        )
        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        if context.selected_objects:
            return True
        else:
            return False


class PARENT_PLUS_vars(PropertyGroup):
    empty_location: EnumProperty(
        items=[
            ('CURSOR', 'CURSOR', 'CURSOR'),
            ('CENTER', 'CENTER', 'CENTER'),
            ('WORLD', 'WORLD', 'WORLD'),
            ('ACTIVE', 'ACTIVE', 'ACTIVE')
        ],
        default='CURSOR'
    )


def register():
    register_class(PARENT_PLUS_vars)
    WindowManager.parent_plus_vars = PointerProperty(type=PARENT_PLUS_vars)
    register_class(PARENT_PLUS_OT_select_children_by_parent)
    register_class(PARENT_PLUS_OT_select_parents_chain)
    register_class(PARENT_PLUS_OT_parent_to_empty)


def unregister():
    unregister_class(PARENT_PLUS_OT_parent_to_empty)
    unregister_class(PARENT_PLUS_OT_select_parents_chain)
    unregister_class(PARENT_PLUS_OT_select_children_by_parent)
    del WindowManager.parent_plus_vars
    unregister_class(PARENT_PLUS_vars)
