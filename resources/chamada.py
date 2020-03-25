from flask_restful import Resource, reqparse
from models.chamada import ChamadaModel

chamadas = [
          {
          'chamada_id': 'primeira',
          'nome': 'Luiz',
          'cpf': 123456789,
          'endereco': 'Canal 1',
          'telefone': 33611234,
          'cell': 91234567,
          'email': 'luiz123@gmail.com'
          },
          {
          'chamada_id': 'segunda',
          'nome': 'Murilo',
          'cpf': 67578404059,
          'endereco': 'Canal 2',
          'telefone': 33611234,
          'cell': 91234567,
          'email': 'murilo123@gmail.com'
          },
          {
          'chamada_id': 'terceiro',
          'nome': 'Ravanelli',
          'cpf': 59766207011,
          'endereco': 'Canal 3',
          'telefone': 33611234,
          'cell': 91234567,
          'email': 'rava123@gmail.com'
          }
]
    
class Chamadas(Resource):
    def get(self):
        return {'chamadas': [chamada.json() for chamada in ChamadaModel.query.all()]}

class Chamada(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str, required=True, help="O campo 'nome' não pode ficar em branco!")
    argumentos.add_argument('cpf', type=float, required=True, help="O campo 'cpf' não pode ficar em branco!")
    argumentos.add_argument('endereco', type=str, required=True, help="O campo 'endereco' não pode ficar em branco!")
    argumentos.add_argument('telefone')
    argumentos.add_argument('cell', type=int, required=True, help="O campo 'cell' não pode ficar em branco!")
    argumentos.add_argument('email')
    
    def get(self, chamada_id):
        chamada = ChamadaModel.find_chamada(chamada_id)
        if chamada:
            return chamada.json()
        return {'message': 'Chamada not found.'}, 404
    
    def post(self, chamada_id):
        if ChamadaModel.find_chamada(chamada_id):
            return {"message": "Chamada id '{}' already exists.".format(chamada_id)}, 400
        dados = Chamada.argumentos.parse_args()
        chamada = ChamadaModel(chamada_id, **dados)
        try:
            chamada.save_chamada()
        except:
            return {'message': 'An internal error ocurred trying to save chamada.'}, 500
        return chamada.json()
    
    def put(self, chamada_id):
        dados = Chamada.argumentos.parse_args()
        chamada_encontrada = ChamadaModel.find_chamada(chamada_id)
        if chamada_encontrada:
            chamada_encontrada.update_chamada(**dados)
            chamada_encontrada.save_chamada()
            return chamada_encontrada.json(), 200
        chamada = ChamadaModel(chamada_id, **dados)
        try:
            chamada.save_chamada()
        except:
            return {'message': 'An internal error ocurred trying to save chamada.'}, 500
        return chamada.json(), 201
    
    def delete(self, chamada_id):
        chamada = ChamadaModel.find_chamada(chamada_id)
        if chamada:
            try:
                chamada.delete_chamada()
            except:
                return {'message': 'An error ocurred trying to delete chamada.'}, 500
            return {'message': 'Chamada deleted.'}
        return {'message': 'Chamada not found.'}, 404