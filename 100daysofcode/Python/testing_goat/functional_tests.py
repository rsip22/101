"""
Functional tests for the to-do Django app

"""
import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    """
    Functional tests for a new visitor
    """

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        """Anna goes to the homepage of the to-do app"""
        self.browser.get('http://localhost:8000')

        # She sees the page title and header mention to-do lists
        self.assertIn('To-do', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away

        # She types "Buy peacock feathers" into a text box (Anna's hobby
        # is tying fly-fishing lures)

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Anna is very methodical)

        # The page updates again, and now shows both items on her list

        # Anna wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.

        # She visits that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep


if __name__ == '__main__':
    unittest.main(warnings='ignore')
