#Há duas versões do código.

1º (inserção_terminal) Os dados para login, busca do orderbook e criação da ordem são inseridos pelo terminal. As chaves (client key, secret key e o userID) podem ser inseridas pela linha de comando.
```
python3 itbit.py -client_key -secret_key -userId
```

2º (inserção_arquivo) Os dados para login, busca do orderbook e criação da ordem são inseridos atráves da leitura do arquivo data.json, contendo todas as informações necessárias em um dicionário.
