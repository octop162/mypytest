import base

class Test_ScenarioB(base.ScenarioBase):
  def test(self):
    self.driver.get(self.fixture['url'])
    search = self.driver.find_element_by_id('search_form_input_homepage')
    search.send_keys(self.fixture["keyword"])
    button = self.driver.find_element_by_id('search_button_homepage')
    button.click()