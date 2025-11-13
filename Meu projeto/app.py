from flask import Flask, render_template, request, redirect
from models.tarefas import adicionar_tarefa, listar_tarefas
app = Flask(__name__)
@app.route('/')
def index():
 return render_template('index.html', tarefas=listar_tarefas())
@app.route('/add', methods=['POST'])
def add():
 nome = request.form['tarefa']
 adicionar_tarefa(nome)
 return redirect('/')
if __name__ == '__main__':
 app.run(debug=True) 