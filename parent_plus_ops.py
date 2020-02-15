# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/blender_parent_plus

from bpy.types import Operator
from bpy.utils import register_class, unregister_class


class PARENT_PLUS_OT_main(Operator):
    bl_idname = 'parent_plus.main'
    bl_label = 'parent_plus: main'
    bl_description = 'parent_plus - main operator'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # print('parent_plus.main - executed with param1 = ', self.param1)
        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        return True


def register():
    register_class(PARENT_PLUS_OT_main)


def unregister():
    unregister_class(PARENT_PLUS_OT_main)
