# reg_and_auth_with_jwt
# регистрация
api/v1/reg/ - 
  - запрос
    - POST:{
      "username":"YOUR_USERNAME",
      "password":"YOUR_PASSWORD",
      "email":"YOUR_EMAIL"
    }
  - ответ
    - STATUS=OK:{
      "status":"good",
      "user_id":"USER_REG_ID"
    }
    - ELSE:{
      "status":"bad"
    }
    
# получение JWT ACCESS и REFRESH токенов
api/v1/token/ - 
  - запрос
    - GET:{
      "username": "YOUR_USERNAME",
      "password": "YOUR_PASSWORD"
    }
  - ответ
    - STATUS=OK:{
      "access":"ACCESS_TOKEN",
      "refresh":"REFRESH_TOKEN"
    }


# повторное получение refresh токена
api/v1/token/refresh/ -
  - запрос
    - GET:{
      "refresh": "CURR_REFRESH_TOKEN"
    }
  - ответ
    - STATUS=OK:{
      "access":"ACCESS_TOKEN",
      "refresh":"NEW_REFRESH_TOKEN"
    }

# проверка действителен ли access token
api/v1/token/verify/ - 
  - запрос
    - GET:{
      "access": "ACCESS_TOKEN"
    }
  - ответ
    - STATUS=OK:{
    
    }
  
# получение письма верификации
get-verif-mail/ -
  - запрос
    - GET:{
      "user_id": USER_ID:int,
    }
  - ответ
    - STATUS=OK:{
      "status":"good",
    }
    - ELSE:{
      "status":"bad"
    }
# ссылка, которая будет помещена в письмо - по ней будет производиться верефикация, отправляется пользователю на почту после перехода на get-verif-mail/
path('verification/<uuid:uuid>/', VerificationAPIView.as_view())
  - запрос
    - GET:{
    }
  - ответ
    - STATUS=OK:{
      "status":"good",
    }
    - ELSE:{
      "status":"bad"
    }
