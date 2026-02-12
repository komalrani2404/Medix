from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator


from typing import List, Dict, Optional,Annotated

class Patient(BaseModel):

    name:str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies:list[str]
    contact_details: dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains=['hdfc.com','icici.com']
        domain_name=value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError(f"Email domain must be one of {valid_domains}")
        return value
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
        
        
        
        
        




def insert_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("Data inserted successfully")




def update_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Data updated successfully")




patient_info = {
    'name': 'neeluuuuuuuu',
    'email': 'johndoe@hdfc.com',
    
    'age': 30,
    'weight': 75.5,
    'married': True,
    'allergies': ['pollen', 'dust'],
    'contact_details': {
        'email': 'abc@gmail.com',
        'phone': '1234567890'}
}


patient1 = Patient(**patient_info)
insert_data(patient1)



