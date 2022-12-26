from app import db, Puppy, app

with app.app_context():
    # ? Create all the tables
    db.create_all()

    # ? Add the objects to the database
    sam = Puppy("Bob", 3)
    frank = Puppy("Charlie", 4)

    print(sam.id)  # None
    print(frank.id)  # None

    db.session.add_all([sam, frank])
    # OR
    # db.session.add(sam)
    # db.session.add(frank)

    # ? Commit the changes
    db.session.commit()

    print(sam.id)  # 1
    print(frank.id)  # 2
