import random

jokes = [
    "🏴‍☠️ Why don't pirates take a shower before they walk the plank? They just wash up on shore! 🌊",
    "💀 What’s a pirate’s favorite letter? You might think it's R, but it’s really the C! 🏝️",
    "🗺️ How do pirates prefer to communicate? Aye-to-aye! 👁️‍🗨️",
    "💰 Why did the pirate go to the treasure island? Because it was arrr-rated! 🏴‍☠️",
    "⚓ What did the ocean say to the pirate? Nothing, it just waved! 🌊",
    "🎩 What kind of grades did the pirate get in school? High seas! 🏫"
]

print(random.choice(jokes))

def get_random_joke():
    return random.choice(jokes)