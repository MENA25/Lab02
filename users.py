import json
from random import randint


# Archivo donde se almacenan los datos de usuarios
USER_FILE = 'users.txt'

# Función para cargar datos de usuarios desde un archivo
def load_users():
    try:
        with open(USER_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}  # Si el archivo no existe, retorna un diccionario vacío

# Función para guardar datos de usuarios en el archivo
def save_users(users):
    with open(USER_FILE, 'w') as file:
        json.dump(users, file)

# Función para registrar un usuario
def registerUser(name, password):
    users = load_users()
    if name in users:
        return "User already registered"
    else:
        users[name] = {"password": password, "session": False, "score": 0}
        save_users(users)
        return "User succesfully registered"

# Función para abrir o cerrar una sesión
def openCloseSession(name, password, flag):
    users = load_users()
    if name in users and users[name]["password"] == password:
        if flag:  # Abrir sesión
            users[name]["session"] = True
            save_users(users)
            return "Session was succesfully opened"
        else:  # Cerrar sesión
            users[name]["session"] = False
            save_users(users)
            return "Session was succesfully closed"
    return "error"

# Función para actualizar el puntaje
def updateScore(name, password, score):
    users = load_users()
    if name in users and users[name]["password"] == password and users[name]["session"]:
        users[name]["score"] = score
        save_users(users)
        return "Score was succesfully updated"
    return "error"

# Función para leer el puntaje
def getScore(name, password):
    users = load_users()
    if name in users and users[name]["password"] == password and users[name]["session"]:
        return users[name]["score"]
    return "error"

# Función para obtener la lista de usuarios conectados
def usersList(name, password):
    users = load_users()
    if name in users and users[name]["password"] == password and users[name]["session"]:
        connected_users = [{"name": u, "score": users[u]["score"]} for u in users if users[u]["session"]]
        return connected_users
    return "error"

