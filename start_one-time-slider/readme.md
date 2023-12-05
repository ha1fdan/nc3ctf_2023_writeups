Kryptonissen har læst op på One Time Pads og er kommet frem til en endnu mere sikker kryptering:

Hvis man nu slider en OTP henover hele ciphertexten, bliver hver plaintext byte krypteret mange gange - det må være bedre end én!

Han har krypteret en besked til dig:
`e9e494dcd1c2c9d3f8d1c6d5f8c3c2d3f8c3d2cad3f8c6d3f8ffe8f5f8c6cbcbc2f8c5ded3c2d4f8cac2c3f8cfd1c2d5f8ccc2def8c5ded3c2989898da`

Vedheftet fil: [onetimeslider.py](onetimeslider.py)
---

[Dette Python-script](app.py) udfører brute force dekryptering af den krypteret værdi, indtil det dekrypterede resultat starter med "NC3{".

Flag: `NC3{vent_var_det_dumt_at_XOR_alle_bytes_med_hver_key_byte???}`