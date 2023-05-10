
darbuotojai = [
    {
        "vardas": "Audrius Spiridavicius",
        "atlyginimas": 123123
    },
    {
        "vardas": "Jonas jonaitis",
       # "atlyginimas": 123123 # ar visada visi irasai privalo tureti tiek varda tiek atlyginima? ar gali tureti tik varda arba tik atlyginima?
    }
]

d = set()
for darbuotojas in darbuotojai:
    atlyginimas = int(darbuotojas.get("atlyginimas",0))
    darbuotojo_vardas = darbuotojas.get("vardas","missing!!")
    vardas = darbuotojas["vardas"].split(" ")[0]
    pavarde = darbuotojas["vardas"].split(" ")[1]
    if len(darbuotojas["vardas"]) > 5 and atlyginimas > 9000:

        print(f"darbuotojo pavarde yra: {pavarde} jis uzdirba tiek pinigu: {darbuotojas['atlyginimas']}")
        d.add(pavarde)
for pavarde in d:
    print(f"jeigu tai yra jusu pavarde, jus uzdirbate daug pinigu {pavarde}\n")
print(d)

while True:
    _vardas = input("Prasome ivesti varda: ")
    if _vardas == "0":
        break
    _pavarde = input("prasome ivesti pavarde: ")
    _atlyginimas = input("prasome ivesti atlyginimas: ")
    #clear()
    darbuotojai.append({"vardas": f"{_vardas} {_pavarde}", "atlyginimas": _atlyginimas})
    darbuotojai
print(darbuotojai)
