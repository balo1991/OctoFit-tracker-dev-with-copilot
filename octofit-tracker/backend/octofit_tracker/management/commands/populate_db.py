from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='marvel')
        dc = Team.objects.create(name='dc')

        # Users
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='marvel'),
            User(email='captain@marvel.com', name='Captain America', team='marvel'),
            User(email='spiderman@marvel.com', name='Spider-Man', team='marvel'),
            User(email='batman@dc.com', name='Batman', team='dc'),
            User(email='superman@dc.com', name='Superman', team='dc'),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team='dc'),
        ]
        for user in users:
            user.save()

        # Activities
        activities = [
            Activity(user='Iron Man', type='run', duration=30, date=timezone.now().date()),
            Activity(user='Captain America', type='cycle', duration=45, date=timezone.now().date()),
            Activity(user='Spider-Man', type='swim', duration=25, date=timezone.now().date()),
            Activity(user='Batman', type='run', duration=40, date=timezone.now().date()),
            Activity(user='Superman', type='fly', duration=60, date=timezone.now().date()),
            Activity(user='Wonder Woman', type='lift', duration=35, date=timezone.now().date()),
        ]
        for activity in activities:
            activity.save()

        # Leaderboard
        Leaderboard.objects.create(team='marvel', points=100)
        Leaderboard.objects.create(team='dc', points=90)

        # Workouts
        workouts = [
            Workout(name='Pushups', description='Do 20 pushups', difficulty='easy'),
            Workout(name='Sprints', description='Sprint for 100m', difficulty='medium'),
            Workout(name='Deadlift', description='Deadlift 100kg', difficulty='hard'),
        ]
        for workout in workouts:
            workout.save()

        self.stdout.write(self.style.SUCCESS('Test data successfully populated in octofit_db.'))
