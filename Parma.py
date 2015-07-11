from b3.parsers.battleye.protocol import BattleyeServer

if __name__ == '__main__':
    import Pwd
    from threading import Thread, Event
    import time
    import MySQLdb
    host = "austac.net.au"
    port = 2303
    pw = Pwd.password()
    _command_queue = []

    def battleyeEventListener(event):
        # temp functionality
        print event
        # Process any ingame commands and add to queue

        # Check if it is a command

        # Check if the issuer is an admin

        # Add command to queue (to DB- we want all commands recorded)

    # Main daemon class
    class Daemon(Thread):
        #
        _stop = Event()
        nb_instances = 0

        def __init__(self, battleye_server, delay=5):
            Thread.__init__(self)
            self.battleye_server = battleye_server
            self.delay = delay



        def run(self):
            # Fetch authe'd GUIDs

            # Fetch ruleset

            while not self.__class__._stop.is_set():
                # Fetch players, update in-app player dict

                # Update player DB

                # Check ruleset matches, add to command queue

                # Fetch DB command queue

                # Execute command queue

                response = self.battleye_server.command('players')
                time.sleep(self.delay)
                # D

        @classmethod
        def stopAll(cls):
            cls._stop.set()

    # connect to the BattlEye server
    t_conn = BattleyeServer(host, port, pw)
    try:
        t_conn.subscribe(battleyeEventListener)
        Daemon(t_conn).start()
        while True:
            pass
    except KeyboardInterrupt:
        pass

    finally:
        # stop all threads
        t_conn.stop()
        Daemon.stopAll()