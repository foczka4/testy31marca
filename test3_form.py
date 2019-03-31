import os
import unittest
from appium import webdriver
from time import sleep

PATH = lambda p: os.path.abspath(
     os.path.join(os.path.dirname(__file__),p)
 )


class TestowanieApp(unittest.TestCase):
    def setUp(self):
        desired_caps = {}

        desired_caps['platformName'] = 'Android'

        # 1 fizyczny smartfon
        #desired_caps['platformVersion'] = '7.0'
        #desired_caps['deviceName'] = 'Gigaset GS170'
        # 2 emulator androida
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['app'] = PATH('C:\AndroidTesty\ContactManager.apk')
        desired_caps['appPackage'] = 'com.example.android.contactmanager'
        desired_caps['appActivity'] = 'com.example.android.contactmanager.ContactManager'
        desired_caps['resetKeyboard'] = 'True'
        desired_caps['unicodeKeyboard'] = 'True'

        # connect to appium server
        self.driver = \
            webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
            #webdriver.Remote("http://localhost/wd/hub", desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_form(self):
        el = self.driver.find_element_by_accessibility_id('Add Contact')
        el.click()

        textFields = self.driver.find_elements_by_class_name("android.widget.EditText")
        textFields[0].send_keys('Jan Kowalski')
        textFields[1].send_keys('666777888')
        textFields[2].send_keys('janek@wsb.pl')

        sleep(3)

        el1 = self.assertEqual('Jan Kowalski', textFields[0].text)
        el2 = self.assertEqual('666777888', textFields[1].text)
        el3 = self.assertEqual('janek@wsb.pl', textFields[2].text)

        button = self.driver.find_elements_by_class_name("android.widget.Button")
        button.click()







if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieApp)
    unittest.TextTestRunner(verbosity=2).run(suite)
