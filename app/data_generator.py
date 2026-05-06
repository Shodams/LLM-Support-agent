"""
Generates a synthetic FAQ dataset for the chatbot.
This simulates a real-world knowledge base.
"""

import json
import random

TOPICS = [
    "refund policy",
    "shipping delays",
    "account issues",
    "subscription cancellation",
    "technical support"
]

def generate_dataset(n=100):
    data = []

    for _ in range(n):
        topic = random.choice(TOPICS)

        question = f"What is your {topic}?"
        answer = f"Our {topic} requires contacting support within 7 days."

        data.append({
            "question": question,
            "answer": answer
        })

    return data


if __name__ == "__main__":
    dataset = generate_dataset()

    with open("data/dataset.json", "w") as f:
        json.dump(dataset, f, indent=2)

    print("Dataset generated successfully.")
