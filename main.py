# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

from CameraModule import CameraModule


def main():

    cm = CameraModule()
    cm.DetectTrash()

if __name__ == "__main__":
    main()
