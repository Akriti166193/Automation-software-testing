from playwright.sync_api import Page, expect

def test_homepage(page: Page):

    # Open JobHive website
    page.goto("http://localhost:5173")

    # Verify website title
    expect(page).to_have_title("JobHive — Find Your Next Role")

    # Verify homepage heading
    expect(
        page.get_by_role("heading", name="Find the job that fits your life")
    ).to_be_visible()

    # Verify jobs are displayed
    expect(page.get_by_text("8 jobs found")).to_be_visible()

    # Take screenshot
    page.screenshot(path="homepage.png", full_page=True)