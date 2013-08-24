A description of your project
Links to the project's ReadTheDocs page
A TravisCI button showing the state of the build
"Quickstart" documentation (how to quickly install and use your project)
A list of non-Python dependencies (if any) and how to install them



Run tests -

nosetests --with-coverage --cover-erase --cover-package=app --cover-html
add new tests to the tests folder
coverage report will appear under the folder coverage, in the index.html folder