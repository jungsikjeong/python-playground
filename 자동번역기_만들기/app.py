import deepl

auth_key = "..."  # Replace with your key
translator = deepl.Translator(auth_key)

result = translator.translate_text("I like kimchi!", target_lang="KO")
print(result.text)  # "나는 김치를 좋아한다!"
