# Formulário de Notificação de Dengue - Frontend Angular

## 📋 Descrição

Este é um projeto Angular que implementa um formulário de notificação de dengue baseado no dicionário DENGBR25. O formulário foi desenvolvido com design inspirado no Google Forms e integra-se com uma API REST para persistência dos dados.

## 🚀 Tecnologias Utilizadas

- **Angular 19.0.0** - Framework principal
- **Angular Material** - Componentes de UI
- **TypeScript** - Linguagem de programação
- **SCSS** - Pré-processador CSS
- **RxJS** - Programação reativa
- **Node.js 20.18.0** - Runtime JavaScript
- **Docker** - Containerização com Node Alpine

## 📁 Estrutura do Projeto

```
dengue-form-app/
├── src/
│   ├── app/
│   │   ├── dengue-form/           # Componente principal do formulário
│   │   │   ├── dengue-form.ts     # Lógica do componente
│   │   │   ├── dengue-form.html   # Template HTML
│   │   │   ├── dengue-form.scss   # Estilos do componente
│   │   │   └── dengue-form.spec.ts # Testes unitários
│   │   ├── services/              # Serviços da aplicação
│   │   │   ├── api.ts            # Serviço de integração com API
│   │   │   └── api.spec.ts       # Testes do serviço
│   │   ├── app.ts                # Componente raiz
│   │   ├── app.html              # Template principal
│   │   └── app.config.ts         # Configurações da aplicação
│   ├── styles.scss               # Estilos globais
│   └── index.html               # Página principal
├── dist/                        # Build de produção
├── Dockerfile                   # Configuração Docker
├── .dockerignore               # Arquivos ignorados pelo Docker
├── package.json                # Dependências do projeto
└── README.md                   # Este arquivo
```

## 🏗️ Funcionalidades

### Formulário de Notificação
- **Seções organizadas** conforme dicionário DENGBR25:
  - 📋 Identificação da Notificação
  - 👤 Dados do Paciente
  - 🏠 Dados de Residência e Procedência
  - 🩺 Sinais e Sintomas Clínicos
  - 🏥 Doenças Pré-existentes
  - 🔬 Exames Laboratoriais
  - 🏥 Hospitalização e Local da Infecção
  - 📋 Encerramento do Caso

### Validações
- Campos obrigatórios marcados com asterisco (*)
- Validação de formato de data
- Validação de campos numéricos
- Feedback visual para campos inválidos

### Integração com API
- Conexão com API REST em `http://localhost:5000`
- Métodos CRUD para notificações de dengue
- Tratamento de erros com mensagens amigáveis
- Indicadores de carregamento durante requisições

### Interface do Usuário
- Design responsivo inspirado no Google Forms
- Componentes Material Design
- Feedback visual com snackbars
- Botões de ação: Enviar, Limpar, Testar Conexão

## 🛠️ Instalação e Execução

### Pré-requisitos
- Node.js 20.18.0 ou superior
- npm ou yarn
- Angular CLI

### Instalação
```bash
# Instalar dependências
npm install

# Instalar Angular CLI globalmente (se necessário)
npm install -g @angular/cli
```

### Execução em Desenvolvimento
```bash
# Iniciar servidor de desenvolvimento
ng serve

# Ou especificar host e porta
ng serve --host 0.0.0.0 --port 4200
```

A aplicação estará disponível em `http://localhost:4200`

### Build de Produção
```bash
# Gerar build otimizada
ng build --configuration production

# Os arquivos serão gerados em dist/dengue-form-app/browser/
```

### Execução com Docker
```bash
# Build da imagem
docker build -t dengue-form-app .

# Executar container
docker run -p 4200:4200 dengue-form-app
```

## 🧪 Testes

### Executar Testes Unitários
```bash
# Executar todos os testes
npm test

# Executar testes em modo headless
CHROME_BIN=/usr/bin/chromium-browser npm test -- --watch=false --browsers=ChromeHeadless
```

### Cobertura de Testes
- ✅ Componente principal da aplicação
- ✅ Componente do formulário de dengue
- ✅ Serviço de integração com API
- ✅ Validações de formulário
- ✅ Integração HTTP

**Resultado dos Testes:** 9/9 testes passando ✅

## 🔌 Integração com API

### Configuração
A aplicação está configurada para conectar-se com a API em:
```
Base URL: http://localhost:5000/api
Health Check: http://localhost:5000/health
```

