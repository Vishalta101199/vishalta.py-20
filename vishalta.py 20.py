from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def imdb_search(name="", profession="", known_for_title="", filter_by="all"):
  """
  Searches for actors/actresses on IMDb with filters.

  Args:
      name (str, optional): Name of the actor/actress to search for. Defaults to "".
      profession (str, optional): Profession (actor/actress) to filter by. Defaults to "".
      known_for_title (str, optional): Title the person is known for. Defaults to "".
      filter_by (str, optional): Filter by "all", "males", or "females". Defaults to "all".
  """
  driver = webdriver.Chrome()
  driver.get("https://www.imdb.com/search/name/")

  # Fill name textbox
  if name:
    name_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "name"))
    )
    name_field.send_keys(name)

  # Select profession
  if profession:
    profession_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "primary-profession"))
    )
    profession_dropdown.select_by_value(profession)  # Use value for specific option

  # Fill known for title textbox
  if known_for_title:
    known_for_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "keyword"))
    )
    known_for_field.send_keys(known_for_title)

  # Select filter by option
  if filter_by != "all":
    filter_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "gender"))
    )
    filter_dropdown.select_by_value(filter_by)  # Use value for specific option

  # Submit search
  search_button = WebDriverWait(driver, 10).until(
      EC.element_to_be_clickable((By.ID, "find"))
  )
  search_button.click()

  # Do something with the search results (e.g., print titles)
  # ...

  driver.quit()

# Example usage
imdb_search(name="Tom Hanks", profession="actor")
imdb_search(known_for_title="Game of Thrones")
imdb_search(filter_by="females")
