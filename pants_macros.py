def django_tests(**kwargs):
    python_library(name='lib')

    deps = kwargs.pop('dependencies', [])
    python_tests(
        dependencies = [
            'tests/test_sqlite.py:test_helpers',
            'django/db/backends/sqlite3/base.py:../../../django',
            ':lib'
        ] + deps,
        **kwargs
    )
