# FastAPI-Series MLSA Program

### Set up & Installation

1. Navigate into your desired folder, then clone this repo as shown, remember the dot (.) so as to avoid duplicating this repo's name again.

`git clone https://github.com/Dev-Elie/FastAPI-Series.git .`

2. Change to that specific directory

`cd directory path`
3. Create a virtual environment & activate it

**Windows**
          
```bash
#create a venv
py -3 -m venv venv
# activate venv
venv\Scripts\activate

```
          
**macOS/Linux**
          
```bash
#create a venv
python3 -m venv venv
# activate venv
source venv/bin/activate

```
4. Install the requirements from the requirements.txt file.

`pip install -r requirements.txt`

5. Create a `.env` file in the root of the directory then add the following contents, adding values for each depending on your configs.

```
DATABASE_HOSTNAME=
DATABASE_PORT=
DATABASE_PASSWORD=
DATABASE_NAME=
DATABASE_USERNAME=
SECRET_KEY=
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=
```
6. Run a database migration

` alembic upgrade head`

7. Start the server

`uvicorn app.main:app --reload`
