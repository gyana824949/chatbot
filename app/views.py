from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import os
import openai

openai.api_key = "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"


def chat(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def chatapi(request):
    if request.method=='POST':
        prompt=request.POST['prompt']
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                "role": "user",
                "content": ""
                }
            ],
            prompt=prompt,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            # body='data',
            # credentials='same-origin',
            )
        print(response)
        return JsonResponse(response)
    return HttpResponse('bad request')

