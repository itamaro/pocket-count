# Pocket Count

Simple stats over Pocket app library.


## Initial setup

First, create an "app" on https://getpocket.com/developer/apps/

Write down the app "consumer key" (of the form 12345-abcd1234abcd1234abcd1234)

Now, obtain an auth code (fill in your consumer key):

```sh
curl -XPOST -H 'Content-Type: application/json; charset=UTF-8' -H 'X-Accept: application/json' https://getpocket.com/v3/oauth/request -d '{"consumer_key":"12345-abcd1234abcd1234abcd1234", "redirect_uri":"pocketapp1234:authorizationFinished"}'
{"code":"abcd1234-ab12-1234-ab12-abc123","state":null}
```

Approve access by browsing to: https://getpocket.com/auth/authorize?request_token=abcd1234-ab12-1234-ab12-abc123&redirect_uri=pocketapp1234:authorizationFinished (note to fill in the auth code obtained above)

Finally, exchange the auth code for an access token:

```sh
curl -XPOST -H 'Content-Type: application/json; charset=UTF-8' -H 'X-Accept: application/json' https://getpocket.com/v3/oauth/authorize -d '{"consumer_key":"12345-abcd1234abcd1234abcd1234", "code":"abcd1234-ab12-1234-ab12-abc123"}'
{"access_token":"abcd1234-ab12-cd34-1234-abc123","username":"yourusername"}
```


## Running the script

This script requires Python 3.6+ and [Pipenv](https://docs.pipenv.org/):

```sh
pipenv install
pipenv run python -m count
```
