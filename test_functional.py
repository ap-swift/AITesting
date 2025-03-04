import os
import openai
import pytest
from openai import OpenAI

# Получаем API-ключ из переменной окружения
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("❌ Ошибка: API-ключ не найден. Проверь переменные окружения!")

# Создаём клиент OpenAI
client = OpenAI(api_key=api_key)

# Функция для отправки запроса в OpenAI API
def chat_with_gpt(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=50
        )
        return response.choices[0].message.content
    except openai.OpenAIError as e:
        return f"❌ Ошибка API OpenAI: {str(e)}"
    except Exception as e:
        return f"❌ Общая ошибка: {str(e)}"


# Функция для отправки запроса в OpenAI API c 2-мя ролями
def chat_with_gpt2(prompt_dev, prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "developer", "content": prompt_dev}, {"role": "user", "content": prompt}],
            temperature=2,  # temperature controls how random or deterministic the response is. Higher values (closer to 2) → more creative and diverse responses.
            max_tokens=256
        )
        return response.choices[0].message.content
    except openai.OpenAIError as e:
        return f"❌ Ошибка API OpenAI: {str(e)}"
    except Exception as e:
        return f"❌ Общая ошибка: {str(e)}"


# Функциональные тесты
@pytest.mark.parametrize("prompt, expected", [
    ("Какая столица Франции?", "Париж"),
    ("Кто написал 'Войну и мир'?", "Толстой"),
    ("Сколько планет в Солнечной системе?", "8"),
])
def test_gpt_responses(prompt, expected):
    response = chat_with_gpt(prompt)
    assert expected in response, f"Ожидали '{expected}', но получили '{response}'"


@pytest.mark.parametrize("prompt_dev, prompt, expected", [
    ("Your task is to convert frase to correct English",
     "capital France?",
     "What is the capital of France?")
])
def test_gpt_correctEnglish(prompt_dev, prompt, expected):
    response = chat_with_gpt2(prompt_dev, prompt)
    assert expected in response, f"Ожидали '{expected}', но получили '{response}'"



