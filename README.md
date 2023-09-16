# Memorize

Simple django application to save your thoughts.

## Prerequsites

  

Create two files (secrets) in the root directory with your custom values:
 
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

To deploy the application run a docker compose command like this:

`docker compose --env-file .prod.env up -d`

***