__author__ = 'bradon'
import re


def players_list(players_output):
    """
    Take output from rcon (unprocessed) and turn it into a dictionary of dictionaries of player info
    :param players_output:
    :return: Dictionary of Dictionaries of player info
    """
    player_list = players_output.splitlines()
    be_players = {}
    for i in range(3, len(player_list)-1):
        _regPlayer_lobby = re.compile(r'^(?P<cid>[0-9]+)\s+(?P<ip>[0-9.]+):(?P<port>[0-9]+)\s+(?P<ping>[0-9-]+)\s+'
                                      r'(?P<guid>[0-9a-f]+)\((?P<verified>[A-Z\?]+)\)\s+(?P<name>.*?)\s+'
                                      r'(?P<lobby>\(Lobby\))$', re.I)
        _regPlayer = re.compile(r'^(?P<cid>[0-9]+)\s+(?P<ip>[0-9.]+):(?P<port>[0-9]+)\s+'
                                r'(?P<ping>[0-9-]+)\s+(?P<guid>[0-9a-f]+)\((?P<verified>[A-Z\?]+)\)\s+(?P<name>.*?)$',
                                re.I)
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