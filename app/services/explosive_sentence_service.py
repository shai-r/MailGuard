from app.db.postgresql.models import Terrorist, DeviceInfo, Location, HostageSentence
from app.repository.explosive_sentence_repository import create_new_explosive_sentence
from app.repository.terrorist_repository import create_new_terrorist_if_not_exists


def insert_email_into_explosive_sql(email: dict):
    terrorist = create_new_terrorist_if_not_exists(
        Terrorist(
            email=email['email'] if 'email' in email.keys() else None,
            username=email['username'] if 'username' in email.keys() else None,
            ip_address=email['ip_address'] if 'ip_address' in email.keys() else None,
            created_at=email['created_at'] if 'created_at' in email.keys() else None,
            device_info=DeviceInfo(
                browser=email['device_info']['browser'] if 'browser' in email['device_info'].keys() else None,
                os=email['device_info']['os'] if 'os' in email['device_info'].keys() else None,
                device_id=email['device_info']['device_id'] if 'device_id' in email['device_info'].keys() else None
            ),
            location=Location(
                latitude=email['location']['latitude'] if 'latitude' in email['location'].keys() else None,
                longitude=email['location']['longitude'] if 'longitude' in email['location'].keys() else None,
                city=email['location']['city'] if 'city' in email['location'].keys() else None,
                country=email['location']['country'] if 'country' in email['location'].keys() else None
            )
        )
    ).value_or(None)
    if not terrorist:
        return
    terrorist_id = terrorist.terrorist_id

    for sentence in email['sentences']:
        explosive_sentence_id = create_new_explosive_sentence(
            HostageSentence(
                sentence=sentence,
                terrorist_id=terrorist_id
            )
        ).explosive_sentence_id