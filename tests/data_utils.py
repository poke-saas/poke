"""
Methods to create testable data.
"""
from backend.internal_utils import *
from backend.db_entry import *
# CONSTANTS


def create_test_data():
    # Create organization for founders
    new_org = add_new_org()
    org_template = get_orgs_template()

    org_template['name'] = "Founders"
    set_org(new_org, org_template)

    # Create users that are tied to founders
    new_user_1 = add_new_user()
    user_template = get_user_template()
    user_template['name'] = "Siraj Chokshi"

    add_org_user(new_org, new_user_1)

    new_user_2 = add_new_user()
    add_org_user(new_org, new_user_2)

create_test_data()

