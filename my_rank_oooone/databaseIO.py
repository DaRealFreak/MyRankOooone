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

        :type row: sqlite3.Row
        :return:
        """
        if not row:
            return {}
        return dict(zip(row.keys(), row))

    def get_player(self, player_name: str) -> dict:
        """Returns the first player

        :type player_name: str
        :return:
        """
        item = self.cursor.execute('SELECT * FROM players WHERE player = ?', [player_name]).fetchone()
        return self.dict_from_row(item)

    def get_first_or_create_player(self, player_name: str) -> dict:
        """Either get the first player or create a new player and return it

        :type player_name: str
        :return:
        """
        player = self.cursor.execute('SELECT * FROM players WHERE player = ?', [player_name]).fetchone()
        if not player:
            # create the player and retrieve it again
            self.add_player(player_name)
            return self.get_first_or_create_player(player_name)
        return self.dict_from_row(player)

    def add_player(self, player_name: str) -> None:
        """Insert a player into the database

        :type player_name: str
        :return:
        """
        self.cursor.execute('INSERT INTO players (player) VALUES (?)', [player_name])
        self.conn.commit()
        return self.cursor.lastrowid
