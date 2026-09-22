---
mode: 'agent'
model: GPT-4.1
description: 'Atualizar a app Django Octofit Tracker com MongoDB, CORS, recursos da API e roteamento.'
---

# Atualizações da App Django Octofit Tracker

- Todos os arquivos do projeto Django estão no diretório `octofit-tracker/backend/octofit_tracker`.

1. Atualize `settings.py` para conexão MongoDB e CORS.
2. Atualize `models.py`, `serializers.py`, `urls.py`, `views.py`, `tests.py` e `admin.py` para suportar coleções de usuários, equipes, atividades, placar de líderes e treinos.
3. Certifique-se de que `/` aponta para a API e `api_root` está presente em `urls.py`.

## Objetivo

Atualize a app Django Octofit Tracker para oferecer autenticação e perfis de usuários, equipes, registro de atividades, placar de líderes e sugestões de treinos personalizados por meio de uma API REST.

## Configuração do projeto

1. Não mude de diretório durante a execução dos comandos. Execute os comandos a partir da raiz do workspace, apontando os caminhos completos ou relativos a partir dela.
2. Use o ambiente virtual existente em `octofit-tracker/backend/venv` e ative-o com `source octofit-tracker/backend/venv/bin/activate`.
3. Atualize `octofit-tracker/backend/octofit_tracker/settings.py` para:
   - conectar ao banco MongoDB `octofit_db` usando Djongo, sem autenticação ou senha;
   - manter `ALLOWED_HOSTS` com `localhost` e `127.0.0.1`;
   - adicionar `{CODESPACE_NAME}-8000.app.github.dev` a `ALLOWED_HOSTS` quando `CODESPACE_NAME` estiver definido;
   - habilitar e configurar `corsheaders` no middleware e no `INSTALLED_APPS`;
   - permitir as origens, métodos e cabeçalhos necessários para o frontend da aplicação.
4. Verifique se `rest_framework`, `corsheaders`, `djongo` e a app do projeto estão configurados em `INSTALLED_APPS` quando aplicável.

## Recursos Django e API REST

Atualize `models.py`, `serializers.py`, `urls.py`, `views.py`, `tests.py` e `admin.py` para suportar as seguintes coleções e endpoints:

- usuários e perfis;
- equipes e seus membros;
- atividades registradas pelos usuários;
- placar de líderes com pontuação e classificação;
- treinos e sugestões de treino personalizadas.

Siga estas regras:

- Use os padrões existentes do Django REST Framework, incluindo serializers, viewsets e routers quando apropriado.
- Os serializers devem converter campos `ObjectId` para strings nas respostas da API.
- Registre os modelos relevantes no Django Admin.
- Garanta relacionamentos e validações coerentes entre usuários, equipes, atividades, placar e treinos.
- Adicione testes para os modelos, serializers, endpoints principais e roteamento.
- Use o ORM do Django para criar, consultar, atualizar e excluir dados. Não use scripts diretos do MongoDB para criar a estrutura ou os dados da aplicação.

## Roteamento

Atualize `octofit-tracker/backend/octofit_tracker/urls.py` para:

- fazer `/` apontar para a API;
- manter `api_root` presente e funcional;
- expor `api_root` em `/api/`;
- incluir as rotas dos recursos da API;
- usar `CODESPACE_NAME` para formar a URL pública `https://{CODESPACE_NAME}-8000.app.github.dev` quando essa variável existir e usar `http://localhost:8000` localmente;
- manter a rota administrativa em `/admin/`.

## Verificação

1. Execute as migrações necessárias usando o ambiente virtual existente.
2. Execute os testes Django do backend.
3. Verifique que o serviço MongoDB está executando com `ps aux | grep mongod`.
4. Inicie a aplicação pela configuração existente do VS Code, quando necessário.
5. Teste `/`, `/api/` e os endpoints principais usando `curl`, incluindo respostas bem-sucedidas e validações básicas.
6. Confirme que não foram introduzidas portas públicas além de `8000` para o backend, `3000` para o frontend e `27017` como porta privada do MongoDB.
