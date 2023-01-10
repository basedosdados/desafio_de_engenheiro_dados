# Desafio Vaga Data Engineer

Este desafio foi preparado de modo a replicar localmente a essência da arquitetura de dados da Base dos Dados. Assim, o candidato que se empenhar em resolver a questão proposta estará, automaticamente, estudando para entender melhor nossa infraestrutura e se preparando para contribuir ativamente nos nossos repositórios. Um efeito colateral de se construir um exercício abrangendo toda a arquitetura da BD é que o exercício ficou relativamente longo. Essa característca, contudo, não deve desencorajar o candidato. Todo o código enviado como resposta será considerado, ainda que o candidato não consiga concluir o exercício. Seguem-se instruções para o exercício.

## Questão

> Construa uma pipeline em Prefect que extrai os dados de operadoras planos de saúde do site da ANS, carrega os dados como uma tabela no Postgres e cria uma tabela derivada usando DBT. A tabela derivada dos dados brutos deve conter o total de planos por categoria em dezembro de 2019.

## Informações auxiliares:

Os dados de operadoras de saúde encontram-se no seguinte link: https://dadosabertos.ans.gov.br/FTP/Base_de_dados/Microdados/dados_dbc/beneficiarios/operadoras/

A categoria dos planos é representada pela variável `cd_contr`. A tabela abaixo mostra o que cada código significa:

| cd_contr |          Descrição          |
|:--------:|:---------------------------:|
|     1    |   'Individual ou Familiar'  |
|     2    |    'Coletivo Empresarial'   |
|     3    |    'Coletivo por adesão'    |
|     4    | 'Coletivo não identificado' |
|     0    |       'Não Informado'       |

A query de materialização da tabela deve ser escrita no arquivo `pipeline/ans/models/planos_cat.sql`. 

Após a implementação da pipeline, o candidato deve rodar a imagem do Docker usando:

```
docker-compose up
```

Se a solução implementada estiver correta o seguinte resultado será imprimido na tela:

```bash
        tipo_plano         | total_planos 
---------------------------+--------------
 Coletivo Empresarial      |     50540286
 Coletivo não identificado |         2233
 Coletivo por adesão       |      8682247
 Individual ou Familiar    |     13365372
 Não Informado             |        92649
```


## Dica

Uma boa forma de abordar esse problema é criar um código em python para fazer a extração, carregamento dos dados e transformação e, depois de se certificar que o código funciona localmente, o candidato implementa o código em Prefect e roda a imagem do Docker. Para entender como implementar o código em Prefect, o candidato pode ver como estão implementadas pipelines da Base dos Dados em produção no repositório [Pipelines](https://github.com/basedosdados/pipelines). Também é possível entender melhor sobre a parte de materialização da tabela em DBT acessando nosso repositório de [Queries](https://github.com/basedosdados/queries). Outra fonte de informações são as Wikis dos nossos repositórios. Boa sorte!

## Avaliação

Você será avaliado por:
- Cumprimento dos objetivos do desafio
- Organização geral do repositório
- Qualidade do código
- Qualidade da documentação


## Forma de Envio da Solução

- Faça um fork desse repositório
- Resolva o desafio da melhor maneira possível
- Tenha certeza que a solução é reprodutível em qualquer outra máquina
- Reponda o formulário com o link do seu repositório. Não esqueça de deixar ele público. 
