from django.test import TestCase
from django.contrib.auth.models import User
from .models import AddGame

class AddGameModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        AddGame.objects.create(
            title="Pandemic",
            owner=self.user,
            description="A cooperative board game",
            review="Great game!",
            minimum_player_count=2,
            maximum_player_count=4,
            image_url="http://example.com/pandemic.jpg"
        )

    def test_add_game_creation(self):
        game = AddGame.objects.get(title="Pandemic")
        self.assertEqual(game.description, "A cooperative board game")
        self.assertEqual(game.review, "Great game!")
        self.assertEqual(game.minimum_player_count, 2)
        self.assertEqual(game.maximum_player_count, 4)
        self.assertEqual(game.image_url, "http://example.com/pandemic.jpg")
        self.assertEqual(game.owner.username, "testuser")

    def test_add_game_str(self):
        game = AddGame.objects.get(title="Pandemic")
        self.assertEqual(str(game), "Pandemic")