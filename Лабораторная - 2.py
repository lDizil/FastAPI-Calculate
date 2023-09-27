from fastapi import FastAPI

app = FastAPI()

@app.post("/calculator")
def calculator(first_number: int, second_number: int, operator: str):
    if operator == "+":
        result = first_number + second_number
        return result
    if operator == "-":
        result = first_number - second_number
        return result
    if operator == "*":
        result = first_number * second_number
        return result
    if operator == "**":
        result = first_number ** second_number
        return result
    if operator == "/" and second_number != 0:
        result = first_number / second_number
        return result
    if operator == "/" and second_number == 0:
        return "Unreal"
    else:
        return "Unreal"



