import requests
import re
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
import json
from Main import FIND_BIRTHDAY

#Initialize FastAPI App
app = FastAPI()

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


# Search Algorithm

import calendar
from datetime import date


today = date.today() 

# current_month_name = calendar.month_name[date.today().month]

# Using the abbreviated version:
current_month_name_abbreviated = calendar.month_abbr[date.today().month]

month = current_month_name_abbreviated

day = today.day

# print(month, today.day)

# Now lets join it like the format in the data

format = str(day)+"-"+month

# print(format)

# Hard coded format for testing purposes

# format = "21-Feb"



@app.get("/")
async def fail_safe3():
    return "Welcome to birthday API"


@app.get("/find-birthday")
async def name_search():
    # print(string_get)
    Birthdays_Today= FIND_BIRTHDAY(format)
    Birthdays_Today = [x.replace(format, '') for x in Birthdays_Today]
    return Birthdays_Today