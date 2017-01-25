from django.db import models


class Member(models.Model):
    year = models.CharField(max_length=20)
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return (u'{0}:{1}...'.format
                (self.id, self.year, self.name))

    class Meta:
        db_table = "message_member"


class Message(models.Model):
    create_for = models.ForeignKey(
        "Member", to_field='name', related_name='create_for')
    message = models.CharField(max_length=255)
    author = models.ForeignKey(
        "Member", to_field='name', related_name='author')

    def __str__(self):
        return (u'{0}:{1}...'.format
                (self.id, self.message[:10], self.create_for, self.author, ))

    class Meta:
        db_table = "message_message"
