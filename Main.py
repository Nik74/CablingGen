# This program is designed for creating spl files.
# This is an example of the main program and does not include all its functions


from CablingGen import AppWindow, Logs, SQLite

Logs.logger.debug("Program is started")

AppWindow.AppWindow()

SQLite.conn.close()
