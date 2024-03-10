#!/usr/bin/env python
""" This is the entrypoint to the Patient Service API.
"""

__author__ = "Fritz G. Batroni"
__contact__ = "fritz.g.batroni@gmail.com"
__copyright__ = "Copyright 2024"
__deprecated__ = False
__status__ = "Development"
__version__ = "0.0.1"

from fastapi import FastAPI

from lib.db_session_maker import SessionMaker
from lib.models.patient import Patient

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/patients")
async def get_patients():
   db_session = SessionMaker().get_session_maker()
   with db_session.begin() as session:
        patients= session.query(Patient)

        return patients