import wikipedia
wikipedia.set_lang("DE")

for i in range(100):
    print(wikipedia.random())
