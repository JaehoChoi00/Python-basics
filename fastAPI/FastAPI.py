from fastapi import FastAPI
from pydantic import BaseModel

from expresso import Expresso, ExposureCategory, ExposureLevel

# Pure Python Side

class User:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.exposure = Expresso.exposure(name)

    def changeName(self, newName):
        if self.name != newName:
            self.name = newName
            self.exposure.l2(ExposureCategory.USER, Expresso.BOLD + f"Changing name to: {self.name}\n" + Expresso.RESET)
        else:
            self.exposure.l2(ExposureCategory.USER, Expresso.BOLD + "Username is the same as before.\n" + Expresso.RESET)

    def growUp(self):
        self.growUpBy(1)

    def growUpBy(self, number):
        self.exposure.l2(ExposureCategory.USER, Expresso.BOLD + Expresso.FG_GREEN + str(self.age) + " increasing by " + str(number) + "\n" + Expresso.RESET + Expresso.RESET)
        self.age += number
        self.exposure.l2(ExposureCategory.USER, Expresso.BOLD + Expresso.FG_GREEN + "Age is now " + str(self.age) + "\n" + Expresso.RESET + Expresso.RESET)

    def printStats(self):
        self.exposure.l1(ExposureCategory.USER, "Printing User Stats...\n" + Expresso.RESET)
        self.exposure.l1(ExposureCategory.USER, "Name: " + self.name + "\n" + Expresso.RESET + Expresso.RESET)
        self.exposure.l1(ExposureCategory.USER, "Age: " + str(self.age) + "\n" + Expresso.RESET + Expresso.RESET)
        self.exposure.l1(ExposureCategory.USER, "Gender: " + self.gender + Expresso.RESET)

ExposureCategory.USER = ExposureCategory("USER")
runtimeExposure = Expresso.exposure("Runtime")

# Pydantic
class UserRequest(BaseModel):
    name: str
    age: int
    gender: str

class UserAgeUpdate(BaseModel):
    age: int

# FastAPI Integration
fastAPIapp = FastAPI()

users = set()

user0 = User("HardCodedUser", 0, "NA")

users.add(user0)

@fastAPIapp.get("/")
def root():
    runtimeExposure.l1(ExposureCategory.SYSTEMLOG, Expresso.BOLD + "GET /" + "\n" + Expresso.RESET)
    return {"message": "The API is running"}


@fastAPIapp.get("/hello/{name}")
def helloName(name: str):
    runtimeExposure.l1(ExposureCategory.SYSTEMLOG, Expresso.BOLD + "GET /hello/" + name + "\n" + Expresso.RESET)
    return {"message": "Hello " + name}


@fastAPIapp.get("/users/{name}")
def getUser(name: str):
    runtimeExposure.l1(ExposureCategory.SYSTEMLOG, Expresso.BOLD + "GET /users/" + name + "\n" + Expresso.RESET)

    for user in users:
        if user.name == name:
            runtimeExposure.l1(ExposureCategory.USER, Expresso.BOLD + "User found: " + user.name + "\n" + Expresso.RESET)
            runtimeExposure.lbr(ExposureCategory.USER, ExposureLevel.LEVEL1)
            return {
                "name": user.name,
                "age": user.age,
                "gender": user.gender
            }

    runtimeExposure.err("User not found: " + name)

    return {"error": "User not found"}

@fastAPIapp.post("/users")
def createUser(user: UserRequest):
    runtimeExposure.l1(ExposureCategory.SYSTEMLOG, Expresso.BOLD + "POST /users" + "\n" + Expresso.RESET)
    runtimeExposure.l1(ExposureCategory.USER, Expresso.BOLD + "Creating User: " + user.name + "\n" + Expresso.RESET)

    newUser = User(user.name, user.age, user.gender)

    users.add(newUser)

    runtimeExposure.l1(ExposureCategory.USER, Expresso.BOLD + "User created: " + newUser.name + "\n" + Expresso.RESET)
    runtimeExposure.lbr(ExposureCategory.USER, ExposureLevel.LEVEL1)
    return {
        "name": newUser.name,
        "age": newUser.age,
        "gender": newUser.gender
    }

