# {{ cookiecutter.project_name }}

This project was generated using the [Arcade Template](https://github.com/pythonarcade/arcade-template). It is designed to work with [uv](https://docs.astral.sh/uv). You will need to install that before using this.

## Initial Setup

```bash
uv sync --prerelease allow
```

## Running the application on desktop

```bash
uv run {{ cookiecutter.project_slug }}
```

## Running the application in a browser

Included in this project is a basic setup for both deploying your Arcade application to the web, and testing it locally.

To test your application on the web locally, run the following command and then navigate to http://localhost:8000

```bash
uv run server.py
```

An important note for running in the browser, if you can change the version of your application, or the version of Arcade that your application uses, you will need to change those in the `web/index.html` file as well for them to reflect in the browser.