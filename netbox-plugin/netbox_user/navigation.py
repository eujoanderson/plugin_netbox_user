from extras.plugins import PluginMenuItem
from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices


menu_items = (
    PluginMenuItem(
        link='plugins:netbox_user:userlist_list',
        link_text='Users'
    ),
    PluginMenuItem(
        link='plugins:netbox_user:resourceaccess_list',
        link_text='Recursos do Usuário'
    ),
)



userlist_buttons = [
    PluginMenuButton(
        link='plugins:netbox_user:userlist_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

userlistrule_buttons = [
    PluginMenuButton(
        link='plugins:netbox_user:resourceaccess_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]


menu_items = (
    PluginMenuItem(
        link='plugins:netbox_user:userlist_list',
        link_text='Users',
        buttons=userlist_buttons
    ),
    PluginMenuItem(
        link='plugins:netbox_user:resourceaccess_list',
        link_text='Resources User',
        buttons=userlistrule_buttons
    ),
)