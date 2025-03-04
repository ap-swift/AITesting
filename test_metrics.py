import os
from openai import OpenAI
from nltk.translate.bleu_score import sentence_bleu
# from nltk.translate.meteor_score import meteor_score

# Получаем API-ключ из переменной окружения
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("❌ Ошибка: API-ключ не найден. Проверь переменные окружения!")

# Создаём клиент OpenAI
client = OpenAI(api_key=api_key)

def test_dif_params():
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an assistant that speaks like Shakespeare."},
            {"role": "user", "content": "What is love?"}
        ],
        temperature=0.8,
        max_tokens=150,
        frequency_penalty=0.5,
        presence_penalty=0.5,
        stop=[".", "\n"]
    )

    # Extract GPT-generated response
    generated_text = response.choices[0].message.content

    # Define the reference text (manually written expected output)
    reference = ["Ah, love, that most wondrous and elusive of emotions! It is a force both gentle and fierce, igniting the heart with passion’s flame"]

    # Tokenize the texts for BLEU calculation
    reference_tokens = [reference[0].split()]
    generated_tokens = generated_text.split()

    # Compute BLEU score
    bleu_score = sentence_bleu(reference_tokens, generated_tokens, weights=(0.5, 0.5, 0, 0))
    # Compute METEOR Score
    # meteor = meteor_score(reference_tokens, generated_text)


    print(f"Generated Response: {generated_text}")
    print(f"BLEU Score: {bleu_score:.4f}")
    # print(f"METEOR Score: {meteor:.4f}")

test_dif_params()

