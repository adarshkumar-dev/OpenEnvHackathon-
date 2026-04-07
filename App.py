from fastapi import FastAPI
from env import SupportEnv
from models import Action

app = FastAPI()
env = SupportEnv()

@app.get("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: Action):
    obs, reward, done, info = env.step(action)
    return {
        "observation": obs.dict(),
        "reward": reward.dict(),
        "done": done,
        "info": info
    }
