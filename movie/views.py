from django.contrib.auth.models import User
from rest_framework.decorators import api_view, throttle_classes
from rest_framework import viewsets, serializers
from rest_framework.response import Response
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource(
    'dynamodb',
    region_name='ap-northeast-1',
    endpoint_url="http://dynamo:8000",
    aws_access_key_id='ACCESS_ID',
    aws_secret_access_key='ACCESS_KEY'
)


# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)


class MovieView(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """

    @staticmethod
    def hello():
        print('hello', flush=True)

    def list(self, request=None):
        table = dynamodb.Table('Movies')

        title = "Fantasia"
        year = 1940

        try:
            # response = table.query(
            #     ProjectionExpression="#yr, title, info.genres, info.actors[0]",
            #     ExpressionAttributeNames={"#yr": "year"},  # Expression Attribute Names for Projection Expression only.
            #     KeyConditionExpression=Key('year').eq(1993) & Key('title').between('B', 'L')
            # )
            response = table.scan(
                FilterExpression=Attr('info.rating').lt(9)
            )
        except Exception as e:
            print('ERROR', flush=True)
            print(e.response['Error']['Message'], flush=True)
        else:
            try:
                print(len(response['Items']), flush=True)
                # print(response.keys, flush=True)
                # item = response['Item']
                # print("GetItem succeeded:")
                return Response(response['Items'])
            except Exception as e:
                print('ERROR', flush=True)
                print(e, flush=True)
                # print('ERROR', flush=True)
                # print(e.response['Error']['Message'], flush=True)

        return Response({1: 1})

    def create(self, request):
        table = dynamodb.Table('Movies')
        title = "The Big New Movie"
        year = 2015

        response = table.put_item(
            Item={
                'year': year,
                'title': title,
                'info': {
                    'plot': "Nothing happens at all.",
                    'rating': decimal.Decimal(0)
                }
            }
        )

        print("PutItem succeeded:")
        print(json.dumps(response, indent=4, cls=DecimalEncoder))

        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
