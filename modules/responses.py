"""This module sends responses to frequently posted messages at #miraheze."""

from sopel.module import commands, example


@commands('addchannel')
@example('.addchannel (insert which)')
def addchan(bot, trigger):
    """Reply to channel request message."""
    bot.say(("Hey Voidwalker, Reception123 or Zppix, {} would like to have "
            + "me in their channel: {}").format(trigger.nick, trigger.group(2)),
            '#ZppixBot')
    if trigger.sender != '#ZppixBot':
        bot.reply("Request sent! Action upon the request should be taken shortly. Thank you for using ZppixBot!")


@commands('gj', 'gw')
@example('.gj (nick)')
def gj(bot, trigger):
    """Tell the user that they are doing good work."""
    bot.say(("You're doing good work, {}!").format(trigger.group(2)))
