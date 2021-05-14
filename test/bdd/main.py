import asyncio
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
    await asyncio.sleep(1)


@test_collector()
async def test_play_song_then_skip(interface):
    play_embed = get_base_embed(":musical_note: Now Playing ***https://www.youtube.com/watch?v=dQw4w9WgXcQ***")
    skip_embed = get_base_embed("You skipped a song!")

    await interface.assert_reply_embed_equals("+play https://www.youtube.com/watch?v=dQw4w9WgXcQ", play_embed)
    await asyncio.sleep(5)
    await interface.assert_reply_embed_equals("+skip", skip_embed)
    await asyncio.sleep(1)


@test_collector()
async def test_play_then_pause_then_resume_then_skip(interface):
    play_embed = get_base_embed(":musical_note: Now Playing ***https://www.youtube.com/watch?v=dQw4w9WgXcQ***")
    pause_embed = get_base_embed("You paused the music.")
    resume_embed = get_base_embed("You resumed playing the music.")
    skip_embed = get_base_embed("You skipped a song!")

    await interface.assert_reply_embed_equals("+play https://www.youtube.com/watch?v=dQw4w9WgXcQ", play_embed)
    await asyncio.sleep(5)
    await interface.assert_reply_embed_equals("+pause", pause_embed)
    await asyncio.sleep(5)
    await interface.assert_reply_embed_equals("+resume", resume_embed)
    await asyncio.sleep(5)
    await interface.assert_reply_embed_equals("+skip", skip_embed)
    await asyncio.sleep(1)


@test_collector()
async def test_queue_two_songs_then_double_skip(interface):
    play_embed = get_base_embed(":musical_note: Now Playing ***https://www.youtube.com/watch?v=dQw4w9WgXcQ***")
    queue_embed = get_base_embed(":musical_note: Queued: ***https://www.youtube.com/watch?v=dQw4w9WgXcQ***")
    skip_embed = get_base_embed("You skipped a song!")

    await interface.assert_reply_embed_equals("+play https://www.youtube.com/watch?v=dQw4w9WgXcQ", play_embed)
    await asyncio.sleep(5)
    await interface.assert_reply_embed_equals("+queue https://www.youtube.com/watch?v=dQw4w9WgXcQ", queue_embed)
    await asyncio.sleep(5)
    await interface.assert_reply_embed_equals("+skip", skip_embed)
    await asyncio.sleep(5)
    await interface.assert_reply_embed_equals("+skip", skip_embed)
    await asyncio.sleep(1)


@test_collector()
async def test_play_then_replay_then_double_skip(interface):
    play_embed = get_base_embed(":musical_note: Now Playing ***https://www.youtube.com/watch?v=dQw4w9WgXcQ***")
    replay_embed = get_base_embed("You replayed a song!")
    skip_embed = get_base_embed("You skipped a song!")

    await interface.assert_reply_embed_equals("+play https://www.youtube.com/watch?v=dQw4w9WgXcQ", play_embed)
    await asyncio.sleep(5)
    await interface.assert_reply_embed_equals("+replay", replay_embed)
    await asyncio.sleep(5)
    await interface.assert_reply_embed_equals("+skip", skip_embed)
    await asyncio.sleep(5)
    await interface.assert_reply_embed_equals("+skip", skip_embed)
    await asyncio.sleep(1)


if __name__ == '__main__':
    run_dtest_bot(sys.argv, test_collector)
