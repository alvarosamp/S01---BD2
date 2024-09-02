from database import Database
from helper import writeAJson

class ProductAnalyser:
    def __init__(self, database):
        self.db = database

    # 1 - Retornar o total de vendas por dia
    def total_vendas_por_dia(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {
                "_id": "$data_compra",
                "total_vendas": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}
            }},
            {"$sort": {"_id": 1}}
        ]
        result = self.db.collection.aggregate(pipeline)
        writeAJson.writeAJson(result, "Total de vendas por dia")
        return result

    # 2 - Retornar o produto mais vendido em todas as compras
    def produto_mais_vendido(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {
                "_id": "$produtos.descricao",
                "total_quantidade": {"$sum": "$produtos.quantidade"}
            }},
            {"$sort": {"total_quantidade": -1}},
            {"$limit": 1}
        ]
        result = self.db.collection.aggregate(pipeline)
        writeAJson.writeAJson(result, "Produto mais vendido")
        return result

    # 3 - Encontrar o cliente que mais gastou em uma única compra
    def cliente_que_mais_gastou(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {
                "_id": {"cliente_id": "$cliente_id", "data_compra": "$data_compra"},
                "total_gasto": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}
            }},
            {"$sort": {"total_gasto": -1}},
            {"$limit": 1}
        ]
        result = self.db.collection.aggregate(pipeline)
        writeAJson.writeAJson(result, "Cliente que mais gastou em uma compra")
        return result

    # 4 - Listar todos os produtos que tiveram uma quantidade vendida acima de 1 unidade
    def produtos_acima_de_uma_unidade(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {
                "_id": "$produtos.descricao",
                "total_quantidade": {"$sum": "$produtos.quantidade"}
            }},
            {"$match": {"total_quantidade": {"$gt": 1}}}
        ]
        result = self.db.collection.aggregate(pipeline)
        writeAJson.writeAJson(result, "Produtos vendidos em mais de uma unidade")
        return result
