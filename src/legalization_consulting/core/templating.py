from fastapi.templating import Jinja2Templates

from legalization_consulting.core.paths import TEMPLATES_DIR

templates = Jinja2Templates(directory=TEMPLATES_DIR)
