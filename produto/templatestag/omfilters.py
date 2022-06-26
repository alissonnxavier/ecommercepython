from django import template
from utils import utils


register = template.Library()


def formata_preco(val):
    return utils.formata_preco(val)


