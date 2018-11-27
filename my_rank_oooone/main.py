#!/usr/local/bin/python
# coding: utf-8
import logging

from pydispatch import Dispatcher

from my_rank_oooone import DatabaseIO


class MyRankOooone(Dispatcher):
    _events_ = ['log', 'update', 'remove']

    def __init__(self, directory: str = '', log_level: int = logging.INFO, *args, **kwargs) -> None:
        """Initializing function

        :type directory: str
        :type log_level: int
        """
        super().__init__(*args, **kwargs)
        logging.basicConfig(level=log_level)
        self.logger = logging.getLogger("rank_logger")
        self.directory = directory

        self._dbIO = DatabaseIO()
        self.bind_events()

    def bind_events(self) -> None:
        """Bind all required events

        :return:
        """
        self.bind(log=self.on_log)

        self.bind(update=self.on_update)
        self.bind(remove=self.on_remove)

    def on_log(self, level: int, message: str) -> None:
        """Centralized logging function to apply settings of the application

        :type level: int
        :type message: str
        :return:
        """
        self.logger.log(level, message)

    def on_update(self, player_name: str, map_name: str) -> None:
        """Listener function, gets called if ranks are getting updated

        :type player_name: str
        :type map_name: str
        :return:
        """
        pass

    def on_remove(self, player_name: str) -> None:
        """Listener function, gets called if a player gets removed from being tracked

        :type player_name: str
        :return:
        """
        pass

    def add_player(self, player_name: str) -> None:
        """Adds a player

        :type player_name: str
        :return:
        """
        self._dbIO.get_first_or_create_player(player_name)
