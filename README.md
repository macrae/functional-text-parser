![pytest](https://github.com/macrae/functional-text-parser/workflows/pytest/badge.svg)
![Publish Docker](https://github.com/macrae/functional-text-parser/workflows/Publish%20Docker/badge.svg)

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

Create a and activate a Python3.6 virtual environment.

```
python3 -m venv .venv
source .venv/bin/activate
```

Install the third-party dependencies.

```
pip3 install -r requirements.txt
pip3 install -r requirements-dev.txt
```

## Running the tests

Snippets below need to be executed in the root of the Flask application, e.g. `./functional_text_parser/app`.

We are using [pytest](https://docs.pytest.org/en/2.9.1/getting-started.html) for testing. To run tests verbosely use:

```
python3 -m pytest -vv
```

We are using [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/) for test coverage reporting. To run tests and generate an HTML formatted report use:

```
pytest --cov-report html --cov functions --verbose
```

After running the coverage report, open the summary in your browser with the following.

```
open cov_html/index.html
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

## Using the Project

You can build and run the Docker container and host the Flask app locally with:

```
docker build -t python:text_parser . -f Dockerfile
docker run -d -p 5000:5000 python:text_parser
```

Then calling the service with:

```
curl -i http://localhost:5000/encode/api/v1.0/AABBCCDDDDD
```

The response will be:

```
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 27
Server: Werkzeug/0.13 Python/3.6.9
Date: Wed, 22 Apr 2020 20:46:54 GMT

{
  "encode": "2A2B2C5D"
}
```

## Built With

* [Python3](https://docs.python.org/3/library/venv.html) - Dependency Management
* [Flask](http://flask.pocoo.org/) - Web Application Service
* [Docker](https://devcenter.heroku.com/) - Cloud Application Service

## Contributing

Please read [CONTRIBUTING.md](https://github.com/macrae/functional-text-parser/graphs/contributors) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

Describe how we version here.

## Authors

* **Sean MacRae** - *Initial work* - [smacrae](https://github.com/macrae)

See also the list of [contributors](https://github.com/macrae/functional-text-parser/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://google.com) file for details
