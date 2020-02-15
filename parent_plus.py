# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/blender_parent_plus

import bpy
from bpy.types import Object
from mathutils import Matrix


class ParentPlus:

    @classmethod
    def select_children_by_parent(cls, parents: [list, Object]):
        # selects all children of the parent objects from list
        if isinstance(parents, Object):
            parents = [parents]
        for current_object in parents:
            if current_object and hasattr(current_object, 'children') and current_object.children:
                for child in current_object.children:
                    child.select_set(True)
                    if hasattr(child, 'children') and child.children:
                        cls.select_children_by_parent(parents=child)

    @staticmethod
    def select_parents_chain(children: [list, Object]):
        # selects all parents chain of the children object
        if isinstance(children, Object):
            children = [children]
        for child in children:
            while child.parent:
                child = child.parent
                child.select_set(True)

    @staticmethod
    def parent_to_empty(context, selection: list, empty_pos=(0.0, 0.0, 0.0)):
        # create new empty in empty_pos and parent all selection to it
        # create empty
        empty = bpy.data.objects.new('Empty', None)
        context.scene.collection.objects.link(empty)
        empty.empty_display_size = 2
        empty.empty_display_type = 'PLAIN_AXES'
        empty.matrix_world @= Matrix.Translation(empty_pos)
        # parent selection to empty
        for current_object in selection:
            current_object.parent = empty
            current_object.matrix_parent_inverse = empty.matrix_world.inverted()