### Endpoints Utilizados
- `POST /api/dengue-notifications` - Criar notificação
- `GET /api/dengue-notifications` - Listar notificações
- `GET /api/dengue-notifications/:id` - Buscar notificação específica
- `PUT /api/dengue-notifications/:id` - Atualizar notificação
- `DELETE /api/dengue-notifications/:id` - Remover notificação
- `GET /health` - Verificar status da API

### Modelo de Dados
```typescript
interface DengueNotification {
  id?: number;
  // Identificação da Notificação
  tp_not: string;
  dt_notific: string;
  sg_uf_not: string;
  // ... outros campos conforme dicionário DENGBR25
}
```

## 🎨 Design e UX

### Características do Design
- **Inspiração Google Forms**: Layout limpo e intuitivo
- **Material Design**: Componentes consistentes e acessíveis
- **Responsivo**: Funciona em desktop e mobile
- **Cores**: Paleta baseada em tons de roxo e azul
- **Tipografia**: Roboto (padrão Material Design)

### Experiência do Usuário
- Formulário dividido em seções lógicas
- Campos agrupados por contexto
- Validação em tempo real
- Feedback imediato para ações
- Indicadores de progresso
- Mensagens de erro claras

## 📊 Campos do Formulário

### Campos Obrigatórios (*)
- Tipo de Notificação
- Data da Notificação
- UF da Notificação
- Sexo do Paciente

### Tipos de Campos
- **Texto**: Códigos, nomes, observações
- **Data**: Datas de notificação, sintomas, exames
- **Seleção**: Dropdowns com opções predefinidas
- **Numérico**: Idades, códigos IBGE

### Validações Implementadas
- Campos obrigatórios não podem estar vazios
- Datas devem estar em formato válido
- Campos numéricos aceitam apenas números
- UF deve ter 2 caracteres

## 🚀 Deploy e Produção

### Build de Produção
O comando `ng build --configuration production` gera:
- Arquivos otimizados e minificados
- Bundle principal: ~835KB (comprimido: ~174KB)
- Polyfills: ~35KB (comprimido: ~11KB)
- Estilos: ~8KB (comprimido: ~1KB)

### Arquivos Gerados
```
dist/dengue-form-app/browser/
├── index.html              # Página principal
├── main-[hash].js         # Bundle principal da aplicação
├── polyfills-[hash].js    # Polyfills para compatibilidade
├── styles-[hash].css      # Estilos compilados
└── favicon.ico           # Ícone da aplicação
```

### Configuração de Servidor
Para servir a aplicação em produção, configure seu servidor web para:
- Servir arquivos estáticos da pasta `dist/dengue-form-app/browser/`
- Redirecionar todas as rotas para `index.html` (SPA routing)
- Configurar headers de cache apropriados

## 🔧 Configurações

### Ambiente de Desenvolvimento
```typescript
// src/app/services/api.ts
private apiUrl = 'http://localhost:5000/api';
```

### Configurações do Angular
```typescript
// angular.json
"serve": {
  "builder": "@angular-devkit/build-angular:dev-server",
  "options": {
    "host": "0.0.0.0",
    "port": 4200
  }
}
```

## 📝 Logs e Debugging

### Console do Navegador
A aplicação registra informações importantes no console:
- Status de conexão com API
- Dados enviados/recebidos
- Erros de validação
- Respostas da API

### Debugging
Para debug em desenvolvimento:
```bash
# Executar com source maps
ng serve --source-map

# Executar em modo verbose
ng serve --verbose
```

## 🤝 Contribuição

### Estrutura de Commits
- `feat:` Nova funcionalidade
- `fix:` Correção de bug
- `docs:` Documentação
- `style:` Formatação
- `refactor:` Refatoração
- `test:` Testes

### Padrões de Código
- Seguir Angular Style Guide
- Usar TypeScript strict mode
- Implementar testes para novas funcionalidades
- Documentar componentes e serviços

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais e de demonstração.

## 📞 Suporte

Para dúvidas ou problemas:
1. Verificar se a API está rodando em `http://localhost:5000`
2. Verificar logs do console do navegador
3. Executar testes para identificar problemas
4. Verificar configurações de CORS na API

---

**Desenvolvido com ❤️ usando Angular e Material Design**
