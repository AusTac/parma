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

import Pwd
import MySQLdb


def get_connection():
    return MySQLdb.connect(user=Pwd.mysql_user(), passwd=Pwd.mysql_password(), host='localhost', port=1234,
                           db=Pwd.mysql_db())


def get_full_table(table_name="server_rule"):
    m_conn = get_connection()
    query = "SELECT * FROM " + table_name
    cursor = m_conn.cursor()
    cursor.execute(query)
    m_conn.commit()
    result = cursor.fetchall()
    cursor.close()
    m_conn.close()
    return result


def get_single_column(table_name="admins", column="guid"):
    m_conn = get_connection()
    query = "SELECT " + column + " FROM " + table_name
    cursor = m_conn.cursor()
    cursor.execute(query)
    m_conn.commit()
    result = cursor.fetchall()
    cursor.close()
    m_conn.close()
    return result


def get_admins():
    admins = get_single_column("admins", "guid")
    guids = []
    for guid in admins:
        guids.append(guid[0])
    return guids


def get_player(guid):
    m_conn = get_connection()
    query = "SELECT name FROM players WHERE guid=%s"
    cursor = m_conn.cursor()
    cursor.execute(query, (guid,))
    m_conn.commit()
    result = cursor.fetchall()
    cursor.close()
    m_conn.close()
    return result


def set_players_offline():
    m_conn = get_connection()
    query = "UPDATE players SET is_online=False"
    cursor = m_conn.cursor()
    cursor.execute(query)
    m_conn.commit()
    cursor.close()
    m_conn.close()


def update_player(guid="", name="", ip="", online=True, lobby_idle=False, score=0, ping=0, timestamp=""):
    pass


def insert_player(guid="", name="", ip="", online=True, lobby_idle=False, score=0, ping=0, timestamp=""):
    pass


def update_players(players={}):
    # For each player
    for guid, player in players.iteritems():
        pass
        # Check if guid in db
        if (len(get_player(guid))>0):
            pass
        else:
            pass

print len(get_player("test"))