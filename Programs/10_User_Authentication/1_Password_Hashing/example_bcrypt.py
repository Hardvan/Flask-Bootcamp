from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

password = "verysecretpassword"

hashed_password = bcrypt.generate_password_hash(password=password)

print(hashed_password)

check = bcrypt.check_password_hash(hashed_password, "wrong password")
print(check)

check = bcrypt.check_password_hash(hashed_password, "verysecretpassword")
print(check)
