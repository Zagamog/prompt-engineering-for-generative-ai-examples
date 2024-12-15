import json

# openai_json_result = generate_article_outline(prompt)

openai_json_result = """
[
  {
    "region": "Northern",
    "institutes": [
      "Instituto Federal do Acre (IFAC)",
      "Instituto Federal do Amazonas (IFAM)",
      "Instituto Federal do Amapá (IFAP)",
      "Instituto Federal de Rondônia (IFRO)",
      "Instituto Federal de Roraima (IFRR)",
      "Instituto Federal do Pará (IFPA)",
      "Instituto Federal do Tocantins (IFTO)"
    ]
  },
  {
    "region": "Northeastern",
    "institutes": [
      "Instituto Federal de Alagoas (IFAL)",
      "Instituto Federal da Bahia (IFBA)",
      "Instituto Federal Baiano (IF Baiano)",
      "Instituto Federal do Ceará (IFCE)",
      "Instituto Federal do Maranhão (IFMA)",
      "Instituto Federal da Paraíba (IFPB)",
      "Instituto Federal de Pernambuco (IFPE)",
      "Instituto Federal do Sertão Pernambucano (IF Sertão-PE)",
      "Instituto Federal do Piauí (IFPI)",
      "Instituto Federal do Rio Grande do Norte (IFRN)",
      "Instituto Federal de Sergipe (IFS)"
    ]
  },
  {
    "region": "Central-West",
    "institutes": [
      "Instituto Federal de Brasília (IFB)",
      "Instituto Federal de Goiás (IFG)",
      "Instituto Federal Goiano (IF Goiano)",
      "Instituto Federal do Mato Grosso (IFMT)",
      "Instituto Federal do Mato Grosso do Sul (IFMS)"
    ]
  },
  {
    "region": "Southeastern",
    "institutes": [
      "Instituto Federal do Espírito Santo (IFES)",
      "Instituto Federal de Minas Gerais (IFMG)",
      "Instituto Federal do Norte de Minas Gerais (IFNMG)",
      "Instituto Federal do Sudeste de Minas Gerais (IF Sudeste-MG)",
      "Instituto Federal do Sul de Minas Gerais (IF Sul-MG)",
      "Instituto Federal do Triângulo Mineiro (IFTM)",
      "Instituto Federal do Rio de Janeiro (IFRJ)",
      "Instituto Federal de São Paulo (IFSP)"
    ]
  },
  {
    "region": "Southern",
    "institutes": [
      "Instituto Federal do Paraná (IFPR)",
      "Instituto Federal do Rio Grande do Sul (IFRS)",
      "Instituto Federal Sul-rio-grandense (IFSul)",
      "Instituto Federal Farroupilha (IF Farroupilha)",
      "Instituto Federal de Santa Catarina (IFSC)"
    ]
  }
]

"""

parsed_json_payload = json.loads(openai_json_result)
print(parsed_json_payload)
