# 💻 Laptop Consultant Chatbot using OpenAI

This project demonstrates a simple yet powerful chatbot that helps users choose a laptop based on their needs using the OpenAI API. It compares user requirements with a sample laptop database and returns a recommendation with explanations.

---

## ✅ Features

- Analyze user needs using OpenAI LLM (GPT-4o or GPT-3.5 Turbo)
- Match against a list of sample laptop specifications
- Return clear recommendations with reasoning (based on CPU, GPU, RAM, battery, and price)
- Console-based interaction loop

---

## 🧠 Requirements

- Python 3.8+
- Required packages:
  - `openai`
  - `json` (built-in)

Install OpenAI SDK:

```bash
pip install openai
```

---

## 🚀 How to Run

1. Clone this repo or copy the Python script.
2. Set your OpenAI API key:
   - Either set it as an environment variable:
     ```bash
     export OPENAI_API_KEY=your_api_key_here
     ```
   - Or insert directly in the script when initializing the OpenAI client.

3. Run the script:

```bash
python laptop_consultant_chatbot_updated.py
```

---

## 💬 Example Inputs

You can type queries like:

- `"I need a laptop for gaming under 30 million VND."`
- `"I’m a student looking for something light and long battery life."`
- `"What is a good machine for programming and portability?"`

---

## 📦 Sample Laptop Data

The chatbot compares against a hardcoded database of 3 laptops:
- Asus TUF Gaming F15 (gaming, high performance)
- MacBook Air M2 (students, coding, portability)
- Dell XPS 13 Plus (productivity, business)

You can expand this list easily by adding more dictionaries in the `laptops` array.

---

## 📄 License

This project is for educational and demo purposes only.