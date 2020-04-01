import pathlib
from selenium import webdriver
import yaml

class ScenarioBase:
  def setup_method(self):
    self.fixture = yaml.safe_load(
      open(
        './fixtures/case_{}.yaml'.format(self.__class__.__name__.split("_")[1]),
        encoding='utf-8'
      ).read()
    )
    self.settings = yaml.safe_load(
      open(
        './settings.yaml',
        encoding='utf-8'
      ).read()
    )
    self.driver = self.__get_driver()

  def teardown_method(self):
    self.driver.close()
    self.driver.quit()

  def __get_driver(self):
    browser_name = self.settings["browser"]
    fullpath = pathlib.Path(
      './drivers/{}/{}'.format(
        self.settings["os"],
        self.settings["driver_name"][browser_name]
      )
    ).resolve()
    driver = getattr(webdriver, self.settings["browser"])(executable_path=fullpath)
    return driver