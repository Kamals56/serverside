from fastapi import FastAPI, Form
import json

app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": "simple statistics calculator"
    }

@app.post("/api/factorial")
async def factorial(n):
    try:
        number = int(n)

        if number < 0:
            raise ValueError("Input must be a non-negative integer.")
        
        factorial = 1
        for i in range(2, n +1):
            factorial *= i
        
        return json.dumps({
            "status": 1,
            "parameter": n,
            "action" : "factorial",
            "result": factorial,

        })
    
    except (ValueError, TypeError) as e:
        return json.dumps({
            "status": 0,
            "message" : str(e)
            })

@app.post("/api/median")
async def median(numbers: str):
    try:
        numbers = json.loads(numbers) # converts json string to list

        if type(numbers) != list or any(type(n) not in [int, float] for n in numbers):
            raise ValueError("Input must be a list of numbers.")
        
        if len(numbers) == 0:
            raise ValueError ("List cannot be empty.")
        
        numbers.sort()
        mid = len(numbers) // 2

    
        median_value = numbers[mid] if len(numbers) % 2 == 1 else (numbers[mid - 1] + numbers[mid]) / 2

        return {
            "status": 1,
            "parameter": numbers,
            "action": "median",
            "result": median_value
        }

    except (ValueError, TypeError) as e:
        return {
            "status": 0,
            "message": str(e)
        }
    
@app.post("/api/variance")

async def variance(numbers: str):
    try:

         numbers = json.loads(numbers) # converts json string to list
     
         if type(numbers) != list or any(type(n) not in [int, float] for n in numbers):
            raise ValueError("Input must be a list of numbers.")
         
         if len(numbers) == 0:
            raise ValueError ("List cannot be empty.")
         mean = 0
         for number in numbers:
            mean += number

         mean = mean // len(numbers)

         variance = 0
         for number in numbers:
             variance += (number - mean)**2

         variance = variance // len(numbers)
        
         return{
             "status": 1,
             "parameter": numbers,
             "action": "variance",
             "result": variance
         }
    except (ValueError, TypeError) as e:
        return {
            "status": 0,
            "message": str(e)
        }
    

@app.post("/api/pstdev")

async def standard_deviation (number: str):
    try:
        numbers = [int(x) for x in number.split(',')] # converts json string to list

        if type(numbers) != list or any(type(n) not in [int, float] for n in numbers):
            raise ValueError("Input must be a list of numbers.")
            
        if len(numbers) == 0:            
            raise ValueError ("List cannot be empty.")
        
        mean = 0
        for number in numbers:
            mean += number

        mean = mean // len(numbers)

        summation = 0
        for number in numbers:
            summation += (number - mean)**2

        standard_deviation = (summation // len(numbers))**0.5

        return{
            "status": 1,
            "parameter": numbers,
            "action": "standard_deviation/pstdev",
            "standard_deviation": standard_deviation
        }
    
    except (ValueError, TypeError) as e:
        return{
            "status": 0,
            "message": str(e)
        }

