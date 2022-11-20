from faker import Faker
import pandas as pd
from sqlalchemy import create_engine
from collections import defaultdict

# Aby wywołać generator trzeba w folderze researchGroup wpisać "python manage.py runscript data-generator"
# falga do printowania danych do konsoli
is_printing = False

number_of_links = 10
number_of_announcements = 10
number_of_projects = 10
number_of_users = 10
number_of_guides = 10
number_of_research_groups = 10
number_of_research_group_users = 10
number_of_research_group_guides = 10
number_of_research_group_posts = 10
number_of_research_group_post_comments = 10
number_of_research_group_disks = 10
number_of_research_group_links = 10
number_of_guide_projects = 10
number_of_project_users = 10
number_of_tutorials = 10
number_of_ratings = 10

fake = Faker()
engine = create_engine('postgresql://admin:pleasechangeme@localhost:5432/backend', echo=False)

def run():
    links = generate_link()
    users = generate_user()
    guides = generate_guide(users)
    research_groups = generate_research_group()
    projects = generate_project()
    tutorials = generate_tutorial(users)
    tutorial_users = generate_tutorial_user(tutorials, users)
    ratings = generate_Rating(users, guides)
    projectUsers = generate_project_user(users, projects)
    guideProjects = generate_guide_project(guides, projects)
    announcements = generate_announcement(users, research_groups)
    research_group_users = generate_research_group_users(users, research_groups)
    research_group_posts = generate_research_group_post(users, research_groups)
    research_group_post_comments = generate_research_group_post_comment(users, research_group_posts)
    research_group_disks = generate_research_group_disk(projects, links)
    research_group_links = generate_research_group_link(projects, links)
    research_group_guides = generate_research_group_guides(research_groups, guides)
    project_posts = generate_project_post(users, projects)
    project_post_comments = generate_project_post_comment(users, project_posts)
    project_disks = generate_project_disk(projects, links)
    project_links = generate_project_link(projects, links)

def generate_link():
    links = defaultdict(list)
    for i in range(number_of_links):
        links["id"].append(i)
        links["link"].append(fake.url())
        links["name"].append(fake.word())
        links["is_public"].append(fake.boolean())
    df_links = pd.DataFrame(links)
    if is_printing:
        print(df_links)
    df_links.to_sql('Link', con=engine, index=False, if_exists="replace")
    return df_links

def generate_user():
    users = defaultdict(list)
    for i in range(number_of_users):
        users["id"].append(i)
        users["username"].append(fake.unique.word()+fake.unique.word())
        users["password"].append(fake.password())
        users["first_name"].append(fake.first_name())
        users["last_name"].append(fake.last_name())
        users["email"].append(fake.email())
        users["is_staff"].append(fake.boolean())
        users["is_active"].append(fake.boolean())
        users["date_joined"].append(fake.past_date())
    df_users = pd.DataFrame(users)
    if is_printing:
        print(df_users)
    df_users.to_sql('User', con=engine, index=False, if_exists="replace")
    return df_users

def generate_research_group():
    research_groups = defaultdict(list)
    for i in range(number_of_research_groups):
        research_groups["id"].append(i)
        research_groups["name"].append(fake.unique.name())
        research_groups["description"].append(fake.text())
        research_groups["about_us"].append(fake.text())
        research_groups["what_we_do"].append(fake.text())
        research_groups["contact"].append(fake.text())
        categories = ["MATH", "MEDICAL", "CHEMISTRY", "DEFAULT"]
        research_groups["category"].append(categories[fake.pyint(0, len(categories)-1)])
    df_research_groups = pd.DataFrame(research_groups)
    if is_printing:
        print(df_research_groups)
    df_research_groups.to_sql('ResearchGroup', con=engine, index=False, if_exists="replace")
    return df_research_groups
def generate_project():
    projects = defaultdict(list)
    for i in range(number_of_projects):
        projects["id"].append(i)
        projects["name"].append(fake.unique.name())
        projects["description"].append(fake.text())
        projects["deadline"].append(fake.date())
        projects["funds"].append(fake.pyfloat(10))
    df_projects = pd.DataFrame(projects)
    if is_printing:
        print(df_projects)
    df_projects.to_sql('Project', con=engine, index=False, if_exists="replace")
    return df_projects
