from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class DataInput(BaseModel):
    data: List[str]

FULL_NAME = "john_doe"
DOB = "17091999"
EMAIL = "john@xyz.com"
ROLL_NUMBER = "ABCD123"

@app.post("/bfhl")
async def bfhl(input_data: DataInput):
    try:
        data = input_data.data
        even_numbers, odd_numbers, alphabets, special_chars = [], [], [], []
        num_sum = 0
        alpha_string = ""

        for item in data:
            if item.isdigit():
                num = int(item)
                if num % 2 == 0:
                    even_numbers.append(item)
                else:
                    odd_numbers.append(item)
                num_sum += num
            elif item.isalpha():
                alphabets.append(item.upper())
                alpha_string += item
            else:
                special_chars.append(item)

        concat_string = ""
        toggle = True
        for ch in alpha_string[::-1]:
            concat_string += ch.upper() if toggle else ch.lower()
            toggle = not toggle

        return {
            "is_success": True,
            "user_id": f"{FULL_NAME.lower()}_{DOB}",
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_chars,
            "sum": str(num_sum),
            "concat_string": concat_string
        }
    except Exception as e:
        return {"is_success": False, "error": str(e)}
