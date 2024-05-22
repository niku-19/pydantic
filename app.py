from pydantic import BaseModel , conlist , Field , EmailStr, constr
from typing import List

PINCODE_REGEX = r"^\d{5,6}$" 

class BillingAddress(BaseModel):
    address : str
    pincode : str
    city : str
    state : str        

class CreatedAt(BaseModel):
    date: str = Field(alias="$date")   

class  ModifiedAt(BaseModel):
    date: str = Field(alias="$date")


class Company(BaseModel):
    _id : str
    address : str
    name : str
    pincode : constr(pattern=PINCODE_REGEX)
    state : str
    city : str
    billingAddresses : conlist(BillingAddress, min_length=1)
    users : List[str]
    isVerified : bool
    status : str
    country : str
    isProcMaster : bool
    isProcStar : bool
    userEmails : List[EmailStr]
    companyStatus : str
    companyType : str
    vendorDocuments : List = []
    GSTIN : str
    branch : List[str]
    orgId : str
    createdAt : CreatedAt
    modifiedAt : ModifiedAt




company = Company(
  _id = "6646f01372df32597deaf35c",
  address = "Seoul Chang po, temple street",
  name = "Song K POP",
  pincode = "808109",
  state = "Gyeonggi ",
  city = "Seoul",
  billingAddresses = [
    {
      "address": "Seoul Chinese Gali, Wada Pav street",
      "pincode": "808109",
      "city": "Seoul",
      "state": "Gyeonggi "
    }
  ],
  users = [
    "6646f01572df32597deaf35d",
    "6646f01572df32597deaf35d"
  ],
  isVerified = True,
  status = "ACTIVE",
  country = "India",
  createdAt = {
    "$date": "2024-05-17T05:50:11.034Z"
  },
  modifiedAt = {
    "$date": "2024-05-21T07:30:20.028Z"
  },
  isProcMaster = False,
  isProcStar = False,
  userEmails = [
    "anuragsahu12@outlook.com",
    "anurag.sahu@braincells.in",
    "om.gaikwad@braincells.in",
    "nikhil.kumar@braincells.in"
  ],
  companyStatus = "ACTIVE",
  companyType = "client",
  vendorDocuments = [],
  GSTIN = "12378923",
  branch = [
    "FQuZnPwxHtY3JXKYt",
    "6570413b0bbd814615f82fe4"
  ],
  orgId = "trios"
)


print(company.model_dump_json())
print(company.model_json_schema())