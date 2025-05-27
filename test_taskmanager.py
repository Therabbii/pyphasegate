import task_manager

from unittest import TestCase

class TestTaskManager(TestCase):
	def test_that_task_manager_function_exists(self):
		task_manager.get_menu_list()
	
	def test_that_get_menu_list_works(self):
		task_manager.get_menu_list()

	def test_that_add_task_exists(self):
		task_manager.add_task()