@fastAPIapp.post("/users/{name}/grow")
def growUser(name: str):
    runtimeExposure.l1(ExposureCategory.SYSTEMLOG, Expresso.BOLD + "POST /users/" + name + "/grow" + "\n" + Expresso.RESET)

    for user in users:
        if user.name == name:
            runtimeExposure.l1(ExposureCategory.USER, Expresso.BOLD + "Growing User: " + user.name + "\n" + Expresso.RESET)

            user.growUp()

            runtimeExposure.l1(ExposureCategory.USER, Expresso.BOLD + "Growth complete. Age: " + str(user.age) + "\n" + Expresso.RESET)
            runtimeExposure.lbr(ExposureCategory.USER, ExposureLevel.LEVEL1)
            return {
                "name": user.name,
                "age": user.age,
                "gender": user.gender
            }

    runtimeExposure.err("User not found: " + name)

    return {"error": "User not found"}

@fastAPIapp.put("/users/{name}")
def replaceUser(name: str, userRequest: UserRequest):
    runtimeExposure.l1(ExposureCategory.SYSTEMLOG, Expresso.BOLD + "PUT /users/" + name + "\n" + Expresso.RESET)

    for user in users:
        if user.name == name:
            runtimeExposure.l1(ExposureCategory.USER, Expresso.BOLD + "Replacing User: " + user.name + "\n" + Expresso.RESET)

            user.name = userRequest.name
            user.age = userRequest.age
            user.gender = userRequest.gender

            runtimeExposure.l1(ExposureCategory.USER, Expresso.BOLD + "User replacement complete" + "\n" + Expresso.RESET)
            runtimeExposure.lbr(ExposureCategory.USER, ExposureLevel.LEVEL1)
            return {
                "name": user.name,
                "age": user.age,
                "gender": user.gender
            }

    runtimeExposure.err("User not found: " + name)

    return {"error": "User not found"}

@fastAPIapp.patch("/users/{name}")
def updateUser(name: str, update: UserAgeUpdate):
    runtimeExposure.l1(ExposureCategory.SYSTEMLOG, Expresso.BOLD + "PATCH /users/" + name + "\n" + Expresso.RESET)

    for user in users:
        if user.name == name:
            runtimeExposure.l1(ExposureCategory.USER, Expresso.BOLD + "Changing age for: " + user.name + "\n" + Expresso.RESET)

            user.age = update.age

            runtimeExposure.l1(ExposureCategory.USER, Expresso.BOLD + "Age changed to: " + str(user.age) + "\n" + Expresso.RESET)
            runtimeExposure.lbr(ExposureCategory.USER, ExposureLevel.LEVEL1)
            return {
                "name": user.name,
                "age": user.age,
                "gender": user.gender
            }

    runtimeExposure.err("User not found: " + name)

    return {"error": "User not found"}

@fastAPIapp.delete("/users/{name}")
def deleteUser(name: str):
    runtimeExposure.l1(ExposureCategory.SYSTEMLOG, Expresso.BOLD + "DELETE /users/" + name + "\n" + Expresso.RESET)

    for user in users:
        if user.name == name:
            runtimeExposure.l1(ExposureCategory.USER, Expresso.BOLD + "Deleting User: " + user.name + "\n" + Expresso.RESET)

            users.remove(user)

            runtimeExposure.l1(ExposureCategory.USER, Expresso.BOLD + "User deleted: " + name + "\n" + Expresso.RESET)
            runtimeExposure.lbr(ExposureCategory.USER, ExposureLevel.LEVEL1)
            return {
                "message": "User deleted",
                "name": name
            }

    runtimeExposure.err("User not found: " + name)

    return {"error": "User not found"}

from fastapi.testclient import TestClient

Expresso.setLevel(ExposureLevel.LEVEL5)
client = TestClient(fastAPIapp)

client.get("/")
client.get("/hello/Bob")
client.get("/users/HardCodedUser")

client.post("/users", json = {
    "name": "Bob",
    "age": 15,
    "gender": "Male"
})

client.get("/users/Bob")
client.post("/users/Bob/grow")
client.patch("/users/Bob", json = {"age": 20})

client.put("/users/Bob", json = {
    "name": "Bob",
    "age": 21,
    "gender": "Male"
})

client.get("/users/Bob")
client.delete("/users/Bob")
client.get("/users/Bob")