from django.db import models
from shareback_app.TableConstants import SessionConstants as SessionTable
from shareback_app.TableConstants import FeedbackConstants as FeedbackTable
from shareback_app.TableConstants import SessionFilesConstant as SessionFilesTable


# Create your models here.
class Sessions(models.Model):
    session_id = models.CharField(max_length=32, primary_key=True, db_column=SessionTable.session_id)
    session_name = models.CharField(max_length=120, db_column=SessionTable.session_name)
    timestamp = models.DateField(auto_now=True, db_column=SessionTable.timestamp)
    rating_1 = models.IntegerField(db_column=SessionTable.rating_1, default=0)
    rating_2 = models.IntegerField(db_column=SessionTable.rating_2, default=0)
    rating_3 = models.IntegerField(db_column=SessionTable.rating_3, default=0)
    rating_4 = models.IntegerField(db_column=SessionTable.rating_4, default=0)
    rating_5 = models.IntegerField(db_column=SessionTable.rating_5, default=0)

    class Meta:
        db_table = "sessions"

    def __str__(self):
        return self.session_name


class Feedbacks(models.Model):
    session_id = models.ForeignKey(Sessions, db_column=FeedbackTable.session_id)
    comment = models.TextField(db_column=FeedbackTable.comment, null=True)

    class Meta:
        db_table = "feedbacks"

    def __str__(self):
        return self.session_id


class SessionFiles(models.Model):
    session_id = models.ForeignKey(Sessions, db_column=SessionFilesTable.session_id)
    file = models.TextField(db_column=SessionFilesTable.file, null=True)

    class Meta:
        db_table = "session_files"

    def __str__(self):
        return self.file


# class Sessions(models.Model):
#     session_id = models.CharField(max_length=32, primary_key=True, db_column='session_id')
#     session_name = models.CharField(max_length=120, db_column='session_name')
#     timestamp = models.DateField(auto_now=True, db_column='timestamp')
#     rating_1 = models.IntegerField(db_column='rating_1')
#     rating_2 = models.IntegerField(db_column='rating_2')
#     rating_3 = models.IntegerField(db_column='rating_3')
#     rating_4 = models.IntegerField(db_column='rating_4')
#     rating_5 = models.IntegerField(db_column='rating_5')
#
#     class Meta:
#         db_table = "sessions"
#
#
# class Feedbacks(models.Model):
#     session_id = models.ForeignKey(Sessions, db_column=Sessions.session_id)
#     comment = models.TextField
#
#     class Meta:
#         db_table = "feedbacks"
#
#
# class SessionFiles(models.Model):
#     session_id = models.ForeignKey(Sessions, db_column=Sessions.session_id)
#     file = models.TextField
#
#     class Meta:
#         db_table = "session_files"
