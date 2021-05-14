import sys

from discord import Embed
from distest import TestCollector
from distest import run_dtest_bot

test_collector = TestCollector()


def get_base_embed(embed_title):
    base_embed = (
        Embed(
            title=embed_title,
            color=6402394,
            type="rich",
        )
        .set_footer(
            icon_url="https://cdn.discordapp.com/embed/avatars/1.png",
            text="ELIA - DEV - 2"
        )
    )
    return base_embed


@test_collector()
async def test_ping(interface):
    embed = get_base_embed("Pong!")
    await interface.assert_reply_embed_equals("+ping", embed)


if __name__ == '__main__':
    run_dtest_bot(sys.argv, test_collector)
