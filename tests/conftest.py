from pytest import fixture

from app.conect_with_db import sync_engine, Base
from app.config import settings


@fixture(scope="session", autouse=True)
# With param "scope" we set up expiration fixture:
# "function" (default state) - fixture ends up after finish work function
#           if test like function, that uses fixture, finish work, also finish work fixture
# "class" - fixture ends up after finishing work class (with group tests)
# "module" - fixture ends up after finishing work module like file
# "package" - fixture ends up after finishing work package modules
# "session" - fixture ends up after finishing work testing session
# "autouse" - fixture will be executed, not depends on used this fixture in test function or no
def started_db_session():
    # Fixture, which removes all tables in our testing database
    # this is preparation for settings testing environment
    if settings.MODE == "TEST":
        print(f"\nTesting started with {settings.DATABASE_NAME}")
        Base.metadata.drop_all(bind=sync_engine)
        # and after, creates all needed tables in db
        Base.metadata.create_all(bind=sync_engine)
        print("\nPytest is working...")
        # current fixture passes control processes (script) execution to pytest
        yield
        print("\nPytest finished work")
        print("\nTesting is finished")

