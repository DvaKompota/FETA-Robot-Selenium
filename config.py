browser = 'Chrome'  # Possible values can be found in SeleniumLibrary/keywords/browsermanagement.py on lines 71-83
headless = True  # If True - runs browser in headless mode. Recommended: 'True' for regular use, 'False' for debugging.
maximized = False  # If True - runs browser in window maximized to screen size. Recommended: 'False'
fixed_size = True  # If True - runs browser in window with fixed size, defined in the next 2 lines. Recommended: 'True'
horizontal = 1920  # Horizontal resolution for fixed size browser window. Recommended: '1920'
vertical = 1080  # Vertical resolution for fixed size browser window. Recommended: '1080'
selenium_timeout = '20 seconds'  # Default timeout waiting time for Selenium Library. Recommended: '20 seconds'
