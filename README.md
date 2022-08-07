# kenwin_challenge

##### Levantar proyecto con docker y correr migraciones
```
docker-compose run db
docker-compose run web python manage.py migrate
```

##### Levantar dump de la base con usuario y productos de prueba
```
docker cp dump.sql kenwin_challenge-db-1:/tmp
docker exec -it kenwin_challenge-db-1 psql --username postgres --dbname postgres -f tmp/dump.sql
```

##### URL login: 127.0.0.1:8000/login
###### usuario: admin
###### contraseña: admin

## API
### Endpoints producto

##### POST 127.0.0.1:8000/api/products
```
body:
{
    "id": 1,
    "description": "producto 1",
    "price": 2345.0,
    "stock": 1
}
```
##### GET 127.0.0.1:8000/api/products
```
response:
[
    {
        "id": 1,
        "description": "producto 1",
        "price": 2345.0,
        "stock": 1
    },
    {
        "id": 2,
        "description": "producto 2",
        "price": 456.0,
        "stock": 1
    }
]
```
##### PUT 127.0.0.1:8000/api/products/{id}
##### DELETE 127.0.0.1:8000/api/products/{id}

### Endpoints Orden

##### GET 127.0.0.1:8000/api/orders

##### POST 127.0.0.1:8000/api/orders
```
body:

{
    "user": user_id,
    "details": [
        {
            "id": 1,
            "cuantity": 2,
            "product": 2
        },
        {
            "id": 2,
            "cuantity": 1,
            "product": 3
        }
    ]
}
```

## Correr tests
```docker exec kenwin_challenge-web-1 python manage.py test```