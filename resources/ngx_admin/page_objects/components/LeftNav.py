from resources.common.CommonPage import CommonPage


class LeftNav(CommonPage):
    menu_heading = 'li.menu-item'
    menu_item = 'li.menu-item .menu-title'
    layout = 'a[title="Layout"]'
    layout_title = layout + ' span.menu-title'
    layout_icon = layout + ' nb-icon.menu-icon'
    forms = 'a[title="Forms"]'
    forms_title = forms + ' span.menu-title'
    forms_icon = forms + ' nb-icon.menu-icon'
    modal_overlays = 'a[title="Modal & Overlays"]'
    modal_overlays_title = modal_overlays + ' span.menu-title'
    modal_overlays_icon = modal_overlays + ' nb-icon.menu-icon'
    extra_components = 'a[title="Extra Components"]'
    extra_components_title = extra_components + ' span.menu-title'
    extra_components_icon = extra_components + ' nb-icon.menu-icon'
    tables_data = 'a[title="Tables & Data"]'
    tables_data_title = tables_data + ' span.menu-title'
    tables_data_icon = tables_data + ' nb-icon.menu-icon'
    auth = 'a[title="Auth"]'
    auth_title = auth + ' span.menu-title'
    auth_icon = auth + ' nb-icon.menu-icon'
