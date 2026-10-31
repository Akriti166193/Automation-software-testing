from playwright.sync_api import Page, expect


# TC02 - Valid Job Search
def test_job_search(page: Page):

    page.goto("http://localhost:5173")

    search = page.get_by_placeholder("Search by title or company")

    search.fill("Frontend Developer")

    expect(
        page.get_by_role("heading", name="Frontend Developer")
    ).to_be_visible()

    expect(page.get_by_text("1 job found")).to_be_visible()

    page.screenshot(path="search_result.png", full_page=True)


# TC03 - Invalid Job Search
def test_invalid_job_search(page: Page):

    page.goto("http://localhost:5173")

    search = page.get_by_placeholder("Search by title or company")

    search.fill("XYZ123InvalidJob")

    expect(page.get_by_text("0 jobs found")).to_be_visible()

    expect(page.get_by_role("button", name="Apply Now")).to_have_count(0)

    page.screenshot(path="invalid_search.png", full_page=True)