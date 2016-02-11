from channels import channel


def test_channel_init():
    c = channel.Channel("Test")


def test_update_channel():
    c = channel.Channel("Test")
    c.update("Hello")


