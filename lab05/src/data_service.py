class DataService:

    def __init__(self, api_client):
        self.api_client = api_client

    def fetch_user_data(self, args):
        return self.api_client.get_data(args)