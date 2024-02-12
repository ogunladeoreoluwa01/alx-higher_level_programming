#!/usr/bin/python3
"""This module contains our base of operations. It contains a class
named Base. We will build classes representing shapes upon
this class, """
import json
import csv
import turtle
import random


class Base:
    """This class will be the base for all other class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """This initializes the attributes of the class"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """This method converts a list of dictionaries into a json string
        We will see the usefulness when we want to store the instances as
        an attribute: value pair

        Args:
            list_dictionaries (dict): A list of dictionaries

        Returns:
            str: a json encoded string
        """
        if not list_dictionaries or list_dictionaries == []:
            return json.dumps([])
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """This saves a list of objects to a json file as
        their attribute:value pair dictionary. It serializes a
        python object to json string

        Args:
            list_objs (list): the list of instances of the class
        """
        if not list_objs:
            the_list = []
        else:
            the_list = [mem.to_dictionary() for mem in list_objs]
        end = cls.to_json_string(the_list)
        name = f"{cls.__name__}.json"
        with open(name, 'w') as ft:
            ft.write(end)

    @staticmethod
    def from_json_string(json_string):
        """Converts/Deserializes a json string back to a
        python object

        Args:
            json_string (str): a serialized python object

        Returns:
            list: the converted object
        """
        if not json_string:
            return []
        result = json.loads(json_string)
        return result

    @classmethod
    def create(cls, **dictionary):
        """This creates an instance of a class

        Returns:
            class: The instance of that class
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """This loads data from a json file.
        This data is usually the instances of the class stored as an
        attribute:value pair in a list of dictionaries

        Returns:
            list: a list of instances of that class
        """
        result = ""
        name = f"{cls.__name__}.json"
        try:
            with open(name, 'r') as ft:
                result = ft.read()
        except IOError:
            pass
        temp = cls.from_json_string(result)
        instance_list = [cls.create(**mem) for mem in temp]
        return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """This saves information to a csv file
        This information is usually the instances of the class,
        its attributes and values. It serializes in csv

        Args:
            list_objs (list): a list of instances of the class
        """
        name = f"{cls.__name__}.csv"
        with open(name, 'w', newline='') as ft:
            if not list_objs or list_objs == []:
                ft.write('[]')
            if name == "Rectangle.csv":
                columns = ['id', 'width', 'height', 'x', 'y']
            else:
                columns = ['id', 'size', 'x', 'y']
            writer = csv.DictWriter(ft, fieldnames=columns)
            for item in list_objs:
                writer.writerow(item.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """This loads the data from a csv file
        This data is usually the instances of the class and their
        values stored in csv format ie it deserializes in csv

        Returns:
            list: a list of new class instances
        """
        name = f"{cls.__name__}.csv"
        instance_list = []
        with open(name, 'r', newline='') as csv_w:
            if name == "Rectangle.csv":
                columns = ['id', 'width', 'height', 'x', 'y']
            else:
                columns = ['id', 'size', 'x', 'y']
            ma = csv.DictReader(csv_w, fieldnames=columns)
            if not ma:
                return []
            for row in ma:
                for k, v in row.items():
                    row[k] = int(v)
                instance_list.append(cls.create(**row))
        return instance_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """This draws the shapes onto a tkinter window

        Args:
            list_rectangles (list): A list of Rectangle instances
            list_squares (list): A list of Square instances
        """
        colors = ["#cd131e", "gold", "yellow", "red",
                  "orange", "cyan", "purple", "violet"]
        base = turtle.Turtle()
        base.screen.bgcolor("white")
        base.shape("turtle")
        for rect in list_rectangles:
            base.setpos(rect.x, rect.y)
            base.pendown()
            base.showturtle()
            base.fillcolor(random.choice(colors))
            base.begin_fill()
            for i in range(2):
                base.forward(rect.width)
                base.rt(90)
                base.forward(rect.height)
                base.rt(90)
            base.end_fill()
            base.penup()
            base.hideturtle()
            base.home()
        for rect in list_squares:
            base.setpos(rect.x, rect.y)
            base.pendown()
            base.showturtle()
            base.fillcolor(random.choice(colors))
            base.begin_fill()
            for i in range(2):
                base.forward(rect.width)
                base.rt(90)
                base.forward(rect.height)
                base.rt(90)
            base.end_fill()
            base.penup()
            base.hideturtle()
            base.home()
        turtle.exitonclick()
