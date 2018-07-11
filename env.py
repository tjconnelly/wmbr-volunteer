import os
import config
from configparser import SafeConfigParser

def config_path():
  return os.path.dirname(os.path.realpath(__file__))

def config_env():
  try:
    environment = config.ENVIRONMENT
  except AttributeError:
    package,environment = os.path.basename(config_path()).split("-")
  return environment

def config_database(env=None):
  if env is None:
    env = config_env()
  db = {};
  db[env] = db.get(env,{});
  parser = SafeConfigParser();
  parser.read(os.path.join(config_path(),'database.config'))
  for key,value in parser.items(env):
    db[env][key] = value;
  connection = db[env];
  return connection;

def config_sqlalchemy(cxn):
  #uri = 'mysql+pymysql://'+cxn['user']+':'+cxn['passwd']+'@'+cxn['host']+'/'+cxn['db']
  uri = 'mysql+pymysql://{user}:{passwd}@{host}/{db}'.format(**cxn)
  return uri

class Config:
  NAME = config.APPNAME
  # setup
  DIRECTORY = config_path()
  ENVIRONMENT = config_env()
  # data comes from somewhere
  DATABASE = config_database()
  # sqlalchemy
  SQLALCHEMY_DATABASE_URI = config_sqlalchemy(DATABASE)
  SQLALCHEMY_COMMIT_ON_TEARDOWN = True
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  # deliver libraries
  # form support
  SECRET_KEY = '+]x-ML7!wTv|2nA]`]CKaN!K8'
  # unicode on
  JSON_AS_ASCII = False
  # debugging off
  DEBUG = False
  TESTING = False
 
# config modifications
class LiveConfig(Config):
  JSON_AS_ASCII = False
  PRINT_ENV = False

class DevConfig(Config):
  DEBUG = True
  TESTING = True
  PRINT_ENV = True

class LocalConfig(Config):
  DEBUG = True
  TESTING = True
  PRINT_ENV = True

configs = {
  "live":         "env.LiveConfig",
  "local":        "env.LocalConfig",
  "dev":          "env.DevConfig",
  "development":  "env.DevConfig",
  "experimental": "env.DevConfig",
  "default":      "env.DevConfig"
}
