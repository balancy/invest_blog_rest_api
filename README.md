# Invest blog REST API

This project serves as a Django REST API with JWT Authenication for REACT frontend educational development.

It has three models: Courses, Mentors and Students. Students and Mentors are linked to Django standard user model by OneToOne relations. Every Course has its Mentor. Students and Courses are linked by ManyToMany relations.

![Image](https://i.ibb.co/1KJZNwx/image.png)

It has 2 types of permissions:
- the first one is `AdminUserOrReadOnly` as default for all views which allows admins to post, update, delete data
- the second one is `IsAuthenticated` for `PUT` method in Students View which allows students to subscribe themselves or unsubscribe from courses

Few tests for Models, Views and API are also added.

## Install

Python3, Git and Poetry should be already installed.

1. Clone the repository by command:
```console
git clone https://github.com/balancy/invest_blog_rest_api
```

2. Go inside cloned repository, install dependencies and activate virtual environment by commands:
```console
poetry install
poetry shell
```

3. Rename `.env.example` to `.env` and define values for environmental variables:

- `DEBUG` — debug mode
- `SECRET_KEY` — project django secret key
- `ALLOWED_HOSTS` — see [Django documentation](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)

## Launch

1. Make migrations
```console
python manage.py migrate
```

2. Run server
```console
python manage.py runserver
```