# We need to have different entities for the pub-sub design architecture, 1- Publisher Entity 2- Subscriber Entity 3- Message Entity 4- Pub-Sub service entity which acts as connector btw
# Publisher and Subscriber.
from collections import deque
from abc import ABC, abstractmethod

# Message object having attribute topic and payload
class Message:
    def __init__(self, topic: str, payload: str):
        self.__topic = topic
        self.__payload = payload

    def getTopic(self):
        return self.__topic

    def setTopic(self, topic: str):
        self.__topic = topic

    def setPayload(self, payload: str):
        self.__payload = payload

    def getPayload(self):
        return self.__payload

class PubSubService:
    def __init__(self):
        self.__messageQue = deque()
        self.__topicSubscribers = dict()

    def addMessageToQue(self, msg: Message):
        self.__messageQue.append(msg)

    def subscribeToTopic(self, topic: str, subscriber):
        if topic in self.__topicSubscribers:
            self.__topicSubscribers[topic].add(subscriber)
        else:
            self.__topicSubscribers[topic] = set()
            self.__topicSubscribers[topic].add(subscriber)

    def unsubscribeToTopic(self, topic: str, subscriber):
        if topic in self.__topicSubscribers:
            self.__topicSubscribers[topic].discard(subscriber)

    def broadCast(self):
        if len(self.__messageQue) == 0:
            print('No Messages to BroadCast')

        while self.__messageQue:
            msg = self.__messageQue.popleft()
            topic = msg.getTopic()
            if topic in self.__topicSubscribers:
                for subscriber in self.__topicSubscribers[topic]:
                    subscriber.addMessage(msg)


# Subscriber abstract class
class SubscriberIterface(ABC):
    def __init__(self):
        self.__message_list =  list()

    def printMyInbox(self, recent: bool = True):
        if len(self.__message_list) == 0:
            print('No messages in the input box')
        if recent:
            for i in range(len(self.__message_list)-1, -1, -1):
                print('Topic: '+self.__message_list[i].getTopic()+' <----> '+'Payload: '+self.__message_list[i].getPayload())
        else:
            for message in self.__message_list:
                print('Topic: '+message.getTopic()+' <----> '+'Payload: '+message.getPayload())

    def addMessage(self, msg: Message):
        self.__message_list.append(msg)


    @abstractmethod
    def subscribeTopic(self):
        pass

    @abstractmethod
    def unsubscribeTopic(self):
        pass

# Subscriber implementation
class Subscriber(SubscriberIterface):

    def subscribeTopic(self, topic: str, pub_sub: PubSubService):
        pub_sub.subscribeToTopic(topic, self)

    def unsubscribeTopic(self, topic: str, pub_sub: PubSubService):
        pub_sub.unsubscribeTopic(self, topic, pub_sub)


# Publisher abstract class
class PublisherInterface(ABC):
    @abstractmethod
    def publish():
        pass


# Publisher class having publish Message method
class Publisher(PublisherInterface):

    def publish(self, msg: Message, pub_sub_service: PubSubService):
        pub_sub_service.addMessageToQue(msg)



if __name__ == '__main__':
    pub_sub = PubSubService()
    topic1 = 'Coding'
    topic2 = 'Song'
    msg1 = Message(topic1, 'Do the development job')
    msg2 = Message(topic2, 'A new album is coming next month')
    pub1 = Publisher()
    pub2 = Publisher()
    pub1.publish(msg1, pub_sub)
    pub2.publish(msg2, pub_sub)
    sub1 = Subscriber()
    sub2 = Subscriber()
    sub3 = Subscriber()
    sub1.subscribeTopic(topic1, pub_sub)
    sub1.subscribeTopic(topic2, pub_sub)
    sub2.subscribeTopic(topic2, pub_sub)
    sub3.subscribeTopic(topic2, pub_sub)
    sub1.printMyInbox()
    sub2.printMyInbox()
    sub3.printMyInbox()
    pub_sub.broadCast()
    sub1.printMyInbox(False)
    sub2.printMyInbox()
    sub3.printMyInbox()
    pub_sub.broadCast()

