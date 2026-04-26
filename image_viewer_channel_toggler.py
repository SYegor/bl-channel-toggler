# SPDX-License-Identifier: GPL-3.0-or-later

# Viewer Channel Toggle Hotkeys for Blender
# Copyright (C) 2026 Yegor Smirnov
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

bl_info = {
    "name": "Viewer Channel Toggler",
    "author": "Yegor Smirnov",
    "version": (1, 0),
    "blender": (5, 1, 1),
    "location": "Image Editor",
    "description": "Toggle viewer channels with R/G/B/A hotkeys",
    "category": "Image",
}

import bpy

addon_keymaps = []


def toggle_display_channel(context, target_channel):
    area = context.area
    if not area or area.type != 'IMAGE_EDITOR':
        return {'CANCELLED'}

    space = area.spaces.active

    if space.display_channels == target_channel:
        space.display_channels = 'COLOR_ALPHA'
    else:
        space.display_channels = target_channel

    return {'FINISHED'}


class IMAGE_OT_toggle_red_channel(bpy.types.Operator):
    bl_idname = "image.toggle_red_channel"
    bl_label = "Toggle Red Channel"

    def execute(self, context):
        return toggle_display_channel(context, 'RED')


class IMAGE_OT_toggle_green_channel(bpy.types.Operator):
    bl_idname = "image.toggle_green_channel"
    bl_label = "Toggle Green Channel"

    def execute(self, context):
        return toggle_display_channel(context, 'GREEN')


class IMAGE_OT_toggle_blue_channel(bpy.types.Operator):
    bl_idname = "image.toggle_blue_channel"
    bl_label = "Toggle Blue Channel"

    def execute(self, context):
        return toggle_display_channel(context, 'BLUE')


class IMAGE_OT_toggle_alpha_channel(bpy.types.Operator):
    bl_idname = "image.toggle_alpha_channel"
    bl_label = "Toggle Alpha Channel"

    def execute(self, context):
        return toggle_display_channel(context, 'ALPHA')


classes = (
    IMAGE_OT_toggle_red_channel,
    IMAGE_OT_toggle_green_channel,
    IMAGE_OT_toggle_blue_channel,
    IMAGE_OT_toggle_alpha_channel,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon

    if kc:
        km = kc.keymaps.new(name='Image', space_type='IMAGE_EDITOR')

        addon_keymaps.append((km, km.keymap_items.new("image.toggle_red_channel", 'R', 'PRESS')))
        addon_keymaps.append((km, km.keymap_items.new("image.toggle_green_channel", 'G', 'PRESS')))
        addon_keymaps.append((km, km.keymap_items.new("image.toggle_blue_channel", 'B', 'PRESS')))
        addon_keymaps.append((km, km.keymap_items.new("image.toggle_alpha_channel", 'A', 'PRESS')))


def unregister():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
