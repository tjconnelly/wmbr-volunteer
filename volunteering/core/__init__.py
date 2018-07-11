from flask import Blueprint
core = Blueprint('core',__name__,template_folder="templates")

#from . import filters
#from . import processors
from . import routes
