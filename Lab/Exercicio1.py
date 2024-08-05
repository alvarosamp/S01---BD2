class Professor:
    def __init__(self, nome):
        self.nome = nome

    def ministrar_aula(self, materia):
        print(f"O professor {self.nome} está ministrando aula de {materia}")


class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def presenca(self):
        print(f"O aluno {self.nome} está presente na aula")

class Aula:
    def __init__(self, professor, assunto, alunos):
        self.professor = professor
        self.assunto = assunto
        self.alunos = alunos
    
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
    
    def listar_presenca(self):
        print(f"Presença na aula sobre {self.assunto}, ministrada pelo professor {self.professor.nome}:")
        for aluno in self.alunos:
            aluno.presenca()

professor = Professor("Chris")
aluno1 = Aluno("Alvaro")
aluno2 = Aluno("Daniel")
aula = Aula(professor, "Programação Orientada a Objetos", [])
aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)
aula.listar_presenca() 
