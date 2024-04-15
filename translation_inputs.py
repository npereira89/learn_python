import gettext
import locale

locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')

locale = gettext.translation('it_IT', localedir='./locales/', languages=["it_IT"], fallback=True)
locale.install()  # Make translations available

# Example: Translate a message
_ = locale.gettext  # Shortcut for translation function
translated_message = _("Tudo bem?")

print(f"Translated message (English): {translated_message}")

