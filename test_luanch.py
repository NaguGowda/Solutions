# https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

import pytest
from patchright.sync_api import sync_playwright, expect

def test_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=False)
        page = browser.new_page()
        page.goto("https://demo.nopcommerce.com/")

        logo = page.get_by_alt_text("nopCommerce demo store")
        expect(logo).to_be_visible(timeout=15000)

        expect(page.get_by_text("Welcome to our store")).to_be_visible()
        expect(page.get_by_text("Featured products")).to_be_visible()
        expect(page.get_by_text("News")).to_be_visible()
        browser.close()
