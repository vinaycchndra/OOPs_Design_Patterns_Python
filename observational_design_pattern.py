# Channel class which can be considered a channel in video sharing platform such as youtube, vimeo. Once a video is uploaded by a channel the notification goes to all the observers or subscribers on the channel

class Channel:
    def __init__(self, name):
        self.name = name
        self.subscribers = set()
        self.videos = []
        
    def upload(self, video):
        self.videos.append(video)
        for subs in self.subscribers:
            msg = "A notification for %s, channel '%s' has uploaded a video with title %s" % (subs.name, self.name, video)
            subs.notification(msg)
    
# Subscriber who is follower of a channel which has a get notification, subscribe, unsubscribe method for observing the channel 
class Subscriber:
    def __init__(self, name):
        self.name = name
        self.subscribed = set()
        
    def subscribe(self, channel):
        self.subscribed.add(channel)
        channel.subscribers.add(self)
        
    def unsubscribe(self, channel):
        if channel in self.subscribed:
            channel.subscribers.remove(self)
            self.subscribed.remove(channel)
            print('You have unsubscribed the {}'.format(channel.name))
        
    def notification(self, msg):
        print(msg)
        
if __name__ == '__main__':
    channel1 = Channel('Code_Develop')
    channel2 = Channel('Code Source')
    user1 = Subscriber('Ravi')
    user2 = Subscriber('Rakesh')
    user3 = Subscriber('Ramesh')
    user4 = Subscriber('Rancho')
    user5 = Subscriber('Ram')
    
    user1.subscribe(channel1)
    user1.subscribe(channel2)
    user2.subscribe(channel2)
    user3.subscribe(channel1)
    user4.subscribe(channel1)
    user5.subscribe(channel2)
    
    channel1.upload('History of India')
    channel2.upload('The features of a clever man')
    user1.unsubscribe(channel1)
    channel1.upload('Languages in India')
    
