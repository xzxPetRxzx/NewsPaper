from django import template

register = template.Library()

@register.filter()
def censor(message: str):
    VARIANTS = ['погода', 'завтра']
    low_message = message.lower()
    for s_word in VARIANTS:
        res = [i for i in range(len(low_message)) if low_message.startswith(s_word, i)]
        for j in res:
            message = message[:j]+('*' * len(s_word))+message[j+len(s_word):]
    return message
