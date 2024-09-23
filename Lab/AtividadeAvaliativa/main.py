from database import Database
from writeAJson import writeAJson
from motorista_model import motorista_model
from motoristaDAO import MotoristaDAO

db = Database(database="Motorista", collection="Corridas")
motorista_model = motorista_model(database=db)


motorista = MotoristaDAO(motorista_model)
motorista.run()