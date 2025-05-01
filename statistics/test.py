import requests
import json

BASE_URL = "http://127.0.0.1:8000"  # Ensure your FastAPI server is running

def test_factorial():
    response = requests.post(f"{BASE_URL}/api/factorial", data={"n": "5"})
    print("Factorial:", response.json())

def test_median():
    numbers = json.dumps([1, 3, 3, 6, 7, 8, 9])  # Convert list to JSON string
    response = requests.post(f"{BASE_URL}/api/median", data={"numbers": numbers})
    print("Median:", response.json())

def test_variance():
    numbers = json.dumps([1, 2, 3, 4, 5])  # Convert list to JSON string
    response = requests.post(f"{BASE_URL}/api/variance", data={"numbers": numbers})
    print("Variance:", response.json())

def test_standard_deviation():
    numbers = "1,2,3,4,5"  # Send as a string
    response = requests.post(f"{BASE_URL}/api/pstdev", data={"number": numbers})
    print("Standard Deviation:", response.json())

if __name__ == "__main__":
    test_factorial()
    test_median()
    test_variance()
    test_standard_deviation()
