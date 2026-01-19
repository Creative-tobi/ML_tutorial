from fastapi import FastAPI
from pydantic import BaseModel

# 1. Initialize the App
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# 2. Define the Data Format (The "Form" users must fill)
class KeystrokeData(BaseModel):
    user_id: str
    dwell_time: float
    flight_time: float

# 3. Create a Test Route (To check if it's alive)
@app.get("/home")
def home():
    return {"message": "Campus Connect Security System is ONLINE 🟢"}

# 4. Create the Login Route (The Guard)
@app.post("/verify")
def verify_user(data: KeystrokeData):
    # We will connect the AI here later.
    # For now, let's just print what we received.
    print(f"Checking User: {data.user_id}")
    print(f"Speed: {data.dwell_time}ms / {data.flight_time}ms")
    
    return {"status": "Received", "verdict": "Analyzing..."}