from faker import Faker
import pandas as pd
from django.contrib.auth.hashers import make_password
from sqlalchemy import create_engine, text
from collections import defaultdict

from sqlalchemy.ext.declarative import declarative_base

# Aby wywołać generator trzeba w folderze researchGroup wpisać "python manage.py runscript data-generator"
# falga do printowania danych do konsoli
is_printing = True

number_of_announcements = 10
number_of_projects = 10
number_of_users = 20
number_of_guides = 10
number_of_research_groups = 10
number_of_research_group_users = 20
number_of_research_group_guides = 10
number_of_research_group_posts = 10
number_of_research_group_post_comments = 10
number_of_research_group_disks = 10
number_of_research_group_links = 10
number_of_guide_projects = 10
number_of_project_users = 20
number_of_tutorials = 10
number_of_ratings = 10

fake = Faker()
engine = create_engine(
    "postgresql://admin:pleasechangeme@postgres:5432/backend", echo=False
    # "postgresql://admin:pleasechangeme@localhost:5432/backend", echo=False
)


def run():
    print("Script is running...")
    dropTables()
    genrateTables()
    print("Script end successfully")


def dropTables():
    DeleteTableData("projects_projectlink")
    DeleteTableData("projects_projectdisk")
    DeleteTableData("projects_projectpostcomment")
    DeleteTableData("projects_projectpost")
    DeleteTableData("research_groups_researchgroupguide")
    DeleteTableData("research_groups_researchgrouplink")
    DeleteTableData("research_groups_researchgroupdisk")
    DeleteTableData("research_groups_researchgrouppostcomment")
    DeleteTableData("research_groups_researchgrouppost")
    DeleteTableData("research_groups_researchgroupuser")
    DeleteTableData("announcements_announcement")
    DeleteTableData("projects_guideproject")
    DeleteTableData("projects_projectuser")
    DeleteTableData("projects_project_research_groups")
    DeleteTableData("tutorials_rating")
    DeleteTableData("tutorials_tutorial_editors")
    DeleteTableData("tutorials_tutorial")
    DeleteTableData("projects_project")
    DeleteTableData("research_groups_researchgroup")
    DeleteTableData("token_blacklist_blacklistedtoken")
    DeleteTableData("token_blacklist_outstandingtoken")
    DeleteTableData("auth_user")


def genrateTables():
    users = generate_user()
    research_groups = generate_research_group(users)
    projects = generate_project(users)
    tutorials = generate_tutorial(users)
    tutorial_users = generate_tutorial_user(tutorials, users)
    ratings = generate_Rating(users, tutorials)
    project_research_group = generate_project_research_group(projects, research_groups)
    projectUsers = generate_project_user(users, projects)
    guideProjects = generate_guide_project(tutorials, projects)
    announcements = generate_announcement(users, research_groups)
    research_group_users = generate_research_group_users(users, research_groups)
    research_group_posts = generate_research_group_post(users, research_groups)
    research_group_post_comments = generate_research_group_post_comment(users, research_group_posts)
    research_group_disks = generate_research_group_disk(projects)
    research_group_links = generate_research_group_link(projects)
    research_group_guides = generate_research_group_guides(research_groups, tutorials)
    project_posts = generate_project_post(users, projects)
    project_post_comments = generate_project_post_comment(users, project_posts)
    project_disks = generate_project_disk(projects)
    project_links = generate_project_link(projects)


def DeleteTableData(name):
    sql = text('DELETE FROM ' + name + ';')
    engine.execute(sql)
    if is_printing:
        print("data deleted from table: " + name)


def generate_user():
    users = defaultdict(list)
    users["id"].append(10000)
    users["username"].append("admin")
    users["password"].append(make_password("admin"))  # "admin" po szyfrowaniu
    users["last_login"].append(fake.date())
    users["is_superuser"].append(True)
    users["first_name"].append("admin")
    users["last_name"].append("admin")
    users["email"].append("admin@ad.min")
    users["is_staff"].append(True)
    users["is_active"].append(True)
    users["date_joined"].append(fake.past_date())
    for i in range(number_of_users):
        users["id"].append(1000 + i)
        username = fake.unique.word() + fake.unique.word()
        users["username"].append(username)
        users["password"].append(make_password(username))
        users["last_login"].append(fake.date())
        users["is_superuser"].append(False)
        users["first_name"].append(fake.first_name())
        users["last_name"].append(fake.last_name())
        users["email"].append(fake.email())
        users["is_staff"].append(False)
        users["is_active"].append(True)
        users["date_joined"].append(fake.past_date())
    df_users = pd.DataFrame(users)
    if is_printing:
        print(df_users)
    df_users.to_sql("auth_user", con=engine, index=False, if_exists="append")
    return df_users


