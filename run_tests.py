from tests.calendar_tests import *
from models import *
from extensions import db
from app import app
from calendars import *
from datetime import datetime, time

# createFakeSlots(app, db, Slot)
# createFakeUsers(app, db, User)

# def test_get_company_calendar(group_id):
#     company = get_company_calendar(group_id)
#     for item in company['data']:
#         print(item)

# with app.app_context():
#     # test_get_company_calendar(11223344)
#     pass