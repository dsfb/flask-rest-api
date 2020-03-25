from sql_alchemy import banco

class ChamadaModel(banco.Model):
    __tablename__ = 'chamadas'
    
    chamada_id = banco.Column(banco.String, primary_key=True)
    nome = banco.Column(banco.String(80))
    cpf = banco.Column(banco.Integer())
    endereco = banco.Column(banco.String())
    telefone = banco.Column(banco.Integer())
    cell = banco.Column(banco.Integer())
    email = banco.Column(banco.String())
    
    def __init__(self, chamada_id, nome, cpf, endereco, telefone, cell, email):
        self.chamada_id = chamada_id
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        self.cell = cell
        self.email = email

    def json(self):
        return {
            'chamada_id': self.chamada_id,
            'nome': self.nome,
            'cpf': self.cpf,
            'endereco': self.endereco,
            'telefone': self.telefone,
            'cell': self.cell,
            'email': self.email
        }
    
    @classmethod
    def find_chamada(cls, chamada_id):
        chamada = cls.query.filter_by(chamada_id=chamada_id).first()
        if chamada:
            return chamada
        return None

    def save_chamada(self):
        banco.session.add(self)
        banco.session.commit()
        
    def update_chamada(self, nome, cpf, endereco, telefone, cell, email):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        self.cell = cell
        self.email = email
    
    def delete_chamada(self):
        banco.session.delete(self)
        banco.session.commit()