from components.base_component import BaseComponent
from playwright.sync_api import Page
from elements.text import Text
from elements.button import Button
import allure

class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.exercises_title = Text(page, 'create-course-exercises-box-toolbar-title-text', 'Exercises title')
        self.create_exercise_button = Button(page, 'create-course-exercises-box-toolbar-create-exercise-button',
                                             'Exercises button')

    @allure.step('Check visible create course exercises toolbar view')
    def check_visible(self):
        self.exercises_title.check_visible()
        self.exercises_title.check_have_text('Exercises')

        self.create_exercise_button.check_visible()

    def click_create_exercise_button(self):
        self.create_exercise_button.click()
