from playwright.sync_api import expect, Page
import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_check = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_check).to_be_visible()
    expect(courses_check).to_have_text('Courses')

    icon_check = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(icon_check).to_be_visible()

    view_title_text_check = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(view_title_text_check).to_be_visible()
    expect(view_title_text_check).to_have_text('There is no results')

    view_description_text_check = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(view_description_text_check).to_be_visible()
    expect(view_description_text_check).to_have_text('Results from the load test pipeline will be displayed here')
