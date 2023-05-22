import random

LISTA = [
            {
                "id": "1",
                "tema": "Anime"
            },
            {
                "id": "2",
                "tema": "Faculdade"
            },
            {
                "id": "3",
                "tema": "Filme"
            },
            {
                "id": "4",
                "tema": "Estudos"
            },
            {
                "id": "5",
                "tema": "Amizade"
            },
            {
                "id": "6",
                "tema": "Sonhos"
            },
            {
                "id": "7",
                "tema": "Infância"
            },
            {
                "id": "8",
                "tema": "Comida"
            },
            {
                "id": "9",
                "tema": "Lembranças"
            },
            {
                "id": "10",
                "tema": "Sobre Hoje"
            },
            {
                "id": "11",
                "tema": "Programação"
            },
            
            {
                "id": "12",
                "tema": "Música"
            },
            {
                "id": "13",
                "tema": "Astronomia"
            },
            {
                "id": "14",
                "tema": "Hobby"
            },
            {
                "id": "15",
                "tema": "Cultura"
            }    
        ]

def theme_choose(): 
    try:
        LISTA
    except ValueError:
        print("A resposta não chegou com o formato esperado.")

    dic = {}
    

    for i, value in enumerate(LISTA):
        dic[i] = value

    theme = random.choice(list(dic.values()))

    return theme['tema']
