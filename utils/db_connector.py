from surrealdb import Surreal

# Function to add data into the "media" table
async def add_data(name, post):
    async with Surreal("ws://localhost:8000/rpc") as db:
        await db.signin({"user": "root", "pass": "root"})
        await db.use("test", "test")

        data = {
            "name": name,
            "post": post,
        }

        await db.query(f"""
        insert into media {data};""")

# Function to fetch data from the "media" table
async def get_data():
    async with Surreal("ws://localhost:8000/rpc") as db:
        await db.signin({"user": "root", "pass": "root"})
        await db.use("test", "test")

        result = await db.query("select name, post from media")
        #data = result["data"]

        return result

# Function to update data in the "media" table
async def update_data(name, new_post):
    async with Surreal("ws://localhost:8000/rpc") as db:
        await db.signin({"user": "root", "pass": "root"})
        await db.use("test", "test")

        update_query = f"update media set post = '{new_post}' where name = '{name}'"
        await db.query(update_query)

# Function to delete data in the "media" table
async def delete_data(name):
    async with Surreal("ws://localhost:8000/rpc") as db:
        await db.signin({"user": "root", "pass": "root"})
        await db.use("test", "test")

        delete_query = f"delete from media where name = '{name}'"
        await db.query(delete_query)
