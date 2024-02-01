from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import CustomerMessage
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
@api_view(['POST'])
def receive_message(request):
    # if request.method == 'POST':
    #     sender_name = request.POST.get('sender_name')
    #     message= request.POST.get('message')

    #     # Check if sender_name is not empty before saving
    #     if sender_name:
    #         # Save the received message to the database
    #         CustomerMessage.objects.create(sender_name=sender_name, message=message)
    #         return JsonResponse({'status': 'success'})
    #     else:
    #         return JsonResponse({'status': 'error', 'message': 'Sender name is required'})
    # else:
    #     return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

    if request.method == 'POST':
        sender_name = request.POST.get('sender_name')
        message = request.POST.get('message')

        # Save the received message to the database
        CustomerMessage.objects.create(sender_name=sender_name, message=message)

        return redirect('chat')  # Redirect to the agent portal or any other desired page
    else:
        return render(request, 'core/chat.html') 
@login_required
def agent_portal(request):
    # Fetch customer messages with no agent response
    messages = CustomerMessage.objects.filter(agent_response__isnull=True)

    return render(request, 'room/agent_portal.html', {'messages': messages})
@login_required
def view_message(request, user_id):
    # Retrieve the specific customer message
    message = get_object_or_404(CustomerMessage, pk=user_id)


    return render(request, 'room/view_message.html', {'message': message})
@login_required
def respond_to_message(request, user_id):
    if request.method == 'POST':
        # Retrieve the specific customer message
        message = get_object_or_404(CustomerMessage, pk=user_id)

        # Get the agent's response from the form
        agent_response = request.POST.get('agent_response')

        # Update the message with the agent's response
        message.agent_response = agent_response
        message.save()

        # return JsonResponse({'status': 'success'})
        return redirect('agent_portal')
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
