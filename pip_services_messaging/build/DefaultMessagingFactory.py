# -*- coding: utf-8 -*-
"""
    pip_services_messaging.build.DefaultMessagingFactory
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    DefaultMessagingFactory  implementation

    :copyright: Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
from pip_services_commons.refer import Descriptor
from pip_services_components.build import Factory
from .MemoryMessageQueueFactory import MemoryMessageQueueFactory
from ..queues.MemoryMessageQueue import MemoryMessageQueue

_Descriptor = Descriptor("pip-services-net", "factory", "message-queue", "memory", "1.0")
MemoryMessageQueueDescriptor = Descriptor("pip-services-net", "message-queue", "memory", "*", "*")
MemoryMessageQueueFactoryDescriptor = Descriptor("pip-services", "factory", "message-queue", "memory", "1.0")

class DefaultMessagingFactory(Factory):
    def __init__(self):
        self.register_as_type(MemoryMessageQueueFactoryDescriptor, MemoryMessageQueueFactory)
        self.register_as_type(MemoryMessageQueueDescriptor, MemoryMessageQueue)



