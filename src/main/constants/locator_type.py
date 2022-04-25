import enum


class LocatorType(enum.Enum):
    xpath = 'xpath',
    css = 'css',
    id = 'id',
    link_text = 'link text',
    name = 'name',
    partial_link_text = 'partial link text',
    tag = 'tag',
    class_name = 'class name'