def generate_guide(users):
    guides = defaultdict(list)
    for i in range(number_of_guides):
        guides["id"].append(i)
        guides["name"].append(fake.unique.name())
        guides["text"].append(fake.text())
        guides["isDraft"].append(fake.boolean())
        guides["isPublic"].append(fake.boolean())
        guides["createDate"].append(fake.past_date())
        guides["author"].append(users["id"].values[(i % len(users["id"]))])
        guides["editor"].append(users["id"].values[(i % len(users["id"]))])
        types = ["Default", "Default"]
        guides["type"].append(types[fake.pyint(0, len(types)-1)])
    df_guides = pd.DataFrame(guides)
    if is_printing:
        print(df_guides)
    df_guides.to_sql('Guides', con=engine, index=False, if_exists="replace")
    return df_guides

def generate_tutorial(users):
    tutorials = defaultdict(list)
    for i in range(number_of_tutorials):
        tutorials["id"].append(i)
        tutorials["title"].append(fake.sentence())
        tutorials["text"].append(fake.text())
        tutorials["isDraft"].append(fake.boolean())
        tutorials["isPublic"].append(fake.boolean())
        create = fake.past_date()
        tutorials["created"].append(create)
        tutorials["edited"].append(fake.date_between(create))
        tutorials["owner"].append(users["id"].values[i % len(users["id"])])
        types = ["Default", "Default"]
        tutorials["type"].append(types[fake.pyint(0, len(types)-1)])
    df_tutorials = pd.DataFrame(tutorials)
    if is_printing:
        print(df_tutorials)
    df_tutorials.to_sql('Tutorial', con=engine, index=False, if_exists="replace")
    return df_tutorials

def generate_tutorial_user(tutorials, users):
    tutorial_users = defaultdict(list)
    for i in range(number_of_tutorials):
        tutorial_users["id"].append(i)
        tutorial_users["tutorial"].append(tutorials["id"].values[i % len(tutorials["id"])])
        tutorial_users["user"].append(users["id"].values[i % len(users["id"])])
    df_tutorial_users = pd.DataFrame(tutorial_users)
    if is_printing:
        print(df_tutorial_users)
    df_tutorial_users.to_sql('TutorialUser', con=engine, index=False, if_exists="replace")
    return df_tutorial_users

def generate_Rating(users, guides):
    ratings = defaultdict(list)
    for i in range(number_of_ratings):
        ratings["id"].append(i)
        ratings["author"].append(users["id"].values[i % len(users["id"])])
        ratings["guide"].append(guides["id"].values[i % len(guides["id"])])
        marks = ["GREAT", "GOOD", "DECENT", "OK", "BAD"]
        ratings["mark"].append(marks[fake.pyint(0, len(marks)-1)])
    df_ratings = pd.DataFrame(ratings)
    if is_printing:
        print(df_ratings)
    df_ratings.to_sql('Rating', con=engine, index=False, if_exists="replace")
    return df_ratings

def generate_guide_project(guides, projects):
    guides_projects = defaultdict(list)
    for i in range(number_of_guides):
        guides_projects["id"].append(i)
        guides_projects["isPublic"].append(fake.boolean())
        guides_projects["guide"].append(guides["id"].values[i % len(guides["id"])])
        guides_projects["project"].append(projects["id"].values[i % len(projects["id"])])
        guides_projects["added"].append(fake.past_date())
    df_guides_projects = pd.DataFrame(guides_projects)
    if is_printing:
        print(df_guides_projects)
    df_guides_projects.to_sql('GuideProject', con=engine, index=False, if_exists="replace")
    return df_guides_projects

