from database import Database
from AnaliseDeProduto import ProductAnalyser

db = Database(database="mercado", collection="produtos")
db.resetDatabase()

product_analyser = ProductAnalyser(db)

product_analyser.produto_mais_vendido()
product_analyser.total_vendas_por_dia()
product_analyser.cliente_que_mais_gastou()
product_analyser.produtos_acima_de_uma_unidade()