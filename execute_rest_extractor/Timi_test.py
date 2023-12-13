import base64
a = b'{"name": "John", "age":42}'
print("Encode: ", base64.b64encode(a))
# eyJuYW1lIjogIkpvaG4iLCAiYWdlIjogNDJ9


# import os
# echo '{
#   "client-id": "77823320-555b-40dc-a246-3d09e6b63f72",
#   "client-secret": "wZi8Q~t3o46RMSeeHJW7-GwNiNXcxGmyb~V7ybF2"
# }' | base64
test_str = b'{"client-id": "77823320-555b-40dc-a246-3d09e6b63f72","client-secret": "wZi8Q~t3o46RMSeeHJW7-GwNiNXcxGmyb~V7ybF2"}'
print("Test encoded: ", base64.b64encode(test_str))

enc1 = 'eyJjbGllbnQtaWQiOiAiNzc4MjMzMjAtNTU1Yi00MGRjLWEyNDYtM2QwOWU2YjYzZjcyIiwiY2xpZW50LXNlY3JldCI6ICJ3Wmk4UX50M280NlJNU2VlSEpXNy1Hd05pTlhjeEdteWJ+Vjd5YkYyIn0='
print("Test decoded: ", base64.b64decode(enc1))


# echo '{
#   "client-id": "0bcc7ec1-79f5-4c34-a68c-c2009b85afac"",
#   "client-secret": "JyU8Q~iUK~3tiWtQgNQOlb5V-YZ4lVxfIxokpa19"
# }' | base64
prod_str = b'{"client-id": "0bcc7ec1-79f5-4c34-a68c-c2009b85afac"", "client-secret": "JyU8Q~iUK~3tiWtQgNQOlb5V-YZ4lVxfIxokpa19"}'
print("Prod: ", base64.b64encode(prod_str))

enc1 = 'eyJjbGllbnQtaWQiOiAiMGJjYzdlYzEtNzlmNS00YzM0LWE2OGMtYzIwMDliODVhZmFjIiIsICJjbGllbnQtc2VjcmV0IjogIkp5VThRfmlVS34zdGlXdFFnTlFPbGI1Vi1ZWjRsVnhmSXhva3BhMTkifQ=='
print("prod decoded: ", base64.b64decode(enc1))
