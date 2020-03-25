from flask import Flask
from flask_restful import Resource, Api
from resources.chamada import Chamadas, Chamada

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def cria_banco():
    banco.create_all()
   
api.add_resource(Chamadas, '/chamadas')
api.add_resource(Chamada, '/chamadas/<string:chamada_id>')

if __name__ == "__main__":
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)