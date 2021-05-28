import json
class sub:
    def read_config(self, key):
        """
        this method contains reading of json configuration file
        :param key: key
        :return: data
        """
        with open('keys.json', 'r') as json_file:
            data = json.load(json_file)
            return data.get(key, None)