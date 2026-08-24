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

O `request.form.get("email")` procura no formulário enviado um elemento HTML com `name="email"`. O link entre o HTML e o Python é o nome do elemento do HTML passado, no caso a seguir, **`name`**:

```html
<input type="email" name="email">
```

```python
request.form.get("email")  # ← busca name="email"
```

Quando o formulário é enviado (`method="POST"`), o navegador envia todos os pares `name=valor`. O Flask transforma isso num dicionário com `request.form`. A chave é sempre o valo de name `name` . `id`, `class` e `placeholder` não importam para isso.

O `.get()` acessa um dicionário e define um valor padrão para parâmetros sem valor. `request.form["email"]` também funciona, mas lança erro se a chave não existir. `.get("email", "")` retorna `""` em vez de erro.

Exemplo completo:

```python
from flask import request

@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email", "")
    senha = request.form.get("senha", "")
    return f"Recebido: {email}"
```

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

## A keyword `with` e o módulo `json`

### `with` (context manager)

O `with` abre um recurso (como um arquivo) e garante que ele seja fechado automaticamente, mesmo se der erro:

```python
# sem with — precisa fechar manualmente
f = open("dados.json", "r")
conteudo = f.read()
f.close()

# com with — fecha sozinho
with open("dados.json", "r") as f:
    conteudo = f.read()
```

Sempre use `with` com arquivos. É mais curto e não esquece de fechar.

### Módulo `json`

O módulo `json` do Python converte entre dicionários/listas Python e texto JSON:

```python
import json

# Python → texto JSON (serializar)
dados = {"nome": "Gabriel", "idade": 25}
texto = json.dumps(dados)
# '{"nome": "Gabriel", "idade": 25}'

# texto JSON → Python (desserializar)
dados = json.loads('{"nome": "Gabriel", "idade": 25}')
# {"nome": "Gabriel", "idade": 25}
```

### Lendo e escrevendo arquivos JSON

```python
import json

# escrever
with open("dados.json", "w") as f:
    json.dump({"nome": "Gabriel"}, f)

# ler
with open("dados.json", "r") as f:
    dados = json.load(f)
```

`dump`/`load` trabalham diretamente com arquivos. `dumps`/`loads` trabalham com strings.

## Adicionando novas dependências

```bash
uv add nome-do-pacote
```