Create the instructions for the prompt, asking the model to determine the language and generate a suitable title for the pre-loaded text excerpt that will be provided using triple backticks (```) delimiters.
Create the output_format with directions to include the text, language, and title, each on a separate line, using 'Text:', 'Language:', and 'Title:' as prefixes for each line.
Create the final_prompt by combining all parts and the delimited text to use.

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create the instructions
instructions = (
    "Infer the language and the number of sentences of the given text delimited by triple backticks. "
    "If the text contains more than one sentence, generate a suitable title for it; otherwise, write 'N/A' for the title. "
)

# Create the output format
output_format = (
    "Output format: Each on a separate line, use the following prefixes: 'Text:', 'Language:', 'Number of sentences:', and 'Title:'.\n"
)

# Example text excerpt (bạn cần thay thế text_excerpt bằng đoạn văn bản thực tế)
text_excerpt = "Your text excerpt goes here."

# Create the final prompt
prompt = instructions + output_format + f"```{text_excerpt}```"
response = get_response(prompt)
print(response)