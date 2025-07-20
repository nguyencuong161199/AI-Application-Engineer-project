from openai import OpenAI
import os
api_version = "2024-07-01-preview"

client = OpenAI(
    base_url="",
    api_key=""
)
def summarize_meeting(transcript):
    # Step 2: Create summarization prompt
    prompt = f"Summarize the following meeting transcript with key points, decisions, and action items:\n\n{transcript}"

    # Step 3: Call OpenAI ChatCompletion API
    response = client.chat.completions.create(
        model="GPT-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant specialized in summarizing meeting notes."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=700
    )

    # Step 4: Return the summary
    return response.choices[0].message.content.strip()

def process_all_transcripts(folder_path):
    if not os.path.isdir(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        return

    output_folder = os.path.join(folder_path, "summaries")
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if filename.endswith(".txt") and os.path.isfile(file_path):
            print(f"Processing: {filename}")
            with open(file_path, "r", encoding="utf-8") as f:
                transcript = f.read()
            summary = summarize_meeting(transcript)

            summary_dir = os.path.join(os.path.dirname(folder_path), "summaries")
            os.makedirs(summary_dir, exist_ok=True)
            summary_path = os.path.join(summary_dir, f"summary_{filename}")

            # summary_path = os.path.join(output_folder, f"summary_{filename}")
            with open(summary_path, "w", encoding="utf-8") as out_f:
                out_f.write(summary)
            print(f"Saved summary to: {summary_path}\n")

def main():
    folder_path = "/Users/admin/AI-Application-Engineer-project/Python_OpenAI_project/Assignment_3/transcripts"
    print("=== AI-Powered Meeting Summarizer ===")
    process_all_transcripts(folder_path)

if __name__ == "__main__":
    main()