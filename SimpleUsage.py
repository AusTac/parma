__author__ = 'Bradon Hall'

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

import b3.parsers.battleye.protocol as be
import b3.lib.sourcelib.SourceQuery as sq
import re
import Pwd
import logging


def get_players(be_connection):
    player_list = be_connection.command('players').splitlines()
    be_players = {}
    for i in range(3, len(player_list)-1):
        _regPlayer_lobby = re.compile(r'^(?P<cid>[0-9]+)\s+(?P<ip>[0-9.]+):(?P<port>[0-9]+)\s+(?P<ping>[0-9-]+)\s+(?P<guid>[0-9a-f]+)\((?P<verified>[A-Z\?]+)\)\s+(?P<name>.*?)\s+(?P<lobby>\(Lobby\))$', re.I)
        _regPlayer = re.compile(r'^(?P<cid>[0-9]+)\s+(?P<ip>[0-9.]+):(?P<port>[0-9]+)\s+(?P<ping>[0-9-]+)\s+(?P<guid>[0-9a-f]+)\((?P<verified>[A-Z\?]+)\)\s+(?P<name>.*?)$', re.I)
        p = re.match(_regPlayer_lobby, player_list[i])
        if p:
            pl = p.groupdict()
            if pl['verified'] =='OK':
                pl['lobby'] = True
                be_players[pl['cid']] = pl
            elif pl['verified'] =='?':
                pl['lobby'] = True
                be_players[pl['cid']] = pl
            else:
                pass
        else:
            p = re.match(_regPlayer, player_list[i])
            if p:
                pl = p.groupdict()
                if pl['verified'] == 'OK':
                    pl['lobby'] = False
                    be_players[pl['cid']] = pl
                elif pl['verified'] == '?':
                    pl['lobby'] = False
                    be_players[pl['cid']] = pl
    return be_players

if __name__ == '__main__':
    logging.basicConfig()
    conn = be.BattleyeServer("austac.net.au", 2302, Pwd.password())
    players = get_players(conn)
    conn.stop()
    for playerNum, b in players.iteritems():
        print b['name'] + "\t" + b['guid']

    server = sq.SourceQuery(host="austac.net.au", port=2303)

    steam_players = server.player()
    server.disconnect()
    for s in steam_players:
        print s['name'] + "\t" + str(s['kills'])
