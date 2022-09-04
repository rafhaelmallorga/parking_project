class SerializerByMethodMixin:
    def get_serializer_class(self):
        # assert (
        #     self.serializer_class is not None
        # ), f"{self.__class__.__name__} should either include a `serializer_map` attribute "

        return self.serializer_map.get(self.request.method)
