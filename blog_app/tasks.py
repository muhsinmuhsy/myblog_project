from celery import shared_task
import logging
from django.core.mail import send_mail
from myblog_project import settings

logger = logging.getLogger(__name__)

@shared_task(bind=True)
def send_comment_notification_email(self, comment_id):
    logger.info(f'Starting task for comment {comment_id}')
    try:
        from .models import Comment  
        comment = Comment.objects.get(id=comment_id)
        post = comment.post
        post_title = post.title
        recipient_email = post.author.email

        message = (
            f'A new comment "{comment.content}" has been posted on your blog.\n\n'
            f'Post Title: {post_title}'
        )

        send_mail(
            'New comment on your post',
            message,
            settings.EMAIL_HOST_USER,
            [recipient_email],
            fail_silently=False,
        )
        logger.info(f'Email sent to {recipient_email} for comment {comment_id}')
        print("Email sent successfully")
    except Comment.DoesNotExist:
        logger.error(f'Comment with id {comment_id} does not exist')
        print("Comment does not exist")
    except Exception as e:
        logger.error(f'Error in sending email for comment {comment_id}: {str(e)}')
        print(f"Error: {str(e)}")
