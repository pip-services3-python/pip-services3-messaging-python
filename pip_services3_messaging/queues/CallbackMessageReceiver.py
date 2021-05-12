# -*- coding: utf-8 -*-
from typing import Callable

from pip_services3_messaging.queues import IMessageReceiver, MessageEnvelope, IMessageQueue


class CallbackMessageReceiver(IMessageReceiver):
    """
    Wraps message callback into IMessageReceiver
    """

    def __init__(self, callback: Callable[[MessageEnvelope, IMessageQueue], None]):
        if callback is None:
            raise Exception('Callback cannot be None')

        self.__callback = callback

    def receive_message(self, message: MessageEnvelope, queue: IMessageQueue):
        """
        Receives incoming message from the queue.

        :param message: an incoming message
        :param queue: a queue where the message comes from
        """
        self.__callback(message, queue)
