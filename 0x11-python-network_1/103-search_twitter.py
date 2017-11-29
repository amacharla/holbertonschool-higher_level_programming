#!/usr/bin/python3
""" Makes a search query using Twitter API and Oauth2 """

if __name__ == "__main__":
    import requests
    import base64
    from sys import argv

    def post_bearer(key, secret):
        """ fetches the Bearer token """

        key = (key + ':' + secret).encode("utf-8")
        token = base64.urlsafe_b64encode(key)
        token = "Basic " + str(token, 'utf-8')
        header = {'Authorization': token,
                  'Content-Type':
                  'application/x-www-form-urlencoded;charset=UTF-8'}

        res_bearer = requests.post('https://api.twitter.com/oauth2/token',
                                   data={'grant_type': 'client_credentials'},
                                   headers=header).json()
        bearer = res_bearer.get('access_token')
        bearer = 'Bearer ' + bearer
        return bearer

    def get_search(query, bearer):
        """ Makes a search query """

        parameters = {'q': query, 'count': 5, 'result_type': 'recent'}
        header = {'Authorization': bearer}
        results = requests.get('https://api.twitter.com/1.1/search/tweets.\
                                json', params=parameters, headers=header)

        if results.ok:
            results = results.json()
            if len(results.get('statuses')) > 0:
                return results
        raise ValueError('Invalid Query')

    def print_nice(results):
        """ Print [<UserId>] <UserText> <UserName> """

        for result in results.get('statuses'):
            usr_id = result.get('id')
            usr_txt = result.get('text')
            usr_name = result.get('user').get('name')
            print('[{}] {} by {}'.format(usr_id, usr_txt, usr_name))

    key = post_bearer(argv[1], argv[2])
    results = get_search(argv[3], key)
    print_nice(results)
