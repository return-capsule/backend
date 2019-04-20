# 추억담기 Backend Endpoints

## 목적

- 계정 관리 및 사용자의 캡슐을 관리할 수 있다.
- 캡슐의 생성 및 중도 파기, 캡슐 업데이트 등을 관리할 수 있습니다.

---

# API DOCS

## /login

### POST

```http
POST /api/login HTTP/1.1
Host: aws.jaehoon.kim:5001
User-Agent: your-client/1.0
Content-Type: application/json
Accept: */*
{
	"email": "asdf@gmail.com",
  "password": "asdf"  
}
```

> 응답은 아래와 같다.

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
{
	"access_token": "엑세스 토큰",
	"refresh_token": "리프레시 토큰"
}

HTTP/1.1 401 Unauthorized
Content-Type: text/plain; charset=utf-8
```

> 사용자의 자격 증명을 확인하기 위해 사용됨

로그인 성공 시 액세스 토큰과 리프레시 토큰을 반환합니다.

조회할 수 없다면 `status code 401` 을 반환합니다.

## /accounts

### POST

```http
POST /api/accounts HTTP/1.1
Host: aws.jaehoon.kim:5001
User-Agent: your-client/1.0
Content-Type: application/json
Accept: */*
{
	"email": "asdf@gmail.com",
  "password": "asdf",
  "name": "이솨~~~"
}
```

> 응답은 아래와 같다.

```http
HTTP/1.1 201 Created
Content-Type: text/plain; charset=utf-8

HTTP/1.1 409 Conflict
Content-Type: text/plain; charset=utf-8
```

> 신규 계정 생성을 위해 사용됨

신규 사용자의 계정을 생성합니다.

중복된 이메일이 발견된 경우 `status code 409`  를 반환합니다.