* The essential idea with a factory design pattern is that rather than instantiating the objects ourself we can call a factory class object which will create objects dynamically for us, however we do not have 
  a full control over the configuration of the objects we are creating for this purpose builder design pattern is being used.

* Builder design pattern gives more control over configuration of the object. I have mentioned rest of the things in more detail inside the  builder_design_pattern.py file.

* Singleton pattern, a singleton is just a class that can only have one instance of it. This is used to mainatain just single instance of the application.

* The observer pattern is a software design pattern in which an object, called the subject, maintains a list of its dependents, called observers, and notifies them automatically of any state changes, usually by calling one of their methods. Here, the subject is monitored by a group of observers wherein each observer is responsible to accomplish a different task. Whenever the state of the observable subject changes, all observers are notified about the change. More detailed description is in this post 'https://www.linkedin.com/pulse/observer-design-pattern-same-publisher-subscriber-ankita-vijan/'.

* Publisher-Subscriber design pattern: Publisher are the entities which create/publish a message on a topic. They are only concerned with creating the original message and can leave the task of serving to the    subscriber on the messaging infrastructure. 
				     : Subscribers are the entities who subscribe to a message on a topic.
				     : In Topic based publish-subscribe pattern, publishers tag each message with the topic instead of referencing specific subscribers. Messaging system then sends 
				       the messages to all the subscribers who have asked to receive messages on that topic.
  				     : So in a pub-sub design pattern publisher does not know the subscriber and subscriber does not the publisher neither they interact directly.They interact through this                                             messaging system. Below diagram describes the pub sub design pattern in detail.


	
			***************		a	    \\										****************
                        * Publisher 1 *	********************//							a	    \\		* Subscriber 1 *
			***************	  		 		*************************	********************//		****************
                                                                        *                       * 
                                                                        *                       *
			***************		b	    \\		*			*		b,c	    \\		****************
                        * Publisher 2 *	********************//		*   | PubSub Service |  *       ********************//		* Subscriber 2 *
			***************					*  Publisher-Subscriber	*					****************
                                                                        *      Service          *
									*                       *
			***************		c	    \\		*			*		a,c	    \\		****************
                        * Publisher 3 *	********************//	        *************************       ********************//		* Subscriber 3 *
			***************													****************
									
									*************************	
                                                                        * Topic *  Subscriber   *
 									*       *               *
                                                                        *************************
			 						*   a	*    S1, S3	*		
                        						*   	*		*      
									*   b	*     S2	*		
                                                                        *     	*	        *
									*   c   *    S2, S3     *
									*   	*		*		
                        					        *************************                                
	

* The abstract class factory design pattern is utilized when we need to create more than one family of related objects for example furniture with different style or pattern like modern furniture or victorian furniture. below article I have used to write the code and learn : https://medium.com/@kalanamalshan98/abstract-factory-design-pattern-the-ultimate-guide-for-beginners-4b0f97694b00