def generate_project_user(users, projects):
    project_users = defaultdict(list)
    for i in range(number_of_project_users):
        project_users["id"].append(i)
        project_users["person"].append(users["id"].values[i % len(users["id"])])
        project_users["project"].append(projects["id"].values[i % len(projects["id"])])
        roles = ["UNSPECIFIED", "MEMBER", "MODERATOR", "OWNER"]
        project_users["role"].append(roles[fake.pyint(0, len(roles)-1)])
        created = fake.past_date()
        project_users["created"].append(created)
        project_users["edited"].append(fake.date_between(created))
    df_project_users = pd.DataFrame(project_users)
    if is_printing:
        print(df_project_users)
    df_project_users.to_sql('ProjectUsers', con=engine, index=False, if_exists="replace")
    return df_project_users

def generate_project_post(users, projects):
    project_post = defaultdict(list)
    for i in range(number_of_project_users):
        project_post["id"].append(i)
        project_post["title"].append(fake.sentence())
        project_post["text"].append(fake.text())
        project_post["author"].append(users["id"].values[i % len(users["id"])])
        project_post["project"].append(projects["id"].values[i % len(projects["id"])])
        created = fake.past_date()
        project_post["added"].append(created)
        project_post["edited"].append(fake.date_between(created))
    df_project_post = pd.DataFrame(project_post)
    if is_printing:
        print(df_project_post)
    df_project_post.to_sql('ProjectPost', con=engine, index=False, if_exists="replace")
    return df_project_post

def generate_project_post_comment(users, post):
    project_post = defaultdict(list)
    for i in range(number_of_project_users):
        project_post["id"].append(i)
        project_post["text"].append(fake.text())
        project_post["author"].append(users["id"].values[i % len(users["id"])])
        project_post["post"].append(post["id"].values[i % len(post["id"])])
        created = fake.past_date()
        project_post["added"].append(created)
    df_project_post = pd.DataFrame(project_post)
    if is_printing:
        print(df_project_post)
    df_project_post.to_sql('ProjectPostComment', con=engine, index=False, if_exists="replace")
    return df_project_post

def generate_research_group_users(df_users, df_guides):
    research_group_users = defaultdict(list)
    for i in range(number_of_research_group_users):
        research_group_users["id"].append(i)
        roles = ["UNSPECIFIED", "MEMBER", "MODERATOR", "CREATOR"]
        research_group_users["role"].append(roles[fake.pyint(0, len(roles)-1)])
        created = fake.past_date()
        research_group_users["created"].append(created)
        research_group_users["edited"].append(fake.date_between(created))
        research_group_users["person"].append(df_users["id"].values[i % len(df_users["id"])])
        research_group_users["research_group"].append(df_guides["id"].values[i % len(df_guides["id"])])
    df_research_group_users = pd.DataFrame(research_group_users)
    if is_printing:
        print(df_research_group_users)
    df_research_group_users.to_sql('ResearchGroupUser', con=engine, index=False, if_exists="replace")
    return df_research_group_users

def generate_research_group_guides(df_research_groups, df_guides):
    research_group_guides = defaultdict(list)
    for i in range(number_of_research_group_guides):
        research_group_guides["id"].append(i)
        research_group_guides["is_public"].append(fake.boolean())
        research_group_guides["research_group"].append(df_research_groups["id"].values[i % len(df_research_groups["id"])])
        research_group_guides["guide"].append(df_guides["id"].values[i % len(df_guides["id"])])
    df_research_group_guides = pd.DataFrame(research_group_guides)
    if is_printing:
        print(df_research_group_guides)
    df_research_group_guides.to_sql('ResearchGroupGuides', con=engine, index=False, if_exists="replace")
    return df_research_group_guides

def generate_research_group_post(df_users, df_research_group):
    research_group_post = defaultdict(list)
    for i in range(number_of_research_group_posts):
        research_group_post["id"].append(i)
        research_group_post["title"].append(fake.sentence())
        research_group_post["author"].append(df_users["id"].values[i % len(df_users["id"])])
        research_group_post["text"].append(fake.text())
        added = fake.past_date()
        research_group_post["added"].append(added)
        research_group_post["edited"].append(fake.date_between(added))
        research_group_post["research_group"].append(df_research_group["id"].values[i % len(df_research_group["id"])])
    df_research_group_post = pd.DataFrame(research_group_post)
    if is_printing:
        print(df_research_group_post)
    df_research_group_post.to_sql('ResearchGroupPost', con=engine, index=False, if_exists="replace")
    return df_research_group_post
