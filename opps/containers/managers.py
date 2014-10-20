from opps.core.managers import PublishableManager, PublishableQuerySet

from modeltranslation.manager import MultilingualQuerySet
from polymorphic.manager import PolymorphicManager
from polymorphic.query import PolymorphicQuerySet


class ContainerQuerySet(PolymorphicQuerySet, PublishableQuerySet,
                        MultilingualQuerySet):
    pass


class ContainerManager(PolymorphicManager, PublishableManager):
    queryset_class = ContainerQuerySet
