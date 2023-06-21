# Instruções para executar o projeto localmente com Docker

Pré-requisito instalado:

- Docker
- Docker Compose

Linux (Ubuntu): https://docs.docker.com/engine/install/ubuntu/

Mac: https://docs.docker.com/docker-for-mac/install/

Windows: https://docs.docker.com/docker-for-windows/install/

## Como executar:

Primeiramente, é preciso criar o arquivo `extra.py`. Ele armazena configurações pessoais usadas em ambiente de
desenvolvimento, ele é ignorado no repositório.

Após isso, rodar os seguintes comandos:

```console
cd docker/dev
docker-compose up
```

O `docker-compose up` vai subir os contâineres, o container com aplicação django vai estar acessível em
`localhost:8000`, contudo, antes de usar a aplicação ainda é necessário fazer algumas conigurações iniciais no banco de
dados. Para isso é preciso executar os seguintes comandos:

```console
cd docker/dev
docker-compose run --rm django bash -c "python manage.py createcachetable"
```

OBS: Os comandos devem ser executados de dentro da pasta `docker/dev`

## Comandos úteis:

Em geral, para executar um comando no contâiner da aplicação django basta utilizar:

```console
cd docker/dev
docker-compose run --rm django bash -c "<command>"
```

Para acessar o shell do contâiner use:

```console
cd docker/dev
docker-compose exec django bash
```

OBS: Os comandos devem ser executados de dentro da pasta `docker/dev`

## Debug usando PyCharm:

https://www.jetbrains.com/help/pycharm/using-docker-compose-as-a-remote-interpreter.html

## Restaurar dump

```console
docker exec -i plenae_db sh -c 'exec mysql -uroot -pplenae123 plenae_db < dump_2022_07_25_15_15_05_staging.sql'
cat backup.sql | docker exec -i plenae_db /usr/bin/mysql -u root --password=plenae123 plenae_db
```
