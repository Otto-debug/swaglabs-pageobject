import pytest
import undetected_chromedriver as uc

@pytest.fixture(scope="session")
def driver():
    options = uc.ChromeOptions()
    options.add_argument('headless')
    driver = uc.Chrome(version_main=126, options=options)
    yield driver
    driver.quit()