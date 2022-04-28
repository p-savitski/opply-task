### Local deployment
- Create and activate virtual env (if needed)
- install required packages: ```pip install -r requirements```
- Run migrations: ```python manage.py migrate```
- Run project: ```python manage.py runserver 127.0.0.1:8000```
- Products can be created using custom command: ```python manage.py populate_db```

### Endpoints
User creation
```
curl --request POST \
  --url http://127.0.0.1:8000/api/users/signup/ \
  --header 'Content-Type: application/json' \
  --data '{
	"username": "user",
	"password": "12345678"
}'
```

Get a access and refresh tokens by credentials
```
curl --request POST \
  --url http://127.0.0.1:8000/api/users/token/ \
  --header 'Content-Type: application/json' \
  --data '{
	"username": "user2",
	"password": "12345678"
}'
```

Get a access token by refresh token
```
curl --request POST \
  --url http://127.0.0.1:8000/api/users/token/refresh/ \
  --header 'Content-Type: application/json' \
  --data '{
	"refresh": "...accesstoken..."
}'
```

Get a list of products:
```
curl --request GET \
  --url 'http://127.0.0.1:8000/api/products/?limit=1&offset=1' \
  --header 'Authorization: Bearer Xaccess_tokenX'
```

Create a new order:
```
curl --request POST \
  --url http://127.0.0.1:8000/api/orders/ \
  --header 'Authorization: Bearer Xaccess_tokenX' \
  --header 'Content-Type: application/json' \
  --data '{
	"ordered_items": [
		{
			"product": 2, # product ID
			"quantity": 300
		},
		{
			"product": 1, # product ID
			"quantity": 4
		}
	]
}'
```

Get a history of User's orders:
```
curl --request GET \
  --url http://127.0.0.1:8000/api/orders/history/ \
  --header 'Authorization: Bearer Xaccess_tokenX' \
  --header 'Content-Type: application/json' \
```
