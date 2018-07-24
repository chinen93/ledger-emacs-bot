from pyrogram import Client, Filters

app = Client("614256101:AAHsSI3RIMwHFOYSg2WpJXimWFz8iT-BvrI", api_id=307767, api_hash="16eecfc45e703e280568cf3f657fd7a5")

@app.on_message(Filters.text & Filters.private)
def echo(client, message):
    client.send_message(
        message.chat.id, message.text,
        reply_to_message_id=message.message_id
    )


app.run()  # Automatically start() and idle()