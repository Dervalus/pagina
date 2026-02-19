import json
with open("archivo_present.json") as f:
    present = json.load(f)  # ahora rules es un diccionario

with open("archivo_past.json") as f:
    past = json.load(f)