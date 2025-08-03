import json
from openai import OpenAI

# ✅ Sample laptop database used for AI recommendations
laptops = [
    {
        "name": "Asus TUF Gaming F15",
        "cpu": "Intel Core i7-11800H",
        "ram": "16GB",
        "gpu": "NVIDIA RTX 3060",
        "price_million_vnd": 30,
        "weight_kg": 2.3,
        "battery_life_hr": 5,
        "suitable_for": ["gaming", "high-performance", "engineering"]
    },
    {
        "name": "MacBook Air M2",
        "cpu": "Apple M2",
        "ram": "8GB",
        "gpu": "Integrated",
        "price_million_vnd": 27,
        "weight_kg": 1.2,
        "battery_life_hr": 15,
        "suitable_for": ["students", "coding", "office", "portability"]
    },
    {
        "name": "Dell XPS 13 Plus",
        "cpu": "Intel Core i7-1360P",
        "ram": "16GB",
        "gpu": "Integrated",
        "price_million_vnd": 35,
        "weight_kg": 1.25,
        "battery_life_hr": 12,
        "suitable_for": ["productivity", "business", "portability"]
    }
]

# ✅ Initialize OpenAI client with proxy API endpoint and your API key
client = OpenAI(
    base_url="https://aiportalapi.stu-platform.live/jpe",
    api_key="YOUR_API_KEY" # Replace with your actual API key
)

# ✅ Function to generate chatbot response based on user input
def get_recommendation(user_input):
    # Set up system instructions for the assistant
    system_prompt = (
        "You are a helpful laptop consultant. Based on the user's needs, "
        "analyze and suggest a suitable laptop from the database. "
        "Always explain your reasoning based on specs like CPU, GPU, RAM, battery, and price."
    )

    # Convert laptop database to a readable JSON string for context
    product_info = json.dumps(laptops, indent=2, ensure_ascii=False)

    # Compose conversation messages
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"My laptop options:\n{product_info}"},
        {"role": "user", "content": user_input}
    ]

    # Call OpenAI API for response
    response = client.chat.completions.create(
        model="GPT-4o-mini",  # use "gpt-3.5-turbo" if needed
        messages=messages,
        temperature=0.6
    )

    # Return the chatbot's reply
    return response.choices[0].message.content

# ✅ Main interaction loop
if __name__ == "__main__":
    print("🧠 Laptop Consultant Chatbot")
    print("Type your laptop needs (e.g., gaming, student use, etc.) or type 'exit' to quit.")

    while True:
        user_query = input("\nYou: ")
        if user_query.lower() in ["exit", "quit"]:
            break
        result = get_recommendation(user_query)
        print(f"💡 Recommendation:\n{result}")