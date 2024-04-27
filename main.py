from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def get_name():
    return {
        "first_name": "Фамилия",
        "last_name": "Имя",
        "sur_name": "Отчество",
    }


@app.get("/users")
def get_contact_info():
    return {
        "phone": "+7-XXX-XXX-XX-XX",
    }


@app.get("/tools")
def get_info():
    return {
        "Labs": {
            "python": [
                "3.12",
                "FastAPI",
            ],
            "backend": [
                "lab1"
            ]
        },
    }