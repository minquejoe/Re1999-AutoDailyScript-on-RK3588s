import logging
import smtplib
from email.mime.text import MIMEText
import config

logger = logging.getLogger(__name__)


def send_email(timeout_commands: list[str]) -> None:
    try:
        server = smtplib.SMTP_SSL(config.SMTP_HOST, config.SMTP_PORT)
        server.login(config.SOURCE_MAIL_ADDR, config.SOURCE_MAIL_PASS)

        msg = MIMEText(
            f"The following commands exceeded the {config.task_timeout} seconds "
            f"runtime limit:\n{timeout_commands}"
        )
        msg['Subject'] = "Re1999 Timeout Alert"
        msg['From'] = config.SOURCE_MAIL_ADDR
        msg['To'] = config.TARGET_MAIL_ADDR

        server.sendmail(config.SOURCE_MAIL_ADDR, config.TARGET_MAIL_ADDR, msg.as_string())
        server.quit()
        logger.info("Alert email sent successfully")
    except Exception as e:
        logger.error("Failed to send alert email: %s", e)
