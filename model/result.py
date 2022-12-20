from dataclasses import dataclass
from typing import Any


@dataclass
class Result:
    title: str
    date: str
    category: str
    groups: str
    recipients: int
    deliveries: int
    clicks: int
    attachmentOpened: int
    dataEntered: int
    otherFailures: int
    pabReported: int
    bounces: int
    frm: str
    subject: str
    attachment: str
    phishDomain: str
    clicksByDay: dict

    @staticmethod
    def from_dict(obj: Any) -> 'Result':
        _title = str(obj.get("title"))
        _date = str(obj.get("date"))
        _category = str(obj.get("category"))
        _groups = str(obj.get("groups"))
        _recipients = int(obj.get("recipients"))
        _deliveries = int(obj.get("deliveries"))
        _clicks = int(obj.get("clicks"))
        _attachmentOpened = int(obj.get("attachmentOpened"))
        _dataEntered = int(obj.get("dataEntered"))
        _otherFailures = int(obj.get("otherFailures"))
        _pabReported = int(obj.get("pabReported"))
        _bounces = int(obj.get("bounces"))
        _frm = str(obj.get("frm"))
        _subject = str(obj.get("subject"))
        _attachment = str(obj.get("attachment"))
        _phishDomain = str(obj.get("phishDomain"))
        _clicksByDay = dict(obj.get("clicksByDay"))
        return Result(_title, _date, _category, _groups, _recipients, _deliveries, _clicks, _attachmentOpened,
                      _dataEntered, _otherFailures, _pabReported, _bounces, _frm, _subject, _attachment, _phishDomain,
                      _clicksByDay)
