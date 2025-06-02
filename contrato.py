from docx import Document
from datetime import datetime

doc = Document()
doc.add_heading('CONTRATO DE PRESTAÇÃO DE SERVIÇOS DE CRIAÇÃO DE MÍDIAS DIGITAIS', level=1)

contrato_texto = [
    ("CONTRATANTE:", "Nome: [Nome do cliente]\nCPF/CNPJ: [Número]\nEndereço: [Endereço completo]\nE-mail: [E-mail]"),
    ("CONTRATADO:", "Nome: [Seu nome ou nome da empresa]\nCPF/CNPJ: [Número]\nEndereço: [Endereço completo]\nE-mail: [E-mail]"),
    ("CLÁUSULA 1 – DO OBJETO", 
     "1.1 O presente contrato tem como objeto a criação de mídias digitais, incluindo, mas não se limitando a:\n"
     "[Ex: 10 artes mensais para Instagram, 2 vídeos para Reels, 1 banner promocional, etc.]\n\n"
     "1.2 O material será desenvolvido conforme briefing fornecido pelo CONTRATANTE e respeitando os prazos acordados."),
    ("CLÁUSULA 2 – DO PRAZO E ENTREGA", 
     "2.1 O serviço terá início em [data] e término previsto para [data], podendo ser prorrogado mediante acordo por escrito.\n\n"
     "2.2 As entregas serão realizadas conforme cronograma acordado entre as partes. O prazo padrão para entrega de cada peça será de "
     "[ex: 5 dias úteis] após aprovação do briefing."),
    ("CLÁUSULA 3 – DO VALOR E FORMA DE PAGAMENTO", 
     "3.1 O CONTRATANTE pagará ao CONTRATADO o valor total de R$ [valor], conforme as condições abaixo:\n"
     "- Forma de pagamento: [Pix, transferência bancária, etc.]\n"
     "- Parcelamento: [se houver]\n"
     "- Vencimentos: [datas]\n\n"
     "3.2 Em caso de atraso no pagamento, incidirá multa de [ex: 2%] e juros de [ex: 1% ao mês]."),
    ("CLÁUSULA 4 – DAS REVISÕES", 
     "4.1 Estão incluídas até [ex: 2] rodadas de revisão por peça.\n\n"
     "4.2 Revisões adicionais serão cobradas à parte, no valor de R$ [valor] por rodada extra."),
    ("CLÁUSULA 5 – DOS DIREITOS AUTORAIS E USO", 
     "5.1 Os direitos de uso das mídias criadas serão transferidos ao CONTRATANTE após o pagamento integral do serviço.\n\n"
     "5.2 O CONTRATADO poderá utilizar as peças criadas em seu portfólio, salvo se houver cláusula de confidencialidade (ver cláusula 6)."),
    ("CLÁUSULA 6 – DA CONFIDENCIALIDADE", 
     "6.1 As partes comprometem-se a manter sigilo sobre quaisquer informações confidenciais trocadas durante a execução do contrato."),
    ("CLÁUSULA 7 – DA RESCISÃO", 
     "7.1 O contrato poderá ser rescindido por qualquer das partes, mediante aviso prévio de [ex: 7 dias], por escrito.\n\n"
     "7.2 Em caso de rescisão, o CONTRATANTE pagará proporcionalmente pelos serviços já realizados até a data do aviso."),
    ("CLÁUSULA 8 – DAS PENALIDADES", 
     "8.1 O descumprimento de qualquer cláusula deste contrato poderá gerar multa de até R$ [valor], conforme a gravidade da infração."),
    ("CLÁUSULA 9 – DO FORO", 
     "9.1 Para dirimir quaisquer controvérsias oriundas deste contrato, as partes elegem o foro da comarca de [cidade/estado], renunciando a qualquer outro, por mais privilegiado que seja."),
    ("", f"E, por estarem assim justos e contratados, firmam o presente instrumento, em duas vias de igual teor, na presença de testemunhas.\n\n[Local], {datetime.now().strftime('%d/%m/%Y')}"),
    ("CONTRATANTE:", "_"),
    ("CONTRATADO:", "_"),
    ("Testemunha 1:", "Nome:\nCPF:\nAssinatura:"),
    ("Testemunha 2:", "Nome:\nCPF:\nAssinatura:")
]

for titulo, conteudo in contrato_texto:
    if titulo:
        doc.add_heading(titulo, level=2)
    for linha in conteudo.split('\n'):
        doc.add_paragraph(linha)

doc.save("Contrato_Criacao_Midias_Digitais.docx")
