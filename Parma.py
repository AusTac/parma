from b3.parsers.battleye.protocol import BattleyeServer, CommandTimeoutError, NetworkError
import ParmaDB
import BEProcessing
import socket
import ConfigParser

if __name__ == '__main__':
    from threading import Thread, Event
    import time
    import b3.lib.sourcelib.SourceQuery as sq
    import ConfigParser
    import MySQLdb

    stop_all = Event()
    host = "austac.net.au"
    port = 2303
    pw = "hunter22"
    _command_queue = []
    admin_guids = []
    players = {}

    def battleyeEventListener(event):
        # temp functionality
        print event
        # Process any ingame commands and add to queue

        # Add chat to db

        # Check if it is a command

        # Check if the issuer is an admin

        # Add command to queue (to DB- we want all commands recorded)

    # Main daemon class
    class Daemon(Thread):

        def __init__(self, battleye_server, source_server, delay=5):
            Thread.__init__(self)
            self.battleye_server = battleye_server
            self.delay = delay
            self.source_server = source_server

        def update_scores(self):
            try:
                steam_players = self.source_server.player()
                # TODO: Handle case when steam!bercon
                # TODO: Handle above case for mistaken names
                for s in steam_players:
                    for guid, player in players.iteritems():
                        # Warning thrown:
                        # UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode -
                        # interpreting them as being unequal if s['name'] == player['name']:
                        if s['name'] == player['name']:
                            player['score'] = s['kills']
                            player['connecttime'] = s['time']
            except socket.timeout:
                pass

        def update_players(self, be_players):
            for playernum, player in be_players.iteritems():
                    # Index players by guid
                    if player['guid'] in players:
                        # GUID in players
                        # Update ping, playernum, ip
                        players[player['guid']]['ping'] = player['ping']
                        players[player['guid']]['playernum'] = player['cid']
                        players[player['guid']]['lobby'] = player['lobby']
                        players[player['guid']]['name'] = player['name']
                        players[player['guid']]['ip'] = player['ip']

                    else:
                        # GUID not in players, add new dict
                        newdict = {}
                        newdict['ping'] = player['ping']
                        newdict['playernum'] = player['cid']
                        newdict['score'] = 0
                        newdict['connecttime'] = 0
                        newdict['lobby'] = player['lobby']
                        newdict['name'] = player['name']
                        newdict['ip'] = player['ip']
                        players[player['guid']] = newdict

        def run(self):
            # Fetch authe'd GUIDs


            # Fetch ruleset


            while not stop_all.is_set():
                # Fetch players, update in-app player dict
                # Can throw commandTimeoutError
                try:
                    response = self.battleye_server.command('players')
                    self.update_players(BEProcessing.players_list(response))
                except CommandTimeoutError:
                    pass
                except NetworkError:
                    t_conn.stop()
                    stop_all.set()
                    # Connection failure?



                # Update scores
                self.update_scores()

                print players

                # Update player DB, and remove old players from dict

                # Check ruleset matches, add to command queue

                # Fetch DB command queue

                # Execute command queue



                time.sleep(self.delay)
                # D

    # connect to the BattlEye server
    t_conn = BattleyeServer(host, port, pw)
    print t_conn.is_alive
    try:
        # if connection did not fail
        if not t_conn.isStopped():
            t_conn.subscribe(battleyeEventListener)
            Daemon(t_conn, sq.SourceQuery(host="austac.net.au", port=2303)).start()
            while not stop_all.is_set():
                time.sleep(10)
    except KeyboardInterrupt:
        pass
    finally:
        # stop all threads
        t_conn.stop()
        stop_all.set()
