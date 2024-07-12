from funcs import space_template


class RequestBuilder:
    def __init__(self, authorizer, domain):
        self.domain = domain
        self.auth = authorizer.get_auth()
        self.headers = authorizer.headers

    def get_all_spaces(self, ids: list = None,
                       keys: list = None,
                       space_type: str = None,
                       status: str = None,
                       labels: list = None,
                       favorited_by: str = None,
                       not_favorited_by: str = None,
                       sort=None,
                       description_format=None,
                       include_icon: bool =False,
                       cursor: str = None,
                       limit: int = 250):
        """
        Returns all spaces. The results will be sorted by id ascending. The number of results is limited by the
        **limit** parameter and additional results (if available) will be available through the **next** URL
        present in the **Link** response header.
        """
        return space_template(self, locals().items())

    def get_space_by_id(self, space_id: int,
                        description_format=None,
                        include_icon=False,
                        include_operations=False,
                        include_properties=False,
                        include_permissions=False,
                        include_labels=False):
        """
        Returns a specific space.
        """
        return space_template(self, locals().items(), space_id)


