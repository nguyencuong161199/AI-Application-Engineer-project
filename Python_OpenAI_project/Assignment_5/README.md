# Efficient OpenAI API Batch Processing with Function Calling

## How to Run

1. Ensure you have Python 3.x and the required packages:
   ```bash
   pip install openai tenacity
   ```
2. Run the script:
   ```bash
   python Efficient_Azure_OpenAI_API.py
   ```

## Design Choices
- **Batching:**
  - Inputs are provided as a Python list of dictionaries (`batch_inputs`).
  - The script processes each input in sequence, collecting all results.
- **Function Calling:**
  - Uses OpenAI's function calling to structure the response for travel itinerary planning.
- **Retry Logic:**
  - Uses `tenacity` to automatically retry API calls on rate limit or transient errors, with exponential backoff and a maximum of 5 attempts.
- **Exception Handling:**
  - All exceptions are caught and logged per input, so one failure does not stop the batch.
- **No Manual Input:**
  - All inputs are hardcoded; no use of `input()`.

## Sample Inputs
```
batch_inputs = [
    {"prompt": "Plan a travel itinerary.", "destination": "Paris", "days": 3},
    {"prompt": "Plan a travel itinerary.", "destination": "Tokyo", "days": 5},
    {"prompt": "Plan a travel itinerary.", "destination": "New York", "days": 4},
]
```

## Sample Output (format)
```
Result for Paris:
<OpenAI API response or error message>
----------------------------------------
Result for Tokyo:
<OpenAI API response or error message>
----------------------------------------
Result for New York:
<OpenAI API response or error message>
----------------------------------------
```

## Challenges & Solutions
- **Model Access Restriction:** The API key was restricted to a specific model (`GPT-4o-mini`). The script was updated to use the allowed model name.
- **Error Handling:** Ensured that all errors are logged and do not interrupt batch processing.
- **API Library Import:** Resolved missing `openai` library by installing the correct package for the Python environment. 