def generate_research_group_post_comment(df_users, df_research_group_post):
    research_group_post_comment = defaultdict(list)
    for i in range(number_of_research_group_post_comments):
        research_group_post_comment["id"].append(i)
        research_group_post_comment["author"].append(df_users["id"].values[i % len(df_users["id"])])
        research_group_post_comment["text"].append(fake.text())
        research_group_post_comment["added"].append(fake.past_datetime())
        research_group_post_comment["post"].append(df_research_group_post["id"].values[i % len(df_research_group_post["id"])])
    df_research_group_post_comment = pd.DataFrame(research_group_post_comment)
    if is_printing:
        print(df_research_group_post_comment)
    df_research_group_post_comment.to_sql('ResearchGroupPostComment', con=engine, index=False, if_exists="replace")
    return df_research_group_post_comment
def generate_research_group_disk(df_projects, df_links):
    research_group_disk = defaultdict(list)
    for i in range(number_of_research_group_disks):
        research_group_disk["id"].append(i)
        research_group_disk["research_group"].append(df_projects["id"].values[i % len(df_projects["id"])])
        research_group_disk["link"].append(df_links["id"].values[i % len(df_links["id"])])
    df_research_group_disk = pd.DataFrame(research_group_disk)
    if is_printing:
        print(df_research_group_disk)
    df_research_group_disk.to_sql('ResearchGroupDisk', con=engine, index=False, if_exists="replace")
    return df_research_group_disk
def generate_research_group_link(df_projects, df_links):
    research_group_link = defaultdict(list)
    for i in range(number_of_research_group_links):
        research_group_link["id"].append(i)
        research_group_link["research_group"].append(df_projects["id"].values[i % len(df_projects["id"])])
        research_group_link["link"].append(df_links["id"].values[i % len(df_links["id"])])
    df_research_group_link = pd.DataFrame(research_group_link)
    if is_printing:
        print(df_research_group_link)
    df_research_group_link.to_sql('ResearchGroupLink', con=engine, index=False, if_exists="replace")
    return df_research_group_link
def generate_project_disk(df_projects, df_links):
    project_disk = defaultdict(list)
    for i in range(number_of_research_group_disks):
        project_disk["id"].append(i)
        project_disk["project"].append(df_projects["id"].values[i % len(df_projects["id"])])
        project_disk["link"].append(df_links["id"].values[i % len(df_links["id"])])
    df_project_disk = pd.DataFrame(project_disk)
    if is_printing:
        print(df_project_disk)
    df_project_disk.to_sql('ProjectDisk', con=engine, index=False, if_exists="replace")
    return df_project_disk
def generate_project_link(df_projects, df_links):
    project_link = defaultdict(list)
    for i in range(number_of_research_group_links):
        project_link["id"].append(i)
        project_link["project"].append(df_projects["id"].values[i % len(df_projects["id"])])
        project_link["link"].append(df_links["id"].values[i % len(df_links["id"])])
    df_project_link = pd.DataFrame(project_link)
    if is_printing:
        print(df_project_link)
    df_project_link.to_sql('ProjectLink', con=engine, index=False, if_exists="replace")
    return df_project_link
def generate_announcement(df_users, df_research_group):
    announcements = defaultdict(list)
    for i in range(number_of_announcements):
        announcements["id"].append(i)
        announcements["title"].append(fake.sentence())
        announcements["text"].append(fake.text())
        announcements["author"].append(df_users["id"].values[i % len(df_users["id"])])
        announcements["date"].append(fake.past_datetime())
        announcements["research_group_id"].append(df_research_group["id"].values[i % len(df_research_group["id"])])
        types = ["def", "Default"]
        announcements["ann_type"].append(types[fake.pyint(0, len(types)-1)])
    df_announcements = pd.DataFrame(announcements)
    if is_printing:
        print(df_announcements)
    df_announcements.to_sql('Announcement', con=engine, index=False, if_exists="replace")
    return df_announcements

