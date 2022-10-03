# 임의의 32자리(문자+숫자) random secure key 생성
import secrets

key = secrets.token_hex(16)
print(key)
