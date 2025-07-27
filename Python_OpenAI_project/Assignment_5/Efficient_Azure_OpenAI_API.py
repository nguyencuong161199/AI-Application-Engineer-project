"""
Efficient OpenAI API Usage with Function Calling, Batching, and Robust Retry Mechanisms
Topic: Travel Itinerary Planning

Sample Inputs:
    batch_inputs = [
        {"prompt": "Plan a travel itinerary.", "destination": "Paris", "days": 3},
        {"prompt": "Plan a travel itinerary.", "destination": "Tokyo", "days": 5},
        {"prompt": "Plan a travel itinerary.", "destination": "New York", "days": 4},
    ]

Sample Output (format):
    Result for Paris:
    <OpenAI API response or error message>
    ----------------------------------------
    Result for Tokyo:
    <OpenAI API response or error message>
    ----------------------------------------
    Result for New York:
    <OpenAI API response or error message>
    ----------------------------------------

How to run:
    python Efficient_Azure_OpenAI_API.py

"""
import os
import time
from openai import OpenAI, RateLimitError, APIError
from tenacity import retry, wait_random_exponential, stop_after_attempt, retry_if_exception_type

# =============================
# OpenAI Client Setup (Direct Key and URL)
# =============================
client = OpenAI(
    base_url="https://aiportalapi.stu-platform.live/jpe",
    api_key="sk-v7MixFROMXjbzCX8NcdSDA"
)

# =============================
# Function Calling Schema
# =============================
functions = [
    {
        "name": "generate_itinerary",
        "description": "Generate a travel itinerary for a given destination and duration.",
        "parameters": {
            "type": "object",
            "properties": {
                "destination": {"type": "string", "description": "Travel destination city or country"},
                "days": {"type": "integer", "description": "Number of days to plan for"}
            },
            "required": ["destination", "days"],
        },
    }
]

# =============================
# Retry Decorator for API Calls
# =============================
@retry(
    retry=retry_if_exception_type((RateLimitError, APIError)),
    wait=wait_random_exponential(min=1, max=10),
    stop=stop_after_attempt(5),
    reraise=True
)
def call_openai_function(prompt, destination, days):
    """
    Calls the OpenAI API with function calling for itinerary generation.
    Retries on rate limit or transient errors.
    """
    response = client.chat.completions.create(
        model="GPT-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        functions=functions,
        function_call={
            "name": "generate_itinerary",
            "arguments": f'{{"destination": "{destination}", "days": {days}}}'
        }
    )
    return response

# =============================
# Batch Processing
# =============================
def batch_process(inputs):
    """
    Processes a batch of input prompts using the OpenAI API.
    Handles exceptions gracefully and collects all results.
    """
    results = []
    for input_data in inputs:
        prompt = input_data["prompt"]
        destination = input_data["destination"]
        days = input_data["days"]
        try:
            res = call_openai_function(prompt, destination, days)
            results.append(res)
        except Exception as e:
            print(f"[ERROR] Error processing {destination}: {e}")
            results.append(None)
        time.sleep(1)  # Optional: prevent hitting rate limits aggressively
    return results

# =============================
# Example Batch Inputs
# =============================
batch_inputs = [
    {"prompt": "Plan a travel itinerary.", "destination": "Paris", "days": 3},
    {"prompt": "Plan a travel itinerary.", "destination": "Tokyo", "days": 5},
    {"prompt": "Plan a travel itinerary.", "destination": "New York", "days": 4},
]

# =============================
# Main Execution
# =============================
if __name__ == "__main__":
    outputs = batch_process(batch_inputs)
    for idx, output in enumerate(outputs):
        print(f"Result for {batch_inputs[idx]['destination']}:")
        if output:
            print(output)
        else:
            print("No result due to error or retry failure.")
        print("-" * 40)