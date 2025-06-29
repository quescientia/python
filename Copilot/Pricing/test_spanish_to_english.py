from transformers import MarianTokenizer, MarianMTModel

# Load the tokenizer and model
model_name = "Helsinki-NLP/opus-mt-es-en"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

def translate_spanish_to_english(text):
    input_ids = tokenizer.encode(f"es: {text}", return_tensors="pt")
    translated_tokens = model.generate(input_ids, max_length=50)
    translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True).replace(" en:", "")

    return translated_text

# Example usage
spanish_text = "¿Cómo estás?"
english_translation = translate_spanish_to_english(spanish_text)
print(f"Spanish: {spanish_text}")
print(f"English: {english_translation.replace("It's: ","")}")