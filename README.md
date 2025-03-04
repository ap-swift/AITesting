# 📌 Automated Testing of LLM (GPT-4o) API with Python

🎯 Project Overview

This project focuses on automated testing of Large Language Models (LLMs) using OpenAI's GPT-4o-mini. The goal is to ensure that the model provides accurate, grammatically correct, and reliable responses in different scenarios.

🔹 Key Features

✅ Functional Testing – Verifies the correctness of factual responses.
✅ Grammar & Rephrasing Tests – Ensures correct sentence structure.
✅ Automated Test Execution – Uses Pytest for validation.
✅ Prompt Engineering – Optimizes responses using different role settings.
✅ Customizable API Calls – Adjusts temperature, max_tokens, and other parameters.
✅ BLEU Score Evaluation – Compares generated and expected responses.

---

## 🚀 **Installation & Setup**

### **1️⃣ Clone the repository**

```sh
git clone https://github.com/your-repo/llm-testing.git
```

### **2️⃣ Create a virtual environment (recommended)**

```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate    # Windows
```

### **3️⃣ Set up OpenAI API Key**

Create a `.env` file or export the key in your terminal:

```sh
export OPENAI_API_KEY="your_api_key"
```

For Windows (PowerShell):

```sh
$env:OPENAI_API_KEY="your_api_key"
```

---

## 📌 **Test Functions**

### **1️⃣ Functional Testing: Factual Responses**

This test verifies if GPT-4o provides **correct answers** to factual questions.

```python
@pytest.mark.parametrize("prompt, expected", [
    ("Какая столица Франции?", "Париж"),
    ("Кто написал 'Войну и мир'?", "Толстой"),
    ("Сколько планет в Солнечной системе?", "8"),
])
def test_gpt_responses(prompt, expected):
    response = chat_with_gpt(prompt)
    assert expected in response, f"Expected '{expected}', but got '{response}'"
```

### **2️⃣ Grammar & Sentence Correction**

This test checks if GPT-4o can **rephrase incorrect English sentences**.

```python
@pytest.mark.parametrize("prompt_dev, prompt, expected", [
    ("Your task is to convert the phrase into correct English",
     "capital France?",
     "What is the capital of France?")
])
def test_gpt_correctEnglish(prompt_dev, prompt, expected):
    response = chat_with_gpt2(prompt_dev, prompt)
    assert expected in response, f"Expected '{expected}', but got '{response}'"
```

---

3️⃣ Evaluating GPT-4o Output with BLEU Score

This script test_metrics.py runs a test prompt and evaluates GPT-4o’s response using the BLEU metric.

---

## 📌 **Running the Tests**

To execute all tests, run:

```sh
python3 -m pytest test_functional.py  
```

✅ **Expected Output (Example):**

```
✅ test_gpt_responses[Какая столица Франции?] - PASSED
✅ test_gpt_responses[Кто написал 'Войну и мир'?] - PASSED
❌ test_gpt_correctEnglish[capital France?] - FAILED
```

If a test fails, **analyze the response and adjust prompts or model settings.**

---
