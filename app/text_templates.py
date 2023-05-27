help_text = '''Welcome to the Sound-equipment Marketplace Help Page!
---------------------------------------
Here are the available commands:

- /start: Start the bot
- /help: View this help message
- /place: Place item for rent or sale
- /my_devices: Show all devices you have placed so far 
- /rent: Rent equipment
- /buy: Purchase equipment

Feel free to explore and enjoy your shopping experience!
'''

place_text = '''Howdy, partner! So, you reckonin' to put your sound device up for rent or sale, eh? Well, let's get y'all sorted out!\n\n
🤠 
Wrangle in potential customers and let your sound device shine like the desert sun.\n
Whether it's for a temporary arrangement or a permanent exchange, we'll help you make it happen!\n'''

rent_sell = {'class_quest': 'Please provide the type or class of the device\n(example: "Microphone")',
             'name_quest': 'Please provide the name and model of your device\n(example: "Rode NT1")',
             'descript_quest': 'Could you describe your device in a few words?\n(example: "1-inch gold-plated capsule and 20Hz–20kHz frequency response captures any source in all its glory..." etc.)',
             'price_quest': "What is the price you're looking to {} your device for?\n(example: '1000'; prices are shown in dollars)"}

my_devices_text = '''\u2022 🎤 <b>Type:</b> {}

\u2022 🏷️ <b>Name:</b> {}

\u2022 📝 <b>Description:</b>

 {}

\u2022 💲 <b>Price:</b> ${}

\u2022 ⚖️ <b>Rent/Sell:</b> {} 
'''

rent_text = '''🤠 <b>Howdy</b>, partner!

Welcome to the <b>Wild West Marketplace</b>!

Welcome to the <b>Rent</b> section! Here you can find a list of devices available for <b>rent</b>:

To view the devices, simply tap on the category you are interested in. If you find a device that suits your needs, you can proceed with the rental process. Enjoy exploring!'''

sell_text = '''🤠 <b>Howdy</b>, partner!

Welcome to the <b>Wild West Marketplace</b>!

Welcome to the <b>Buy</b> section! Here you can find a list of devices available for <b>sale</b>:

To view the devices, simply tap on the category you are interested in. If you find a device that you'd like to purchase, you can contact the owner for further details. Happy shopping!'''

deal_text = '''Great news! @{} is interested in your {}. They would like to get in touch with you to discuss further details.
'''
