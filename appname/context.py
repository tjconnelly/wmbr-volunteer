from appname import db

from flask import current_app as app
from flask import g

import datetime

def database():
  import pymysql as mysql
  if app.config['DATABASE'] is not None:
    ### mysql database
    connection = app.config['DATABASE']
    db = mysql.connect(**connection);
    # unfuck the innodb tables
    db.autocommit(True);
    cursor = db.cursor(mysql.cursors.DictCursor);
    return cursor
  else:
    return False

def timezone(tz=None):
  if tz is not None:
    zone = tz
  else:
    zone = 'America/New_York'
  return zone

def envtag():
  # tag title for browser hallway vision
  app_env = app.config['ENVIRONMENT']
  if app_env == 'live':
    envid = app.config['NAME']
  else:
    envid = app.config['NAME']+' : '+app_env.upper()
  return envid

def beforerequest():
  #g.cursor = database()
  g.tz = timezone()
  g.envid = envtag()

  # today
  g.today = datetime.date.today();
  g.now = datetime.datetime.now();

  # context globals
  #g.labels = labels()
