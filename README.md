# Studies

Repo for keeping notes, experiments and other studies related stuff.

# Full-stack apps

## Stack #1 (React-Flask)

TODO (ALL):

- More pre-commit commands, esp. frontend
- Have name from input, propagate everywhere
- Tests...

TODO (BACKEND):

- Refactor readmodel to base, event store subscriptions, queue...
- Refactor alchemy session
- Refactor reuse of model for json

TODO (FRONTEND):

- Stylize a bit more (esp navbar)
- Bootstrap theme
- Localizations. Localization tools
- Console errors (due to hot reload or smth like that)
- NPM install warnings (a few things depretiated)

TODO (APP LOGIC):

- Item name
- Delete item

## Stack #2 (Vue-Django)

TODO:

1. VueX? https://vuex.vuejs.org/
2. Continue with items app development. Maybe continue with https://www.youtube.com/watch?v=uZ2U4aT4cgk&list=PLnzr8Oa9Vyla0s7oGaFeC_GU1XRL3war6&index=9
3. Try out yarn?
4. Pip-compile? https://github.com/jazzband/pip-tools
5. Add swagger https://marcgibbons.com/django-rest-swagger/
6. Add GraphQL http://docs.graphene-python.org/projects/django/en/latest/

## Overview of full stack apps

| Component                                | Stack #1 (React-Flask)   |  status  | Stack #2 (Vue-Django)     |  status  | Stack #3 (.Net Core) | status |
| :--------------------------------------- | :----------------------- | :------: | :------------------------ | :------: | :------------------- | :----: |
| .                                        |                          |          |                           |          |                      |        |
| **PROJECT SETUP**                        |                          |          |                           |          |                      |        |
| One-command setup                        | Docker compose           | **DONE** | <- same (?)               |    td    | <- same (?)          |   td   |
| Minimal dependencies                     | Docker compose           | **DONE** | Docker compose            | **DONE** | <- same (?)          |   td   |
| One-command local run                    | Bash                     | **DONE** | <- same (?)               |    td    | <- same (?)          |   td   |
| On-save checks                           | VS Code plugins          | **DONE** | <- same (?)               |    td    | <- same (?)          |   td   |
| Pre-commit checks                        | Pre-commit hooks         | **DONE** | <- same (?)               |    td    | <- same (?)          |   td   |
| Selenium tests                           | Robot tests              |    td    | (?)                       |    td    | (?)                  |   td   |
| .                                        |                          |          |                           |          |                      |        |
| **FRONTEND - TECH STACK**                |                          |          |                           |          |                      |        |
| Css framework                            | Bootstrap                | **DONE** | Material (?)              |    td    | CSS grid(?)          |   td   |
| Web framework                            | React                    | **DONE** | Vue                       | **DONE** | React (?)            |   td   |
| App framework                            | Flux                     | **DONE** | VueX (?)                  |    td    | Redux (?)            |   td   |
| Language                                 | ES6                      | **DONE** | ES6                       | **DONE** | Typescript (?)       |   td   |
| Bundler                                  | Webpack                  | **DONE** | Webpack                   | **DONE** | (?)                  |   td   |
| Packager                                 | NPM                      | **DONE** | NPM                       | **DONE** | Yarn                 |   td   |
| .                                        |                          |          |                           |          |                      |        |
| **FRONTEND - LIBS & TOOLS**              |                          |          |                           |          |                      |        |
| Routing                                  | React router             | **DONE** | Vue router                |    td    | Custom (?)           |   td   |
| Ajax requests                            | Superagent               | **DONE** | (?)                       |    td    | (?)                  |   td   |
| Transpiler                               | Babel                    | **DONE** | Babel                     | **DONE** | Typescript (?)       |   td   |
| Integrations                             | React-Bootstrap          | **DONE** | (?)                       |    td    |                      |   td   |
| Integrations                             | React-Router-Bootstrap   | **DONE** | (?)                       |    td    |                      |   td   |
| Debugger                                 | (?)                      |    td    | (?)                       |    td    | (?)                  |   td   |
| Localization framework                   | React-Intl               |    td    | (?)                       |    td    | (?)                  |   td   |
| .                                        |                          |          |                           |          |                      |        |
| **FRONTEND - AUTOMATED CHECKS**          |                          |          |                           |          |                      |        |
| Code formatter                           | VS Code prettier         |  PARTLY  | (?)                       |    td    | (?)                  |   td   |
| Code quality checks                      | ESlint (?)               |    td    | (?)                       |    td    | (?)                  |   td   |
| Code complexity checks                   | ESlint (?)               |    td    | (?)                       |    td    | (?)                  |   td   |
| Static security checks                   | NPM audit (?)            |    td    | (?)                       |    td    | (?)                  |   td   |
| Tests                                    | (?)                      |    td    | (?)                       |    td    | (?)                  |   td   |
| Test coverage checks                     | (?)                      |    td    | (?)                       |    td    | (?)                  |   td   |
| .                                        |                          |          |                           |          |                      |        |
| **FRONTEND - CUSTOM PROGRAMMING**        |                          |          |                           |          |                      |        |
| Css customizations                       | SASS                     |    td    | <- same (?)               |    td    | <- same (?)          |   td   |
| Custom theme                             | (?)                      |    td    | <- same (?)               |    td    | <- same (?)          |   td   |
| Extensive logging (posts to back)        | Custom                   |    td    | (?)                       |    td    | (?)                  |   td   |
| Form validation mechanism                | Custom                   |    td    | Custom                    |    td    | Custom               |   td   |
| .                                        |                          |          |                           |          |                      |        |
| **BACKEND - TECH STACK**                 |                          |          |                           |          |                      |        |
| Language                                 | Python                   | **DONE** | Python                    | **DONE** | C#                   |   td   |
| Packager                                 | Pip                      | **DONE** | Pip with pip-tools        |    td    | (?)                  |   td   |
| Web framework                            | Flask                    | **DONE** | Django                    | **DONE** | ASP.Net Core         |   td   |
| REST - Swagger & schema validation       | FlaskRest&Schematics (?) |    td    | (?)                       |    td    | (?)                  |   td   |
| GraphQL Endpoints                        | (?)                      |    td    | (?)                       |    td    | (?)                  |   td   |
| Event store                              | MongoDB                  | **DONE** | (?)                       |    td    | (?)                  |   td   |
| Read model                               | PostgreSQL               | **DONE** | <- same (?)               |    td    | (?)                  |   td   |
| Read model - ORM                         | SQL Alchemy              | **DONE** | Django ORM                |    td    | (?)                  |   td   |
| Read model - Schema migrations           | Alembic                  |    td    | Django ORM migrations (?) |    td    | (?)                  |   td   |
| Session storage                          | Redis                    |    td    | (?)                       |    td    | (?)                  |   td   |
| Cashe storage                            | Redis                    | **DONE** | (?)                       |    td    | (?)                  |   td   |
| Async tasks framework                    | Celery + RabbitMQ        | **DONE** | (?)                       |    td    | (?)                  |   td   |
| Queue                                    | RabbitMQ + pika lib      | **DONE** | (?)                       |    td    | (?)                  |   td   |
| Full-text search                         | Elastic search           |    td    | (?)                       |    td    | (?)                  |   td   |
| Object storage (?)                       | Minio (?)                |    td    | (?)                       |    td    | (?)                  |   td   |
| .                                        |                          |          |                           |          |                      |        |
| **BACKEND - LIBS & TOOLS**               |                          |          |                           |          |                      |        |
| Debugger                                 | Pdb                      | **DONE** | (?)                       |    td    | (?)                  |   td   |
| Event store - Admin UI                   | MongoDB Express          | **DONE** | (?)                       |    td    | (?)                  |   td   |
| Read model - Admin UI                    | PgAdmin                  | **DONE** | (?)                       |    td    | (?)                  |   td   |
| Redis - Admin UI                         | (?)                      | **DONE** | (?)                       |    td    | (?)                  |   td   |
| Rabbit MQ - Admin UI                     | (?)                      | **DONE** | (?)                       |    td    | (?)                  |   td   |
| .                                        |                          |          |                           |          |                      |        |
| **BACKEND - AUTOMATED CHECKS**           |                          |          |                           |          |                      |        |
| Code formatter                           | Black                    | **DONE** | (?)                       |    td    | (?)                  |   td   |
| Code quality checks                      | Flake8                   | **DONE** | (?)                       |    td    | (?)                  |   td   |
| Code complexity checks                   | Flake8                   | **DONE** | (?)                       |    td    | (?)                  |   td   |
| Static security checks                   | Bandit (?)               | **DONE** | (?)                       |    td    | (?)                  |   td   |
| Tests                                    | Pytest                   |    td    | (?)                       |    td    | (?)                  |   td   |
| Test coverage checks                     | Pytest coverage          |    td    | (?)                       |    td    | (?)                  |   td   |
| .                                        |                          |          |                           |          |                      |        |
| **BACKEND - CUSTOM PROGRAMMING**         |                          |          |                           |          |                      |        |
| Extensive logging                        | Custom                   |    td    | (?)                       |    td    | (?)                  |   td   |
| App engine - permissions, auth, worflows | Custom                   |    td    | (?)                       |    td    | (?)                  |   td   |
| Solution for GDPR vs immutability        | Custom (?)               |    td    | (?)                       |    td    | (?)                  |   td   |
| .                                        |                          |          |                           |          |                      |        |
| **CI/CD & INFRA**                        |                          |          |                           |          |                      |        |
| CI service                               | Travis                   |    td    | (?)                       |    td    | (?)                  |   td   |
| Repeat pre-commit checks                 | Custom                   |    td    | (?)                       |    td    | (?)                  |   td   |
| Hosting (for runners, alpha, prod)       | DigitalOcean (?)         |    td    | (?)                       |    td    | (?)                  |   td   |
| Infra as a code                          | Minikube (?)             |    td    | (?)                       |    td    | (?)                  |   td   |
| Web server                               | Nginx                    |    td    | (?)                       |    td    | (?)                  |   td   |
| Web application server                   | uWSGI                    |    td    | (?)                       |    td    | (?)                  |   td   |
| Deploy to alpha & prod                   | Custom                   |    td    | (?)                       |    td    | (?)                  |   td   |
| Version endpoint and after-deploy checks | Custom                   |    td    | (?)                       |    td    | (?)                  |   td   |
| Liveness & readyness endpoints           | Custom                   |    td    | (?)                       |    td    | (?)                  |   td   |
| Selenium test run                        | Robot framework          |    td    | (?)                       |    td    | (?)                  |   td   |
| Backend error tracker - alpha            | Sentry                   |    td    | <- same (?)               |    td    | (?)                  |   td   |
| Logging aggregation (a, p)               | Graylog (?)              |    td    | ES & Kibana (?)           |    td    | (?)                  |   td   |
| Infra metrics - prod                     | NewRelic (?)             |    td    | Graphite & Graphana (?)   |    td    | (?)                  |   td   |
| User metrics - prod                      | Google analytics (?)     |    td    | (?)                       |    td    | (?)                  |   td   |
| .                                        |                          |          |                           |          |                      |        |
| **A FEW EXOTIC IDEAS**                   |                          |          |                           |          |                      |        |
| Memory leak checks                       | (?)                      |    td    | (?)                       |    td    | (?)                  |   td   |
| Performance tests                        | (?)                      |    td    | (?)                       |    td    | (?)                  |   td   |
| Clean error log enforced                 | (?)                      |    td    | (?)                       |    td    | (?)                  |   td   |
| Selenium tests coverage                  | (?)                      |    td    | (?)                       |    td    | (?)                  |   td   |
| Selenium tests screenshots               | (?)                      |    td    | (?)                       |    td    | (?)                  |   td   |

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

## 6. Fire lib for CLI in python

DONE.

## 7. InfluxDB and Grafana

DONE:

- Follow: https://github.com/jkehres/docker-compose-influxdb-grafana

TODO:

- Add https://influxdb-python.readthedocs.io/en/latest/include-readme.html#examples

See [Link](/experiments/6/)

## IDEAS for more experiments:

- Charts.JS https://www.chartjs.org/docs/latest/getting-started/installation.html
- Memory leaks?
- Cookie cutter to generate any kind of project: https://cookiecutter.readthedocs.io/en/1.7.0/README.html#features
- Locust load testing: https://github.com/locustio/locust
- Pysnooper (debugger): https://github.com/cool-RR/PySnooper
- Progress bar: https://github.com/tqdm/tqdm
- Alternative command line lib https://pypi.org/project/click/
- WTF is https://behave.readthedocs.io/en/latest/ (BDD in python)
