from django.core.management.base import BaseCommand

from octofit_tracker.models import Activity, LeaderboardEntry, Team, User, Workout


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        Activity.objects.all().delete()
        LeaderboardEntry.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()

        heroes = [
            User.objects.create(name='Peter Parker', email='spider-man@marvel.example', avatar='https://example.com/spider-man.png'),
            User.objects.create(name='Diana Prince', email='wonder-woman@dc.example', avatar='https://example.com/wonder-woman.png'),
            User.objects.create(name='Tony Stark', email='iron-man@marvel.example', avatar='https://example.com/iron-man.png'),
            User.objects.create(name='Bruce Wayne', email='batman@dc.example', avatar='https://example.com/batman.png'),
        ]

        marvel = Team.objects.create(name='Marvel', description='Heroes da Marvel')
        dc = Team.objects.create(name='DC', description='Heroes da DC')
        marvel.members.add(heroes[0], heroes[2])
        dc.members.add(heroes[1], heroes[3])

        workouts = [
            Workout.objects.create(
                name='Treino do Aranha',
                description='Agilidade e resistência',
                difficulty='medium',
                target='agility',
            ),
            Workout.objects.create(
                name='Circuito Amazon',
                description='Força e mobilidade',
                difficulty='hard',
                target='strength',
            ),
        ]

        for index, hero in enumerate(heroes):
            Activity.objects.create(
                user=hero,
                activity_type='hero training',
                duration_minutes=30 + index * 10,
                points=100 - index * 10,
            )
            LeaderboardEntry.objects.create(user=hero, points=100 - index * 10, rank=index + 1)

        self.stdout.write(self.style.SUCCESS(
            f'{len(heroes)} usuarios, 2 equipes, {len(workouts)} treinos e atividades populados.'
        ))