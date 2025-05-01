from fastapi import FastAPI, Query
import random

app = FastAPI()

game_sessions = {}

def determine_winner(choice1, choice2):
    rules = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
    if choice1 == choice2:
        return "draw"
    return "player1" if rules[choice1] == choice2 else "player2"

@app.get("/api/start_session")
def start_session():
    session_id = str(random.randint(100000, 999999))
    game_sessions[session_id] = {"players": {}, "winner": None}
    return {"status": 1, "message": f"Session {session_id} was created successfully.", "sessionId": session_id}

@app.get("/api/join_session")
def join_session(sessionId: str = Query(...), username: str = Query(...)):
    if sessionId not in game_sessions:
        return {"status": 0, "message": "Cannot join a session – Session with this ID does not exist."}
    
    session = game_sessions[sessionId]
    if username in session["players"]:
        return {"status": 0, "message": "User already joined the session."}
    
    if len(session["players"]) >= 2:
        return {"status": 0, "message": "Session is already full."}
    
    choice = random.choice(["rock", "paper", "scissors"])
    session["players"][username] = choice
    
    if len(session["players"]) == 2:
        players = list(session["players"].keys())
        winner = determine_winner(session["players"][players[0]], session["players"][players[1]])
        session["winner"] = "draw" if winner == "draw" else players[0] if winner == "player1" else players[1]
    
    return {"status": 1, "message": "User joined successfully.", "username": username, "choice": choice}

@app.get("/api/session_info")
def session_info(sessionId: str = Query(...)):
    if sessionId not in game_sessions:
        return {"status": 0, "message": "Session with this ID does not exist."}
    
    session = game_sessions[sessionId]
    return {
        "status": 1,
        "players": session["players"],
        "winner": session["winner"]
    }