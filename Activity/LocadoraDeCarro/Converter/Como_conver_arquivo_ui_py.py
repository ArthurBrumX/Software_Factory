# primeiro voce vai no explorador de arquivo onde o arquivo esta localizado
# vai clica no caminho do arquivo e digitar "cmd"
# Vai abrir o cmd do caminho do arquivo

# Com esse comando vou achar o executavel do pyuci6
    # python -m site --user-base

# no cmd do caminho aberto vai ser colocado
    # 1º Arrastar o executavel do pyuci6 para o cmd
        # esse que está aq - (python -m site --user-base) -> ("na pasta Scripts")

    # 2º Da um espaco e coloca (-x)

    # 3º Arrastar o arquivo que eu quero converter para o cmd

    # 4º Da um espaco e colocar (-o)

    # 5º Arrastar novamente o aquivo que eu quero para o cmd so que na extencao colocar (.py)

# Exemplo

# C:\xampp\htdocs\GitHub\Software_Factory\Activity\LocadoraDeCarro\Telas> (Aqui é o local da pasta do arquivo)
    # C:\Users\User\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts\pyuic6.exe -x (Aqui é o executavel do pyuci6)
        # C:\xampp\htdocs\GitHub\Software_Factory\Activity\LocadoraDeCarro\Telas\TelaCadastro.ui -o (Aqui é o arquivo com a extencao original)
            #C:\xampp\htdocs\GitHub\Software_Factory\Activity\LocadoraDeCarro\Telas\TelaCadastro.py (Aqui é o arquivo com a extencao ja convertida)

            # Depois Apenas Executar.

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 1. instalação de ferramentas pyqt6
# Na linha de comando execute este código.
# pip.exe instalar ferramentas pyqt6
# Arraste e solte pip.exe na linha de comando para obter o caminho completo.

# 2. Abra o designer
# designer.exe pode ser encontrado em
# C:\Users\!!nome de usuário!!\AppData\Local\Programs\Python\Python37\Lib\site-packages\qt5_applications\Qt\bin

# 3. Salve o arquivo da IU

# 4. Converta o arquivo UI para Python
# pyuic6 -x "arquivo.ui" -o "arquivo.py"