from faker import Faker
import pandas as pd
from sqlalchemy import create_engine
from collections import defaultdict

is_printing = False
number_of_links = 10
number_of_announcements = 10
number_of_users = 10
number_of_research_groups = 10
number_of_research_group_users = 10
number_of_research_group_guides = 10


fake = Faker()
engine = create_engine('postgresql://admin:pleasechangeme@localhost:5432/backend', echo=False)

def run():
    links = generate_link()
    users = generate_user()
    research_groups = generate_research_group()
    research_group_users = generate_research_group_users(users, research_groups)
    # research_group_guides = generate_research_group_guides(research_groups, guides)
    # announcements = generate_announcement(users, research_groups)

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
    df_links.to_sql('link', con=engine, index=False, if_exists="replace")
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
    df_users.to_sql('user', con=engine, index=False, if_exists="replace")
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
    df_research_groups.to_sql('researchGroup', con=engine, index=False, if_exists="replace")
    return df_research_groups

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
    df_research_group_users.to_sql('researchGroupUser', con=engine, index=False, if_exists="replace")
    return df_research_group_users

def generate_research_group_guides(df_research_groups, df_guides):
    research_group_guides = defaultdict(list)
    for i in range(number_of_research_group_guides):
        research_group_guides["id"].append(i)
        research_group_guides["is_public"].append(fake.boolean)
        research_group_guides["research_group"].append(df_research_groups["id"].values[i % len(df_research_groups["id"])])
        research_group_guides["guide"].append(df_guides["id"].values[i % len(df_guides["id"])])
    df_research_group_guides = pd.DataFrame(research_group_guides)
    if is_printing:
        print(df_research_group_guides)
    df_research_group_guides.to_sql('researchGroupGuides', con=engine, index=False, if_exists="replace")
    return df_research_group_guides

def generate_announcement(df_users, df_research_group):
    announcements = defaultdict(list)
    for i in range(number_of_announcements):
        announcements["id"].append(i)
        announcements["title"].append(fake.sentence())
        announcements["text"].append(fake.text())
        announcements["author"].append(df_users["id"].value[i % len(df_users["id"])])
        announcements["date"].append(fake.past_datetime())
        announcements["research_group_id"].append(df_research_group["id"].value[i % len(df_research_group["id"])])
        types = ["def", "Default"]
        announcements["ann_type"].append(types[fake.pyint(0, len(types))])
    df_announcements = pd.DataFrame(announcements)
    if is_printing:
        print(df_announcements)
    df_announcements.to_sql('announcement', con=engine, index=False, if_exists="replace")
    return df_announcements

