from .. import loader

class AMLib(loader.Library):
  developer = "@ToXicUse"
  version = (0, 0, 1)
  
  async def list(
    text = getattr(message, "raw_text", "")
    P = "пПnPp"
    I = "иИiI1uІИ́Їіи́ї"  # noqa: E741
    E = "еЕeEЕ́е́"
    D = "дДdD"
    Z = "зЗ3zZ3"
    M = "мМmM"
    U = "уУyYuUУ́у́"
    O = "оОoO0О́о́"  # noqa: E741
    L = "лЛlL1"
    A = "аАaAА́а́@"
    N = "нНhH"
    G = "гГgG"
    K = "кКkK"
    R = "рРpPrR"
    H = "хХxXhH"
    YI = "йЙyуУY"
    YA = "яЯЯ́я́"
    YO = "ёЁ"
    YU = "юЮЮ́ю́"
    B = "бБ6bB"
    T = "тТtT1"
    HS = "ъЪ"
    SS = "ьЬ"
    Y = "ыЫ"

    occurrences = re.findall(
        rf"""\b[0-9]*(\w*[{P}][{I}{E}][{Z}][{D}]\w*|(?:[^{I}{U}\s]+|{N}{I})?(?<!стра)[{H}][{U}][{YI}{E}{YA}{YO}{I}{L}{YU}](?!иг)\w*|\w*[{B}][{L}](?:[{YA}]+[{D}{T}]?|[{I}]+[{D}{T}]+|[{I}]+[{A}]+)(?!х)\w*|(?:\w*[{YI}{U}{E}{A}{O}{HS}{SS}{Y}{YA}][{E}{YO}{YA}{I}][{B}{P}](?!ы\b|ол)\w*|[{E}{YO}][{B}]\w*|[{I}][{B}][{A}]\w+|[{YI}][{O}][{B}{P}]\w*)|\w*(?:[{P}][{I}{E}][{D}][{A}{O}{E}]?[{R}](?!о)\w*|[{P}][{E}][{D}][{E}{I}]?[{G}{K}])|\w*[{Z}][{A}{O}][{L}][{U}][{P}]\w*|\w*[{M}][{A}][{N}][{D}][{A}{O}]\w*|\w*[{G}][{O}{A}][{N}][{D}][{O}][{N}]\w*)""",
        text,
    )

    occurrences = [
        word
        for word in occurrences
        if all(
            excl not in word for excl in self.api.variables["censor_exclusions"]
        )
    ]
  )
