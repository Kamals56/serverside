import requests

BASE_URL = "http://127.0.0.1:8000"

def test_rock_paper_scissors():
    # Start a session
    response = requests.get(f"{BASE_URL}/api/start_session")
    session_data = response.json()
    session_id = session_data.get("sessionId")
    print("Session Created:", session_data)
    
    if not session_id:
        print("Failed to create a session")
        return
    
    # Join session with two users
    users = ["Kamal", "Ram"]
    for user in users:
        response = requests.get(f"{BASE_URL}/api/join_session", params={"sessionId": session_id, "username": user})
        print(f"{user} joined:", response.json())
    
    # Get session info
    response = requests.get(f"{BASE_URL}/api/session_info", params={"sessionId": session_id})
    print("Session Info:", response.json())

test_rock_paper_scissors()