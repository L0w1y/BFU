# ====================== BEGIN GPL LICENSE BLOCK ============================
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	 See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.	 If not, see <http://www.gnu.org/licenses/>.
#  All rights reserved.
#
# ======================= END GPL LICENSE BLOCK =============================

# ----------------------------------------------
#  BBPL -> BleuRaven Blender Python Library
#  BleuRaven.fr
#  XavierLoux.com
# ----------------------------------------------

import bpy
import importlib
from . import types
from . import functions
from . import utils
from .functions import *

if "types" in locals():
    importlib.reload(types)
if "functions" in locals():
    importlib.reload(functions)
if "utils" in locals():
    importlib.reload(utils)

classes = (
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    
    types.register()


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    types.unregister()
