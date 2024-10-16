# yt-bot
Este é um projeto criado para o canal Maickon Rangel. Abaixo você encontra as instruções para te ajudar na configuração. O projeto tem a finalidade de conseguir postar videos no youtube através da ferramenta do google app script. O projeto usa um segundo script que é capaz de baixar os vídeos do youtube para que você possa fazer o upload no google drive.

# Como obter uma chave de API do YouTube

Siga os passos abaixo para gerar sua chave de API e utilizá-la no seu projeto:

## Passo 1: Acesse o Google Cloud Console

1. Vá para o Google Cloud Console: [https://console.cloud.google.com/](https://console.cloud.google.com/)
2. Faça login com sua conta Google.

## Passo 2: Crie um novo projeto

1. No topo da página, clique no menu suspenso do seletor de projeto.
2. Clique em "Novo Projeto".
3. Dê um nome ao projeto (por exemplo: "API YouTube").
4. Clique em "Criar".

## Passo 3: Ative a API do YouTube

1. No menu à esquerda, vá para **APIs e serviços** > **Biblioteca**.
2. Na barra de busca, digite **YouTube Data API v3**.
3. Clique na **YouTube Data API v3** nos resultados.
4. Clique em "Ativar".

## Passo 4: Crie credenciais de API

1. Após ativar a API, vá para **APIs e serviços** > **Credenciais** no menu à esquerda.
2. Clique em "Criar credenciais" e selecione **Chave de API**.
3. Sua chave de API será gerada. Copie essa chave.

## Passo 5: Use sua chave de API no projeto

Agora, basta inserir a chave de API no seu código Python em `youtube.py`, como no exemplo abaixo:

```python
# Substitua pela sua chave de API do YouTube
API_KEY = 'SUA_CHAVE_DE_API_AQUI'
```

# Python: Como configurar o projeto e instalar as bibliotecas necessárias

Siga os passos abaixo para configurar o ambiente e instalar todas as bibliotecas necessárias para o projeto.

## Passo 1: Instale o Python

- Certifique-se de que você tenha o Python instalado em seu sistema.

  - **Windows**: Baixe o Python a partir do site oficial: [https://www.python.org/downloads/](https://www.python.org/downloads/) e siga as instruções de instalação. Marque a opção "Add Python to PATH" durante a instalação.

  - **Linux/Mac**: O Python já vem pré-instalado. Para confirmar, abra o terminal e digite:

```bash
python3 --version
```

## Passo 2: Instale o pip

- O pip é o gerenciador de pacotes do Python, usado para instalar bibliotecas. Ele vem pré-instalado na maioria das instalações do Python. Verifique se o pip está instalado com:

```bash
pip --version
```

- Se não estiver instalado, siga as instruções em https://pip.pypa.io/en/stable/installation/.

## Passo 3: Abra o terminal ou prompt de comando

- **Windows**: Pressione `Win + R`, digite `cmd` e pressione `Enter`.
- **Linux/Mac**: Abra o terminal.

## Passo 4: Navegue até o diretório do projeto

- No terminal ou prompt de comando, vá até a pasta onde o projeto está localizado. Por exemplo, se o projeto estiver na pasta `Documentos/projeto`, digite o seguinte comando:

```bash
cd Documentos/projeto
```

## Passo 5: Instale as bibliotecas necessárias

- Agora que você está no diretório do projeto, execute o seguinte comando para instalar todas as bibliotecas:

```bash
pip install -r requirements.txt
```

- Este comando vai ler o arquivo requirements.txt (que contém as bibliotecas necessárias) e instalar todas elas automaticamente.


## Passo 6: Verifique a instalação

    - Depois que a instalação terminar, todas as bibliotecas mencionadas no requirements.txt estarão prontas para uso. Você pode confirmar isso tentando rodar o projeto com o Python.

## Passo 7: Executar o projeto

    - Agora que tudo está configurado, você pode executar o projeto normalmente usando:

```bash
    python nome_do_seu_arquivo.py
```