def generate_research_group(users):
    research_groups = defaultdict(list)
    for i in range(number_of_research_groups):
        research_groups["id"].append(1000 + i)
        research_groups["name"].append(fake.unique.name())
        research_groups["about_us"].append(fake.text())
        research_groups["what_we_do"].append(fake.text())
        research_groups["contact"].append(fake.text())
        categories = ["math", "med", "chem"]
        research_groups["category"].append(categories[fake.pyint(0, len(categories) - 1)])
        research_groups["group_owner_id"].append(users["id"].values[i % len(users["id"])])
    df_research_groups = pd.DataFrame(research_groups)
    if is_printing:
        print(df_research_groups)
    df_research_groups.to_sql("research_groups_researchgroup", con=engine, index=False, if_exists="append")
    return df_research_groups


def generate_project(users):
    projects = defaultdict(list)
    for i in range(number_of_projects):
        projects["id"].append(1000 + i)
        projects["name"].append(fake.unique.name())
        projects["description"].append(fake.text())
        projects["deadline"].append(fake.date())
        projects["funds"].append(fake.pyfloat(10))
        categories = ["def"]
        projects["category"].append(categories[fake.pyint(0, len(categories) - 1)])
        projects["project_owner_id"].append(users["id"].values[i % len(users["id"])])
    df_projects = pd.DataFrame(projects)
    if is_printing:
        print(df_projects)
    df_projects.to_sql("projects_project", con=engine, index=False, if_exists="append")
    return df_projects


def generate_tutorial(users):
    tutorials = defaultdict(list)
    for i in range(number_of_tutorials):
        tutorials["id"].append(1000 + i)
        tutorials["title"].append(fake.sentence())
        tutorials["text"].append(fake.text())
        tutorials["is_draft"].append(fake.boolean())
        tutorials["is_public"].append(fake.boolean())
        create = fake.past_date()
        tutorials["created"].append(create)
        tutorials["edited"].append(fake.date_between(create))
        tutorials["owner_id"].append(users["id"].values[i % len(users["id"])])
        types = ["Default", "Default"]
        tutorials["type"].append(types[fake.pyint(0, len(types) - 1)])
    df_tutorials = pd.DataFrame(tutorials)
    if is_printing:
        print(df_tutorials)
    df_tutorials.to_sql("tutorials_tutorial", con=engine, index=False, if_exists="append")
    return df_tutorials


def generate_tutorial_user(tutorials, users):
    tutorial_users = defaultdict(list)
    for i in range(number_of_tutorials):
        tutorial_users["id"].append(1000 + i)
        tutorial_users["tutorial_id"].append(tutorials["id"].values[i % len(tutorials["id"])])
        tutorial_users["user_id"].append(users["id"].values[i % len(users["id"])])
    df_tutorial_users = pd.DataFrame(tutorial_users)
    if is_printing:
        print(df_tutorial_users)
    df_tutorial_users.to_sql("tutorials_tutorial_editors", con=engine, index=False, if_exists="append")
    return df_tutorial_users


def generate_Rating(users, guides):
    ratings = defaultdict(list)
    for i in range(number_of_ratings):
        ratings["id"].append(1000 + i)
        ratings["author_id"].append(users["id"].values[i % len(users["id"])])
        ratings["guide_id"].append(guides["id"].values[i % len(guides["id"])])
        marks = [5, 4, 3, 2, 1]
        ratings["mark"].append(marks[fake.pyint(0, len(marks) - 1)])
    df_ratings = pd.DataFrame(ratings)
    if is_printing:
        print(df_ratings)
    df_ratings.to_sql("tutorials_rating", con=engine, index=False, if_exists="append")
    return df_ratings


def generate_project_research_group(projects, research_groups):
    project_research_groups = defaultdict(list)
    for i in range(number_of_guides):
        project_research_groups["id"].append(1000 + i)
        project_research_groups["researchgroup_id"].append(research_groups["id"].values[i % len(research_groups["id"])])
        project_research_groups["project_id"].append(projects["id"].values[i % len(projects["id"])])
    df_project_research_groups = pd.DataFrame(project_research_groups)
    if is_printing:
        print(df_project_research_groups)
    df_project_research_groups.to_sql("projects_project_research_groups", con=engine, index=False, if_exists="append")
    return df_project_research_groups


def generate_guide_project(guides, projects):
    guides_projects = defaultdict(list)
    for i in range(number_of_guides):
        guides_projects["id"].append(1000 + i)
        guides_projects["is_public"].append(fake.boolean())
        guides_projects["guide_id"].append(guides["id"].values[i % len(guides["id"])])
        guides_projects["project_id"].append(projects["id"].values[i % len(projects["id"])])
        guides_projects["added"].append(fake.past_date())
    df_guides_projects = pd.DataFrame(guides_projects)
    if is_printing:
        print(df_guides_projects)
    df_guides_projects.to_sql("projects_guideproject", con=engine, index=False, if_exists="append")
    return df_guides_projects


