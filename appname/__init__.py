###
# flask setup
from flask import Flask, g
from flask.json import JSONEncoder
#from flask_bootstrap import Bootstrap
#from flask_moment import Moment
#from flask_sqlalchemy import SQLAlchemy
#from flaskext.mysql import MySQL

# add .fml to templates                                       
class FuckingMagic(Flask):                                    
  def select_jinja_autoescape(self, filename):                
    if filename is None:                                      
      return False                                            
    if filename.endswith('.fml'):                             
      return True                                             
    return Flask.select_jinja_autoescape(self, filename)      
                                                              
# overwrite json encoder                                      
class ExtendedJSONEncoder(JSONEncoder):                       
  def default(self, obj):                                     
    if hasattr(obj, 'isoformat'):                             
      return obj.isoformat()                                  
    return super(ExtendedJSONEncoder, self).default(obj)  

###
# app setup
from env import configs,config_env

# helper modules
#bootstrap = Bootstrap()
#moment = Moment()
#db = SQLAlchemy()
#mysql = MySQL()

def initialize(environment=None):
  app = FuckingMagic(__name__);
  if environment is None:
    environment = config_env()
  app.config.from_object(configs[environment])

  #bootstrap.init_app(app)
  #moment.init_app(app)
  #db.init_app(app)
  #mysql.init_app(app)

  # timezone
  app.config['TZ'] = 'America/New_York'

  # blueprints
  from appname.core import core as core_blueprint
  app.register_blueprint(core_blueprint)

  # custom class
  app.json_encoder = ExtendedJSONEncoder
  return app
