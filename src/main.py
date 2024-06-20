import os

import uvicorn
from fastapi import Request
from fastapi.templating import Jinja2Templates

from config.app import app


@app.get('/', tags=['root'])
async def root_index():
    return {
        "service": "fb4s-chrome-extension"
    }


@app.get('/.env', tags=['root'], include_in_schema=False)
async def feel_free(request: Request):
    template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
    templates = Jinja2Templates(directory=template_dir)
    return templates.TemplateResponse("feel_free.html", {"request": request}, status_code=402)


if __name__ == "__main__":
    # module : app
    # uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

    uvicorn.run("main:app", host="0.0.0.0", port=5003, reload=False)

