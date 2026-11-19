import asyncio
import pytest
from patchright.async_api import async_playwright, expect
from browsemng import BrowserLauncher

@pytest.mark.asyncio
async def test_page():
    browsers_to_test = ["chromium"]
    url = "https://uat-digitalfactory.heromotocorp.com/login"

    async with async_playwright() as p:
        for browser_name in browsers_to_test:
            launcher = BrowserLauncher(playwright=p, browser_name=browser_name, headless=False)
            try:
                page = await launcher.launch_maximized()
                await launcher.open_url(url)

                sso = page.get_by_role("button", name="Sign in with Google")
                await sso.click()

                await expect(page.get_by_text("Head Count")).to_be_visible()
                await page.wait_for_timeout(50000)

            finally:
                await launcher.close()

if __name__ == "__main__":
    pytest.main([__file__])




# from ast import main
#
# from browser_manager import BrowserLauncher
# import pytest
# from patchright.sync_api import sync_playwright, expect
#
# def test_page():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(channel="chrome", headless=False)
#         page = browser.new_page()
#         browsers_to_test = ["chromium"]
#         url= page.goto("https://uat-digitalfactory.heromotocorp.com/login")
#
#         with (sync_playwright() as p):
#             for browser_name in browsers_to_test:
#                 launcher = BrowserLauncher(playwright=p, browser_name=browser_name, headless=False)
#                 try:
#                     page = launcher.launch_maximized()
#                     launcher.open_url(url)
#                     SSO = page.get_by_role("button", name="Sign in with Google")
#                     SSO.click()
#                     expect(page.get_by_text("Head Count")).to_be_visible()
#                     page.wait_for_timeout(1000)
#
#
#                 finally:
#                     launcher.close()
#
#     if __name__ == "__main__":
#         main()
