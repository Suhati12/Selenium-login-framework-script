import pytest
from pages.table_page import TablePage

def test_language_filter_python(driver):
    table_page = TablePage(driver)
    table_page.open()
    
    # Filter by Python
    table_page.filter_by_python()
    
    # Verify all visible table rows match 'Python'
    languages = table_page.get_displayed_languages()
    assert len(languages) > 0, "No rows found after applying Python filter"
    assert all(lang == "Python" for lang in languages), f"Unexpected language found in filtered results: {languages}"