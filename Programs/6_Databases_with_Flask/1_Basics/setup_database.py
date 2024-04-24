from app import db, Puppy, app

with app.app_context():

    # ? Create all the tables
    db.create_all()

    # ? Add the objects to the database
    sam = Puppy("Bob", 3, "Labrador")
    frank = Puppy("Charlie", 4, "Poodle")

    print(f"Sam's ID: {sam.id}")  # Sam's ID: None
    print(f"Frank's ID: {frank.id}")  # Frank's ID: None

    db.session.add_all([sam, frank])
    # OR
    # db.session.add(sam)
    # db.session.add(frank)

    # ? Commit the changes
    db.session.commit()

    print(f"Sam's ID: {sam.id}")  # Sam's ID: {sam.id}
    print(f"Frank's ID: {frank.id}")  # Frank's ID: {frank.id}
