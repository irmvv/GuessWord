from translate import Translator
translator = Translator(to_lang="spanish")
i = "hello"
print(i)
i = translator.translate(i)
print(i)
