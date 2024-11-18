from netbox.plugins import PluginConfig

class NetBoxAccessListsConfig(PluginConfig):
    name = 'netbox_user'
    verbose_name = 'Netbox User'
    author="Joanderson Dos Santos"
    author_email='joandersonsantossouza09@gmail.com'
    description = 'Netbox plugin de Users'
    version = '0.2'
    base_url = 'plugin-user'
    min_version = '3.4.0'


config = NetBoxAccessListsConfig
