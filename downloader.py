from pol import Server


port = sys.argv[1] if len(sys.argv) >= 2 else 1234

Server(port, DATABASES['default'], SNAPSHOT_DIR, DOWNLOADER_USER_AGENT, DEBUG).run()
