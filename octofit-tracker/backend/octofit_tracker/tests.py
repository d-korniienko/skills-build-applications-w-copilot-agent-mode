from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(name='Test', email='test@example.com', team='Marvel')
        self.assertEqual(user.email, 'test@example.com')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='TestTeam', description='A test team')
        self.assertEqual(team.name, 'TestTeam')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user='test@example.com', activity='Running', duration=30)
        self.assertEqual(activity.activity, 'Running')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(user='test@example.com', workout='Push-ups', reps=20)
        self.assertEqual(workout.reps, 20)

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        lb = Leaderboard.objects.create(user='test@example.com', points=100)
        self.assertEqual(lb.points, 100)
