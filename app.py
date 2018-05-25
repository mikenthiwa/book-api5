import os
from app import create_app


config_name = os.getenv("APP_SETTINGS")
app = create_app(config_name)

if __name__ == '__main__':
    # app.run()
    port = int(os.environ.get("PORT", 5000))
    app.run('0.0.0.0', port=port)
