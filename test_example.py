import pytest
from playwright.sync_api import Page, expect


class TestWebsiteBasics:
    def test_page_loads(self, page: Page):
        page.goto("https://example.com")
        expect(page).to_have_title("Example Domain")

    def test_element_exists(self, page: Page):
        page.goto("https://example.com")
        h1 = page.locator("h1")
        expect(h1).to_be_visible()
        expect(h1).to_contain_text("Example Domain")

    def test_link_click(self, page: Page):
        page.goto("https://example.com")
        page.get_by_text("More information...").click()
        expect(page).to_have_url("https://www.iana.org/help/example-domains")


class TestFormInteraction:
    def test_text_input(self, page: Page):
        page.goto("https://example.com")
        # Customize based on target website
        input_field = page.locator("input[name='search']")
        if input_field.count() > 0:
            input_field.fill("test query")
            expect(input_field).to_have_value("test query")

    def test_button_click(self, page: Page):
        page.goto("https://example.com")
        button = page.locator("button[type='submit']")
        if button.count() > 0:
            button.click()


class TestNavigation:
    def test_back_forward(self, page: Page):
        page.goto("https://example.com")
        page.goto("https://www.iana.org/domains/reserved")
        page.go_back()
        expect(page).to_have_url("https://example.com/")
        page.go_forward()
        expect(page).to_have_url("https://www.iana.org/domains/reserved")

    def test_multiple_pages(self, page: Page):
        pages = ["https://example.com", "https://www.iana.org/domains/reserved"]
        for url in pages:
            page.goto(url)
            assert len(page.title()) > 0
