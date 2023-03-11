from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from Main import GetTodayBirthdays,PromoteYear,Add_student,getAllBirthdays, Delete_student,updateBirthday
from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles #new
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")

def configure_static(app):  #new
    app.mount("/static", StaticFiles(directory="static"), name="static")

def start_application():
    app = FastAPI()
    configure_static(app)
    
    return app 



#Initialize FastAPI App
app = start_application()

# Add CORS allowed sites and local host for debugging
origins = [
    "http://localhost",
    "http://localhost:5000",
    "http://127.0.0.1:5500",
    "http://192.168.43.117:8080",
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/today")
async def home(request: Request):
	return templates.TemplateResponse("today.html",{"request":request})
 
@app.get("/home")
async def home(request: Request):
	return templates.TemplateResponse("index.html",{"request":request})

@app.get("/addstudent")
async def addstudent(request: Request):
	return templates.TemplateResponse("addstudent.html",{"request":request})
 


@app.get("/")
async def index():
    return "Welcome to birthday API"


@app.get("/getbirthday")
async def getBirthday():
    birthdays = GetTodayBirthdays()

    return birthdays

@app.get("/updateyeargroup")
async def UpdateYeargroups():
    PromoteYear()

    return 'Promotion Successfull'

@app.get("/add-birthday")
async def add_birthday(name: str,day: str,month: str, yeargroup: str, image: str):
    try:
        Add_student(name,day,month,yeargroup,image)
        return 'success'
    except:
        return 'An error occurred'


# Get alll
@app.get("/getall")
async def getall():
    All_birthdays = getAllBirthdays()

    return All_birthdays

# Delete a specific Birthday ##

@app.get("/delete-birthday")
async def delete_birthday(day: str,month: str,name: str, yeargroup: str):
    try:
        Delete_student(name,day,month,yeargroup)

        print('successfully Deleted')
    except:
        return 'An error occurred'
    
@app.get("/update-birthday")
async def update_birthday(day: str,month: str,name: str, yeargroup: str,id: int):
    try:
        updateBirthday(name,day,month,yeargroup,id)
        return 'Successfully updated'
    except:
        return 'An error occurred'