from playwright.sync_api import Page, expect
import uuid

BASE_URL = "http://localhost:5173"


# TC08 - Login Page
def test_login_page(page: Page):

    page.goto(BASE_URL)
    page.get_by_role("button", name="Login").click()

    expect(page.get_by_role("heading", name="Welcome back")).to_be_visible()

    page.screenshot(path="login_page.png")


# TC09 - Valid Login
def test_valid_login(page: Page):

    page.goto(BASE_URL)
    page.get_by_role("button", name="Login").click()

    page.locator('input[type="email"]').fill("demo@jobhive.com")
    page.locator('input[type="password"]').fill("Demo@123")

    page.get_by_role("button", name="Log In").click()

    expect(page.get_by_role("heading", name="Welcome back")).not_to_be_visible()

    page.screenshot(path="valid_login.png")


# TC10 - Invalid Login
def test_invalid_login(page: Page):

    page.goto(BASE_URL)
    page.get_by_role("button", name="Login").click()

    page.locator('input[type="email"]').fill("wrong@gmail.com")
    page.locator('input[type="password"]').fill("Wrong123")

    page.get_by_role("button", name="Log In").click()

    expect(page.get_by_role("heading", name="Welcome back")).to_be_visible()

    page.screenshot(path="invalid_login.png")


# TC11 - Empty Login
def test_empty_login(page: Page):

    page.goto(BASE_URL)
    page.get_by_role("button", name="Login").click()

    page.get_by_role("button", name="Log In").click()

    expect(page.get_by_role("heading", name="Welcome back")).to_be_visible()

    page.screenshot(path="empty_login.png")


# TC12 - Registration Page
def test_registration_page(page: Page):

    page.goto(BASE_URL)
    page.get_by_role("button", name="Register").click()

    expect(
        page.get_by_role("heading", name="Create your account")
    ).to_be_visible()

    page.screenshot(path="registration_page.png")


# TC13 - Password Mismatch
def test_password_mismatch(page: Page):

    page.goto(BASE_URL)
    page.get_by_role("button", name="Register").click()

    page.locator('input[type="text"]').fill("Test User")
    page.locator('input[type="email"]').fill("testuser@gmail.com")

    page.locator('input[type="password"]').nth(0).fill("Test@123")
    page.locator('input[type="password"]').nth(1).fill("Wrong@123")

    page.get_by_role("button", name="Create Account").click()

    expect(
        page.get_by_role("heading", name="Create your account")
    ).to_be_visible()

    page.screenshot(path="password_mismatch.png")


# TC14 - Successful Registration
def test_successful_registration(page: Page):

    page.goto(BASE_URL)
    page.get_by_role("button", name="Register").click()

    email = f"test{uuid.uuid4().hex[:10]}@example.com"

    page.locator('input[type="text"]').fill("Automation Test User")
    page.locator('input[type="email"]').fill(email)

    page.locator('input[type="password"]').nth(0).fill("Test@123")
    page.locator('input[type="password"]').nth(1).fill("Test@123")

    page.get_by_role("button", name="Create Account").click()

    expect(
        page.get_by_role("heading", name="Create your account")
    ).not_to_be_visible()

    page.screenshot(path="successful_registration.png")