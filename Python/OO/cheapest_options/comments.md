# Problema

## Rodar a aplicação

Requisitos:
- Python 3.6+

Rodar a partir do diretório "cheapest_options":
```
$ python3 main.py ${INPUT_FILE}
```
Ex:
```
$ python3 main.py "samples/sample_data.txt"
```

Para rodar os testes, a partir do diretório "cheapest_options":
```
$ python3 -m unittest
```

### Suposições:

- O tipo de cliente (Regular ou Rewards) não será enviado em branco;
- A lista de datas não tem necessariamente um limite (passado ou futuro), elas também não precisam estar em ordem cronológica, contanto que sejam datas que possam ser validadas;
- Final de semana é considerado apenas sábado e domingo; o preço total deve agregar valores para os diferentes tipos de dias, quando cabível (não assume o valor mais alto ou mais baixo);
- O arquivo de input terá um tamanho limitado e o programa rodará em um computador com recursos suficientes para processá-lo adequadamente. Não foi considerado um input contínuo como um arquivo de log que continua sendo escrito enquanto está sendo processado, por exemplo. 

### Design da aplicação:

O ponto de entrada foi criado no módulo main.py, que faz o setup e lida com o input do arquivo. A partir desse ponto, a função run() será chamada para cada linha do input, executando o seguinte fluxo da aplicação:
- InputProcessor parseia a linha, separando string com o tipo de cliente da lista de strings com as datas da reserva;
- ReservationDate converte as strings de datas em objetos datetime, além de já calcular informações sobre as datas, como o número de dias da semana, de final de semana e a extensão da estada;
- Registra se o cliente é Rewards ou Regular
- Price organiza os preços, instanciando as categorias de estabelecimento de acordo com as datas e do tipo de cliente da reserva. 
- A classe Establishment fornece as informações, como qual valor deve ser considerado de acordo com o tipo de data, de cliente e a categoria do estabelecimento.
- A partir das informações e do processamento feito, a saída é retornada na forma do nome do estabelecimento mais barato.

Além disso:
- _Helpers_: módulo com funções de suporte, mais genéricas e que podem ser reaproveitadas futuramente;
- _Enums_: utilizados para valores que não mudam necessariamente e que não precisam de uma grande lógica por trás;
- _Constants_: módulo com as constantes da aplicação. Foi colocado lá a tabela de preços no formato de dicionário - embora esteja como um objeto mutável e suscetível a alterações pelo código, o objetivo era abstrair da aplicação essas informações e emular um banco de dados não-relacional. 



### Execução da aplicação:
```
[user@user cheapest_options]$ python3 main.py "samples/sample_data.txt"
Econômico
Médio
Esbanjar
```

### Execução dos testes:
```
[user@user cheapest_options]$ python3 -m unittest
..........................................
----------------------------------------------------------------------
Ran 42 tests in 0.006s

OK
```

### Coverage report:

```
[user@user cheapest_options]$ coverage report

Name                             Stmts   Miss  Cover
----------------------------------------------------
constants.py                         1      0   100%
enums/__init__.py                    0      0   100%
enums/client.py                      4      0   100%
enums/stars.py                       5      0   100%
helpers/helpers.py                  40      0   100%
main.py                             29     15    48%
models/__init__.py                   0      0   100%
models/establishment.py             25      1    96%
models/input_processor.py           16      1    94%
models/price.py                     36      0   100%
models/reservation_date.py          13      0   100%
tests/__init__.py                    0      0   100%
tests/test_establishment.py         41      1    98%
tests/test_helpers.py               70      1    99%
tests/test_input_processor.py       40      1    98%
tests/test_main.py                  14      1    93%
tests/test_price.py                 25      1    96%
tests/test_reservation_date.py      22      1    95%
----------------------------------------------------
TOTAL                              381     23    94%
```