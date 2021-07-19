import os, json

class SettingsManager:
	"""A class that manages the settings/saves"""
	save_dir = os.path.join(os.environ['LOCALAPPDATA'], 'PyPadPRO') # save directory is in %localappdata%/PyPadPRO
	settings_file = os.path.join(save_dir, 'settings.json') # settings file is 'settings.json' in save directory 

	@classmethod
	def setup(cls, objFormat, font):
		"""A method to setup the settings"""
		#check if save directory exists, if not then create it
		if not os.path.exists(cls.save_dir): os.makedirs(cls.save_dir)

		#check if settings file exists, if not then create one with default settings
		if not os.path.exists(cls.settings_file):
			default_settings = {
				"background_color": "#ffffff",
				"font_color": "#000000",
				"font_family": "Arial",
				"font_size": 10
			}
			# writes the default setting into the settings.json file with json format
			json.dump(default_settings, open(cls.settings_file, "w"))

		cls.load_setting(objFormat, font) #load settings

	@classmethod
	def change_setting(cls, setting, value):
		"""A method to change the value of a setting in settings"""
		settings_dict = json.load(open(cls.settings_file, 'r')) # retrieve settings from settings.json
		settings_dict[setting] = value #change the settings
		json.dump(settings_dict, open(cls.settings_file, "w")) #save the changed settings

	@classmethod
	def change_font(cls, font, setting, value):
		"""A method to change the value of a font setting and save it into settings.json"""
		if setting == "font_family": font.configure(family=value)
		if setting == "font_size": font.configure(size=value)
		cls.change_setting(setting, value)

	@classmethod
	def load_setting(cls, objFormat, font):
		"""A method to load the settings from settings.json"""
		settings_dict = json.load(open(cls.settings_file, 'r')) # retrieve settings from settings.json
		objFormat.text.config(bg=settings_dict["background_color"])
		objFormat.text.config(fg=settings_dict["font_color"])
		font.configure(family=settings_dict["font_family"])
		font.configure(size=settings_dict["font_size"])

if __name__ == "__main__":
    print("Please run 'PyPad.pyw'")