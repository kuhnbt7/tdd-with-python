from selenium import webdriver
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
        self.fail('Finish the test!')

        # She is invited to insert an item right away

        # She types 'buy peacock feathers' into the box

        # When she hits enter, the page updates, and now the page lists
        # 1. Buy peacock feathers as an item in a todo list

        # There is still a text box inviting her to add another item
        # She enters 'use peacock feathers to make a fly'

        # The page updates again, and now shows both items

        # The site has generated a unique url to remember her list, and there is
        # some text to indicate this

        # She visits the URL - her list is still there

        # Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main()
