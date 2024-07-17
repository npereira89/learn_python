import gettext
import locale

locale.setlocale(locale.LC_ALL, 'pt_PT.UTF-8')

locale = gettext.translation('pt_PT', localedir='./locales/', languages=["pt_PT"], fallback=True)
locale.install()  # Make translations available

# Example: Translate a message
_ = locale.gettext  # Shortcut for translation function
translated_message = _("Python's very funny")

lng= locale.info()

if lng['language'] == "pt_PT":
    print(f"Translated message (Portuguese): {translated_message}")
elif lng['language'] == "it_IT":
    print(f"Translated message (Italian): {translated_message}")

