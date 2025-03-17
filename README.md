# django-session-demo

Run the following command to start the server:

```bash
python manage.py runserver
```

Navigate to `http://localhost:8000/get-user/` and you will see `User: (not logged in)`.

Then, navigate to `http://localhost:8000/login/?user=admin&password=password` and you will see `Successfully logged in`.

Now, navigate to `http://localhost:8000/get-user/` again and you will see `User: admin`.
