# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

# AUTHOR: PabloVazquez
# CONVERTED TO ADDON / FIXED BY JFranMatheu

bl_info = {
    "name" : "Collectioranth",
    "author" : "PabloVazquez",
    "description" : "Old 2.7 Collections",
    "blender" : (2, 80, 0),
    "version" : (0, 3, 0),
    "location" : "View3D > Header",
    "category" : "Generic"
}

import bpy 
from bpy.types import Header
from bpy import context, types, ops
from bpy.utils import register_class, unregister_class
#from bl_ui.space_view3d import VIEW3D_HT_header

class COL_HT_toolHeader_collections(Header):
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOL_HEADER"
    bl_options = {'REGISTER'}

    def draw(self, context):

        row = self.layout.split().row(align=True)
        view3d_header_collections_test(self, context)


def register():
    #unregister_class(VIEW3D_HT_header)
    bpy.types.VIEW3D_HT_header.append(view3d_header_collections) #
    #register_class(COL_HT_toolHeader_collections) # TOOL HEADER - SCULPT MODE
    #register_class(VIEW3D_HT_header)
	

from bpy.types import Operator
from bpy.props import BoolProperty
from bl_ui.space_view3d import VIEW3D_HT_tool_header #

def unregister():
    bpy.types.VIEW3D_HT_header.remove(view3d_header_collections) #
    #unregister_class(COL_HT_toolHeader_collections) # TOOL HEADER - SCULPT MODE



def view3d_header_collections(self, context):
 
    layout = self.layout
 
    collections = bpy.data.collections
    act_ob = context.active_object
 
    idx = 1
 
    split = layout.split()
    col = split.column(align=True)
    row = col.row(align=True)
    row.scale_y = 0.5
 
 
    for coll in bpy.data.collections:
 
        # If there are icons, use LAYER_USED
        icon = 'LAYER_USED' if len(coll.objects) > 0 else 'BLANK1'
 
        # if the active object is in the current collection
        if act_ob and (coll in act_ob.users_collection):
            icon = 'LAYER_ACTIVE'
 
        props = row.operator('object.hide_collection', text='', icon=icon)
        props.collection_index = idx
 
        if idx%5==0:
            row = col.row(align=True)
            row.scale_y = 0.5
 
        if idx%10==0:
            layout.separator()
            col = layout.column(align=True)
            row = col.row(align=True)
            row.scale_y = 0.5
 
        idx += 1