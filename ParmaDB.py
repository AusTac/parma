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


def get_rules():
    m_conn = MySQLdb.connect(user=Pwd.mysql_user(), passwd=Pwd.mysql_password(), host='localhost', port=1234,
                             db=Pwd.mysql_db())
    query = "SELECT * FROM server_rule"
    cursor = m_conn.cursor()
    cursor.execute(query)
    m_conn.commit()
    result = cursor.fetchall()
    cursor.close()
    m_conn.close()
    return result