def generate_project_user(users, projects):
    project_users = defaultdict(list)
    for i in range(number_of_project_users):
        project_users["id"].append(1000 + i)
        project_users["person_id"].append(users["id"].values[i % len(users["id"])])
        project_users["project_id"].append(projects["id"].values[i % len(projects["id"])])
        if i >= number_of_projects:
            roles = ["mem", "mod"]
        else:
            roles = ["own"]
        project_users["role"].append(roles[fake.pyint(0, len(roles) - 1)])
        created = fake.past_date()
        project_users["created"].append(created)
        project_users["edited"].append(fake.date_between(created))
    df_project_users = pd.DataFrame(project_users)
    if is_printing:
        print(df_project_users)
    df_project_users.to_sql(
        "projects_projectuser", con=engine, index=False, if_exists="append"
    )
    return df_project_users


def generate_project_post(users, projects):
    project_post = defaultdict(list)
    for i in range(number_of_project_users):
        project_post["id"].append(1000 + i)
        project_post["title"].append(fake.sentence())
        project_post["text"].append(fake.text())
        project_post["author_id"].append(users["id"].values[i % len(users["id"])])
        project_post["project_id"].append(projects["id"].values[i % len(projects["id"])])
        created = fake.past_date()
        project_post["added"].append(created)
        project_post["edited"].append(fake.date_between(created))
    df_project_post = pd.DataFrame(project_post)
    if is_printing:
        print(df_project_post)
    df_project_post.to_sql("projects_projectpost", con=engine, index=False, if_exists="append")
    return df_project_post


def generate_project_post_comment(users, post):
    project_post = defaultdict(list)
    for i in range(number_of_project_users):
        project_post["id"].append(1000 + i)
        project_post["text"].append(fake.text())
        project_post["author_id"].append(users["id"].values[i % len(users["id"])])
        project_post["post_id"].append(post["id"].values[i % len(post["id"])])
        created = fake.past_date()
        project_post["added"].append(created)
    df_project_post = pd.DataFrame(project_post)
    if is_printing:
        print(df_project_post)
    df_project_post.to_sql("projects_projectpostcomment", con=engine, index=False, if_exists="append")
    return df_project_post


def generate_research_group_users(df_users, df_research_group):
    research_group_users = defaultdict(list)
    for i in range(number_of_research_group_users):
        research_group_users["id"].append(1000 + i)
        if i >= number_of_research_groups:
            roles = ["mem", "mod"]
        else:
            roles = ["cr"]
        research_group_users["role"].append(roles[fake.pyint(0, len(roles) - 1)])
        created = fake.past_date()
        research_group_users["created"].append(created)
        research_group_users["edited"].append(fake.date_between(created))
        research_group_users["person_id"].append(df_users["id"].values[i % len(df_users["id"])])
        research_group_users["research_group_id"].append(
            df_research_group["id"].values[i % len(df_research_group["id"])]
        )
    df_research_group_users = pd.DataFrame(research_group_users)
    if is_printing:
        print(df_research_group_users)
    df_research_group_users.to_sql("research_groups_researchgroupuser", con=engine, index=False, if_exists="append")
    return df_research_group_users


def generate_research_group_guides(df_research_groups, df_guides):
    research_group_guides = defaultdict(list)
    for i in range(number_of_research_group_guides):
        research_group_guides["id"].append(1000 + i)
        research_group_guides["is_public"].append(fake.boolean())
        research_group_guides["research_group_id"].append(
            df_research_groups["id"].values[i % len(df_research_groups["id"])]
        )
        research_group_guides["guide_id"].append(df_guides["id"].values[i % len(df_guides["id"])])
    df_research_group_guides = pd.DataFrame(research_group_guides)
    if is_printing:
        print(df_research_group_guides)
    df_research_group_guides.to_sql("research_groups_researchgroupguide", con=engine, index=False, if_exists="append")
    return df_research_group_guides


def generate_research_group_post(df_users, df_research_group):
    research_group_post = defaultdict(list)
    for i in range(number_of_research_group_posts):
        research_group_post["id"].append(1000 + i)
        research_group_post["title"].append(fake.sentence())
        research_group_post["author_id"].append(df_users["id"].values[i % len(df_users["id"])])
        research_group_post["text"].append(fake.text())
        added = fake.past_datetime()
        research_group_post["added"].append(added)
        research_group_post["edited"].append(added)
        research_group_post["research_group_id"].append(
            df_research_group["id"].values[i % len(df_research_group["id"])]
        )
    df_research_group_post = pd.DataFrame(research_group_post)
    if is_printing:
        print(df_research_group_post)
    df_research_group_post.to_sql("research_groups_researchgrouppost", con=engine, index=False, if_exists="append")
    return df_research_group_post


