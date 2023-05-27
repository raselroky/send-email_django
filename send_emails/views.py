from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from send_emails import email_send
from smtplib import SMTPException


class SendEmailApi(APIView):
    def post(self,request):
        #many email accept
        email=request.data['email']
        s=str(email)
        k=s.split(',')
        # subject,body,to
        try:
            email_send.send('welcome','Thank you for joining us!',k)
            return Response({"Message":"OK!"})
        except SMTPException as e:
            return Response({"message":e})
        except:
            return Response({"Message":"Failed to send!"})
