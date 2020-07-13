import requests
import yaml, json

import util

credentials = util.readYAML( 'credentials' )


key = credentials['steam']['key']
steam_id = credentials['steam']['steam_id']
service = 'IPlayerService'
get_games = 'GetOwnedGames'

protocol = f'{service}/{get_games}/v0001'
url = f'https://api.steampowered.com/{protocol}?key={key}&steamid={steam_id}'


response = requests.get( url )

data = json.loads( response.text )

# response
# game_count OR games
# array index
# appid OR playtime_forever OR playtime_windows_forever OR playtime_mac_forever OR playtime_linux_forever

game_count = data['response']['game_count']

games = data['response']['games']

with open( 'data.yml', 'w' ) as f:
    f.write( yaml.dump( yaml.load( response.text )))
