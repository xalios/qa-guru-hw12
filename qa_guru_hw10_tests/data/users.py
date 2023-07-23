import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    subjects: str
    date_of_birth: tuple
    hobbies: list
    image: str
    current_address: str
    state: str
    city: str


john = User(
    first_name='John',
    last_name='Doe',
    email='jdoe@test.com',
    gender='Male',
    phone_number='9123456789',
    date_of_birth=('1988', 'May', '31'),
    subjects='Computer Science',
    hobbies=['Sports'],
    image='avatar.jpg',
    current_address='Москва',
    state='NCR',
    city='Delhi'
)