def generate_research_group_post_comment(df_users, df_research_group_post):
    research_group_post_comment = defaultdict(list)
    for i in range(number_of_research_group_post_comments):
        research_group_post_comment["id"].append(1000 + i)
        research_group_post_comment["author_id"].append(df_users["id"].values[i % len(df_users["id"])])
        research_group_post_comment["text"].append(fake.text())
        research_group_post_comment["added"].append(fake.past_datetime())
        research_group_post_comment["post_id"].append(
            df_research_group_post["id"].values[i % len(df_research_group_post["id"])]
        )
    df_research_group_post_comment = pd.DataFrame(research_group_post_comment)
    if is_printing:
        print(df_research_group_post_comment)
    df_research_group_post_comment.to_sql(
        "research_groups_researchgrouppostcomment", con=engine, index=False, if_exists="append"
    )
    return df_research_group_post_comment


def generate_research_group_disk(df_research_groups):
    research_group_disk = defaultdict(list)
    for i in range(number_of_research_group_disks):
        research_group_disk["id"].append(1000 + i)
        research_group_disk["link"].append(fake.url())
        research_group_disk["name"].append(fake.word() + " " + fake.word())
        research_group_disk["is_public"].append(fake.boolean())
        research_group_disk["project_id"].append(df_research_groups["id"].values[i % len(df_research_groups["id"])])
    df_research_group_disk = pd.DataFrame(research_group_disk)
    if is_printing:
        print(df_research_group_disk)
    df_research_group_disk.to_sql("research_groups_researchgroupdisk", con=engine, index=False, if_exists="append")
    return df_research_group_disk


def generate_research_group_link(df_research_groups):
    research_group_link = defaultdict(list)
    for i in range(number_of_research_group_links):
        research_group_link["id"].append(1000 + i)
        research_group_link["link"].append(fake.url())
        research_group_link["name"].append(fake.word() + " " + fake.word())
        research_group_link["is_public"].append(fake.boolean())
        research_group_link["project_id"].append(df_research_groups["id"].values[i % len(df_research_groups["id"])])
    df_research_group_link = pd.DataFrame(research_group_link)
    if is_printing:
        print(df_research_group_link)
    df_research_group_link.to_sql("research_groups_researchgrouplink", con=engine, index=False, if_exists="append")
    return df_research_group_link


def generate_project_disk(df_projects):
    project_disk = defaultdict(list)
    for i in range(number_of_research_group_disks):
        project_disk["id"].append(1000 + i)
        project_disk["link"].append(fake.url())
        project_disk["name"].append(fake.word() + " " + fake.word())
        project_disk["is_public"].append(fake.boolean())
        project_disk["project_id"].append(df_projects["id"].values[i % len(df_projects["id"])])

    df_project_disk = pd.DataFrame(project_disk)
    if is_printing:
        print(df_project_disk)
    df_project_disk.to_sql("projects_projectdisk", con=engine, index=False, if_exists="append")
    return df_project_disk


def generate_project_link(df_projects):
    project_link = defaultdict(list)
    for i in range(number_of_research_group_links):
        project_link["id"].append(1000 + i)
        project_link["link"].append(fake.url())
        project_link["name"].append(fake.word() + " " + fake.word())
        project_link["is_public"].append(fake.boolean())
        project_link["project_id"].append(df_projects["id"].values[i % len(df_projects["id"])])
    df_project_link = pd.DataFrame(project_link)
    if is_printing:
        print(df_project_link)
    df_project_link.to_sql("projects_projectlink", con=engine, index=False, if_exists="append")
    return df_project_link


def generate_announcement(df_users, df_research_group):
    announcements = defaultdict(list)
    for i in range(number_of_announcements):
        announcements["id"].append(1000 + i)
        announcements["title"].append(fake.sentence())
        announcements["text"].append(fake.text())
        announcements["author_id"].append(df_users["id"].values[i % len(df_users["id"])])
        announcements["date"].append(fake.past_datetime())
        announcements["research_group_id_id"].append(df_research_group["id"].values[i % len(df_research_group["id"])])
        types = ["def", "Default"]
        announcements["ann_type"].append(types[fake.pyint(0, len(types) - 1)])
    df_announcements = pd.DataFrame(announcements)
    if is_printing:
        print(df_announcements)
    df_announcements.to_sql("announcements_announcement", con=engine, index=False, if_exists="append")
    return df_announcements
