from py2neo import Graph, Node, Relationship

class GameDatabase:
    def __init__(self, uri, user, password):
        self.graph = Graph(uri, auth=(user, password))

    def create_player(self, player_id, name):
        player_node = Node("Player", player_id=player_id, name=name)
        self.graph.create(player_node)
        print(f"Jogador {name} criado com sucesso!")

    def update_player(self, player_id, new_name):
        query = "MATCH (p:Player {player_id: $player_id}) SET p.name = $new_name RETURN p"
        self.graph.run(query, player_id=player_id, new_name=new_name)
        print(f"Jogador {player_id} atualizado para {new_name}")

    def delete_player(self, player_id):
        query = "MATCH (p:Player {player_id: $player_id}) DETACH DELETE p"
        self.graph.run(query, player_id=player_id)
        print(f"Jogador {player_id} excluído!")

    def create_match(self, match_id, players_scores):
        match_node = Node("Match", match_id=match_id)
        self.graph.create(match_node)

        for player_id, score in players_scores.items():
            player_node = self.graph.nodes.match("Player", player_id=player_id).first()
            if player_node:
                relation = Relationship(player_node, "PLAYED_IN", match_node, score=score)
                self.graph.create(relation)
            else:
                print(f"Jogador {player_id} não encontrado!")

        print(f"Partida {match_id} criada com sucesso!")

    def update_match_result(self, match_id, players_scores):
        query = """
        MATCH (m:Match {match_id: $match_id})-[r:PLAYED_IN]->(p:Player {player_id: $player_id})
        SET r.score = $score
        """
        for player_id, score in players_scores.items():
            self.graph.run(query, match_id=match_id, player_id=player_id, score=score)
        print(f"Resultados da partida {match_id} atualizados!")

    def delete_match(self, match_id):
        query = "MATCH (m:Match {match_id: $match_id}) DETACH DELETE m"
        self.graph.run(query, match_id=match_id)
        print(f"Partida {match_id} excluída!")

    def list_players(self):
        query = "MATCH (p:Player) RETURN p"
        players = self.graph.run(query)
        return [record['p'] for record in players]

    def get_player_history(self, player_id):
        query = """
        MATCH (p:Player {player_id: $player_id})-[r:PLAYED_IN]->(m:Match)
        RETURN m, r.score
        """
        result = self.graph.run(query, player_id=player_id)
        history = []
        for record in result:
            match = record["m"]
            score = record["r.score"]
            history.append((match, score))
        return history

    def get_match_info(self, match_id):
        query = """
        MATCH (m:Match {match_id: $match_id})<-[r:PLAYED_IN]-(p:Player)
        RETURN p, r.score
        """
        result = self.graph.run(query, match_id=match_id)
        match_info = []
        for record in result:
            player = record["p"]
            score = record["r.score"]
            match_info.append((player, score))
        return match_info
