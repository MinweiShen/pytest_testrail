This is a functional demo of how to integrate TestRail with pytest. I mainly use it for E2E web application testing using Selenium.

# Before testing
1. Set variables in ``testrail/consts.py`` based on your TestRail setting
2. If necessary, test related variables are in ``tests/consts.py``
3. All tests are linked with TestRail test cases by the decorator ``@pytest.mark.testrail(id)`` where ``id`` is the test case id in TestRail.

# How to use
Except for the pytest's command line paramters, I also added some custom parameters:
1. ``--platform=<platform>``: this is used to specify test platform
2. ``--browser=<browser>``: specify selenium webdriver
3. ``--publish``: if set, result will be published on TestRail
4. ``--include_all``: when creating a test run, include all test cases
5. ``--tr_name=<test run name>``: when publishing, create a new test run with this name
6. ``--tr_id=<run id>``: run tests given a test run
7. ``--ids=id1,id2,id3....``: run tests with given id

# Use cases
I think use cases are more helpful in explaining how it works.

```
# as normal pytest case discovery, run tests in test_demo_class
# publish the result to TestRail using a auto-generated name
pytest test_demo_class --publish
```
```
# run all tests, publish results to a new test run, test run name is 
# auto-generated
pytest --platform=qe --browser=0 --publish
```
```
# run all tests, publish results to a new test run named 'Auto Test Run'
pytest --publish --tr_name='Auto Test Run'
```

```
# run all tests in test run 123, publish results
pytest --tr_id=123
```
```
# only run test 1,2,3
pytest --ids=1,2,3
```
```
# create a new test run with all test cases, but only run test 1, 2, 3
# and publish results
pytest --ids=1,2,3 --publish --include_all
```

# License
MIT