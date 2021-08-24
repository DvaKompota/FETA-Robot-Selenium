import pytest
from resources import pages


@pytest.mark.base_page
class TestBasePage:

    def test_page_inheritance(self):
        assert pages.BasePage().header
        assert pages.ElementsPage().header
        assert pages.ElementsPage().page_heading_text
