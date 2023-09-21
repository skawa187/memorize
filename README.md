# Memorize

A Django application to save your thoughts containerized with docker compose.

## Prerequsites

  

1. Create two files (secrets) in the root directory with your custom values:
 
- django_key
```
secret_key
```
***
- db_pass
```
db_password
```
***

2. In the `./nginx` directory create a certificate with a private key using the command:
`openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout memorize.com.key -out memorize.com.crt`

***
3. In the `./nginx` directory generate a dhparam.pem file:
`openssl dhparam -out dhparam.pem 4096`

***

4. In the `./redis` directory place a file named `users.acl` describing access rules (replace 'user_password')
`user celery +@all allkeys allchannels on >user_password`
`user django +@all allkeys allchannels on nopass`

***

## 	Stack components

| Service | Purpose | Ports |
|--|--|--|
|**nginx**  | Acts as a gateway | 80tcp, 443tcp (exposed to the host at 8080, 443) |
| **django-app** | Generate web content | 8000tcp (internal) |
| **db** | Store persistent  | 5432tcp (internal) |
| **redis** | Db reads caching, message broker for celery, storing celery results | 6379tcp (internal) |
| **celery** | Execute offloaded tasks |  |
| **celery-beat** | Execute scheduled tasks |  |
***

## Configuration
1. `nginx/nginx.conf.template`
2. `postgres/postgresql.conf`
3. `redis/redis.conf`
4. Env files in the `env` directory for every service and one `.prod.env` with all services 
***

## Deployment
To deploy run a docker compose command:
`docker compose --env-file env/.prod.env up -d`

***