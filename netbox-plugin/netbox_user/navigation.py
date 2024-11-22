from extras.plugins import PluginMenu,PluginMenuItem
from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices



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


resources_buttons = [
    PluginMenuButton(
        link='plugins:netbox_user:resources_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]


environment_buttons = [
    PluginMenuButton(
        link='plugins:netbox_user:environment_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]


groups_buttons = [
    PluginMenuButton(
        link='plugins:netbox_user:groups_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]


approver_buttons = [
    PluginMenuButton(
        link='plugins:netbox_user:approver_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]


sector_buttons = [
    PluginMenuButton(
        link='plugins:netbox_user:sector_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]




menu = PluginMenu(
    label='NETBOX USERS',
    icon_class="mdi mdi-puzzle ",
    groups=(
        ('Usuários e Recursos', 
            (
                PluginMenuItem(
                    link="plugins:netbox_user:userlist_list", 
                    link_text="Usuários", 
                    buttons=userlist_buttons
                ),
                PluginMenuItem(
                    link="plugins:netbox_user:resourceaccess_list", 
                    link_text="Recursos dos Usuários", 
                    buttons=userlistrule_buttons
                ),
            ),
        ),
        ('Opções', 
            (
                PluginMenuItem(
                    link="plugins:netbox_user:resources_list", 
                    link_text="Opções de Recursos",
					buttons=resources_buttons
                ),
                PluginMenuItem(
                    link="plugins:netbox_user:environment_list", 
                    link_text="Opções de Ambiente",
					buttons=environment_buttons
                ),
                PluginMenuItem(
                    link="plugins:netbox_user:groups_list", 
                    link_text="Opções de Grupos",
					buttons=groups_buttons
                ),
				
                PluginMenuItem(
                    link="plugins:netbox_user:approver_list", 
                    link_text="Opções de Aprovador",
					buttons=approver_buttons
                ),
				
                PluginMenuItem(
                    link="plugins:netbox_user:sector_list", 
                    link_text="Opções de Setor",
					buttons=sector_buttons
                ),
            ),
        ),
    ),
)
