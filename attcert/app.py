from attcert.main import check_attendee, CodeNotFound
from fastapi import FastAPI, HTTPException, Form, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates


app = FastAPI()
app.mount("/static", StaticFiles(directory="attcert/static"), name="static")
templates = Jinja2Templates(directory="attcert/templates/")


class Attendee(BaseModel):
    name: str
    code: str


@app.get("api/code/{code}", response_model=Attendee)
def check_code_rest(code: str):
    try:
        name = check_attendee(code)
        return Attendee(name=name, code=code)
    except CodeNotFound:
        raise HTTPException(404, detail="Attendee not found")


@app.get("/")
def check_code(request: Request):
    return templates.TemplateResponse(
        "template.html",
        context={"request": request, "name": None, "not_found": False, "code": ""},
    )


@app.get("/{code}", response_class=HTMLResponse)
def check_code(request: Request, code: str):
    return check_code_web(request, code)


@app.post("/", response_class=HTMLResponse)
def check_code(request: Request, code: str = Form(...)):
    return check_code_web(request, code)


@app.post("/{_}", response_class=HTMLResponse)
def check_code(request: Request, code: str = Form(...)):
    return check_code_web(request, code)


def check_code_web(request: Request, code: str) -> Response:
    try:
        name = check_attendee(code)
        not_found = False
    except CodeNotFound:
        name = None
        not_found = True
    return templates.TemplateResponse(
        "template.html",
        context={
            "request": request,
            "name": name,
            "not_found": not_found,
            "code": code,
        },
    )
