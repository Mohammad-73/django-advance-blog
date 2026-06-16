from  django.test import TestCase, Client

class TestBlogView(TestCase):
    def setUp(self):
        self.client = Client

    def test_blog_index_url_successful_response(self):
        url = reverse("blog:index")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTrue(str(response.content).find("index"))
        self.assertTemplateUsed(template_name = "index.html")