from storage import Session, init_db
from models import Users, Books, Checkout, Admins

# Function to add a new user
def add_new_user():
    session=Session()
    name = input("Enter Name of New User: ")
    new_user=Users(name=name)
    session.add(new_user)
    session.commit()
    print("User added successfully")
    session.close()

# Function to add a new admin
def add_new_admin():
    session=Session()
    username = input("Enter Username of New Admin: ")
    password=input("Enter Password of New Admin: ")
    user_id=input("Enter User Id of New Admin: ")
    new_admin=Admins(username=username, password=password, user_id=user_id)
    session.add(new_admin)
    session.commit()
    print("New Admin Established Successfully")
    session.close()

# Check if admin credentials are valid in database
def check_valid(username, password):
    session=Session()
    checks=session.query(Admins).filter_by(username=username).all()
    for check in checks:
        if check.password==password:
            return True
    return False

# Delete a current User
def delete_user():
    session=Session()
    user_id=int(input("Enter User Id to be deleted: "))
    query=session.query(Users).get(user_id)
    if(query==None):
        print("User Not Found")
        session.close()
        return
    flag=input(f"Are you sure you want to delete {query.id} named {query.name} (Y/N)")
    
    print(flag)
    
    if(flag.lower()=='y'):
        session.delete(query)
        session.commit()
        session.close()
        print("User deleted Successfully")
        return
    else:
        session.close()
        return

# List all Current Users in DataBase
def list_users():
    session=Session()
    users = session.query(Users).all()
    for user in users:
        print(f"User id:{user.id}, User name:{user.name}")
    session.close()

def edit_user():
    session = Session()
    user_id = int(input("Enter User ID to edit: "))
    user = session.query(Users).get(user_id)
    if user is None:
        print("User not found.")
        session.close()
        return

    new_name = input(f"Enter new name for {user.name}: ")
    user.name = new_name
    session.commit()
    print("User updated successfully.")
    session.close()


def search_user():
    session = Session()
    search_choice = input("Search by (ID/Name): ").strip().lower()

    if search_choice == "id":
        user_id = int(input("Enter User ID: "))
        user = session.query(Users).get(user_id)
        if user:
            print(f"User found: ID = {user.id}, Name = {user.name}")
        else:
            print("No user found with that ID.")
    
    elif search_choice == "name":
        user_name = input("Enter User Name: ").strip()
        user = session.query(Users).filter(Users.name.ilike(f"%{user_name}%")).all()
        if user:
            print("Users found:")
            for u in user:
                print(f"User ID: {u.id}, Name: {u.name}")
        else:
            print("No user found with that name.")

    else:
        print("Invalid search type. Please choose 'ID' or 'Name'.")

    session.close()
