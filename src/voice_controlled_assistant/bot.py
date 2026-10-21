from os import getenv

from dotenvx import load_dotenv
from playwright.sync_api import sync_playwright

class Bot:
    # Method works only for the college websites among LACCD
    def login(self, url: str) -> bool:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto(url)

            # Viewing the homepage.
            page.get_by_role('button', name='Login').click()
            page.get_by_role('link', name='SIS Portal').click()

            # Directed to an external page where prompted to input credentials for sign in.
            with page.expect_popup() as new_page_info:
                page.wait_for_load_state()

            new_page = new_page_info.value

            # Accessing credentials for sign in.
            load_dotenv()
            student_id: str = getenv('STUDENT_ID')
            pwd: str = getenv('PORTAL_PASSWORD')

            new_page.get_by_role('textbox', name='User Account').fill(student_id)
            new_page.get_by_role('textbox', name='Password').fill(pwd)
            new_page.get_by_role('button', name='Sign in').click()

            browser.close()

        return True