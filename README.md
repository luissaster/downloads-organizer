# Downloads Organizer 

Um script Python para organizar arquivos baixados em pastas categorizadas.

## Uso

* Edite o script para especificar o caminho da pasta que você deseja organizar. Por padrão, o script está configurado para organizar a pasta `C:/Users/User/Downloads`.
* Execute o script usando Python (por exemplo, `python downloads_organizer.py`).

## Pastas

O script cria as seguintes pastas categorizadas:

* `Images`: para arquivos de imagem (jpg, jpeg, png, gif, tiff, bmp, svg, webp)
* `Documents`: para arquivos de documento (pdf, docx, xlsx, pptx, txt, md, csv)
* `Audio`: para arquivos de áudio (mp3, wav, aac, flac, ogg)
* `Videos`: para arquivos de vídeo (mp4, mov, avi, mkv, flv)
* `Archives`: para arquivos compactados (zip, rar, tar.gz, 7z)
* `Scripts`: para arquivos de script (py, js, sh, bat, sql)

Para adicionar novas pastas e/ou tipos de arquivos, basta inserir um novo dicionário no código.

## Requisitos

* Python 3.x