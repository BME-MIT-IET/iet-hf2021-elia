import asyncio
import sys
from datetime import datetime, timedelta
import discord
from discord.member import VoiceState
from distest import TestCollector
from distest import run_dtest_bot
from discord import Embed, Member, Status
from distest.TestInterface import TestInterface

test_collector = TestCollector()

performance_output: str = ""

def add_time_to_output(message: str, time_taken: timedelta):
    global performance_output
    performance_output += "{}\n\tTime taken:\t\t\t{}\n\n".format(message, time_taken.total_seconds())

@test_collector()
async def ping_time(interface: TestInterface):
    start_time: datetime = datetime.now()
    for i in range(0, 10):
        await interface.assert_reply_embed_regex("+ping", {"title": "Pong!"})
    add_time_to_output("Sent 10 ping requests", datetime.now() - start_time)

@test_collector()
async def write_performance_metrics(interface: TestInterface):
    await interface.send_message("```{}```".format(performance_output))

if __name__ == "__main__":
    run_dtest_bot(sys.argv, test_collector, timeout=10)