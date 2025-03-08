# if you're adding a langauge, remember to create a dictation_cc.talon file
# using one of the other ones as an example

languages = """
de_DE german
en_EN english
es_ES spanish
fr_FR french
ja_JP japanese
nl_NL dutch
pt_PT portuguese
ro_RO romanian
ru_RU russian
sv_SE swedish
zh_CMN mandarin
"""

from talon import Module, Context
import textwrap

cc_and_language = [line.strip().split(maxsplit=1)
                   for line in languages.strip().split('\n')
                   if line.strip()]

mod = Module()
mod.list("webspeech_language")

ctx = Context()
ctx.lists["user.webspeech_language"] = [lang for cc, lang in cc_and_language]

all_modes = []
contexts = []
for cc, language in cc_and_language:
    mod.mode(language)
    all_modes.append(f"user.{language}")
    engine_ctx = Context()
    engine_ctx.matches = textwrap.dedent(f"""
    mode: user.{language}
    and not mode: command
    """)
    engine_ctx.settings = {
        "speech.engine": "webspeech",
        "speech.language": cc,
    }
    contexts.append(engine_ctx)
