# Regular Length Expression (RLE)

This application maps a string to a string as such:

```
"AABBCCDDDE" => "2A2B2C3D1E"
```

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

Snippets below need to be executed in the root of the Flask application, e.g. `./functional_text_parser/app`.

We are using [pytest](https://docs.pytest.org/en/2.9.1/getting-started.html) for testing. To run tests verbosely use:

```
pytest -vv
```

We are using [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/) for test coverage reporting. To run tests and generate an HTML formatted report use:

```
pytest --cov-report html --cov functions --verbose
```

After running the coverage report, open the summary in your browser with the following.

```
open htmlcov/index.html
```

_Although it may not be possible to achieve 100% coverage - nor does 100% coverage ensure a well written test suite - it is still a useful heuristic in assessing the overall health of an application._

### Break down into end to end tests

Since `rle` is the main application method and it is composed of all other methods in the application to achieve 100% test coverage we would only need to write tests for it.

```
def test_rle():
    assert rle('A') == '1A'
    assert rle('AA') == '2A'
    assert rle('AAAB') == '3A1B'
    assert rle('AAABB55') == '3A2B25'
```

However, for documentation and future test-driven development purposes tests were also written for each method composing `rle`, for example:

```
string = 'AABBCDDDE'


def test_listify_string():
    l = listify_string(string)

    assert l == ['A', 'A', 'B', 'B', 'C', 'D', 'D', 'D', 'E']


def test_get_pairs():
    pairs = get_pairs(listify_string(string))

    assert pairs == [('A', 'A'), ('A', 'B'), ('B', 'B'), ('B', 'C'),
                     ('C', 'D'), ('D', 'D'), ('D', 'D'), ('D', 'E')]
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
