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

To deploy run a docker compose command like this:

`docker compose --env-file .prod.env up -d`

***