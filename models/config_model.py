import yaml
from fastapi import HTTPException
from pydantic.dataclasses import dataclass


def load_config():
    with open('config.yaml', 'r') as file_descriptor:
        config = yaml.load(file_descriptor, Loader=yaml.FullLoader)
    try:
        return Configurations(**config)
    except TypeError:
        raise HTTPException(status_code=500, detail='Could not load configs')


@dataclass
class Configurations:
    url: str
    resource_id: str
    default_query: str
    limit: int


