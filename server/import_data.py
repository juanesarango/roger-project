import pandas as pd
from sitters.models import Review, Owner, Dog, Sitter


def import_reviews_data(start_row=0, end_row=500):
    """Read the data of the csv file using panda. And populate the db"""
    reviews = pd.read_csv('reviews.csv')[start_row:end_row]

    owners = store_owners(reviews)
    owners = store_dogs(owners)
    store_sitters(reviews)
    store_reviews(reviews, owners)


def store_owners(reviews):
    """Each owner is recognized by its profile and user id in there."""
    rows = reviews.values.tolist()
    columns = reviews.T.values.tolist()
    owners_profiles = columns[4]

    unique_owners = {}
    owners = []
    for row_index, owner_profile in enumerate(owners_profiles):
        owner_id = owner_profile.split('user=')[1]
        if owner_id not in unique_owners:
            unique_owners[owner_id] = row_index
            name, image, dogs = (
                rows[row_index][7],
                rows[row_index][4],
                rows[row_index][5]
            )
            owners.append({
                'id': owner_id,
                'name': name,
                'image': image,
                'dogs': dogs
            })
            owner = Owner(
                id=owner_id,
                name=name,
                image=image
            )
            owner.save()
    return owners


def store_dogs(owners):
    """For each row of dogs parse each dog and added to db with its owner."""
    for owner in owners:
        dogs = owner['dogs'].split('|')
        owner_model = Owner.objects.get(id=owner['id'])
        owner_dogs = []
        for dog in dogs:
            dog = Dog(
                name=dog,
                owner=owner_model
            )
            dog.save()
            owner_dogs.append(dog.id)
        owner['dog_ids'] = owner_dogs
    return owners


def store_sitters(reviews):
    """For each review get the unique sitters"""
    rows = reviews.values.tolist()
    columns = reviews.T.values.tolist()
    sitters_profiles = columns[1]

    unique_sitters = {}
    for row_index, sitter_profile in enumerate(sitters_profiles):
        sitter_id = sitter_profile.split('user=')[1]
        if sitter_id not in unique_sitters:
            unique_sitters[sitter_id] = row_index
            name, image = (
                rows[row_index][6],
                rows[row_index][1]
            )
            score = get_sitter_score(name)
            sitter = Sitter(
                id=sitter_id,
                name=name,
                image=image,
                sitter_score=score
            )
            sitter.save()
    return unique_sitters


def store_reviews(reviews, owners):
    """Store each one of the rows of the reviews table"""

    rows = reviews.values.tolist()
    for index, row in enumerate(rows):
        rating, start_date, end_date, text = (
            row[0],
            row[8],
            row[2],
            row[3]
        )
        sitter_id = row[1].split('user=')[1]
        owner_id = row[4].split('user=')[1]
        dog_ids = get_owner_dogs(owners, owner_id)
        sitter_model = Sitter.objects.get(id=sitter_id)
        owner_model = Owner.objects.get(id=owner_id)
        dog_models = Dog.objects.filter(id__in=dog_ids)
        review = Review(
            id=index + 1,
            rating=rating,
            start_date=start_date,
            end_date=end_date,
            text=text,
            sitter=sitter_model,
            owner=owner_model
        )
        review.save()
        for dog_model in dog_models:
            review.dogs.add(dog_model)


def get_sitter_score(name):
    name = ''.join([letter for letter in name.lower() if letter.isalnum()])
    return 5 * len(set(name))/26


def get_owner_dogs(owners, owner_id):
    for owner in owners:
        if owner['id'] == owner_id:
            return owner['dog_ids']


if __name__ == "__main__":
    import_reviews_data()
