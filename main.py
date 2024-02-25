from reactpy import component, html, run
from reactpy.backend.fastapi import configure
from fastapi import FastAPI


@component
def App():
    return html.div({"class_name": "prueba"}, "Hiho")

app = FastAPI()
configure(app, App)

run(App)
