# coding: utf-8
from collections import defaultdict
from sentry.plugins.bases.notify import NotificationPlugin
from sentry import http

from .forms import WorkWeixinOptionsForm
from . import __version__, __doc__ as package_doc

Work_Weixin_API = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={key}"


class WorkWeixinNotificationPlugin(NotificationPlugin):

    title = 'Work Weixin Notifications'
    slug = 'sentry_work_weixin'
    author = 'Eugene'
    author_url = 'http://gitlab-test.dianmi365.com:81/eugene/sentry-work-weixin'
    version = __version__
    description = package_doc
    resource_links = [
        ('Source', 'http://gitlab-test.dianmi365.com:81/eugene/sentry-work-weixin'),
        ('Bug Tracker', 'http://gitlab-test.dianmi365.com:81/eugene/sentry-work-weixin/issues'),
        ('README', 'http://gitlab-test.dianmi365.com:81/eugene/sentry-work-weixin/blob/master/README.md'),
    ]

    conf_key = slug
    conf_title = title
    project_conf_form = WorkWeixinOptionsForm

    def is_configured(self, project):
        """
        Check if plugin is configured.
        """
        return bool(self.get_option('key', project))

    def notify(self, notification):
        event = notification.event
        group = event.group
        project = group.project

        if not self.is_configured(project):
            return

        if group.is_ignored():
            return

        key = self.get_option('key', group.project)
        url = Work_Weixin_API.format(key=key)
        values = self.build_message(project, group, event)
        self.send_message(url, values)

    def build_message(self, project, group, event):
        the_tags = defaultdict(lambda: '[NA]')
        the_tags.update({k: v for k, v in event.tags})
        values = {
            "msgtype": "markdown",
            "markdown": {
                "content": u"*[Sentry]* {project_name} {tag[level]}: *{title}*\n```{message}```\n{url}".format(
                    project_name=project.name,
                    title=event.title,
                    tag=the_tags,
                    message=event.message,
                    url=u"{}events/{}/".format(group.get_absolute_url(), event.id),
                )
            }
        }
        return values

    def send_message(self, url, values):
        return http.safe_urlopen(url, method="POST", data=values, timeout=5)
