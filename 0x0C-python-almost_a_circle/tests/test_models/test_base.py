#!/usr/bin/bash
import unittest
from models.base import Base
from models.rectangle import Rectangle
import json
from models.square import Square
import os


class TestBaseClass(unittest.TestCase):
    def test_is_an_instance_of_base(self):
        test_n = Base()
        self.assertIsInstance(test_n, Base)

    def test_base_id(self):
        test_n = Base(2)
        self.assertEqual(test_n.id, 2)
        temp = Base()
        another = Base()
        self.assertEqual(another.id, 2)

    def test_wrong_id(self):
        test_n = Base("3")
        self.assertRaises(ValueError)

    def test_wrong_id_2(self):
        test_n = Base([3])
        self.assertRaises(ValueError)


class TestToJsonStringDict(unittest.TestCase):
    def test_to_json_string_valid_input(self):
        dic = [{1: 3, 2: 4}, {5: 6}]
        expected = '[{"1": 3, "2": 4}, {"5": 6}]'
        self.assertIsInstance(Base.to_json_string(dic), str)
        self.assertEqual(Base.to_json_string(dic), json.dumps(dic))
        self.assertEqual(Base.to_json_string(dic), expected)

    def test_to_json_string_invalid_input(self):
        dic_2 = None
        self.assertEqual(Base.to_json_string(dic_2), json.dumps([]))

    def test_to_json_string_empty_input(self):
        dic = []
        self.assertEqual(Base.to_json_string(dic), json.dumps([]))