# Función que genera una pregunta en una categoría
def question(name, password, cat):
    users = load_users()
    if name in users and users[name]["password"] == password and users[name]["session"]:
        # Aquí deberías agregar un conjunto de preguntas por categoría (cat)
        categoriaDeportes = [
            {
                "pregunta": "¿En qué año ganó Colombia la Copa América?",
                "opciones": "a. 2005 b. 2000 c. 2001 d. 2002",
                "rCorrecta": "c"
            },
            {
                "pregunta": "¿Qué selección ganó el Mundial de Sudáfrica?",
                "opciones": "a. España b. Alemania c. Países Bajos d. Uruguay",
                "rCorrecta": "a"
            },
            {
                "pregunta": "¿En qué año Óscar Figueroa obtuvo medalla de oro en unos Juegos Olímpicos?",
                "opciones": "a. 2012 b. 2015 c. 2016 d. 2020",
                "rCorrecta": "c"
            },
            {
                "pregunta": "¿Quién tiene el récord olímpico de 100 metros en atletismo?",
                "opciones": "a. Asafa Powell b. Yohan Blake c. Tyson Gay d. Usain Bolt",
                "rCorrecta": "d"
            },
            {
                "pregunta": "¿Qué deporte no hace parte de los Juegos Olímpicos?",
                "opciones": "a. Balonmano b. Atletismo c. Patinaje d. Tiro con arco",
                "rCorrecta": "c"
            },
            {
                "pregunta": "¿Quién fue la primera mujer en ganar una medalla olímpica?",
                "opciones": "a. Trudy Ederle b. Charlotte Cooper c. Alice Milliat d. Megan Rapinoe",
                "rCorrecta": "b"
            },
            {
                "pregunta": "¿Cuál es el deporte más popular en India?",
                "opciones": "a. Criquet b. Badminton c. Fútbol d. Mallakhamb",
                "rCorrecta": "a"
            },
            {
                "pregunta": "¿Cuál es el deporte más difícil del mundo?",
                "opciones": "a. Lucha libre b. Gimnasia c. Fútbol americano d. Boxeo",
                "rCorrecta": "d"
            },
            {
                "pregunta": "¿Cuántos colombianos asistieron a los Juegos Olímpicos?",
                "opciones": "a. 87 b. 85 c. 90 d. 93",
                "rCorrecta": "a"
            },
            {
                "pregunta": "¿Cada cuántos años se celebra el Mundial de fútbol?",
                "opciones": "a. 5 b. 3 c. 4 d. 2",
                "rCorrecta": "c"
            }
        ]
        categoriaCiencia = [
            {
                "pregunta": "¿En el MRU que magnitud varia constantemente?",
                "opciones": "A. Velocidad B. Aceleracion C. Pocicion D. Distancia",
                "rCorrecta": "c"
            },
            {
                "pregunta": "Qué órgano del cuerpo humano afecta el licor",
                "opciones": "a. Próstata B. Hígado C. Riñones D. Colón",
                "rCorrecta": "b"
            },
            {
                "pregunta": "Cual es la fórmula correcta para hallar energía cinética",
                "opciones": "A. Ec=(1/2)m^2*V B. Ec=(1/2)m*V^2 C. Ec=(1/2)*V^2 D. Ec=(1/2)m*V ",
                "rCorrecta": "b"
            },
            {
                "pregunta": "Cual es la derivada correcta de la función Ln(Sec(x))",
                "opciones": "A. 1/secx B. cscx*secx C. secx/tanx D. tanx",
                "rCorrecta": "d"
            },
            {
                "pregunta": "Cual de las siguientes afirmaciones es correcta",
                "opciones": "a. La primera derivada de la posicion es la aceleración b. La derivada de la aceleración es la posición c. La integral de la velocidad es posicion d. la integral de la aceleración es posicion",
                "rCorrecta": "c"
            },
            {
                "pregunta": "¿Cuantos huesos tiene el cuerpo humano?",
                "opciones": "a. 206 b. 305 c. 20 d. 300",
                "rCorrecta": "a"
            },
            {
                "pregunta": "¿Cual es el órgano que se encarga de producir insulina?",
                "opciones": "a. estómago b. riñones c. hígado d. páncreas",
                "rCorrecta": "d"
            },
            {
                "pregunta": "¿Quien fue el encargado de desarrollar la teoría del big bang?",
                "opciones": "a. Stephen Hawking b. Charles Darwin c. Georges Lemaître d. Albert einstein",
                "rCorrecta": "c"
            },
            {
                "pregunta": "¿Cual de los siguientes físicos descubrió la gravedad?",
                "opciones": "a. Albert einstein b. Isaac newton c. Stephen Hawking d. Charles Darwin",
                "rCorrecta": "b"
            },
            {
                "pregunta": "¿Quien fue la primera mujer en recibir un premio nobel?",
                "opciones": "a. lise meitner b. Marie Curie c. caroline herschel d. rosalind franklin",
                "rCorrecta": "b"
            }

        ]
        while True:
            nRespuestasMalas = 0
            n = 9
            nRespuestasCorrectas = 0
            if cat == 0:  ##categoria Deportes

                while True:

                    numeroAl = randint(0, n)
                    print(categoriaDeportes[numeroAl]["pregunta"])
                    print(categoriaDeportes[numeroAl]["opciones"])
                    eleccionC = input().lower()
                    if eleccionC == (categoriaDeportes[numeroAl]["rCorrecta"]):
                        print("Correcto")
                        nRespuestasCorrectas += 1
                    else:
                        print("Incorrecto")
                        print(f"La respuesta correcta es: {categoriaDeportes[numeroAl]["rCorrecta"]}")
                        nRespuestasMalas += 1
                    categoriaDeportes.pop(numeroAl)
                    if nRespuestasMalas == 3:  ##Penalizacion
                        print("Numero maximo de errores alcanzado \n¡Fin del juego!")
                        break
                    if len(categoriaDeportes) == 0:
                        print("Haz contestado todas las preguntas de la categoria")
                        break
                    n -= 1


            elif cat == 1:  ## Categoria Ciencia
                ##print("\n")
                while True:

                    numeroAl = randint(0, n)
                    print(categoriaCiencia[numeroAl]["pregunta"])
                    print(categoriaCiencia[numeroAl]["opciones"])
                    eleccionC = input().lower()
                    if eleccionC == (categoriaCiencia[numeroAl]["rCorrecta"]):
                        print("Correcto")
                        nRespuestasCorrectas += 1
                    else:
                        print("Incorrecto")
                        print(f"La respuesta correcta es: {categoriaCiencia[numeroAl]["rCorrecta"]}")
                        nRespuestasMalas += 1
                    categoriaCiencia.pop(numeroAl)
                    if nRespuestasMalas == 3:
                        print("Numero maximo de errores alcanzado \n¡Fin del juego!")
                        break
                    if len(categoriaCiencia) == 0:
                        print("Haz contestado todas las preguntas de la categoria")
                        break
                    n -= 1
    return "error"
