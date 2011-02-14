#!/usr/bin/env python


import re
import commands


REDIS_INFO_CMD = "redis-cli info"


class Redis:
    def __init__(self, agent_config, checks_logger, raw_config):
        self.agent_config = agent_config
        self.checks_logger = checks_logger
        self.raw_config = raw_config

    def run(self):
        stats = {}
        status, out = commands.getstatusoutput(REDIS_INFO_CMD)
        if status != 0:
            return stats
        # Grab every statistic available and leave it to the end user to
        # determine which fields they care about
        for key, val in [line.split(':') for line in out.splitlines()]:
            stats[key] = val
        return stats


if __name__ == '__main__':
    redis = Redis(None, None, None)
    print redis.run()
