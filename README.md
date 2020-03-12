# Studies

Repo for keeping notes, experiments and other studies related stuff.

# Full-stack apps

## Stack #1 (React-Python)

TODO (PROJECT SETUP):

- More pre-commit commands

TODO (BACKEND):

- RabbitMQ + pika lib
- Have name from input, propagate everywhere
- Celery
- Tests...
- Refactor readmodel to base, event store subscriptions...
- Refactor alchemy session
- Refactor reuse of model for json

TODO (FRONTEND):

- Simplify FLUX
- Stylize a bot more (esp navbar)
- Bootstrap theme
- Localizations. Localization tools
- Console errors (due to hot reload or smth like that)
- NPM install warnings (a few things depretiated)

TODO (APP LOGIC):

- Item name
- Delete item

## Overview of full stack apps

| Component                                | Stack #1 (React-Python)  |  status  | Stack #2 (Vue-Django)     | status | Stack #3 (.Net Core) | status |
| :--------------------------------------- | :----------------------- | :------: | :------------------------ | :----: | :------------------- | :----: |
| .                                        |                          |          |                           |        |                      |        |
| **PROJECT SETUP**                        |                          |          |                           |        |                      |        |
| One-command setup                        | Docker compose           | **DONE** | <- same (?)               |   td   | <- same (?)          |   td   |
| Minimal dependencies                     | Docker compose           | **DONE** | <- same (?)               |   td   | <- same (?)          |   td   |
| One-command local run                    | Bash                     | **DONE** | <- same (?)               |   td   | <- same (?)          |   td   |
| On-save checks                           | VS Code plugins          | **DONE** | <- same (?)               |   td   | <- same (?)          |   td   |
| Pre-commit checks                        | Pre-commit hooks         | **DONE** | <- same (?)               |   td   | <- same (?)          |   td   |
| Selenium tests                           | Robot tests              |    td    | (?)                       |   td   | (?)                  |   td   |
| .                                        |                          |          |                           |        |                      |        |
| **FRONTEND - TECH STACK**                |                          |          |                           |        |                      |        |
| Css framework                            | Bootstrap                | **DONE** | CSS grid                  |   td   | Pure (?)             |   td   |
| Web framework                            | React                    | **DONE** | Vue (?)                   |   td   | Vue (?)              |   td   |
| App framework                            | Flux                     | **DONE** | Vue (?)                   |   td   | Vue (?)              |   td   |
| Language                                 | ES6                      | **DONE** | <- same (?)               |   td   | Typescript           |   td   |
| Bundler                                  | Webpack                  | **DONE** | <- same (?)               |   td   | (?)                  |   td   |
| Packager                                 | NPM                      | **DONE** | <- same (?)               |   td   | Yarn                 |   td   |
| .                                        |                          |          |                           |        |                      |        |
| **FRONTEND - LIBS & TOOLS**              |                          |          |                           |        |                      |        |
| Routing                                  | React router             | **DONE** | React router              |   td   | Custom (?)           |   td   |
| Ajax requests                            | Superagent               | **DONE** | (?)                       |   td   | (?)                  |   td   |
| Transpiler                               | Babel                    | **DONE** |                           |   td   |                      |   td   |
| Integrations                             | React-Bootstrap          | **DONE** |                           |   td   |                      |   td   |
| Integrations                             | React-Router-Bootstrap   | **DONE** |                           |   td   |                      |   td   |
| Debugger                                 | (?)                      |    td    | (?)                       |   td   | (?)                  |   td   |
| Localization framework                   | React-Intl               |    td    | (?)                       |   td   | (?)                  |   td   |
| .                                        |                          |          |                           |        |                      |        |
| **FRONTEND - AUTOMATED CHECKS**          |                          |          |                           |        |                      |        |
| Code formatter                           | VS Code prettier         |    td    | (?)                       |   td   | (?)                  |   td   |
| Code quality checks                      | ESlint (?)               |    td    | (?)                       |   td   | (?)                  |   td   |
| Code complexity checks                   | ESlint (?)               |    td    | (?)                       |   td   | (?)                  |   td   |
| Static security checks                   | NPM audit (?)            |    td    | (?)                       |   td   | (?)                  |   td   |
| Tests                                    | (?)                      |    td    | (?)                       |   td   | (?)                  |   td   |
| Test coverage checks                     | (?)                      |    td    | (?)                       |   td   | (?)                  |   td   |
| .                                        |                          |          |                           |        |                      |        |
| **FRONTEND - CUSTOM PROGRAMMING**        |                          |          |                           |        |                      |        |
| Css customizations                       | SASS                     |    td    | <- same (?)               |   td   | <- same (?)          |   td   |
| Custom theme                             | (?)                      |    td    | <- same (?)               |   td   | <- same (?)          |   td   |
| Extensive logging (posts to back)        | Custom                   |    td    | (?)                       |   td   | (?)                  |   td   |
| Form validation mechanism                | Custom                   |    td    | Custom                    |   td   | Custom               |   td   |
| .                                        |                          |          |                           |        |                      |        |
| **BACKEND - TECH STACK**                 |                          |          |                           |        |                      |        |
| Language                                 | Python                   | **DONE** | Python                    |   td   | C#                   |   td   |
| Web framework                            | Flask                    | **DONE** | Django                    |   td   | ASP.Net Core         |   td   |
| REST - Swagger & schema validation       | FlaskRest&Schematics (?) |    td    | (?)                       |   td   | (?)                  |   td   |
| GraphQL Endpoints                        | (?)                      |    td    | (?)                       |   td   | (?)                  |   td   |
| Event store                              | MongoDB                  | **DONE** | (?)                       |   td   | (?)                  |   td   |
| Read model                               | PostgreSQL               | **DONE** | <- same (?)               |   td   | (?)                  |   td   |
| Read model - ORM                         | SQL Alchemy              | **DONE** | Django ORM                |   td   | (?)                  |   td   |
| Read model - Schema migrations           | Alembic                  |    td    | Django ORM migrations (?) |   td   | (?)                  |   td   |
| Session storage                          | Redis                    |    td    | (?)                       |   td   | (?)                  |   td   |
| Cashe storage                            | Redis                    | **DONE** | (?)                       |   td   | (?)                  |   td   |
| Async tasks framework                    | Celery + RabbitMQ        |    td    | (?)                       |   td   | (?)                  |   td   |
| Queue                                    | RabbitMQ + pika lib      |    td    | (?)                       |   td   | (?)                  |   td   |
| Full-text search                         | Elastic search           |    td    | (?)                       |   td   | (?)                  |   td   |
| .                                        |                          |          |                           |        |                      |        |
| **BACKEND - LIBS & TOOLS**               |                          |          |                           |        |                      |        |
| Debugger                                 | Pdb                      | **DONE** | (?)                       |   td   | (?)                  |   td   |
| Event store - Admin UI                   | MongoDB Express          | **DONE** | (?)                       |   td   | (?)                  |   td   |
| Read model - Admin UI                    | PgAdmin                  | **DONE** | (?)                       |   td   | (?)                  |   td   |
| Redis - Admin UI                         | (?)                      | **DONE** | (?)                       |   td   | (?)                  |   td   |
| Rabbit MQ - Admin UI                     | (?)                      | **DONE** | (?)                       |   td   | (?)                  |   td   |
| .                                        |                          |          |                           |        |                      |        |
| **BACKEND - AUTOMATED CHECKS**           |                          |          |                           |        |                      |        |
| Code formatter                           | Black                    | **DONE** | (?)                       |   td   | (?)                  |   td   |
| Code quality checks                      | Flake8                   | **DONE** | (?)                       |   td   | (?)                  |   td   |
| Code complexity checks                   | Flake8                   | **DONE** | (?)                       |   td   | (?)                  |   td   |
| Static security checks                   | Bandit (?)               |    td    | (?)                       |   td   | (?)                  |   td   |
| Tests                                    | Pytest                   |    td    | (?)                       |   td   | (?)                  |   td   |
| Test coverage checks                     | Pytest coverage          |    td    | (?)                       |   td   | (?)                  |   td   |
| .                                        |                          |          |                           |        |                      |        |
| **BACKEND - CUSTOM PROGRAMMING**         |                          |          |                           |        |                      |        |
| Extensive logging                        | Custom                   |    td    | (?)                       |   td   | (?)                  |   td   |
| App engine - permissions, auth, worflows | Custom                   |    td    | (?)                       |   td   | (?)                  |   td   |
| Solution for GDPR vs immutability        | Custom (?)               |    td    | (?)                       |   td   | (?)                  |   td   |
| .                                        |                          |          |                           |        |                      |        |
| **CI/CD & INFRA**                        |                          |          |                           |        |                      |        |
| CI service                               | Travis                   |    td    | (?)                       |   td   | (?)                  |   td   |
| Repeat pre-commit checks                 | Custom                   |    td    | (?)                       |   td   | (?)                  |   td   |
| Hosting (for runners, alpha, prod)       | DigitalOcean (?)         |    td    | (?)                       |   td   | (?)                  |   td   |
| Infra as a code                          | Minikube (?)             |    td    | (?)                       |   td   | (?)                  |   td   |
| Web server                               | Nginx                    |    td    | (?)                       |   td   | (?)                  |   td   |
| Web application server                   | uWSGI                    |    td    | (?)                       |   td   | (?)                  |   td   |
| Deploy to alpha & prod                   | Custom                   |    td    | (?)                       |   td   | (?)                  |   td   |
| Version endpoint and after-deploy checks | Custom                   |    td    | (?)                       |   td   | (?)                  |   td   |
| Liveness & readyness endpoints           | Custom                   |    td    | (?)                       |   td   | (?)                  |   td   |
| Selenium test run                        | Robot framework          |    td    | (?)                       |   td   | (?)                  |   td   |
| Backend error tracker - alpha            | Sentry                   |    td    | <- same (?)               |   td   | (?)                  |   td   |
| Logging aggregation (a, p)               | Graylog (?)              |    td    | ES & Kibana (?)           |   td   | (?)                  |   td   |
| Infra metrics - prod                     | NewRelic (?)             |    td    | Graphite & Graphana (?)   |   td   | (?)                  |   td   |
| User metrics - prod                      | Google analytics (?)     |    td    | (?)                       |   td   | (?)                  |   td   |
| .                                        |                          |          |                           |        |                      |        |
| **A FEW EXOTIC IDEAS**                   |                          |          |                           |        |                      |        |
| Memory leak checks                       | (?)                      |    td    | (?)                       |   td   | (?)                  |   td   |
| Performance tests                        | (?)                      |    td    | (?)                       |   td   | (?)                  |   td   |
| Clean error log enforced                 | (?)                      |    td    | (?)                       |   td   | (?)                  |   td   |
| Selenium tests coverage                  | (?)                      |    td    | (?)                       |   td   | (?)                  |   td   |
| Selenium tests screenshots               | (?)                      |    td    | (?)                       |   td   | (?)                  |   td   |

