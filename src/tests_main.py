import unittest
from main import first_part,second_part
from settings import input_song, input_artist
import pandas as pd
import requests
from bs4 import BeautifulSoup as BS


class Testmain(unittest.TestCase):
    def test_input_part_one(self):
        self.assertIsNone(first_part('!@##$%^&','*()_+~'))
        self.assertRaises(ValueError,first_part,input_artist, '')
        self.assertRaises(ValueError,first_part,'', input_song)
        self.assertRaises(TypeError,first_part,123,('',2))

