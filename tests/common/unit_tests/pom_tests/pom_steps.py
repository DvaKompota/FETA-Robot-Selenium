from tests.common.unit_tests import pom_tests
from robot.libraries.BuiltIn import BuiltIn


def robot_log(message):
    BuiltIn().log(message)


def validate_page_objects_inheritance():
    parent_page_parent_method_output = pom_tests.ParentPage().parent_method()
    robot_log(parent_page_parent_method_output)
    assert parent_page_parent_method_output == "Parent method: url=//parent, element=Parent element"

    child_page_parent_method_output = pom_tests.ChildPage().parent_method()
    robot_log(child_page_parent_method_output)
    assert child_page_parent_method_output == "Parent method: url=//parent/child, element=Child element"

    child_page_child_method_output = pom_tests.ChildPage().child_method()
    robot_log(child_page_child_method_output)
    assert child_page_child_method_output == "Child method: url=//parent/child, element=Child element"
