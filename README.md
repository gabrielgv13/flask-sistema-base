# Flask Sistema Base

Projeto base para aplicações Flask.

## Iniciando o projeto

```bash
uv sync
uv run app.py
```

O servidor inicia em `http://localhost:5000`.

## Estrutura

```
app.py              ← aplicação Flask
templates/
  index.html        ← template HTML
pyproject.toml      ← dependências
```

## Rotas

Uma rota conecta uma URL a uma função Python:

```python
@app.route("/")
def index():
    return "Olá, Mundo!"
```

Para retornar HTML de um arquivo, use `render_template`:

```python
from flask import render_template

@app.route("/")
def index():
    return render_template("index.html")
```

O Flask procura templates na pasta `templates/`.

## Templates HTML

Os templates usam Jinja2. Variáveis passadas por `render_template` ficam disponíveis no HTML:

```python
@app.route("/")
def index():
    return render_template("index.html", nome="Gabriel")
```

```html
<h1>Olá, {{ nome }}!</h1>
```

### Loops e condicionais

```html
<ul>
    {% for item in lista %}
        <li>{{ item }}</li>
    {% else %}
        <li>Nenhum item.</li>
    {% endfor %}
</ul>
```

## Recebendo dados de formulários

```python
from flask import request

@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email", "")
    senha = request.form.get("senha", "")
    return f"Recebido: {email}"
```

O HTML do formulário:

```html
<form method="POST" action="/login">
    <input type="email" name="email" placeholder="Email" required>
    <input type="password" name="senha" placeholder="Senha" required>
    <button type="submit">Entrar</button>
</form>
```

## Retornando JSON (API)

```python
from flask import jsonify

@app.route("/api/dados")
def dados():
    return jsonify({"mensagem": "ok"})
```

## Adicionando novas dependências

```bash
uv add nome-do-pacote
```