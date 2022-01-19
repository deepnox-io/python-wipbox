# python-deepnox-box-in-progress[![codecov](https://codecov.io/gh/deepnox-io/python-deepnox-box-in-progress/branch/devel/graph/badge.svg?token=IGALD1N09C)](https://codecov.io/gh/deepnox-io/python-deepnox-box-in-progress)[![license](https://img.shields.io/github/license/deeepnox-io/deeepnox-io.svg)](https://github.com/deepnox-io/python-deepnox-box-in-progress/blob/main/LICENSE)[![GitHub contributors](https://img.shields.io/github/contributors/python-deepnox-box-in-progress/locust.svg)](https://github.com/deepnox-io/python-deepnox-box-in-progress/graphs/contributors)<!--[![PyPI](https://img.shields.io/pypi/v/locust.svg)](https://pypi.org/project/locust/)[![PyPI](https://img.shields.io/pypi/pyversions/locust.svg)](https://pypi.org/project/locust/)-->> A set of modern Python libraries under development to simplify the execution of reusable routines by different projects.## Table of Contents* [Synopsis](#synopsis)* [Usage](#usage)* [Installation](#installation)* [Build](#build)* [Tests](#tests)* [Développement](#develop)* [Compatibility](#compatibility)* [Issues](#issues)* [Contributing](#contributing)* [Credits](#credits)* [Resources](#resources)* [History](#history)* [License](#license)## <a name="synopsis">Synopsis</a>A set of modern Python libraries under development to simplify the execution of reusable routines by different projects.Each namespace is intended to become a separate library, subject to validation of its quality level.Each of the namespaces named `deepnox.*` is intended to be externalized as part of a specialized Python operating package.## <a name="usage">Usage</a>```python```## <a name="installation">Installation</a>### Using `pip````bashpip3 install deepnox-box-in-progress```### Using `setup.py`Clone the repository:```bashgit clone https://github.com/deepnox-io/python-deepnox-box-in-progresscd deepnox-box-in-progressgit checkout main # or any branch, tag or commit...```Install dependencies:```bashpip install -r requirements.txtpip install -r requirements-test.txt # Optionnel: pour exécution des tests unitaires.```## <a name="build">Build</a>```bashpython3 setup.py build```## <a name="tests">Tests</a>```bashpython3 setup.py test```### Code coverage[Coverage.py](https://coverage.readthedocs.io/en/latest/) is required.To run a code coverage process:```bashcoverage run --omit '*/.venv/*' -m pytest test && coverage report -m```## DevelopPlease install dependencies from files:- `requirements.txt`- `requirements-dev.txt`- `requirements-test.txt`Then install the [pre-commit](https://pre-commit.com/) hook to forbidden pushing code if unit tests are not passing.## <a name="issues"> Issues</a>Feel free to [submit issues](https://github.com/deepnox-io/python-deepnox-log/issues) and enhancement requests.## <a name="contributing">Contributing</a>Please refer to project's style guidelines and guidelines for submitting patches and additions. In general, we follow the "fork-and-pull" Git workflow.1. **Fork** the repo on GitHub2. **Clone** the project to your own machine3. **Commit** changes to your own branch4. **Push** your work back up to your fork5. Submit a **Pull request** so that we can review your changes**NOTE**: Be sure to merge the latest from "upstream" before making a pull request!## <a name="credits">Credits</a>Thank you very much to this used or integrated open source developments:## <a name="resources">Resources</a>* [Making a Python package](https://python-packaging-tutorial.readthedocs.io/en/latest/setup_py.html)* [Using pre-commit git hooks to automate code checks](https://ericmjl.github.io/essays-on-data-science/terminal/pre-commits/)## Dependencies### Commit hooks* Code formatting: [Black](https://github.com/psf/black)* Documentation formatting: [http://www.pydocstyle.org/en/stable/usage.html] * [isort](https://github.com/PyCQA/isort)## <a name="history">History</a>Please refer to [the changelog file](CHANGELOG.md).## <a name="license">License</a>>> [The MIT License](https://opensource.org/licenses/MIT)>> Copyright (c) 2021 [Deepnox SAS](https://deepnox.io/), Paris, France.>> Permission is hereby granted, free of charge, to any person obtaining a copy> of this software and associated documentation files (the "Software"), to deal> in the Software without restriction, including without limitation the rights> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell> copies of the Software, and to permit persons to whom the Software is> furnished to do so, subject to the following conditions:>> The above copyright notice and this permission notice shall be included in all> copies or substantial portions of the Software.>> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE>AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE> SOFTWARE.>## <a name="resources" /> ResourcesAmong others, to carry out this large and infinite project, we made use, among many others, of the following documentary resources.Thank you to their authors for sharing their knowledge with our team.### CI/CD- [PyTest With GitHub Actions](https://blog.dennisokeeffe.com/blog/2021-08-08-pytest-with-github-actions)### Unit tests- [Unit test log output with python](https://memotut.com/en/8a92970f0f6e5309e1df/)<!--## Variables d'environnement```bashexport PYTHON_VENV_HOME="~/Workspace/.venv/3.9"export DPS_HOME="~/Workspace/io/deepnox/sandbox-python"export PATH="${PATH}:${PYTHON_VENV_HOME}/bin"export PYTHONPATH="${DPS_HOME}/src"```-->