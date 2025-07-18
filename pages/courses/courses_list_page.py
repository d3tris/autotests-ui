from components.courses.course_view_component import CourseViewComponent
from components.courses.course_view_menu_component import CourseViewMenuComponent
from components.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent
from components.navigation.sidebar_component import SidebarComponent
from components.navigation.navbar_component import NavbarComponent
from components.views.empty_view_component import EmptyViewComponent
from pages.base_page import BasePage
import allure


class CoursesListPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.empty_view = EmptyViewComponent(page, 'courses-list')
        self.course_view = CourseViewComponent(page)
        self.course_view_menu = CourseViewMenuComponent(page)
        self.toolbar_view = CoursesListToolbarViewComponent(page)

    def check_visible_empty_view(self):
        self.empty_view.check_visible(
            title='There is no results',
            description='Results from the load test pipeline will be displayed here'
        )
