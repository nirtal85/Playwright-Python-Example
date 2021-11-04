def test_login(page):
    page.type("[data-test=username]", "standard_user")
    page.type("[data-test=password]", "secret_sauce")
    page.click("[data-test=login-button]")
    assert (page.url == "https://www.dasdsa.com/inventory.html")


def test_invalid_login(page):
    page.type("[data-test=username]", "standard_user")
    page.type("[data-test=password]", "secret_sauce1")
    page.click("[data-test=login-button]")
    assert (page.text_content(
        "data-test=error") == "Epic sadface: Username and password do not match any user in this service")
