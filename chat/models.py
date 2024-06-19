from django.db import models
# from django.conf import settings

# class Message(models.Model):
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='messages')
#     content = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.author.username + ' - ' + self.timestamp.strftime("%Y-%m-%d %H:%M:%S")

# class ChatRoom(models.Model):
#     participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='chatrooms')
#     messages = models.ManyToManyField(Message, related_name='chatrooms')

#     def __str__(self):
#         return f"ChatRoom {self.id}"

