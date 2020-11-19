
python_library(
  name = 'test_helpers',
  sources = ['conftest.py', 'test_sqlite.py'],
  dependencies = [
      ':pytest-django',
      ':templates',
      'django/core/management/commands/migrate.py:../../../django',
      'django/core/management/commands/createcachetable.py:../../../django',
  ]
)

python_requirement_library(
    name = 'pytest-django',
    requirements = ['pytest-django==4.1.0']
)

resources(
    name = 'templates',
    sources = ['templates/**']
)
