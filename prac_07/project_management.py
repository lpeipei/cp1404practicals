
from project import load_projects, save_projects, display_projects, add_new_project, update_project, filter_projects_by_date

FILE = "projects.txt"

MENU = """\n- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit
"""


def main():
    projects = load_projects(FILE)

    while True:
        print(MENU)
        choice = input(">>> ").strip().lower()

        if choice == 'l':
            filename = input("Enter filename to load projects from: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Enter filename to save projects to: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects, True)
        elif choice == 'f':
            date_str = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_projects_by_date(projects, date_str)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


main()
