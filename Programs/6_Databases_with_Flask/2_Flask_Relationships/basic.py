# Creating Entries into the Tables

from models import db, Puppy, Owner, Toy, app

with app.app_context():

    # Creating 2 Puppies
    bob = Puppy("Bob")
    charlie = Puppy("Charlie")

    # Add puppies to database
    db.session.add_all([bob, charlie])
    db.session.commit()

    # Check
    puppies = Puppy.query.all()
    print(f"All puppies: {puppies}")

    bob = Puppy.query.filter_by(name="Bob").first()
    print(f"Bob: {bob}")

    # Create Owner Object
    hardvan = Owner(name="Hardvan", puppy_id=bob.id)

    # Give Bob some toys
    toy1 = Toy(item_name="Chew Toy", puppy_id=bob.id)
    toy2 = Toy(item_name="Ball", puppy_id=bob.id)

    db.session.add_all([hardvan, toy1, toy2])
    db.session.commit()

    # Grab Bob
    bob = Puppy.query.filter_by(name="Bob").first()
    print(f"Bob: {bob}")

    print(f"{bob.report_toys()}")
