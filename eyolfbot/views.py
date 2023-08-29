from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from django.utils.http import urlencode

from social_core.backends.gitlab import GitLabOAuth2
from social_django.utils import load_strategy

from rest_framework import viewsets
from rest_framework import permissions

import requests

from .models import Connection
from .serializers import ConnectionSerializer

API_ENDPOINT = 'https://discord.com/api/v10'

def get_discord_token(code):
    url = f'{API_ENDPOINT}/oauth2/token'
    data = {
        'client_id': settings.EYOLFBOT_CLIENT_ID,
        'client_secret': settings.EYOLFBOT_CLIENT_SECRET,
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': settings.EYOLFBOT_REDIRECT_URI,
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    r = requests.post(url, data=data, headers=headers)
    r.raise_for_status()
    return r.json()

def get_discord_user_data(token):
    url = f'{API_ENDPOINT}/users/@me'
    headers = {
        'Authorization': f"{token['token_type']} {token['access_token']}",
    }
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    return r.json()

def add_discord_guild_member(user_id, token):
    url = f"{API_ENDPOINT}/guilds/{settings.EYOLFBOT_GUILD_ID}/members/{user_id}"
    data = {
        'access_token': token['access_token'],
        'roles': settings.EYOLFBOT_ROLES,
    }
    headers = {
        'Authorization': f"Bot {settings.EYOLFBOT_BOT_TOKEN}",
    }
    r = requests.put(url, json=data, headers=headers)
    if r.status_code == 204:
        return {}
    r.raise_for_status()
    return r.json()

def add_discord_guild_roles(user_id, roles):
    for role_id in roles:
        url = f"{API_ENDPOINT}/guilds/{settings.EYOLFBOT_GUILD_ID}/members/{user_id}/roles/{role_id}"
        headers = {
            'Authorization': f"Bot {settings.EYOLFBOT_BOT_TOKEN}",
        }
        requests.put(url, headers=headers)

@login_required(login_url='/social/login/gitlab/')
def discord(request):
    try:
        connection = request.user.eyolfbot_connection
        return render(request, 'eyolfbot/discord.html',
                      {'connection': connection})
    except ObjectDoesNotExist:
        pass

    if not 'code' in request.GET:
        redirect_uri = urlencode({'redirect_uri': settings.EYOLFBOT_REDIRECT_URI})
        return redirect(f'https://discord.com/api/oauth2/authorize?client_id={settings.EYOLFBOT_CLIENT_ID}&{redirect_uri}&response_type=code&scope=identify%20guilds.join')

    user = request.user
    try:
        social = user.social_auth.get(provider='gitlab')
    except ObjectDoesNotExist:
        # TODO: This could be a real error if the account is already associated
        #       with a different user account.
        return redirect(f'/social/login/gitlab/?next={request.path}')
    strategy = load_strategy(request)
    backend = social.get_backend_instance(strategy)
    access_token = social.get_access_token(strategy)

    gitlab_user_data = backend.user_data(access_token)
    gitlab_id = int(gitlab_user_data['id'])
    gitlab_username = gitlab_user_data['username']

    discord_code = request.GET['code']
    discord_token = get_discord_token(discord_code)
    discord_user_data = get_discord_user_data(discord_token)
    discord_id = int(discord_user_data['id'])

    guild_member_data = add_discord_guild_member(discord_id, discord_token)
    if not guild_member_data:
        add_discord_guild_roles(discord_id, settings.EYOLFBOT_ROLES)

    connection = Connection(user=request.user, utoronto_id=gitlab_username,
                            discord_id=discord_id, gitlab_id=gitlab_id)
    connection.save()

    return redirect('eyolfbot:discord')

class ConnectionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer
    permission_classes = [permissions.IsAuthenticated]
