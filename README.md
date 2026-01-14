## LINE Daily English Reminder (GitHub Actions)

### GitHub Secrets
Set these repository secrets:
- `LINE_CHANNEL_ACCESS_TOKEN`: your LINE Messaging API channel access token.
- `LINE_USER_ID`: the target userId to receive push messages.

### Manual Test (workflow_dispatch)
1. Go to the GitHub repo.
2. Actions tab → "Daily LINE English Reminder" → Run workflow.

### Common Push Failure Reasons
- You didn’t add the LINE Official Account (bot) as a friend.
- Wrong `LINE_USER_ID` (not the same account you’re testing with).
- Invalid/expired `LINE_CHANNEL_ACCESS_TOKEN` (use the Messaging API channel token).
- The channel/bot is not allowed to push to that user (friendship not established).
- GitHub Actions cron runs in UTC (Taipei 21:00 = UTC 13:00).

