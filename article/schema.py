import graphene
from graphene_django.types import DjangoObjectType

from article.models import Category, Article


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class ArticleType(DjangoObjectType):
    class Meta:
        model = Article


class Query(graphene.AbstractType):
    all_categories = graphene.List(CategoryType)
    all_articles = graphene.List(ArticleType)

    category = graphene.Field(CategoryType, id=graphene.Int(), name=graphene.String())
    article = graphene.Field(ArticleType, id=graphene.Int(), name=graphene.String(), content=graphene.String(),
                             create_time=graphene.String())

    def resolve_all_categories(self, arg, context, info):
        return Category.objects.all()

    def resolve_all_articles(self, arg, context, info):
        return Article.objects.all()

    def resolve_category(self, arg, context, info):
        id = arg.get('id')
        name = arg.get('name')

        if id is not None:
            return Category.objects.get(pk=id)

        if name is not None:
            return Category.objects.get(name=name)
        return None

    def resolve_articles(self, arg, context, info):
        id = arg.get('id')
        name = arg.get('name')
        if id is not None:
            return Article.objects.get(pk=id)

        if name is not None:
            return Article.objects.get(name=name)
        return None
