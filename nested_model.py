from pydantic import BaseModel,EmailStr,AnyUrl,Field

class address(BaseModel):
    city: str
    state: str
    pin: str


class Patient(BaseModel):
    name:str
    gender: str
    age:int
    address: address


address_dict={'city':'Bangalore','state':'Karnataka','pin':'560001'}

address1=address(**address_dict)

patient_dict={
    'name':'neelu',
    'gender':'female',
    'age':30,
    'address': address1}

patient1=Patient(**patient_dict)

print(patient1)
print(patient1.address.city)