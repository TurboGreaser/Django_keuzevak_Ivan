from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Medicine(models.Model):
    Name = models.CharField(max_length=255)
    Manufacturer = models.CharField(max_length=255)
    Cures = models.TextField()
    SideEffects = models.TextField()

    def __str__(self):
        return self.Name


class Collection(models.Model):
    Medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collections')
    Date = models.DateField()
    Collected = models.BooleanField(default=False)
    CollectedApproved = models.BooleanField(default=False)
    CollectedApprovedBy = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='approved_collections')

    def __str__(self):
        return f"Collection of {self.Medicine.Name} by {self.user.username} on {self.Date} Approved: {self.Collected}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    BioText = models.TextField(blank=True, null=True)
    City = models.CharField(max_length=100)
    DateOfBirth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
