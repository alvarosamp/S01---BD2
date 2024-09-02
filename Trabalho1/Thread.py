import random
import time
from pymongo import collection
class Sensores:
    def __init__(self,database):
        self.database = database

    def sensor(self, nome, intervalo):
        while True:
            temp = random.randint(30, 40)
            print(f'A temperatura no {nome} é de {temp}°C. Daqui a {intervalo}s vamos medir novamente')
            # Busca o estado atual do sensor no MongoDB
            sensor_data = self.database.collection.find_one({'nomeSensor': nome})
            if sensor_data and sensor_data.get('sensorAlarmado'):
                print(f"Atenção! Temperatura muito alta! Verificar {nome}!")
                break  # Interrompe o loop se o sensor está alarmado
            # Atualiza o MongoDB com a nova temperatura e estado do alarme
            alarmado = temp > 38
            update_data = {'$set': {'valorSensor': temp, 'sensorAlarmado': alarmado}}
            self.database.collection.update_one({'nomeSensor': nome}, update_data)



            time.sleep(intervalo)