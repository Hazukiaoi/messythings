# ##### BEGIN GPL LICENSE BLOCK #####
#
#  Messy Things project organizer for Blender.
#  Copyright (C) 2017-2019  Mikhail Rachinskiy
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####


import bpy


class Materials:

    def cleanup_materials(self, context):
        count = 0
        override = {"object": None}

        for mat in bpy.data.materials:
            if not mat.is_grease_pencil:
                bpy.data.materials.remove(mat)
                count += 1

        for ob in context.scene.objects:
            if ob.type != "GPENCIL":
                if ob.material_slots:
                    override["object"] = ob

                    for _ in ob.material_slots:
                        bpy.ops.object.material_slot_remove(override)

        return count