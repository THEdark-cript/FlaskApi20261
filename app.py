from helpers.application import app
from controllers.AvicultorController import avicultor_bp
from controllers.AviarioController import aviario_bp
from controllers.AvicolaController import avicola_bp
from controllers.GalpaoController import galpao_bp


@app.get("/")
def index():
    return '{"versao":"1.0.1"}', 200


@app.get("/health")
def healthCheck():
    return "{'online':'true'}", 200


app.register_blueprint(avicultor_bp)
app.register_blueprint(aviario_bp)
app.register_blueprint(avicola_bp)
app.register_blueprint(galpao_bp)



# /avicultores - nome, cpf, caf, nascimento
# /avicolas
# /aviarios ou /galpoes
