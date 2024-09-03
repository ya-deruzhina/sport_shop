# Sport Shop project

# Project consists from some parts:

## postgreSQL (it's about configurations of Docker for PostgreSQL)
## sport_shop_api (it's a Django REST API)

# For install
## 1. Clone the repository
## Uncomment necessary settings in sport_shop_api/.env and Read sport_shop_api/README.md  
## 2. Use command 'docker-compose up --build' in folder 'sport_shop'

# If you use PostgreSQL, Redis or Elasticsearch, use command line in terminal
1. sudo /etc/init.d/postgresql stop
2. sudo /etc/init.d/redis-server stop
3. sudo systemctl stop elasticsearch