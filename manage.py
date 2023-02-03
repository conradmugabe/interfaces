#! /usr/bin/env python
"""automation scripts"""
import os
import json
import time
import subprocess
from typing import List

import click
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

CONFIG_PATH = "config"
DOCKER_PATH = "docker"
APPLICATION_CONFIG = "APPLICATION_CONFIG"


def setenv(variable: str, value: str) -> None:
    """set environment variable"""
    os.environ[variable] = os.getenv(variable, value)


def config_file(config: str) -> str:
    """get config file path"""
    return os.path.join(CONFIG_PATH, f"{config}.json")


def read_config_file(config: str) -> dict:
    """read contents of config file"""
    with open(config_file(config), encoding="utf-8") as file:
        config_data = json.load(file)
    config_data = dict((i["name"], i["value"]) for i in config_data)
    return config_data


def configure_app(config: str) -> None:
    """configure app environment variables"""
    configuration = read_config_file(config)
    for key, value in configuration.items():
        setenv(key, value)


def run_sql(statements: List[str]):
    """run sql commands"""
    connection = psycopg2.connect("postgresql://user:testing@localhost:5432/")

    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()

    for statement in statements:
        cursor.execute(statement)

    cursor.close()
    connection.close()


def wait_for_logs(command_line, message: str) -> None:
    """check terminal logs"""
    logs = subprocess.check_output(command_line)
    while message not in logs.decode("utf-8"):
        time.sleep(1)
        logs = subprocess.check_output(command_line)


def docker_compose_file(config: str) -> str:
    """get docker compose file"""
    return os.path.join(DOCKER_PATH, f"{config}.yml")


def docker_compose(commands_string: str = None) -> list[str]:
    """docker compose cli"""
    config = os.getenv(APPLICATION_CONFIG)
    configure_app(config)
    compose_file = docker_compose_file(config)
    if not os.path.isfile(compose_file):
        raise ValueError(f"The file {compose_file} does not exist")

    command_line = ["docker-compose", "-p", config, "-f", compose_file]
    if commands_string:
        command_line.extend(commands_string.split(" "))

    return command_line


@click.group()
def cli():
    """group all cli commands in 'cli'"""


@cli.command(context_settings={"ignore_unknown_options": True})
@click.argument("args", nargs=-1)
def test(args):
    """test cli"""
    # declare testing environment
    os.environ[APPLICATION_CONFIG] = "testing"
    configure_app(os.getenv(APPLICATION_CONFIG))

    # start containers with docker-compose
    command_line = docker_compose("up -d")
    subprocess.call(command_line)

    # check if postgres container is running
    command_line = docker_compose("logs postgres")
    wait_for_logs(command_line, "ready to accept connections")

    # connect to postgres and create database
    run_sql(["CREATE DATABASE test"])

    # run tests with pytest
    command_line = ["pytest", "-svv", "--cov=src", "--cov-report=term-missing"]
    command_line.extend(args)
    subprocess.call(command_line)

    # stop containers
    command_line = docker_compose("down")
    subprocess.call(command_line)


if __name__ == "__main__":
    cli()
