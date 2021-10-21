pytest -v -m "regression" --html=Reports\reports.html testCases/test_login_logout.py --browser chrome
pytest -v -m "sanity" --html=Reports\reports.html testCases/test_new_entity.py --browser chrome