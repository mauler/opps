from modeltranslation.translator import translator, TranslationOptions

from .models import Container


class ContainerTranslationOptions(TranslationOptions):
    fields = ('title', 'hat', )


translator.register(Container, ContainerTranslationOptions)
