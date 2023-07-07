from django.test import TestCase
from articles.models import Article
from django.contrib.auth.models import User

# Create your tests here.

class ArticleTestCase(TestCase):
    
    def create_article(self, title="Patch Notes 5.0.0", article="short article", full_article="full article", created_date='2023-06-27', created_by=User.objects.create_user(username="Shusui", email="test@gmail.com", password="testpassword")):
        return Article.objects.create(title=title, article=article, full_article=full_article, created_date=created_date, created_by=created_by)
    
    def test_article_creation(self):
        article = self.create_article()
        self.assertTrue(isinstance(article,Article))
        self.assertEqual(article.__str__(), article.title)
        
    def test_article_template_name(self):
        article = self.create_article()
        self.assertEqual(article.replace_space_and_dot_in_title(), 'patch_notes_5_0_0')
    
    def test_article_template_name_false(self):
        article = self.create_article()
        self.assertNotEqual(article.replace_space_and_dot_in_title(), 'patch_notes.5.0.0')
        
    def test_is_article_in_templates(self):
        article = self.create_article()
        self.assertTrue()
