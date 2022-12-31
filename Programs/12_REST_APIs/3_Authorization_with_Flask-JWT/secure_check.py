from user import User

users = [User(1, "Bob", "mypassword"),
         User(2, "Charlie", "secret")]

username_table = {u.username: u for u in users}
user_id_table = {u.id: u for u in users}


def authenticate(username, password):

    user = username_table.get(username, None)

    if user and password == user.password:
        return user


def identity(payload):

    # ? payload is the contents of the JWT token

    user_id = payload["identity"]
    return user_id_table.get(user_id, None)
