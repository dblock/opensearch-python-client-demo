# OpenSearch Python Client Demo

Makes requests to Amazon OpenSearch using the [OpenSearch Python Client](https://github.com/opensearch-project/opensearch-py).

### Install Prerequisites

#### Pyenv

Use pyenv to manage multiple versions of Python. This can be installed with [pyenv-installer](https://github.com/pyenv/pyenv-installer) on Linux and MacOS, and [pyenv-win](https://github.com/pyenv-win/pyenv-win#installation) on Windows.

```
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
```

Follow the intructions to add `pyenv init` into your `.bashrc`, reopen a new shell.

#### Python 3.9

Python projects in this repository use Python 3.x. The latest version at the time of writing this is 3.11.1. See the [Python Beginners Guide](https://wiki.python.org/moin/BeginnersGuide) if you have never worked with the language.

```
$ python3 --version
Python 3.11.1
```

If you are using pyenv.

```
pyenv install 3.11.1
pyenv global 3.11.1
```

#### Pipenv

This project uses [pipenv](https://pipenv.pypa.io/en/latest/), which is typically installed with `pip install --user pipenv`. Pipenv automatically creates and manages a virtualenv for your projects, as well as adds/removes packages from your `Pipfile` as you install/uninstall packages. It also generates the ever-important `Pipfile.lock`, which is used to produce deterministic builds.

```
$ pip install pipenv

$ pipenv --version
pipenv, version 2022.12.19
```

On Windows, run `pyenv rehash` if `pipenv` cannot be found. This rehashes pyenv shims, creating a `pipenv` file in `/.pyenv/pyenv-win/shims/`.

#### Install Packages

Install dependencies.

```
pipenv install
```

## Running

Create an OpenSearch domain in (AWS) which support IAM based AuthN/AuthZ.

```
export AWS_ACCESS_KEY_ID=
export AWS_SECRET_ACCESS_KEY=
export AWS_SESSION_TOKEN=
export AWS_REGION=us-west-2

export ENDPOINT=https://....us-west-2.es.amazonaws.com

pipenv run python example.py 
```

This will output the version of OpenSearch and a search result.

```
opensearch: 2.3.0
{'director': 'Bennett Miller', 'title': 'Moneyball', 'year': 2011}
```

The [code](sync/example.py) will create an index, add a document, search for it, then cleanup. And for async client, the following [code](async/example.py) can be used.

## License 

This project is licensed under the [Apache v2.0 License](LICENSE.txt).

## Copyright

Copyright OpenSearch Contributors. See [NOTICE](NOTICE.txt) for details.
