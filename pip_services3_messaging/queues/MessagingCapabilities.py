# -*- coding: utf-8 -*-
"""
    pip_services3_messaging.queues.MessagingCapabilities
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Messaging capabilities implementation.
    
    :copyright: Conceptual Vision Consulting LLC 2018-2019, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""


class MessagingCapabilities(object):
    """
    Data object that contains supported capabilities of a message queue.
    If certain capability is not supported a queue will throw NotImplemented exception.
    """

    def __init__(self, message_count: bool, send: bool, receive: bool, peek: bool, peek_batch: bool, renew_lock: bool,
                 abandon: bool, dead_letter: bool, clear: bool):
        """
        Creates a new instance of the capabilities object.

        :param message_count: true if queue supports reading message count.
        :param send: true if queue is able to send messages.
        :param receive: true if queue is able to receive messages.
        :param peek: true if queue is able to peek messages.
        :param peek_batch: true if queue is able to peek multiple messages in one batch.
        :param renew_lock: true if queue is able to renew message lock.
        :param abandon: true if queue is able to abandon messages.
        :param dead_letter: true if queue is able to send messages to dead letter queue.
        :param clear: true if queue can be cleared.
        """
        self.__message_count = message_count
        self.__send = send
        self.__receive = receive
        self.__peek = peek
        self.__peek_batch = peek_batch
        self.__renew_lock = renew_lock
        self.__abandon = abandon
        self.__dead_letter = dead_letter
        self.__clear = clear

    def can_message_count(self) -> bool:
        """
        Informs if the queue is able to read number of messages.

        :return: true if queue supports reading message count.
        """
        return self.__message_count

    def can_send(self) -> bool:
        """
        Informs if the queue is able to send messages.

        :return: true if queue is able to send messages.
        """
        return self.__send

    def can_receive(self) -> bool:
        """
        Informs if the queue is able to receive messages.

        :return: true if queue is able to receive messages.
        """
        return self.__receive

    def can_peek(self) -> bool:
        """
        Informs if the queue is able to peek messages.

        :return: true if queue is able to peek messages.
        """
        return self.__peek

    def can_peek_batch(self) -> bool:
        """
        Informs if the queue is able to peek multiple messages in one batch.

        :return: true if queue is able to peek multiple messages in one batch.
        """
        return self.__peek_batch

    def can_renew_lock(self) -> bool:
        """
        Informs if the queue is able to renew message lock.

        :return: true if queue is able to renew message lock.
        """
        return self.__renew_lock

    def can_abandon(self) -> bool:
        """
        Informs if the queue is able to abandon messages.

        :return: true if queue is able to abandon.
        """
        return self.__abandon

    def can_dead_letter(self) -> bool:
        """
        Informs if the queue is able to send messages to dead letter queue.

        :return: true if queue is able to send messages to dead letter queue.
        """
        return self.__dead_letter

    def can_clear(self) -> bool:
        """
        Informs if the queue can be cleared.

        :return: true if queue can be cleared.
        """
        return self.__clear
