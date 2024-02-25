Orbs are prebundled commands that are used in circleci
one of those orbs is the slack orb.
which can be placed before executors
```
orbs: 
  slack: circleci/slack@4.10.1
```
it needs slack app key and a relevant workspace to send notifications to.
after acquiring both of these, we add them as environmental variables `SLACK_ACCESS_TOKEN` and `SLACK_DEFAULT_CHANNEL`
we can use the app to send messages by adding the following code to steps in circleci.
```
      - slack/notify:
          event: fail/pass
          custom: |
            {"blocks": [{
              "type": "section",
              "fields": [{
                  "type": "plain_text",
                  "text": "text",
                  "emoji": true
                }]}]}
```