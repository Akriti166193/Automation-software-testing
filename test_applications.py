from playwright.sync_api import Page, expect

BASE_URL = "http://localhost:5173"

EMAIL = "demo@jobhive.com"
PASSWORD = "Demo@123"


# Reusable Login Function
def login(page: Page):

    page.goto(BASE_URL)

    page.get_by_role("button", name="Login").click()

    page.locator('input[type="email"]').fill(EMAIL)
    page.locator('input[type="password"]').fill(PASSWORD)

    page.get_by_role("button", name="Log In").click()

    expect(page.get_by_text("Job Listings")).to_be_visible()


# TC15 - Apply Without Login
def test_apply_without_login(page: Page):

    page.goto(BASE_URL)

    page.get_by_role("button", name="Apply Now").first.click()

    # Website should ask user to login
    expect(
        page.get_by_role("heading", name="Welcome back")
    ).to_be_visible()

    page.screenshot(path="apply_without_login.png")


# TC16 - Successful Job Application
def test_successful_application(page: Page):

    login(page)

    # Choose a job not already applied for
    job = page.locator(".card").filter(
        has=page.get_by_role("heading", name="UI/UX Designer")
    )

    expect(job).to_be_visible()

    job.get_by_role("button", name="Apply Now").click()

    # Button should change to Withdraw
    expect(
        job.get_by_role("button", name="Withdraw")
    ).to_be_visible()

    page.screenshot(path="successful_application.png")


# TC17 - My Applications
def test_my_applications(page: Page):

    login(page)

    # Open Applications section
    page.get_by_text("Applications", exact=True).click()

    # Verify application section is displayed
    expect(
        page.get_by_text("My Applications")
    ).to_be_visible()

    page.screenshot(
        path="my_applications.png",
        full_page=True
    )


# TC18 - Logout
def test_logout(page: Page):

    login(page)

    page.get_by_text("Profile", exact=True).click()

    # Locate logout button
    page.get_by_role("button", name="Logout").click()

    # Verify logged-out navigation
    expect(
        page.get_by_role("button", name="Login")
    ).to_be_visible()

    page.screenshot(path="logout.png")