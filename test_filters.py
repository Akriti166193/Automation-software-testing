from playwright.sync_api import Page, expect


# TC04 - Location Filter Testing
def test_location_filter(page: Page):

    page.goto("http://localhost:5173")

    # Select Remote location
    page.get_by_role("combobox").nth(0).select_option(label="Remote")

    # Verify result count
    expect(page.get_by_text("2 jobs found")).to_be_visible()

    # Verify Remote jobs
    expect(
        page.get_by_role("heading", name="UI/UX Designer")
    ).to_be_visible()

    expect(
        page.get_by_role("heading", name="React Native Developer")
    ).to_be_visible()

    page.screenshot(path="location_filter.png", full_page=True)


# TC05 - Job Type Filter Testing
def test_job_type_filter(page: Page):

    page.goto("http://localhost:5173")

    # Select Internship
    page.get_by_role("combobox").nth(1).select_option(label="Internship")

    # Verify result
    expect(page.get_by_text("1 job found")).to_be_visible()

    expect(
        page.get_by_role("heading", name="Marketing Intern")
    ).to_be_visible()

    # Verify unrelated job is hidden
    expect(
        page.get_by_role("heading", name="Frontend Developer")
    ).not_to_be_visible()

    page.screenshot(path="internship_filter.png", full_page=True)


# TC06 - Category Filter Testing
def test_category_filter(page: Page):

    page.goto("http://localhost:5173")

    # Select Design category
    page.get_by_role("combobox").nth(2).select_option(label="Design")

    # Verify result
    expect(page.get_by_text("1 job found")).to_be_visible()

    expect(
        page.get_by_role("heading", name="UI/UX Designer")
    ).to_be_visible()

    page.screenshot(path="category_filter.png", full_page=True)


# TC07 - Combined Filter Testing
def test_combined_filters(page: Page):

    page.goto("http://localhost:5173")

    # Search job
    page.get_by_placeholder(
        "Search by title or company"
    ).fill("React")

    # Select Remote location
    page.get_by_role("combobox").nth(0).select_option(label="Remote")

    # Verify matching job
    expect(
        page.get_by_role("heading", name="React Native Developer")
    ).to_be_visible()

    # Verify result count
    expect(page.get_by_text("1 job found")).to_be_visible()

    # Verify unrelated job is hidden
    expect(
        page.get_by_role("heading", name="Frontend Developer")
    ).not_to_be_visible()

    page.screenshot(path="combined_filter.png", full_page=True)