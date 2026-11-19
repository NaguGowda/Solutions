class BrowserLauncher:
    def __init__(self, playwright, browser_name="chromium", headless=False):
        self.playwright = playwright
        self.browser_name = browser_name
        self.headless = headless
        self.browser = None
        self.context = None
        self.page = None

    async def launch_maximized(self):
        browser_type = getattr(self.playwright, self.browser_name)
        self.browser = await browser_type.launch(
            channel="chrome" if self.browser_name == "chromium" else None,
            headless=self.headless,
            args=["--start-maximized"] if self.browser_name == "chromium" else []
        )
        self.context = await self.browser.new_context(no_viewport=True)
        self.page = await self.context.new_page()
        return self.page

    async def open_url(self, url: str):
        await self.page.goto(url)

    async def close(self):
        if self.context:
            await self.context.close()
        if self.browser:
            await self.browser.close()
