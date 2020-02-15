# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/blender_parent_plus

from . import parent_plus_ops
from . import parent_plus_panel
from .addon import Addon


bl_info = {
    'name': 'parent_plus',
    'category': 'All',
    'author': 'Nikita Akimov',
    'version': (1, 0, 0),
    'blender': (2, 82, 0),
    'location': 'N-Panel > Parent+',
    'wiki_url': 'https://b3d.interplanety.org/en/blender-add-on-parent-plus/',
    'tracker_url': 'https://b3d.interplanety.org/en/blender-add-on-parent-plus/',
    'description': 'Parent+'
}


def register():
    if not Addon.dev_mode():
        parent_plus_ops.register()
        parent_plus_panel.register()
    else:
        print('It seems you are trying to use the dev version of the ' + bl_info['name'] + ' add-on. It may work not properly. Please download and use the release version!')


def unregister():
    if not Addon.dev_mode():
        parent_plus_panel.unregister()
        parent_plus_ops.unregister()


if __name__ == '__main__':
    register()
