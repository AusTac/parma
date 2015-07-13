"""
Database communication for parma
"""


__author__ = 'Bradon Hall, Booties'

# Licensed under the GPL v2

# This program is largely developed from:
# BigBrotherBot(B3) (www.bigbrotherbot.net)
# Copyright (C) 2011 Thomas LEVEIL


# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

import MySQLdb


class ParmaDB:
    """
    Database communication for Parma
    """

    def __init__(self, mysql_user, mysql_password, mysql_port, mysql_host, mysql_db):
        self.mysql_user = mysql_user
        self.mysql_password = mysql_password
        self.mysql_port = mysql_port
        self.mysql_host = mysql_host
        self.mysql_db = mysql_db

    def get_connection(self):
        """
        Connect to MYSQL DB
        :return: Connection
        """
        pass

    def set_players_offline(self):
        """
        Set is_online to false for entire players table
        :return: None
        """
        pass

    def players_dictionary_example(self):
        """
        Example players dictionary to help with  designing update players table
        :return: Dictionary of Dictionaries of player info
        """
        result = {}
        example_one = {}
        example_one['ping'] = 44
        example_one['playernum'] = 1
        example_one['score'] = -50
        example_one['lobby'] = False
        example_one['connecttime'] = 1234
        example_one['name'] = "John Doe"
        example_one['ip'] = "127.0.0.1"
        guid_one = "12345678123456781234567812345678"
        result[guid_one] = example_one

        example_two = {}
        example_two['ping'] = 46
        example_two['playernum'] = 3
        example_two['score'] = -40
        example_two['lobby'] = False
        example_two['connecttime'] = 4321
        example_two['name'] = "Jane Doe"
        example_two['ip'] = "8.8.8.8"
        guid_two = "22345678123456781234567812345672"
        result[guid_two] = example_two
        return result

    def update_players_table(self, players):
        """
        Update players database, inserting new players and updating existing

        :param players: Dictionary of Dictionaries of player info
        :return: None
        """

    def get_admins(self):
        """
        Retrieve guids of all admins as a list
        :return: List of strings
        """
        pass

    def get_action(self):
        """
        Get a single pending action from the DB and mark it as in progress.
        We will want an action at a time since we will hand off to the main process and get a result
        (fail, succeed etc)
        :return: Command
        """
        pass

    def add_action(self, player_guid, automatic, action, action_value,action_status, timestamp, admin_guid, rule_id,
                   player_name):
        """
        Add a pending action to the database
        :param player_guid: String guid
        :param automatic: boolean is action automatic
        :param action:
        :param action_value:
        :param action_status:
        :param timestamp:
        :param admin_guid:
        :param rule_id:
        :param player_name:
        :return:
        """
        pass

    # Proper code above

    # Draft code below, delete as you replace functionality or names conflict

    def draft_get_connection(self):
        return MySQLdb.connect(user=self.mysql_user, passwd=self.mysql_password, host=self.mysql_host,
                               port=self.mysql_port, db=self.mysql_db)


    def get_full_table(self, table_name="server_rule"):
        m_conn = self.draft_get_connection()
        query = "SELECT * FROM " + table_name
        cursor = m_conn.cursor()
        cursor.execute(query)
        m_conn.commit()
        result = cursor.fetchall()
        cursor.close()
        m_conn.close()
        return result


    def get_single_column(self, table_name="admins", column="guid"):
        m_conn = self.draft_get_connection()
        query = "SELECT " + column + " FROM " + table_name
        cursor = m_conn.cursor()
        cursor.execute(query)
        m_conn.commit()
        result = cursor.fetchall()
        cursor.close()
        m_conn.close()
        return result


    def draft_get_admins(self):
        admins = self.get_single_column("admins", "guid")
        guids = []
        for guid in admins:
            guids.append(guid[0])
        return guids


    def get_player(self, guid):
        m_conn = self.draft_get_connection()
        query = "SELECT name FROM players WHERE guid=%s"
        cursor = m_conn.cursor()
        cursor.execute(query, (guid,))
        m_conn.commit()
        result = cursor.fetchall()
        cursor.close()
        m_conn.close()
        return result


    def update_player(self, guid="", name="", ip="", online=True, lobby_idle=False, connection_time = 0, score=0, ping=0, timestamp=""):
        pass


    def insert_player(self, guid="", name="", ip="", online=True, lobby_idle=False, connection_time = 0, score=0, ping=0, timestamp=""):
        pass


    def update_players(self, players={}):
        # For each player
        for guid, player in players.iteritems():
            pass
            # Check if guid in db
            if (len(self.get_player(guid))>0):
                pass
            else:
                pass


if __name__ == '__main__':
    # Perhaps create database if it does not exist
    pass