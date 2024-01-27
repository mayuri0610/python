from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')



# var ws = new WebSocket('ws://127.0.0.1:8000/ws/sc/')
#     ws.onopen = function () { 
#         console.log('Websocket Connection open...')
#     }
#     ws.onmessage = function (event) { 
#         console.log('Massage received from server', event)
#     }
#     ws.onclose = function (event) {  
#         console.error('Websocket Connection closed unexpectedly')
#     };