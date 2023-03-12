from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class ArticleTests(TestCase):
    def test_url_exists_at_correct_location_articles(self):
        response = self.client.get("/articles/")
        self.assertEqual(response.status_code,200)

    def test_article_list(self):
        response = self.client.get(reverse("article_list"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"article_list.html")


   
    
