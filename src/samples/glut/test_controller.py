#!/bin/env python

# file hello_glfw.py

from glut_app import GlutApp
from openvr.gl_renderer import OpenVrGlRenderer
from test_controller_actor import ControllerActor

"""
Minimal glfw programming example which colored OpenGL cube scene that can be closed by pressing ESCAPE.
"""


if __name__ == "__main__":
    actor = ControllerActor()
    renderer = OpenVrGlRenderer(actor)
    with GlutApp(renderer, "glut OpenVR color cube") as glutApp:
        glutApp.run_loop()