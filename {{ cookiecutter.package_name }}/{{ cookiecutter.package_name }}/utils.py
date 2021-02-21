"""Helper functions for the project."""


class FilterParam:
    """Filter a query based on an op and param"""

    def __init__(
        self,
        name,
        op,
        _in="query",
        schema="int",
        transform=None,
        format_=None,
        default=None,
    ):
        self.name = name
        self.op = op
        self.val = None
        self.__schema__ = {"name": name, "in": _in, "type": schema, "format": format_}
        self.transform = transform
        self.default = default

    def identity(self, x):
        return x

    def __call__(self, val=None):
        if not self.default and not val:
            raise ValueError("Should provide either val or default value")
        self.val = (self.transform or self.identity)(val or self.default)
        return self

    def apply(self, query, model):
        if "." in self.attribute:
            child_class, child_attr = self.attribute.split(".")
            child_class_ = model.__mapper__.relationships[child_class].mapper.class_
            return query.filter(
                getattr(model, child_class).any(
                    self.op(getattr(child_class_, child_attr), self.val)
                )
            )
        return query.filter(self.op(getattr(model, self.attribute), self.val))

    def apply(self, query, model):
        return query.filter(self.op(getattr(model, self.name), self.val))

    def __repr__(self):
        return f"filter {self.name} by {self.op}"

    def __str__(self):
        return self.__repr__()
