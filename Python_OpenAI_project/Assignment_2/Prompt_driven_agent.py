import os
from openai import OpenAI
import pandas as pd


# Step 1: Mock Input Data (5 task descriptions)
task_descriptions = [
    "Install the battery module in the rear compartment, connect to the high-voltage harness, and verify torque on fasteners.",
    "Calibrate the ADAS (Advanced Driver Assistance Systems) radar sensors on the front bumper using factory alignment targets.",
    "Apply anti-corrosion sealant to all exposed welds on the door panels before painting.",
    "Perform leak test on coolant system after radiator installation. Record pressure readings and verify against specifications.",
    "Program the infotainment ECU with the latest software package and validate connectivity with dashboard display."
]

client = OpenAI(
    base_url="https://aiportalapi.stu-platform.live/jpe",
    api_key="sk-v7MixFROMXjbzCX8NcdSDA"
)


# Replace with your actual deployment name (from Azure OpenAI Studio)
deployment_name = "gpt-4o-mini"

# Step 3: Prompt-driven instruction generation function
def generate_instruction(task: str) -> str:
    prompt = f"""
You are an expert automotive manufacturing supervisor. Generate step-by-step work instructions for the following new model task. 
Include:
- Safety precautions
- Required tools (if any)
- Acceptance checks

Write in clear, numbered steps suitable for production workers.

Task:
\"\"\"{task}\"\"\"

Work Instructions:
"""
    response = client.chat.completions.create(
    model="GPT-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature=0,
 )
    return response.choices[0].message.content.strip()

results = []


# Step 4: Execute and print results
# Thực thi
if __name__ == "__main__":
    for i, task in enumerate(task_descriptions, start=1):
        try:
            print(f"--- Task {i} ---")
            print(f"Description: {task}")
            instructions = generate_instruction(task)
            print("Generated Instructions:")
            print(instructions)
            print()

            # Lưu vào kết quả
            results.append({
                "Task Number": i,
                "Description": task,
                "Work Instructions": instructions
            })

        except Exception as e:
            print(f"[ERROR] Failed to process Task {i}: {e}\n")

    # Xuất ra Excel
    df = pd.DataFrame(results)
    df.to_excel("work_instructions.xlsx", index=False)
    print("✅ Kết quả đã được lưu vào file 'work_instructions.xlsx'")