import os
import pytest
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--remote-allow-origins=*")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # Attach driver to request instance so hooks can access it
    request.node.driver = driver

    yield driver

    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    
    # Store report status on the item
    setattr(item, f"rep_{rep.when}", rep)

    # Attach screenshot to pytest-html report on test failure
    if rep.when == "call" and rep.failed:
        driver = getattr(item, "driver", None)
        if driver:
            screenshots_dir = Path("screenshots")
            screenshots_dir.mkdir(exist_ok=True)
            
            screenshot_name = f"FAILED_{item.name}.png"
            screenshot_path = screenshots_dir / screenshot_name
            
            # Save screenshot file locally
            driver.save_screenshot(str(screenshot_path))
            
            # Embed image into pytest-html report
            pytest_html = item.config.pluginmanager.getplugin("pytest-html")
            if pytest_html:
                extra = getattr(rep, "extra", [])
                extra.append(pytest_html.extras.image(str(screenshot_path)))
                rep.extra = extra