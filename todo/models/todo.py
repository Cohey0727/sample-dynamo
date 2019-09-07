from datetime import datetime

from pynamodb.attributes import UnicodeAttribute, BooleanAttribute, UTCDateTimeAttribute
from pynamodb.models import Model


class ToDo(Model):
    class Meta:
        table_name = 'todo'
        region = 'ap-northeast-1'
        write_capacity_units = 1
        read_capacity_units = 1
        host = 'http://dynamo:8000'
        endpoint_url = "http://dynamo:8000"
        aws_access_key_id = 'ACCESS_ID'
        aws_secret_access_key = 'ACCESS_KEY'

    # テーブル定義
    createdBy = UnicodeAttribute(hash_key=True, null=False)
    createdAt = UTCDateTimeAttribute(range_key=True, null=False, default=datetime.now())
    text = UnicodeAttribute(null=False)
    checked = BooleanAttribute(null=False, default=False)
    updatedAt = UTCDateTimeAttribute(null=False, default=datetime.now())
