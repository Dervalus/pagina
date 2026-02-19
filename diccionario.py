import data_base

def check(sentence):
    sentence = sentence.strip().lower()
    

    if sentence in data_base.past:
        return f"✅ Correct infinitive {data_base.past[sentence]}  "
    elif sentence in data_base.present:
        return f"✅ Correct infinitive {data_base.present[sentence]}  "
   
    else:
        return "❌ Incorrect"

user_input = input("Introduce un verbo en pasado: ")
result = check(user_input)
print(result)  