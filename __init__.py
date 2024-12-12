bl_info = {
    "name": "RenderPath Prefix",
    "author": "Roland Vyens",
    "version": (1, 0, 0),  # bump doc_url as well!
    "blender": (3, 0, 0),
    "location": "No UI",
    "description": "Use prefix for render path when rendering",
    "category": "Render",
    "doc_url": "",
    "tracker_url": "",
}


import bpy
import render_tokens


def register():
    bpy.app.handlers.render_init.append(render_tokens.replaceTokens)
    bpy.app.handlers.render_cancel.append(render_tokens.restoreTokens)
    bpy.app.handlers.render_complete.append(render_tokens.restoreTokens)


def unregister():
    bpy.app.handlers.render_init.remove(render_tokens.replaceTokens)
    bpy.app.handlers.render_cancel.remove(render_tokens.restoreTokens)
    bpy.app.handlers.render_complete.remove(render_tokens.restoreTokens)


if __name__ == "__main__":
    register()
