# Use Node.js Alpine como base
FROM node:20-alpine

# Definir diretório de trabalho
WORKDIR /app

# Copiar arquivos de dependências
COPY package*.json ./

# Instalar dependências
RUN npm ci --only=production

# Copiar código fonte
COPY . .

# Construir a aplicação para produção
RUN npm run build

# Expor a porta
EXPOSE 4200

# Comando para iniciar a aplicação
CMD ["npm", "start"]

