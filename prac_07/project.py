import datetime


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"


def load_projects(filename):
    projects = []
    try:
        file = open(filename, 'r')
        next(file)  # Skip the header line
        for line in file:
            data = line.strip().split('\t')
            name, start_date, priority, cost_estimate, completion_percentage = data
            project = Project(name, start_date, int(priority), float(cost_estimate), int(completion_percentage))
            projects.append(project)
        file.close()
    except FileNotFoundError:
        print("File not found. No projects loaded.")
    return projects


def save_projects(filename, projects):
    file = open(filename, 'w')
    file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
    for project in projects:
        file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}"
                   f"\t{project.completion_percentage}\n")
    file.close()


def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(project)


def update_project(projects):
    while True:
        display_projects(projects, False)
        choice = int(input("Project choice: "))

        if 0 <= choice < len(projects):
            project = projects[choice]
            print(project)
            new_percentage = int(input("New Percentage: "))
            new_priority = input("New Priority: ")

            if new_priority:
                new_priority = int(new_priority)
                project.priority = new_priority
            project.completion_percentage = new_percentage
            break
        else:
            print("Invalid project choice.")


def display_projects(projects, default=True):
    incomplete_projects = [project for project in projects if project.completion_percentage < 100]
    completed_projects = [project for project in projects if project.completion_percentage == 100]

    if default:
        incomplete_projects.sort(key=lambda project: project.priority, reverse=False)
        completed_projects.sort(key=lambda project: project.priority, reverse=False)
        print("Incomplete projects:")
        for project in incomplete_projects:
            print(f"  {project}")

        print("Completed projects:")
        for project in completed_projects:
            print(f"  {project}")
    else:
        print("Incomplete projects:")
        for index, project in enumerate(incomplete_projects):
            print(f"{index} {project}")

        print("Completed projects:")
        for index, project in enumerate(completed_projects, start=len(incomplete_projects)):
            print(f"{index} {project}")


def filter_projects_by_date(projects, date_str):
    try:
        parts = date_str.split('/')
        day, month, year = map(lambda x: x.strip(), parts)
        date_str = f"{day.zfill(2)}/{month.zfill(2)}/{year.zfill(4)}"

        date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
        filtered_projects = [project for project in projects if
                             datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date() >= date]

        print(f"Show projects that start on or after date ({date_str}):")

        filtered_projects.sort(key=lambda project: datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date())

        if filtered_projects:
            for project in filtered_projects:
                print(f"  {project}")
        else:
            print("No projects found on or after the specified date.")

    except ValueError:
        print("Invalid date format. Use dd/mm/yyyy.")
