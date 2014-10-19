from modeltranslation.translator import translator, TranslationOptions

from .models import Article, Post


class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'hat', 'short_title', 'headline', )


translator.register(Article, ArticleTranslationOptions)


class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'hat', 'content', )


translator.register(Post, PostTranslationOptions)
