# API de Usuários - Python Flask

Uma API RESTful desenvolvida em Python utilizando Flask, implementando boas práticas de programação e separação de camadas.

## 🏗️ Arquitetura

Esta API foi desenvolvida seguindo os princípios de **Clean Architecture** e **Separation of Concerns**, organizando o código em camadas bem definidas:

### Estrutura de Camadas

```
src/
├── controllers/     # Camada de Apresentação
├── services/        # Camada de Lógica de Negócio
├── repositories/    # Camada de Acesso aos Dados
├── models/          # Modelos de Dados
├── config.py        # Configurações da Aplicação
└── main.py          # Ponto de Entrada da Aplicação
```

#### 1. **Camada de Apresentação (Controllers)**
- Responsável por lidar com requisições HTTP
- Validação de entrada e formatação de resposta
- Conversão entre formatos HTTP e objetos de domínio

#### 2. **Camada de Lógica de Negócio (Services)**
- Implementa as regras de negócio da aplicação
- Validações de domínio
- Orquestração entre diferentes repositórios

#### 3. **Camada de Acesso aos Dados (Repositories)**
- Abstrai o acesso ao banco de dados
- Operações CRUD básicas
- Consultas específicas de dados

#### 4. **Camada de Modelos (Models)**
- Definição das entidades do domínio
- Mapeamento objeto-relacional (ORM)

## 🚀 Tecnologias Utilizadas

- **Python 3.11**
- **Flask** - Framework web
- **SQLAlchemy** - ORM para banco de dados
- **SQLite** - Banco de dados (desenvolvimento)
- **Flask-CORS** - Suporte a CORS
- **pytest** - Framework de testes
- **pytest-flask** - Extensão do pytest para Flask

## 📋 Pré-requisitos

- Python 3.11 ou superior
- pip (gerenciador de pacotes Python)

## 🔧 Instalação e Configuração

### 1. Clone o repositório
```bash
git clone <url-do-repositorio>
cd api_project
```

### 2. Ative o ambiente virtual
```bash
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação
```bash
python src/main.py
```

A API estará disponível em `http://localhost:5000`

## 🧪 Executando os Testes

### Testes Unitários
```bash
python -m pytest tests/ -v
```

### Testes com Cobertura
```bash
python -m pytest tests/ --cov=src --cov-report=html
```

## 📚 Documentação da API

### Base URL
```
http://localhost:5000
```

### Health Check
```http
GET /health
```

**Resposta:**
```json
{
    "status": "healthy",
    "message": "API está funcionando"
}
```

### Endpoints de Usuários

#### 1. Listar todos os usuários
```http
GET /api/users
```

**Resposta de Sucesso (200):**
```json
{
    "success": true,
    "data": [
        {
            "id": 1,
            "username": "usuario1",
            "email": "usuario1@example.com"
        }
    ],
    "message": "Usuários recuperados com sucesso"
}
```

#### 2. Buscar usuário por ID
```http
GET /api/users/{id}
```

**Parâmetros:**
- `id` (integer): ID do usuário

**Resposta de Sucesso (200):**
```json
{
    "success": true,
    "data": {
        "id": 1,
        "username": "usuario1",
        "email": "usuario1@example.com"
    },
    "message": "Usuário recuperado com sucesso"
}
```

**Resposta de Erro (404):**
```json
{
    "success": false,
    "error": "Usuário com ID 1 não encontrado",
    "message": "Usuário não encontrado"
}
```

#### 3. Criar novo usuário
```http
POST /api/users
Content-Type: application/json
```

**Corpo da Requisição:**
```json
{
    "username": "novousuario",
    "email": "novo@example.com"
}
```

**Resposta de Sucesso (201):**
```json
{
    "success": true,
    "data": {
        "id": 2,
        "username": "novousuario",
        "email": "novo@example.com"
    },
    "message": "Usuário criado com sucesso"
}
```

**Resposta de Erro (400):**
```json
{
    "success": false,
    "error": "Nome de usuário é obrigatório",
    "message": "Dados inválidos"
}
```

#### 4. Atualizar usuário
```http
PUT /api/users/{id}
Content-Type: application/json
```

**Parâmetros:**
- `id` (integer): ID do usuário

**Corpo da Requisição:**
```json
{
    "username": "usuarioatualizado",
    "email": "atualizado@example.com"
}
```

**Resposta de Sucesso (200):**
```json
{
    "success": true,
    "data": {
        "id": 1,
        "username": "usuarioatualizado",
        "email": "atualizado@example.com"
    },
    "message": "Usuário atualizado com sucesso"
}
```

#### 5. Remover usuário
```http
DELETE /api/users/{id}
```

**Parâmetros:**
- `id` (integer): ID do usuário

**Resposta de Sucesso (200):**
```json
{
    "success": true,
    "message": "Usuário removido com sucesso"
}
```

## 🔒 Validações Implementadas

### Validações de Username
- Mínimo de 3 caracteres
- Máximo de 80 caracteres
- Apenas letras, números, underscore (_) e hífen (-)
- Deve ser único no sistema

### Validações de Email
- Formato válido de email (contém @ e .)
- Máximo de 120 caracteres
- Deve ser único no sistema

## 🏛️ Padrões de Resposta

Todas as respostas da API seguem um padrão consistente:

### Resposta de Sucesso
```json
{
    "success": true,
    "data": { /* dados da resposta */ },
    "message": "Mensagem descritiva"
}
```

### Resposta de Erro
```json
{
    "success": false,
    "error": "Descrição detalhada do erro",
    "message": "Mensagem amigável ao usuário"
}
```

## 🔧 Configuração de Ambientes

A aplicação suporta diferentes configurações para diferentes ambientes:

### Desenvolvimento (padrão)
```python
FLASK_ENV=development
DEBUG=True
```

### Produção
```python
FLASK_ENV=production
DEBUG=False
SECRET_KEY=sua-chave-secreta-segura
```

### Testes
```python
FLASK_ENV=testing
TESTING=True
```

## 🚀 Deploy

### Usando Flask (Desenvolvimento)
```bash
python src/main.py
```

### Usando Gunicorn (Produção)
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 src.main:app
```

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👥 Autores

- Desenvolvido seguindo boas práticas de Clean Architecture
- Implementação de separação de camadas
- Testes unitários abrangentes
- Documentação completa da API

