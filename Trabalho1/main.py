import threading

from Thread import Sensores
from database import Database
#Criando uma instancia
from database import Database  # Asegure-se que este módulo esteja correto

db = Database(database="bancoiot", collection="sensores")
sensores = Sensores(db)

# Cria uma thread para cada sensor
threads = []
for i in range(1, 4):  # Três sensores
    t = threading.Thread(target=sensores.sensor, args=(f"Sensor{i}", 5))
    t.start()
    threads.append(t)

