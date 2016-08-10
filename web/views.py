from pyramid.view import view_config
import json
import os


@view_config(route_name="index", renderer="templates/index.jinja2")
def index(request):
    data = {"html": ""}
    year = "2016"
    week = "32"
    server = "212914826169679872"
    str = "year" + "-" + "week" + "-" + "server"

    for file in os.listdir("log"):
        name = file[8:26]
        if name == server:
            channel = file[27:-4]
            data["html"] += """<button type="button" onclick="ReadFile(this);"
                            file="{}">{}</button>""".format(file, channel)

    return data


@view_config(route_name="readfile", renderer="json")
def readfile(request):
    file = request.POST.get("file")
    data = {"text": "Error"}
    with open("log/" + file, "r") as f:
        data["text"] = f.read()

    return data