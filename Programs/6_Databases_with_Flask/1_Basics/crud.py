# Running this script again will give error because we try to delete a id that is not in the database
# Fix: Delete data.sqlite file and run setup_database.py again

from app import db, Puppy, app

with app.app_context():

    # ? 1) CREATE
    my_puppy = Puppy("Dorothy", 5, "Golden Retriever")
    db.session.add(my_puppy)
    db.session.commit()

    # ? 2) READ
    all_puppies = Puppy.query.all()  # list of all puppies in the table
    print(f"All puppies: {all_puppies}")

    # * Select by ID
    puppy_one = Puppy.query.get(1)
    print(f"Puppy name: {puppy_one.name}")

    # * Filters
    puppy_charlie = Puppy.query.filter_by(name="Charlie")
    print(f"Puppy Charlie: {puppy_charlie.all()}")

    # ? 3) UPDATE
    first_puppy = Puppy.query.get(1)
    first_puppy.age = 10
    db.session.add(first_puppy)
    db.session.commit()

    # ? 4) DELETE
    second_puppy = Puppy.query.get(2)
    db.session.delete(second_puppy)
    db.session.commit()

    all_puppies = Puppy.query.all()
    print(f"All puppies: {all_puppies}")
