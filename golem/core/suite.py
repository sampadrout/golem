import importlib
import os
import types
import inspect

from golem.core import utils


def _format_list_items(list_items):
    list_string = ''
    if list_items:
        for item in list_items:
            list_string = list_string + "    '" + item + "',\n"
        list_string = "[\n    {}\n]".format(list_string.strip()[:-1])
    else:
        list_string = '[]'
    return list_string


def save_suite(root_path, project, suite, test_cases, workers, browsers):
    suite_path = os.path.join(root_path, 'projects', project, 'suites',
                                    '{}.py'.format(suite))
    with open(suite_path, 'w', encoding='utf-8') as f:
        f.write('\n\n')
        f.write('browsers = {}\n'.format(_format_list_items(browsers)))
        f.write('\n')
        f.write('workers = {}'.format(workers))
        f.write('\n\n')
        f.write('test_case_list = {}\n'.format(_format_list_items(test_cases)))


def new_suite(root_path, project, suite_name):
    errors = []
    if utils.file_exists(root_path, project, 'suites', suite_name):
        errors.append('A file with that name already exists')

    if not errors:
        suite_path = os.path.join(root_path, 'projects', project, 'suites')
        suite_full_path = os.path.join(suite_path, suite_name + '.py')
        test_case_content = ('\n'
                             'browsers = []\n\n'
                             'workers = 1\n\n'
                             'test_case_list = []\n')
        with open(suite_full_path, 'w') as f:
            f.write(test_case_content)
    return errors

