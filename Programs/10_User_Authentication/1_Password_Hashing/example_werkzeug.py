from werkzeug.security import generate_password_hash, check_password_hash

hashed_password = generate_password_hash("mypassword")
print(hashed_password)

check = check_password_hash(hashed_password, "wrong password")
print(check)

check = check_password_hash(hashed_password, "mypassword")
print(check)
