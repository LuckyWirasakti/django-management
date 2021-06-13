from core.issue.models import Card
from django.dispatch import receiver
from django.core.mail import send_mail
from django.db.models.signals import post_save

@receiver(post_save, sender=Card)
def state_card_change_handler(sender, instance, created,  **kwargs):
    if not created:
        pass
        # send_mail(
        #     instance.get_category(),
        #     'Here is the message.',
        #     'from@example.com',
        #     ['to@example.com'],
        #     fail_silently=False,
        # )