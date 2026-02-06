from fastapi import FastAPI ,Path;

import json



app=FastAPI()


def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data



@app.get("/")
def hello():
    return {"message":"Patient management System API"}


@app.get('/about')
def about():
    return {"message":"A Fully functional API to manage patient data and health records."}



@app.get('/view')
def view():
    data = load_data()
    return data

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str=Path(..., description="The ID of the patient in DB", example="P001")):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    return {"error": "Patient not found"}