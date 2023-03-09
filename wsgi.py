from blog.app import create_app

app = create_app()
app.secret_key = "secret key"
