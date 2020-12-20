python_library(
    sources = ['**/*.py'],
    dependencies = [':locales']
)

resources(
    name = 'locales',
    sources = ['conf/locale/**/*.po', 'conf/locale/**/*.mo']
)

# Useful when using IntelliJ/PyCharm remote debugging. Importing `pydevd_pycharm` at
# the breakpoint will cause dep inference to add this dep on the remote debugger client.
python_requirement_library(
    name = "pydevd-pycharm",
    requirements=["pydevd-pycharm==203.5419.8"],
)
