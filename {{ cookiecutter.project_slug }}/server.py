import os
import subprocess
from pathlib import Path

import bottle

import {{ cookiecutter.project_slug }}

SERVER_HOST = "localhost"
SERVER_PORT = {{ cookiecutter.web_server_port }}

version = {{ cookiecutter.project_slug }}.__version__
wheel_filename = f"{{ cookiecutter.project_slug}}-{version}-py3-none-any.whl"

bottle.TEMPLATES.clear()
bottle.debug(True)

here = Path(__file__).parent.resolve()
web_root = here / "web"


@bottle.route("/")
def index():
    return bottle.template("web/index.html")


@bottle.route("/<filepath:re:.*\.whl>")
def whl(filepath):
    return bottle.static_file(filepath, root=str(here / "dist"))


def main():
    os.chdir(here)
    subprocess.run(["uv", "build"])
    bottle.run(host=SERVER_HOST, port=SERVER_PORT)


if __name__ == "__main__":
    main()