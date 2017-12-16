# Regular Length Expression (RLE)

Add description here...

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing. See "Using the Project" below for notes on how to use the project in a live environment.

### Prerequisites

Python3 is required to run this application. The list of third-party dependencies can be found in the `requirements.txt` file.

### Installing

Create a Python3 virtual environment.

```
python3 -m venv .venv
```

If you get an error saying "returned non-zero exit status 1",
make sure you have Python3 and pip3 upgraded to the current version and
if that doesn't work, re-run the above command as:

```
python3 -m venv --without-pip .venv
```

Activate the virtual environemnt

```
source .venv/bin/activate
```

Install the third-party dependencies.

```
pip3 install -r requirements.txt
```

## Running the tests

We are using [pytest](https://docs.pytest.org/en/2.9.1/getting-started.html) for test writing. Run this snippet in a terminal window to run the tests - you need to be in the root `./jira-api`.

```
pytest -vv
```

You can also run the test suite with a coverage report. Although it may not be possible to achieve 100% coverage - nor does 100% coverage ensure a well written test suite - it is still a useful heuristic in assessing overall application health.

```
pytest --cov-report html --cov functions --verbose
```

After running the coverage report, open the summary in your browser with the following.

```
open htmlcov/index.html
```

### Break down into end to end tests

...

```
test_get_task() # authenticates and gets task status
```

### And coding style tests

Check for PEP8 style guide adherence.

```
test_pep8(self)
```

## Using the Project

etc...

## Built With

* [Python3 venv](https://docs.python.org/3/library/venv.html) - Dependency Management

## Contributing

Please read [CONTRIBUTING.md](https://google.com) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

Describe how we version here.

## Authors

* **Sean MacRae** - *Initial work* - [smacrae](https://google.com)

See also the list of [contributors](https://google.com) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://google.com) file for details

## Acknowledgments

Tip of the hat to [a person](https://google.com) for...
