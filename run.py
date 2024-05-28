import os
from app import create_app,db
from flask_migrate import Migrate

app = create_app()
migrate = Migrate(app, db)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 10000)) 
    
    app.run(debug=True, host='0.0.0.0', port=port)