class TestFromJsonString(unittest.TestCase):
    def test_valid_input(self):
        core = [{"am": 3}]
        test_subject = json.dumps(core)
        self.assertEqual(Base.from_json_string(test_subject),
                         [{'am': 3}])
        self.assertEqual(Base.from_json_string(test_subject),
                         json.loads(test_subject))

    def test_empty_list(self):
        test_subject = json.dumps([])
        self.assertEqual(Base.from_json_string(test_subject), [])
        self.assertEqual(Base.from_json_string(test_subject),
                         json.loads(test_subject))
        self.assertEqual(Base.from_json_string('[]'), [])

    def test_none_as_value(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_large_list(self):
        core = json.dumps([{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8},
                          {"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}])
        expected_output = [{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8},
                           {"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}]
        self.assertEqual(Base.from_json_string(core), expected_output)


class TestLoadFromFile(unittest.TestCase):
    @staticmethod
    def check(filename):
        try:
            a = ""
            with open(filename, 'r') as ft:
                a = ft.read()
            return a
        except IOError:
            return None

    @staticmethod
    def teardown(flag, filename):
        if flag is None:
            try:
                os.remove(filename)
            except IOError:
                pass
        else:
            with open(filename, 'w') as ft:
                ft.write(flag)

    def prep_rectangle(self, filename, value=None):
        return_v = self.check(filename)
        if value is None:
            try:
                os.remove(filename)
            except IOError:
                pass
        if value is not None:
            with open(filename, 'w') as f:
                f.write(value)
        return return_v

    def test_no_file(self):
        filename = "Rectangle.json"
        a = self.prep_rectangle(filename)
        res = []
        self.assertEqual(res, Rectangle.load_from_file())
        self.teardown(a, filename)

    def test_empty_file(self):
        filename = "Rectangle.json"
        a = self.prep_rectangle("Rectangle.json", "")
        res = []
        self.assertEqual([], Rectangle.load_from_file())
        self.teardown(a, filename)

    def test_valid_input(self):
        filename = "Rectangle.json"
        dict_1 = {"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}
        dict_2 = {"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}
        value = json.dumps([dict_1, dict_2])
        a = self.prep_rectangle(filename, value)
        expected_output = [Rectangle(10, 7, 2, 8, 1), Rectangle(1, 2, 3, 4, 5)]
        self.assertIsInstance(expected_output[0], Rectangle)
        outcome = Rectangle.load_from_file()
        self.assertEqual(expected_output[0].to_dictionary(),
                         outcome[0].to_dictionary())
        self.assertEqual(expected_output[1].to_dictionary(),
                         outcome[1].to_dictionary())
        self.teardown(a, filename)

    def test_square(self):
        filename = "Square.json"
        value = json.dumps([{"id": 1, "size": 7,
                             "x": 2, "y": 8},
                            {"id": 5, "size": 2, "x": 3, "y": 4}])
        a = self.prep_rectangle(filename, value)
        expected_output = [Square(7, 2, 8, 1), Square(2, 3, 4, 5)]
        outcome = Square.load_from_file()
        self.assertIsInstance(outcome[0], Square)
        self.assertEqual(expected_output[0].to_dictionary(),
                         outcome[0].to_dictionary())
        self.assertEqual(expected_output[1].to_dictionary(),
                         outcome[1].to_dictionary())
        self.teardown(a, filename)


class TestCreate(unittest.TestCase):
    def test_create_with_rectangle(self):
        a = Rectangle.create(id=0, width=3)
        self.assertIsInstance(a, Rectangle)
        self.assertEqual(a.id, 0)

    def test_create_with_square(self):
        test_value = Square(1, 2, 3, 4)
        dict_test = test_value.to_dictionary()
        new_value = Square.create(**dict_test)
        self.assertIsInstance(new_value, Square)
        self.assertEqual(new_value.to_dictionary(), test_value.to_dictionary())


class TestSaveToJson(unittest.TestCase):

    @staticmethod
    def check(filename):
        try:
            a = ""
            with open(filename, 'r') as ft:
                a = ft.read()
            return a
        except IOError:
            return None

    @staticmethod
    def teardown(flag, filename):
        if flag is None:
            try:
                os.remove(filename)
            except IOError:
                pass
        else:
            with open(filename, 'w') as ft:
                ft.write(flag)

    def test_valid_input(self):
        flag = self.check("Square.json")
        test_list = [Square(7, 2, 8, 1), Square(2, 3, 4, 5)]
        Square.save_to_file(test_list)
        with open("Square.json", 'r') as ft:
            self.assertEqual(ft.read(),
                             '[{"id": 1, "size": 7, "x": 2, "y": 8}, '
                             '{"id": 5, "size": 2, "x": 3, "y": 4}]'
                             )
        self.teardown(flag, "Square.json")

    def test_the_dict_result(self):
        flag = self.check("Square.json")
        test_list = [Square(7, 2, 8, 1), Square(2, 3, 4, 5)]
        Square.save_to_file(test_list)
        outcome = []
        with open("Square.json", 'r') as ft:
            outcome = json.load(ft)
        self.assertEqual(test_list[0].to_dictionary(), outcome[0])
        self.teardown(flag, "Square.json")

    def test_empty_list(self):
        flag = self.check("Square.json")
        test_list = []
        Square.save_to_file(test_list)
        with open("Square.json", 'r') as ft:
            self.assertEqual(ft.read(), '[]')
        self.teardown(flag, "Square.json")

    def test_empty_list_as_object(self):
        flag = self.check("Square.json")
        test_list = []
        outcome = []
        Square.save_to_file(test_list)
        with open("Square.json", 'r') as ft:
            self.assertEqual(ft.read(), '[]')
        self.teardown(flag, "Square.json")

    def test_none_as_value(self):
        flag = self.check("Square.json")
        test_list = None
        Square.save_to_file(test_list)
        with open("Square.json", 'r') as ft:
            self.assertEqual(ft.read(), '[]')
        self.teardown(flag, "Square.json")

    def test_none_list_result__empty_list__(self):
        flag = self.check("Square.json")
        test_list = None
        outcome = []
        Square.save_to_file(test_list)
        with open("Square.json", 'r') as ft:
            self.assertEqual(ft.read(), '[]')
        self.teardown(flag, 'Square.json')


class TestSaveToJsonRect(unittest.TestCase):
    @staticmethod
    def check(filename):
        try:
            a = ""
            with open(filename, 'r') as ft:
                a = ft.read()
            return a
        except IOError:
            return None

    @staticmethod
    def teardown(flag, filename):
        if flag is None:
            try:
                os.remove(filename)
            except IOError:
                pass
        else:
            with open(filename, 'w') as ft:
                ft.write(flag)

    def test_valid_input(self):
        flag = self.check("Rectangle.json")
        e_1 = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, '
        e_2 = '{"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}]'
        expected = e_1 + e_2
        test_list = [Rectangle(10, 7, 2, 8, 1), Rectangle(1, 2, 3, 4, 5)]
        end = ""
        Rectangle.save_to_file(test_list)
        with open("Rectangle.json", 'r') as ft:
            end = ft.read()
        self.assertEqual(end, expected)
        self.teardown(flag, "Rectangle.json")

    def test_the_dict_result(self):
        flag = self.check("Rectangle.json")
        test_list = [Rectangle(10, 7, 2, 8, 1), Rectangle(1, 2, 3, 4, 5)]
        Rectangle.save_to_file(test_list)
        outcome = []
        with open("Rectangle.json", 'r') as ft:
            outcome = json.load(ft)
        self.assertEqual(test_list[0].to_dictionary(), outcome[0])
        self.teardown(flag, "Rectangle.json")

    def test_empty_list(self):
        flag = self.check("Rectangle.json")
        test_list = []
        Rectangle.save_to_file(test_list)
        with open("Rectangle.json", 'r') as ft:
            self.assertEqual(ft.read(), '[]')
        self.teardown(flag, "Rectangle.json")

    def test_empty_list_as_object(self):
        flag = self.check("Rectangle.json")
        test_list = []
        Rectangle.save_to_file(test_list)
        with open("Rectangle.json", 'r') as ft:
            self.assertEqual(ft.read(), '[]')
        self.teardown(flag, "Rectangle.json")

    def test_none_as_value(self):
        flag = self.check("Rectangle.json")
        test_list = None
        Rectangle.save_to_file(test_list)
        with open("Rectangle.json", 'r') as ft:
            self.assertEqual(ft.read(), '[]')
        self.teardown(flag, "Rectangle.json")

    def test_none_list_result__empty_list__(self):
        flag = self.check("Rectangle.json")
        test_list = None
        outcome = []
        Rectangle.save_to_file(test_list)
        with open("Rectangle.json", 'r') as ft:
            self.assertEqual(ft.read(), '[]')
        self.teardown(flag, "Rectangle.json")


class TestSaveToFileCsv(unittest.TestCase):
    @staticmethod
    def check(filename):
        try:
            a = ""
            with open(filename, 'r') as ft:
                a = ft.read()
            return a
        except IOError:
            return None

    @staticmethod
    def teardown(flag, filename):
        if flag is None:
            try:
                os.remove(filename)
            except IOError:
                pass
        else:
            with open(filename, 'w') as ft:
                ft.write(flag)

    def test_save_to_csv_rect(self):
        filename = "Rectangle.csv"
        flag = self.check(filename)
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        list_r = [r1, r2]
        expected = "1,10,7,2,8\n2,2,4,0,0\n"
        Rectangle.save_to_file_csv(list_r)
        with open(filename, 'r') as csv_c:
            self.assertEqual(csv_c.read(), expected)
        self.teardown(flag, filename)

    def test_save_to_csv_square(self):
        filename = "Square.csv"
        flag = self.check(filename)
        s1 = Square(5, 0, 0, 1)
        s2 = Square(7, 9, 1, 2)
        expected = "1,5,0,0\n2,7,9,1\n"
        list_s = [s1, s2]
        Square.save_to_file_csv(list_s)
        with open(filename, 'r') as csv_c:
            self.assertEqual(csv_c.read(), expected)
        self.teardown(flag, filename)


class TestLoadFromCsv(unittest.TestCase):
    @staticmethod
    def check(filename):
        try:
            a = ""
            with open(filename, 'r') as ft:
                a = ft.read()
            return a
        except IOError:
            return None

    @staticmethod
    def teardown(flag, filename):
        if flag is None:
            try:
                os.remove(filename)
            except IOError:
                pass
        else:
            with open(filename, 'w') as ft:
                ft.write(flag)

    def prep_rectangle(self, filename, value=None):
        return_v = self.check(filename)
        if value is None:
            try:
                os.remove(filename)
            except IOError:
                pass
        if value is not None:
            with open(filename, 'w') as f:
                f.write(value)
        return return_v

    def test_load_from_csv_rect(self):
        filename = "Rectangle.csv"
        value = '1,10,7,2,8\n2,2,4,0,0\n'
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        flag = self.prep_rectangle(filename, value)
        result = Rectangle.load_from_file_csv()
        self.assertEqual(
            r1.to_dictionary(), result[0].to_dictionary()
        )
        self.assertEqual(
            r2.to_dictionary(), result[1].to_dictionary()
        )
        self.teardown(flag, filename)

    def test_load_from_csv_square(self):
        filename = "Square.csv"
        value = '5,5,0,0\n6,7,9,1\n'

        s1 = Square(5, 0, 0, 5)
        s2 = Square(7, 9, 1, 6)
        flag = self.prep_rectangle(filename, value)
        result = Square.load_from_file_csv()
        self.assertEqual(
            s1.to_dictionary(), result[0].to_dictionary()
        )
        self.assertEqual(
            s2.to_dictionary(), result[1].to_dictionary()
        )
        self.teardown(flag, filename)


if __name__ == '__main__':
    unittest.main()
