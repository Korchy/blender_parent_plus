# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/blender_parent_plus

import bpy


class PARENT_PLUS_KeyMap:

    _keymaps = []

    @staticmethod
    def _extend_select_menu(self, context):
        self.layout.separator()
        self.layout.operator('parent_plus.select_parents_chain')
        self.layout.operator('parent_plus.select_children_by_parent')

    @classmethod
    def register(cls, context):
        if context.window_manager.keyconfigs.addon:
            keymap = context.window_manager.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
            # add keys
            keymap_item = keymap.keymap_items.new('parent_plus.select_children_by_parent', 'RIGHT_BRACKET', 'PRESS', ctrl=True)
            cls._keymaps.append((keymap, keymap_item))
            keymap_item = keymap.keymap_items.new('parent_plus.select_parents_chain', 'LEFT_BRACKET', 'PRESS', ctrl=True)
            cls._keymaps.append((keymap, keymap_item))
        # modify select menu
        bpy.types.VIEW3D_MT_select_object_more_less.append(cls._extend_select_menu)

    @classmethod
    def unregister(cls):
        # clear select menu
        bpy.types.VIEW3D_MT_select_object_more_less.remove(cls._extend_select_menu)
        # clear keys
        for keymap, keymap_item in cls._keymaps:
            keymap.keymap_items.remove(keymap_item)
        cls._keymaps.clear()


def register():
    # register_class(SUP_MT_ex_menu)
    PARENT_PLUS_KeyMap.register(context=bpy.context)


def unregister():
    PARENT_PLUS_KeyMap.unregister()
    # unregister_class(SUP_MT_ex_menu)
