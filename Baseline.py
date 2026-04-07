import os
from openai import OpenAI
from env import SupportEnv
from models import Action

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def simple_policy(obs):
    return Action(
        action_type="classify_ticket",
        content="billing"
    )

def run():
    env = SupportEnv()
    obs = env.reset()
    total = 0

    for _ in range(5):
        action = simple_policy(obs)
        obs, reward, done, _ = env.step(action)
        total += reward.score
        if done:
            break

    print("Baseline Score:", total)

if __name__ == "__main__":
    run()
