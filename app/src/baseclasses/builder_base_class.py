class BuilderBaseClass:

    def __init__(self):
        self.properties = {}

    def update_inner_property(self, inner_structure: list,
                              attribute, value):
        # Example of putting value in deepest inner attribute
        if isinstance(attribute, list):
            self.properties[attribute] = value
        else:
            current_inner_level = self.properties

            for key in inner_structure:
                if key not in current_inner_level:
                    current_inner_level[key] = {}
                if key == attribute:
                    current_inner_level[attribute] = value
                current_inner_level = current_inner_level[key]

        return self
