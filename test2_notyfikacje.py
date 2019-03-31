import os
import unittest
from appium import webdriver
from time import sleep

PATH = lambda p: os.path.abspath(
     os.path.join(os.path.dirname(__file__),p)
 )

# PATH = lambda p: os.path.abspath(
#     os.path.join(os.path.dirname('C:\AndroidTesty\ApiDemos-debug.apk',p)
# )

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
        desired_caps['app'] = PATH('C:\AndroidTesty\ApiDemos-debug.apk')
        desired_caps['appPackage'] = 'io.appium.android.apis'
        desired_caps['appActivity'] = 'io.appium.android.apis.ApiDemos'

        # connect to appium server
        self.driver = \
            webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
            #webdriver.Remote("http://localhost/wd/hub", desired_caps)

    def tearDown(self):
        self.driver.quit()


    def test_open_notifications(self):
        self.driver.open_notifications()
        sleep(5)
        elements = self.driver.find_elements_by_class_name('android.widget.TextView')

        title = False
        body = False

        for el in elements:
            text = el.text

            if text == "USB debugging connected":
                title = True
            elif text == "Touch to disable USB debugging.":
                body = True

        self.assertTrue(title)
        self.assertTrue(body)

        self.driver.keyevent(4)



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieApp)
    unittest.TextTestRunner(verbosity=2).run(suite)
