# menu.py

def main_menu():
    print("=======================")
    print("    Welcome to BYOAI")
    print("=======================")
    print("1. Project Management")
    print("2. Model Management")
    print("3. Training and Deployment")
    print("4. Settings")
    print("5. Help")
    print("6. Exit")
    print("=======================")
    choice = input("Select an option (1-6): ")
    return choice

def project_management_menu():
    print("=======================")
    print("   Project Management")
    print("=======================")
    print("1. Create New Project")
    print("2. Open Existing Project")
    print("3. Delete Project")
    print("4. Back to Main Menu")
    print("=======================")
    choice = input("Select an option (1-4): ")
    return choice

def main():
    while True:
        choice = main_menu()
        if choice == '1':
            pm_choice = project_management_menu()
            if pm_choice == '1':
                create_new_project()
            elif pm_choice == '2':
                open_existing_project()
            elif pm_choice == '3':
                delete_project()
            elif pm_choice == '4':
                continue
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

def create_new_project():
    project_name = input("Enter Project Name: ")
    print(f"Project '{project_name}' created successfully!")
    # Add further implementation here

def open_existing_project():
    print("Available Projects:")
    # List available projects
    project_number = input("Enter Project Number to Open: ")
    print(f"Opening Project {project_number}")
    # Add further implementation here

def delete_project():
    print("Available Projects:")
    # List available projects
    project_number = input("Enter Project Number to Delete: ")
    print(f"Deleting Project {project_number}")
    # Add further implementation here

if __name__ == "__main__":
    main()