# Buzzword index

[Link](/notes/buzzwords.md)

# Bookmarked useful links

[Link](/notes/bookmarks.md)

# CheatSheet

[Link](/notes/cheatsheet.md)

# Experiments:

## 1. Python script, experimenting with queries of three DBs: Redis, MongoDB and PostgreSQL

[Link](/experiments/1/)

To run, execute `docker-compose up`

Status: In progress...

Done:

- Redis POC
- Mongo POC
- Mounted source files
- PostgreSQL POC
- One entity experiment with all providers
- Add time measurements
- Scale up
- Indexes

Todo:

- Another experiment: Two entities and JOINS
  - Provider by provider
- Another provider - SQL Alchemy + migrations
- Why no perf improvement with postgres index?
- MySql?
- Couchbase?

Ideas:

- PostgresAdmin? Other kind of admins?

## 2. PDB debugging with docker and flask

DONE.

See [Link](/experiments/2/Readme.md)

## 3. Swagger UI served for trivial flask app

Following https://medium.com/@sean_bradley/add-swagger-ui-to-your-python-flask-api-683bfbb32b36

DONE.

See [Link](/experiments/3/)

## 4. Swagger autogenerated by FlaskRestPlus

Following https://towardsdatascience.com/working-with-apis-using-flask-flask-restplus-and-swagger-ui-7cf447deda7f

DONE.

## 5. Graphene lib for GraphQL in python

FAILED. Got stuck at https://github.com/graphql-python/graphene/issues/546
