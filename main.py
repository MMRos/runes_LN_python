from reactpy import component, html
from reactpy.backend.fastapi import configure
from fastapi import FastAPI


@component
def App():
    return html.div("Hi")


app = FastAPI()
configure(app, App)
