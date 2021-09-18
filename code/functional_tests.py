from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_list_and_retrieve_it_later(self):
        # Edith has heard of a cool new todo app. She goes to check out its
        # homepage
        self.browser.get('http://localhost:8000')
        # She notices the page title mentions todo lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to insert an item right away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a todo item'
        )

        # She types 'buy peacock feathers' into the box
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates, and now the page lists
        # 1. Buy peacock feathers as an item in a todo list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            'New todo item did not appear in table'
        )

        # There is still a text box inviting her to add another item
        # She enters 'use peacock feathers to make a fly'
        self.fail('Finish the test!')

        # The page updates again, and now shows both items

        # The site has generated a unique url to remember her list, and there is
        # some text to indicate this

        # She visits the URL - her list is still there

        # Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main()
