from sanic import Sanic
from sanic.response import text
from sanic import Sanic, response

from tomlconfig import TomlConfig

app = Sanic("MyHelloWorldApp")
# sanic配置
app.config.DB_NAME="appdb"
app.config["DB_USER"]="appuser"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8012)

@app.get("/")
async def hello_world(request):
    return text("Hello, world.")

@app.get("/get_sanic")
async def get_sanic(request):
    app1=Sanic.get_app("MyHelloWorldApp")
    print(app1)
    return text(app1.name)

@app.post("/update_config")
async def update_config(request):
    db_settings = {
        'DB_HOST': 'localhost',
        'DB_NAME': 'appdb',
        'DB_USER': 'appuser'
    }
    app.config.update(db_settings)
    return text("配置更新成功!")

@app.get("/get_config")
async def get_custom_config(request):
    toml_config = TomlConfig(path="config.toml")
    app = Sanic(toml_config.APP_NAME, config=toml_config)
    return response.json(app.config)