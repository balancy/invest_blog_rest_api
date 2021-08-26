# Invest blog REST API

This project serves as a Django REST API with JWT Authenication for REACT frontend educational development.

It has three models: Courses, Mentors and Students. Students and Mentors are linked to Django standard user model by OneToOne relations. Every Course has its Mentor. Students and Courses are linked by ManyToMany relations.

![Image](https://i.ibb.co/1KJZNwx/image.png)
