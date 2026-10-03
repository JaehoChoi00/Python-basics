# FastAPI

<img src="FastAPI_Logo.png" width="100" height="100">

[:arrow_left: Return to Main README](../README.md)

> ["FastAPI is a modern, fast (high-performance), web framework for building APIs with Python based on standard Python type hints."](https://fastapi.tiangolo.com/#:~\:text=FastAPI%20is%20a%20modern%2C%20fast%20\(high%2Dperformance\)%2C%20web%20framework%20for%20building%20APIs%20with%20Python%20based%20on%20standard%20Python%20type%20hints)

>

:arrow_right: [Link to FastAPI Homepage](https://fastapi.tiangolo.com)

## Sections

> * [The Prologue](#the-prologue)
> * [Creating the FastAPI Application](#creating-the-fastapi-application)
> * [GET Requests](#get-requests)
> * [POST Requests](#post-requests)
> * [Path Parameters](#path-parameters)
> * [Request Bodies](#request-bodies)
> * [PUT Requests](#put-requests)
> * [PATCH Requests](#patch-requests)
> * [DELETE Requests](#delete-requests)
> * [Combining Parameters and Functions](#combining-parameters-and-functions)
> * [Testing](#testing)

---

### [The Prologue](#sections)

FastAPI connects HTTP requests to normal Python functions.

```text
HTTP Request
↓
FastAPI Route
↓
Python Function
↓
Python Logic
↓
Response
```

---

### [Creating the FastAPI Application](#sections)

fastAPI Syntax

```py
from fastapi import FastAPI

fastAPIapp = FastAPI()
```

`FastAPI()` creates the application.

The application provides methods for registering HTTP routes:

```py
fastAPIapp.get()
fastAPIapp.post()
fastAPIapp.put()
fastAPIapp.patch()
fastAPIapp.delete()
```

---

### [GET Requests](#sections)

fastAPI Syntax

```py
@fastAPIapp.get("/hello")
def hello():
return {"message": "Hello"}
```

`@fastAPIapp.get("/hello")` connects a `GET` request to the function below it.

```text
GET /hello
↓
hello()
↓
Response
```

The function itself is normal Python.

---

### [POST Requests](#sections)

fastAPI Syntax

```py
@fastAPIapp.post("/users")
def createUser():
return {"message": "User created"}
```

`post()` connects a `POST` request to the function.

```py
@fastAPIapp.get("/users")
def getUsers():
...

@fastAPIapp.post("/users")
def createUser():
...
```

The HTTP method determines which function FastAPI calls.

---

### [Path Parameters](#sections)

fastAPI Syntax

```py
@fastAPIapp.get("/hello/{name}")
def helloName(name: str):
return {"message": "Hello " + name}
```

`{name}` takes a value from the URL and passes it to the function.

```text
GET /hello/Bob
↓
name = "Bob"
↓
helloName("Bob")
```

---

### [Request Bodies](#sections)

fastAPI + Pydantic Syntax

```py
from pydantic import BaseModel

class UserRequest(BaseModel):
name: str
age: int
gender: str
```

The model defines the structure of the request body.

```py
@fastAPIapp.post("/users")
def createUser(user: UserRequest):
return {
"name": user.name,
"age": user.age,
"gender": user.gender
}
```

For example:

```json
{
"name": "Bob",
"age": 15,
"gender": "Male"
}
```

FastAPI provides the request body to the function as `user`.

```text
POST /users
↓
Request Body
↓
UserRequest
↓
createUser(user)
```

---

### [PUT Requests](#sections)

fastAPI Syntax

```py
@fastAPIapp.put("/users/{name}")
def replaceUser(name: str, userRequest: UserRequest):
...
```

`put()` connects a `PUT` request to the function.

`PUT` is commonly used to replace an existing resource.

The function can receive both a path parameter and request body:

```text
PUT /users/Bob
+
UserRequest
↓
replaceUser(name, userRequest)
```

---

### [PATCH Requests](#sections)

fastAPI Syntax

```py
@fastAPIapp.patch("/users/{name}")
def updateUser(name: str, update: UserAgeUpdate):
...
```

`patch()` connects a `PATCH` request to the function.

`PATCH` is commonly used to change part of an existing resource.

```py
class UserAgeUpdate(BaseModel):
age: int
```

The request can therefore contain only:

```json
{
"age": 20
}
```

```text
PATCH /users/Bob
+
UserAgeUpdate
↓
updateUser(name, update)
```

---

### [DELETE Requests](#sections)

fastAPI Syntax

```py
@fastAPIapp.delete("/users/{name}")
def deleteUser(name: str):
...
```

`delete()` connects a `DELETE` request to the function.

```text
DELETE /users/Bob
↓
deleteUser("Bob")
↓
Python removes Bob
```

---

### [Combining Parameters and Functions](#sections)

FastAPI functions can receive information from different parts of a request.

```py
@fastAPIapp.put("/users/{name}")
def replaceUser(name: str, userRequest: UserRequest):
...
```

```text
/users/{name} → name
Request Body  → userRequest
↓
replaceUser(name, userRequest)
```

The basic FastAPI pattern is:

```text
HTTP Request
↓
Route
↓
Parameters
↓
Python Function
↓
Python Logic
↓
Response
```

The decorator determines when the function is called.

The parameters determine what information it receives.

The function determines what happens.

---

### [Testing](#sections)

python + FastAPI Syntax

```py
from fastapi.testclient import TestClient

client = TestClient(fastAPIapp)

client.get("/")

client.get("/hello/Bob")

client.post("/users", json={
"name": "Bob",
"age": 15,
"gender": "Male"
})

client.get("/users/Bob")

client.patch("/users/Bob", json={
"age": 20
})

client.delete("/users/Bob")
```

***[Expresso](https://pypi.org/project/expresso-framework/) Output:***
```txt
[#1] [Runtime] [SYSTEMLOG] [LEVEL1] GET /
[#2] [Runtime] [SYSTEMLOG] [LEVEL1] GET /hello/Bob
[#3] [Runtime] [SYSTEMLOG] [LEVEL1] GET /users/HardCodedUser
[#4] [Runtime] [USER] [LEVEL1] User found: HardCodedUser

--------------------------------
[#5] [Runtime] [SYSTEMLOG] [LEVEL1] POST /users
[#6] [Runtime] [USER] [LEVEL1] Creating User: Bob
[#7] [Runtime] [USER] [LEVEL1] User created: Bob

--------------------------------
[#8] [Runtime] [SYSTEMLOG] [LEVEL1] GET /users/Bob
[#9] [Runtime] [USER] [LEVEL1] User found: Bob

--------------------------------
[#10] [Runtime] [SYSTEMLOG] [LEVEL1] POST /users/Bob/grow
[#11] [Runtime] [USER] [LEVEL1] Growing User: Bob
[#12] [Bob] [USER] [LEVEL2] 15 increasing by 1
[#13] [Bob] [USER] [LEVEL2] Age is now 16
[#14] [Runtime] [USER] [LEVEL1] Growth complete. Age: 16

--------------------------------
[#15] [Runtime] [SYSTEMLOG] [LEVEL1] PATCH /users/Bob
[#16] [Runtime] [USER] [LEVEL1] Changing age for: Bob
[#17] [Runtime] [USER] [LEVEL1] Age changed to: 20

--------------------------------
[#18] [Runtime] [SYSTEMLOG] [LEVEL1] PUT /users/Bob
[#19] [Runtime] [USER] [LEVEL1] Replacing User: Bob
[#20] [Runtime] [USER] [LEVEL1] User replacement complete

--------------------------------
[#21] [Runtime] [SYSTEMLOG] [LEVEL1] GET /users/Bob
[#22] [Runtime] [USER] [LEVEL1] User found: Bob

--------------------------------
[#23] [Runtime] [SYSTEMLOG] [LEVEL1] DELETE /users/Bob
[#24] [Runtime] [USER] [LEVEL1] Deleting User: Bob
[#25] [Runtime] [USER] [LEVEL1] User deleted: Bob

--------------------------------
[#26] [Runtime] [SYSTEMLOG] [LEVEL1] GET /users/Bob
[ERROR]: [Runtime] User not found: Bob%       
```

`TestClient(fastAPIapp)` allows FastAPI routes to be triggered directly from Python.

The methods correspond to the FastAPI methods:

```py
client.get()
client.post()
client.put()
client.patch()
client.delete()
```

For example:

```text
client.post("/users", json={...})
↓
@fastAPIapp.post("/users")
↓
createUser(user)
↓
Python Logic
↓
Response
```

---

### [References](#sections)

> * [Link to FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
> * [Link to FastAPI Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/)
> * [Link to FastAPI Request Body](https://fastapi.tiangolo.com/tutorial/body/)
> * [Link to FastAPI Testing](https://fastapi.tiangolo.com/tutorial/testing/)

---

[:arrow_up: Return to Top](#fastapi)
