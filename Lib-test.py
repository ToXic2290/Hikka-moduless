from .. import loader

class AM_Library(loader.Library):
  developer = "@ToXicUse"
  version = (0, 0, 2)
  
  mats = ['пизда', 'хуй', 'блять', 'пиздец', 'сука', 'еблан', 'долбоеб']
  
  strings = {
		"name": "АнтиМат",
		"am_on": "🤬 <b>Antimat enabled.</b>",
		"am_off": "🤬 <b>Antimat disabled.</b>",
		"action_text": "What action should be taken when a swear word is found in a message?",
		"list_mats_txt": 'Enter the mats that the module should remove',
	}
