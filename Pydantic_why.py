
from pydantic import BaseModel,EmailStr,AnyUrl,Field

from typing import List,Optional,Annotated
from typing import Dict
class Patient(BaseModel):

    name : Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Nitish', 'Amit'])]

    email: EmailStr
    age : int=Field(gt=0,lt=120)
    weight:Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None, description='Is the patient married or not')]

    allergies:Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details:Dict[str,str]
    
def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('insertd')
def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('updated')
patient_info = {'name' : 'Aman','email':'abc@gmail.com' ,'age':30,'weight':76.3,'married':True,'allergies':['pollen','dust'],'contact_details':{'phone':'7870787'}}

patient1=Patient(**patient_info)

insert_patient_data(patient1)
update_patient_data(patient1)
