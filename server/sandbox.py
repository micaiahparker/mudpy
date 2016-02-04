from server import mudpy_server


def test(port):
    server = mudpy_server.MudPyServer(port)
    server.start()
    server.stop()

if __name__ == "__main__":
    test(1234)
