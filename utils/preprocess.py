import ftfy

import string


def mapping(text):
    return text


def replace_emoji(text):
    return text


def text_clean(text):
    text =  " ".join(re.findall("[0-9a-zaáàảãạâấầẩẫậăắằẳẵặeéèẻẽẹêếềểễệ\
        iíìỉĩịoóòỏõọôốồổỗộơớờởỡợuúùủũụưứừửữựyýỳỷỹỵđ]+", text.lower()))
    return text


def normalize(text):
    text = ftfy.fix_text(text)
    return text


