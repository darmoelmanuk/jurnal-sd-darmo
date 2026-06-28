## Endpoint Login

**Endpoint:** `/api/v1/login`

**Method:** `POST`

### Request Body

```json
{
  "username": "admin",
  "password": "admin123"
}
```

### Response Body

```json
{
  "status": "success",
  "message": "Login berhasil",
  "token": "jwt-token-example"
}
```
