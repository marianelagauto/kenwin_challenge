# kenwin_challenge

## Levantamos docker y corremos migraciones
```docker-compose run web python manage.py migrate```

## URL login: 127.0.0.1:8000/login

## Cargar dump de la base con usuario para loguearse


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
```python manage.py test```