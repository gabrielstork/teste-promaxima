# Desafio (Django + Scraping)


https://user-images.githubusercontent.com/86558706/156783006-7c6e2c08-b026-4043-9ae7-35d8441f7a84.mp4


Foi utilizado o `BeautifulSoup` para raspagem de dados no [site requisitado](https://economizaalagoas.sefaz.al.gov.br/exibicaoPrecoCombustivel.htm?codTipoCombustivel=1). E foi feita a aplicação `Django` + `SQLite`, que permite **adicionar**, **editar**,**deletar** e **atualizar** (todos os dados, menos os criados manualmente pelo usuário, são substituídos pelos novos dados que serão obtidos na raspagem) os itens. Além de recursos extras como a **ordenação** dos dados na lista de acordo com um campo e a opção de selecionar a quantidade de itens exibidos por **página**.

## Execução

Para executar localmente a aplicação, primeiramente o `Python` deve estar instalado em sua máquina (a versão utilizada para esse projeto foi a `3.9.6`). Para instalar a versão de sua preferência basta acessar o [site oficial](https://www.python.org/).

O próximo passo é clonar esse repositório para a sua máquina, para isso, em seu teminarl, utilize o comando (caso ainda não tenha o `git` instalado, acesse [esse site](https://git-scm.com/downloads)):

```sh
git clone https://github.com/gabrielstork/teste-promaxima.git
```

Agora, pelo terminal, entre na pasta `src` presente no diretório do repositório clonado. É lá que todos os arquivos necessários estão. 

Alguns pacotes `Python` são necessários para o funcionamento dessa aplicação, e eles já estão listados com sua devida versão no arquivo `requirements.txt`. Para os instalar digite:

```sh
pip install -r requirements.txt
```

Agora tudo já está pronto para ser utilizado! Digite no terminal:

```sh
python manage.py runserver
```

E acesse (no meu caso) [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
