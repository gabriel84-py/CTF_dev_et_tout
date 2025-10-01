from faker import Faker


fake = Faker(locale="fr_FR")


def get_user():
    user = fake.name()
    return user

def get_users(combien: int):
    users = []
    for i in range(combien):
        users.append(fake.name())
    return users