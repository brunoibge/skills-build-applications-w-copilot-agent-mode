---
agent: 'agent'
model: GPT-4.1
description: 'Criar o projeto Django Octofit Tracker e inicializá-lo corretamente.'
---

# Criação do Projeto Django Octofit Tracker

Sua tarefa é criar o projeto Django no diretório `octofit-tracker/backend/octofit_tracker` usando o ambiente virtual Python existente em `octofit-tracker/backend/venv`, que já contém todos os pré-requisitos.

## Regras de execução

- Certifique-se de que estamos no diretório raiz do workspace e não mude de diretórios durante a execução dos comandos.
- Não crie um novo ambiente virtual Python.
- Use o ambiente virtual existente com: `source octofit-tracker/backend/venv/bin/activate`.
- Siga as instruções de configuração do projeto descritas em `.github/instructions/octofit_tracker_setup_project.instructions.md`.

## Passos

1. Verifique se a estrutura do projeto está correta e que o diretório `octofit-tracker/backend` existe.
2. Ative o ambiente virtual Python do projeto.
3. Crie o projeto Django com o comando: `django-admin startproject octofit_tracker octofit-tracker/backend`.
4. Confirme que o projeto foi criado em `octofit-tracker/backend/octofit_tracker`.
5. Navegue para o diretório do projeto Django e execute `python manage.py migrate` para aplicar as migrações iniciais.
6. Instrua o usuário para executar a aplicação Django a partir da configuração existente em `.vscode/launch.json` no repositório.

## Verificação

- Confirme que o projeto Django foi criado sem erros.
- Confirme que as migrações iniciais foram aplicadas com sucesso.
- Certifique-se de que o diretório do projeto e os arquivos iniciais do Django foram gerados corretamente.
