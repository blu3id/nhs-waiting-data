import os
os.environ['DATABASE_URL'] = 'sqlite:///../test.db'

from app import app
app.run(port=5000,host='0.0.0.0',threaded=True)