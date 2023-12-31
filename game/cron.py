from django_cron import CronJobBase, Schedule
from django.utils import timezone

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1 # Define how often the task should run (e.g., every 1 minute)
    
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'game.cron'  # Path to your cron job function

    def do(self):
        pass