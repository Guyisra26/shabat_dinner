from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from services.rsvp_handler import submit_rsvp, get_summary
from modules.schemas import RSVP


router = APIRouter()
templates = Jinja2Templates(directory="frontend")

@router.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/submit", response_class=RedirectResponse)
def submit(family: str = Form(...), num_people: int = Form(...)):
    rsvp = RSVP(family=family, num_people=num_people)
    submit_rsvp(rsvp)
    return RedirectResponse(url="/summary", status_code=303)

@router.get("/summary", response_class=HTMLResponse)
def summary(request: Request):
    data, total = get_summary()
    return templates.TemplateResponse("summary.html", {"request": request, "data": data, "total": total})
