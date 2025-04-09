from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Create test users
        user1 = User.objects.create(id='user1', email='john.doe@example.com', name='John Doe', age=30)
        user2 = User.objects.create(id='user2', email='jane.smith@example.com', name='Jane Smith', age=25)

        # Create test teams
        team1 = Team.objects.create(name='Team Alpha')
        team2 = Team.objects.create(name='Team Beta')

        # Add users to teams
        team1.members.add(user1)
        team2.members.add(user2)

        # Create test activities
        Activity.objects.create(user=user1, activity_type='Running', duration=30, date='2025-04-08')
        Activity.objects.create(user=user2, activity_type='Cycling', duration=45, date='2025-04-08')

        # Create test leaderboard entries
        Leaderboard.objects.create(user=user1, points=100)
        Leaderboard.objects.create(user=user2, points=150)

        # Create test workouts
        Workout.objects.create(name='Morning Yoga', description='A relaxing yoga session', duration=60)
        Workout.objects.create(name='HIIT', description='High-intensity interval training', duration=30)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))