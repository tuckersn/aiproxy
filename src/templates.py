# These routes issue HTML from HTML templates in the /templates directory.
# /debug_interface renders templates/debug_interface.html

from flask import Blueprint, request, render_template

import os
import openai
import json

template_routes = Blueprint('template_routes', __name__)

@template_routes.route("/debug_interface")
def debug_interface_html():
    with open('test/data/u3l23_01.js', 'r') as f:
        code = f.read()

    with open('test/data/u3l23.txt', 'r') as f:
        prompt = f.read()

    with open('test/data/u3l23.csv', 'r') as f:
        rubric = f.read()
        
    return render_template(
        "debug_interface.html",
        code=code,
        prompt=prompt,
        rubric=rubric,
    )
