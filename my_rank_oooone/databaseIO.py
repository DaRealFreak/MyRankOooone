#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sqlite3


class DatabaseIO(object):
    DATABASE_PATH = os.path.join(os.path.dirname(__file__), os.path.pardir, 'my_rank_oooone.db')

    def __init__(self) -> None:
        """Initializing function"""
        self.conn = sqlite3.connect(self.DATABASE_PATH)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    @staticmethod
    def dict_from_row(row: sqlite3.Row) -> dict:
        """Convert the sqlite.Row result to a dictionary

        :param row:
        :return:
        """
        if not row:
            return {}
        return dict(zip(row.keys(), row))
