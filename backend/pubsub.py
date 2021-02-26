import time

from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

pnconfig = PNConfiguration()

pnconfig.subscribe_key = "sub-c-b15fe5f6-774e-11eb-8e97-5aaf7c820018"
pnconfig.publish_key = "pub-c-346c2dc6-42ea-45f8-b4e9-48c2cf5a7c2e"

pubnub = PubNub(pnconfig)

TEST_CHANNEL = 'TEST_CHANNEL'


class Listener(SubscribeCallback):
    def message(self, pubnub, message_object):
        print(
            f'\n-- Channel: {message_object.channel} | Message: {message_object.message}')


class PubSub():
    """
    Handles the publish/subscribe layer of the application.
    Provides communication between the nodes of the blockchain network.     
    """

    def __init__(self):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels([TEST_CHANNEL]).execute()
        self.pubnub.add_listener(Listener())

    def publish(self, channel, message):
        """
        Publish the message to the channel.
        """
        self.pubnub.publish().channel(
            channel).message(message).sync()


def main():
    pubsub = PubSub()
    time.sleep(1)
    pubsub.publish(TEST_CHANNEL, {'foo': 'bar'})


if __name__ == '__main__':
    main()
