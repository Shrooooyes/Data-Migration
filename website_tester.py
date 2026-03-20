from playwright.sync_api import sync_playwright
import sys


class WebsiteTester:
    def __init__(self, browser_type="chromium", headless=True):
        self.browser_type = browser_type
        self.headless = headless
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

    def __enter__(self):
        self.playwright = sync_playwright().start()
        browser_map = {
            "chromium": self.playwright.chromium,
            "firefox": self.playwright.firefox,
            "webkit": self.playwright.webkit,
        }
        self.browser = browser_map[self.browser_type].launch(headless=self.headless)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        return self

    def __exit__(self, *args):
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()

    def goto(self, url):
        self.page.goto(url)
        return self

    def find_element(self, selector):
        return self.page.locator(selector)

    def click(self, selector):
        self.page.locator(selector).click()
        return self

    def fill(self, selector, text):
        self.page.locator(selector).fill(text)
        return self

    def get_text(self, selector):
        return self.page.locator(selector).text_content()

    def get_title(self):
        return self.page.title()

    def get_url(self):
        return self.page.url

    def screenshot(self, path):
        self.page.screenshot(path=path)
        return self

    def wait_for_selector(self, selector, timeout=5000):
        self.page.wait_for_selector(selector, timeout=timeout)
        return self


def main():
    url = sys.argv[1] if len(sys.argv) > 1 else "https://example.com"
    
    with WebsiteTester(headless=True) as tester:
        tester.goto(url)
        print(f"Title: {tester.get_title()}")
        print(f"URL: {tester.get_url()}")
        tester.screenshot("screenshot.png")
        print("Screenshot saved to screenshot.png")


if __name__ == "__main__":
    main()
